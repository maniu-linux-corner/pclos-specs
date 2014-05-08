# http://trac.wildfiregames.com/wiki/BuildInstructions#Linux

# enable special maintainer debug build ?
%define		with_debug		0
%if %{with_debug}
%define		config			debug
%define		dbg			_dbg
%else
%define		config			release
%define		dbg			%{nil}
%endif

# Remember to rerun licensecheck after every update:
#	https://bugzilla.redhat.com/show_bug.cgi?id=818401#c46
#	http://trac.wildfiregames.com/ticket/1682

%global		with_system_nvtt	0
%global		without_nvtt		1

%if 0%{?fedora} <= 16
%global		with_system_enet	0
%else
%global		with_system_enet	1
%endif

Name:		0ad
Version:	0.0.14
Release:	1%{?dist}
# BSD License:
#	build/premake/*
#	libraries/valgrind/*		(not built/used)
# MIT License:
#	libraries/enet/*
#	libraries/fcollada/*
#	source/third_party/*
# LGPLv2+
#	libraries/cxxtest/*		(not built/used)
# GPLv2+
#	source/*
# IBM
#	source/tools/fontbuilder2/Packer.py
# MPL-1.1
#	libraries/spidermonkey/*	(not built/used)
License:	GPLv2+ and BSD and MIT and IBM
Group:		Amusements/Games
Summary:	Cross-Platform RTS Game of Ancient Warfare
Url:		http://play0ad.com/

%if %{without_nvtt}
# wget http://releases.wildfiregames.com/%%{name}-%%{version}-alpha-unix-build.tar.xz
# tar Jxf %%{name}-%%{version}-alpha-unix-build.tar.xz
# rm -fr %%{name}-%%{version}-alpha/libraries/nvtt
# rm -f %%{name}-%%{version}-alpha-unix-build.tar.xz
# tar Jcf %%{name}-%%{version}-alpha-unix-build.tar.xz %%{name}-%%{version}-alpha
Source0:	%{name}-%{version}-alpha-unix-build.tar.xz
%else
Source0:	%{name}-%{version}-alpha-unix-build.tar.xz
%endif

# Simplify checking differences when updating the package
# (also to validate one did not forget to remake the tarball if
# %{without_nvtt} is enabled) Create it with:
# cd BUILD/%{name}-%{version}-alpha
# licensecheck -r . > ../../SOURCES/%{name}-licensecheck.txt
Source1:	%{name}-licensecheck.txt

# adapted from binaries/system/readme.txt
# It is advisable to review this file at on newer versions, to update the
# version field and check for extra options. Note that windows specific,
# and disabled options were not added to the manual page.
Source2:	%{name}.6
Requires:	%{name}-data = %{version}
BuildRequires:	%{_lib}boost-devel
BuildRequires:	cmake
#BuildRequires:	desktop-file-utils
BuildRequires:	%{_lib}devil-devel
%if %{with_system_enet}
BuildRequires:	%{_lib}enet-devel
%endif
BuildRequires:	%{_lib}gamin-1_0-devel
BuildRequires:	js-devel
BuildRequires:	%{_lib}curl-devel
BuildRequires:	%{_lib}dnet-devel
BuildRequires:	%{_lib}jpeg62-devel
BuildRequires:	%{_lib}png-devel
BuildRequires:	%{_lib}vorbis0-devel
BuildRequires:	%{_lib}xml2-devel
BuildRequires:	zlib1-devel
BuildRequires:	nasm
%if %{with_system_nvtt}
BuildRequires:	%{_lib}Cg-devel
%endif
BuildRequires:	%{_lib}openal-devel
BuildRequires:	%{_lib}openjpeg-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	%{_lib}SDL-devel
BuildRequires:	subversion
BuildRequires:	libwxgtku2.8-devel
BuildRequires:  libgjs-devel

# Display more clear error messages when creating custom scenarios
# The suggested usage is:
#	$ sudo mkdir /usr/share/0ad/public/maps
#	$ sudo chmod 7777 /usr/share/0ad/public/maps
#	$ 0ad -editor
# Supposing saved the map as mymap, can test it with:
#	$ 0ad -autostart=mymap
Patch1:		%{name}-saveas.patch

# Only do fcollada debug build with enabling debug maintainer mode
# It also prevents assumption there that it is building in x86
Patch2:		%{name}-debug.patch

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or rewrite
the history of Western civilizations, focusing on the years between 500 B.C.
and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D
graphics, detailed artwork, sound, and a flexible and powerful custom-built
game engine.

The game has been in development by Wildfire Games (WFG), a group of volunteer,
hobbyist game developers, since 2001.

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}-alpha

%if %{with_system_nvtt}
rm -fr libraries/nvtt
%endif

#-----------------------------------------------------------------------
%build

# avoid warnings with gcc 4.7 due to _FORTIFY_SOURCE in CPPFLAGS
export CPPFLAGS="-O0"
build/workspaces/update-workspaces.sh	\
    --bindir %{_bindir}			\
    --datadir %{_datadir}/%{name}	\
    --libdir %{_libdir}/%{name}		\
%if %{with_system_enet}
    --with-system-enet			\
%endif
%if %{with_system_nvtt}
    --with-system-nvtt			\
%endif
%if %{without_nvtt}
    --without-nvtt			\
%endif

make -C build/workspaces/gcc config=%{config} verbose=0


#-----------------------------------------------------------------------
# Depends on availablity of nvtt
###%if !%{without_nvtt}
###%check
###LD_LIBRARY_PATH=binaries/system binaries/system/test%{dbg} -libdir binaries/system
###%endif

#-----------------------------------------------------------------------
%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 binaries/system/pyrogenesis%{dbg} %{buildroot}%{_bindir}/pyrogenesis%{dbg}

install -d -m 755 %{buildroot}%{_libdir}/%{name}
for name in AtlasUI%{dbg} Collada%{dbg}; do
    install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
done

# Install libmozjs185-ps.
install -D binaries/system/libmozjs185-ps-release.so.1.0 %{buildroot}/%{_libdir}/libmozjs185-ps-release.so.1.0


%if !%{with_system_enet}
    install -p -m 755 binaries/system/libenet.so.1 %{buildroot}%{_libdir}/libenet.so.1
%endif

%if !%{without_nvtt} && !%{with_system_nvtt}
for name in nvcore nvimage nvmath nvtt; do
    install -p -m 755 binaries/system/lib${name}.so %{buildroot}%{_libdir}/%{name}/lib${name}.so
done
%endif

install -d -m 755 %{buildroot}%{_datadir}/applications
install -p -m 644 build/resources/0ad.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -p -m 644 build/resources/0ad.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -a binaries/data/* %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man6/%{name}.6
ln -sf %{name}.6 %{buildroot}%{_mandir}/man6/pyrogenesis.6

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

cat > %{buildroot}%{_bindir}/0ad <<EOF
#!/bin/sh

cd %{_datadir}/0ad
LD_LIBRARY_PATH=%{_libdir}/0ad %{_bindir}/pyrogenesis%{dbg} "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/0ad

%if %{with_debug}
export STRIP=/bin/true
%endif

#-----------------------------------------------------------------------
%files
%doc README.txt LICENSE.txt
%doc license_gpl-2.0.txt license_lgpl-2.1.txt
%{_bindir}/0ad
%{_bindir}/pyrogenesis%{dbg}
%{_libdir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man6/*.6*

%changelog
* Fri Jan 4  2013 Mank <mank@pclinuxos.cz> - 0.0.12-2
   Some mirror changes for PCLOS .
* Wed Dec 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-2
- Enable build with system nvtt as it is now approved in Fedora (#823096)
- Correct release date in manual page
- Minor consistency correction in manual page formatting
- Regenerate the licensecheck text file to match pristine tarball

* Tue Dec 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-1
- Update to latest upstream release
- Remove no longer required gamin patch
- Rediff rpath patch
- Remove libxml2 patch already applied upstream
- Update 0ad manpage for newer options and release information
- Add versioned requires to data files
- Add 0ad licensecheck text file to simplify checking changes

* Sat Nov 3 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-4
- Add %%with_debug maintainer mode build
- Disable fcollada debug build if %%with_debug is false
- Add patch to not crash and display helful messages in editor (#872801)

* Tue Sep 11 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-3
- Clarify source tree licenses information in spec (#818401)
- Preserve time stamp of installed files (#818401)

* Sat Sep 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-2
- Correct manpage group and symlink 0ad manual to pyrogenesis manual (#818401)
- Correct some typos and wrong information in 0ad.6

* Sat Sep 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-1
- Update to latest upstream release
- Switch to new versioning pattern
- Remove rpath patch already applied upstream
- Remove without-nvtt patch already applied upstream
- Remove boost patch already applied upstream
- Remake rpath patch to avoid package build special conditions

* Thu Sep 6 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-6
- Repackage tarball to not redistribute patented s3tc implementation (#818401)
- Add patch to rebuild with newer libxml2.
- Add upstream trac patch for build with newer boost.
- Rename patches to remove %%version and use %%name in source files.

* Fri Jul 13 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-5
- Clearly state nvtt is not mean't to be used (unless user build from sources).
- Update to use patch in wildfire trac instead of my patch to remove rpath.

* Fri Jun  1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-4
- Actually remove %%defattr.
- Correct wrong fedora release check for enet-devel build requires.

* Sat May 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-4
- Make package build in Fedora 16 (rpmfusion #2342).
- Add conditionals to build with or without system nvtt or disable nvtt.

* Tue May 22 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-3
- Remove %%defattr from spec (#823096).
- Run desktop-file-validate (#823096).

* Mon May 21 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-2
- Disable dependency on nvidia-texture-tools (#823096).
- Disable %%check as it requires nvtt.
- Add manual page.

* Sat May 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-1
- Correct package license.
- Update to latest upstream release.
- Remove license_dbghelp.txt as dbghelp.dll is not in sources neither installed.

* Tue May 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11339-1
- Initial 0ad spec.
