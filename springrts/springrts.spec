%define name	springrts
%define version	0.91
%define release	%mkrel 1
%define	Summary	A RTS Engine
%define sdir spring

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://springrts.com/
Source0:	spring.tar.xz
License:	GPLv2
Group:		Games/RTS
BuildRequires: %{_lib}boost-devel cmake %{_lib}SDL-devel %{_lib}openal-devel %{_lib}devil-devel zlib1-devel freetype %{_lib}vorbis-devel %{_lib}xcursor-devel     
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
..

%prep
%setup -n %{sdir}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DBINDIR=/usr/bin -DDATADIR=/usr/share/%{name} .

%make spring

%install
%define qsdir %{_builddir}/%{sdir}
make install-spring DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/applications/%{sdir}.desktop
%{_bindir}/spring*
%{_datadir}/springrts/*
%{_datadir}/doc/*
%{_datadir}/mime/*
%{_datadir}/pixmaps/*
%{_libdir}/*
#%{_iconsdir}/hicolor/scalable/apps/*

%changelog
* Wed May 28 2012 Maniu <me  at maniu dot eu> 0.91-1pclinux2012.1
-	Build for PCLinuxOS

