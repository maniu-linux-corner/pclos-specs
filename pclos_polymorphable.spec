%define name	polymorphable
%define version	0.1
%define release	%mkrel 2
%define	Summary	A RPG clone Based on flare. Laurelia's Polymorphable Citizens
%define sdir flare-engine-branch0.18

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://flarerpg.org
Source0:	flare-engine-branch0.18.zip
Source1: polymorphable.tar.xz
License:	GPLv2
Group:		Games/RPG
BuildRequires:	%{_lib}SDL_image-devel %{_lib}SDL_net-devel %{_lib}SDL_mixer1.2-devel %{_lib}SDL-devel %{_lib}SDL_ttf2.0-devel cmake
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts: flare
%description
Laurelia's Polymorphable Citizens

%prep
%setup -n %{sdir}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DBINDIR=/usr/bin -DDATADIR=/usr/share/flare .
tar -xf %{SOURCE1}

%make

%install
%define qsdir %{_builddir}/%{sdir}
make install DESTDIR=$RPM_BUILD_ROOT
cp -r polymorphable/mods/polymorphable $RPM_BUILD_ROOT/usr/share/flare/mods/
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/applications/flare.desktop
%{_bindir}/flare
%{_datadir}/flare/mods/*
%{_iconsdir}/hicolor/scalable/apps/*

%changelog
* Wed May 28 2012 Mank <mank@pclinuxos.cz> 0.17-1pclinux2012.2
-	Build for PCLinuxOS
