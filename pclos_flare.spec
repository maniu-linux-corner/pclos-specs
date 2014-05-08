%define name	flare
%define version	0.19
%define release	%mkrel 1
%define	Summary	A RPG clone with Smal code base

Source0:	flare.0.19.tar.gz
Source2:	flare.desktop
Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://flarerpg.org
License:	GPL
%description
...

%package data
Summary:	%{Summary} Data Files
Version:	%{version}
Release:	%{release}
URL:		http://flarerpg.org
License:	GPL
%description data
 Data Files

Group:		Games/RPG
BuildRequires:	%{_lib}SDL_image-devel %{_lib}SDL_net-devel %{_lib}SDL_mixer1.2-devel %{_lib}SDL-devel %{_lib}SDL_ttf-devel cmake
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%prep
%setup -n flare.0.19

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DBINDIR=/usr/bin -DDATADIR=/usr/share/flare .
%make

%install
make install DESTDIR=$RPM_BUILD_ROOT

#fix the desktop file
mkdir -p "$RPM_BUILD_ROOT%{_datadir}/applications/";
mkdir -p "$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/";
cp "%{SOURCE2}" "$RPM_BUILD_ROOT%{_datadir}/applications/";
cp distribution/flare_logo.svg "$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/";
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/applications/flare.desktop
%{_datadir}/man/*
%{_iconsdir}/hicolor/scalable/apps/*
%{_bindir}/*

%files data
%{_datadir}/flare/*

%changelog
* Wed Jun 15 2013 Mank <mank@pclinuxos.cz> 0.19-1
-	Build for PCLinuxOS

