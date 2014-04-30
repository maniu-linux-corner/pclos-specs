%define name gnome-bisigi-cursor-themes
%define version 2.0
%define release %mkrel 1

%define iconsdir %{_datadir}/icons
%define docsdir %{_docdir}/%{name}

Summary:	Bisigi cursor themes
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	bisigi-cursors.tar.bz2

License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://www.bisigi-project.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	murrine

%description
Three bisigi cursor themes for your bisigi themes 
in GNOME Desktop.

%prep
%setup -q -n bisigi-cursors

%build

%install

%__rm -rf %{buildroot}
%__install -d %{buildroot}%{iconsdir}
%__install -d %{buildroot}%{docsdir}

%__cp -rf COPYING %{buildroot}%{docsdir}
%__cp -rf credits %{buildroot}%{docsdir}

cd Cursors
%__cp -rf ./* %{buildroot}%{iconsdir}
cd ..



%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{docsdir}/* 
%{iconsdir}/*


%changelog
* Fri Apr 29 2014 Mank <mank@pclinuxos.cz> 2.0-1mank2014
- First time ported to Mandriva by MIB.
* Fri Feb 11 2011 Cristobal Lopez <lopeztobal@gmail.com> 0.3-1mib2010.2
- First time ported to Mandriva by MIB.
