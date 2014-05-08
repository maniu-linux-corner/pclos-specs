Name: yarock
Summary: YaRock - A QT Music Player
Version: 0.0.58
Release: 1
License: GPLv2
URL: http://qt-apps.org/content/show.php/YaRock?content=129372
Group: Applications/Sound
Source0: Yarock_0.0.58_source.tar.xz
Requires: phonon-xine xine-faad xine-flac
BuildRequires:	%{_lib}qt4-devel phonon-devel %{_lib}taglib-devel %{_lib}boost-devel
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A QT Music Player
http://qt-apps.org/content/show.php/YaRock?content=129372

%prep
%setup -c Yarock_0.0.58_source

%build
cd Yarock_0.0.58_source/
%qmake_qt4 PREFIX="/usr/"
#make 

%install
cd Yarock_0.0.58_source/
make INSTALL_ROOT=$RPM_BUILD_ROOT install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/YaRock
%{_datadir}/*

%changelog
* Sat Mar 25 2012 Mank <mank@pclinuxos.cz> 0.0.58-1
- YaRock: Version : 0.0.58
* Sat Mar 25 2011 Mank <mank@pclinuxos.cz> 0.0.56-1
- YaRock: Version : 0.0.56
