# http://trac.wildfiregames.com/wiki/BuildInstructions#Linux

Name:		0ad-data
Version:	0.0.14
Release:	1%{?dist}
Summary:	The Data Files for 0 AD
License:	CC-BY-SA
Group:		Amusements/Games
Url:		http://play0ad.com/
Source:		http://releases.wildfiregames.com/0ad-%{version}-alpha-unix-data.tar.xz
BuildRequires:	unzip
Requires:	fonts-ttf-dejavu
BuildArch:	noarch

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform
real-time strategy (RTS) game of ancient warfare. In short, it is a
historically-based war/economy game that allows players to relive or rewrite
the history of Western civilizations, focusing on the years between 500 B.C.
and 500 A.D. The project is highly ambitious, involving state-of-the-art 3D
graphics, detailed artwork, sound, and a flexible and powerful custom-built
game engine.

This package contains the 0ad data files.

%prep
%setup -q -n 0ad-%{version}-alpha

%build
pushd binaries/data/mods/public
    mkdir tmp
    pushd tmp
        unzip -x ../public.zip
	cp -a art/LICENSE.txt ../../../../../LICENSE-art.txt
	cp -a audio/LICENSE.txt ../../../../../LICENSE-audio.txt
        rm -fr *
    popd
    rm -fr tmp
popd

%install
%__mkdir_p %{buildroot}%{_datadir}
%__rm -f tools/fontbuilder/fonts/*.ttf
%__mv binaries/data %{buildroot}%{_datadir}/0ad

%files
%doc LICENSE-art.txt LICENSE-audio.txt
%{_datadir}/0ad

%changelog
* Tue Dec 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.12-1
- Update to latest upstream release

* Tue Sep 25 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-3
- Install LICENSE.txt files in proper documentation directory.

* Tue Sep 11 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-2
- Install license files (#823102)
- Clarify this package are the 0ad data files (#823102)
- Use system dejavu-sans fonts.

* Sat Sep 8 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.0.11-1
- Update to latest upstream release

* Sat May 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11863-1
- Correct package license.
- Update to latest upstream release.

* Tue May 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - r11339-1
- Initial 0ad-data spec.
