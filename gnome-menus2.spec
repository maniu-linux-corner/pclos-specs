%define major 2
%define libname %mklibname gnome-menu %major
%define libnamedev %mklibname -d gnome-menu %api
%define api 2.0
%define oname gnome-menus

Summary: GNOME menu library
Name: gnome-menus2
Version: 3.0.1
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/%oname/%{oname}-%{version}.tar.gz
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glib2-devel >= 2.5.6
BuildRequires: intltool >= 0.40.0
BuildRequires: python-devel
BuildRequires: gobject-introspection-devel
Requires: python-%{name}

%description
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:
http://www.freedesktop.org/Standards/menu-spec

Also contained here are the GNOME menu layout configuration files,
.directory files and assorted menu related utility programs.

%package -n python-%{name}
Group: Development/Python
Summary: Module to access XDG menu

%description -n python-%{name}
Python module to access XDG menu.

%package -n %libname
Group: System/Libraries
Summary: GNOME menu library
Conflicts: gir-repository < 0.6.5-8

%description -n %libname
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:
http://www.freedesktop.org/Standards/menu-spec

%package -n %libnamedev
Group: Development/C
Summary: GNOME menu library development files
Requires: %libname = %version
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d gnome-menu 2
Conflicts: gir-repository < 0.6.5-8

%description -n %libnamedev
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:
http://www.freedesktop.org/Standards/menu-spec

%prep
%setup -q -n %oname-%version

%build
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT %oname.lang
%makeinstall_std
# gw these produce rpmlint errors:
rm -rf %buildroot%_datadir/locale/{io,be@latin,bn_IN,si,uz@cyrillic}
%find_lang %oname

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/xdg/gnome
mv $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus $RPM_BUILD_ROOT%{_sysconfdir}/xdg/gnome

chmod 755 %buildroot%_libdir/python*/site-packages/GMenuSimpleEditor/*.py

#gw some build nodes remove these automatically, some don't
rm -f %buildroot%_libdir/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %oname.lang
%defattr(-,root,root)
%doc README NEWS HACKING AUTHORS ChangeLog
%exclude %_datadir/desktop-directories
%dir %_sysconfdir/xdg/gnome
%dir %_sysconfdir/xdg/gnome/menus
%config(noreplace) %_sysconfdir/xdg/gnome/menus/*
%_bindir/*
%_datadir/applications/*
%_datadir/%{oname}

%files -n python-%{name}
%defattr(-,root,root)
%_libdir/python*/site-packages/*

%files -n %libname
%defattr(-,root,root)
%_libdir/libgnome-menu.so.%{major}*
%_libdir/girepository-1.0/GMenu-%api.typelib

%files -n %libnamedev
%defattr(-,root,root)
%_libdir/lib*.so
%_libdir/lib*.a
%_includedir/gnome-menus/
%_libdir/pkgconfig/*.pc
%_datadir/gir-1.0/GMenu-%api.gir



%changelog
* Wed Dec 14 2011 Götz Waschk <waschk@mandriva.org> 2.30.5-4mdv2012.0
+ Revision: 741057
- remove libtool archive manually, build system is broken
- bump release
- readd libtool archive
- bring back gnome 2.x menu library
- update to new version 2.30.5
- update to new version 2.30.4
- update to new version 2.30.3
- rebuild for new g-i
- update to new version 2.30.2
- update to new version 2.30.0
- add conflict with old gir-repositry
- new version
- add gobject introspection support
- update to new version 2.29.91
- update to new version 2.29.6
- new version
- drop merged patches 2,3
- update to new version 2.28.0
- new version
- rediff patch 0
- update to new version 2.27.5
- new version
- rediff patch 0
- new version
- update patch 2
- update to new version 2.26.1
- update to new version 2.26.0
- update to new version 2.25.91
- update to new version 2.25.5
- update to new version 2.25.2
- update to new version 2.24.2
- update to new version 2.24.1
- new version
- new version
- new version
- new version
- new version
- new version
- rediff patch 1
- update license
- update buildrequires
- new version
- rediff patch 1
- drop patch 2 (different fix upstream)
- new version
- new version
- new version
- fix rpmlint errors
- new version
- new version
- new version
- drop patch 3
- fix build with new gio
- new version
- new version
- new version
- new version
- new version
- new version
- new devel name
- new version
- new version
- new version
- new version
- new version

  + mandrake <mandrake@mandriva.com>
    - %repsys markrelease
      version: 2.30.5
      release: 2
      revision: 664874
      Copying 2.30.5-2 to releases/ directory.

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

  + Funda Wang <fwang@mandriva.org>
    - rebuild for py2.7
    - rebuild for new gobject-introspection
    - link against python

  + Frederic Crozat <fcrozat@mandriva.com>
    - Fix buildrequires
    - Redo patch2
    - Patch3: ensure name is correctly filled for comparison
    - Update patch0 to not try to translate empty fields (Mdv bug #44964)
    - Update patch1 to no hide GNOME;Settings;System (Mdv bug #34269)
    - Resync with desktop-common-data
    - Patch2: fix separator handling (Mdv bug #32867)
    - Update patch1 to fill administration menu with System Tools menu content

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild with python 2.6

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags
