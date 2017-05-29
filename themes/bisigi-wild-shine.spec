%define name gnome-bisigi-wild-shine-theme
%define version 2.0.0
%define release %mkrel 2

%define themesdir %{_datadir}/themes
%define iconsdir %{_datadir}/icons
%define wallpapersdir %{_datadir}/backgrounds
%define wallpaperspropdir %{_datadir}/gnome-background-properties
%define docsdir %{_docdir}/%{name}
%define themeinside wild-shine

Summary:	Bisigi theme
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source1:	wild-shine-theme.tar.gz

License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://www.bisigi-project.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	murrine

%description
Wild Shine theme contains a full theme for GNOME based system.
It includes the following components:
			* "Wild Shine" wallpapers
			* GTK+ theme
			* Metacity theme
			* Wild Shine Icons set

%prep

tar -xf %{SOURCE1}
cd wild-shine-theme/Gtk/
tar -xf %{themeinside}.tar.gz
cd ..
cd Icons
tar --bzip2 -xf %{themeinside}.tar.bz2

%build

%install

%__rm -rf %{buildroot}
%__install -d %{buildroot}%{themesdir}
%__install -d %{buildroot}%{iconsdir}
%__install -d %{buildroot}%{wallpapersdir}
%__install -d %{buildroot}%{wallpaperspropdir}
%__install -d %{buildroot}%{docsdir}

cd wild-shine-theme/Wallpaper
%__cp -rf *.png %{buildroot}%{wallpapersdir}
%__cp -rf *.xml %{buildroot}%{wallpaperspropdir}
cd ..
%__cp -rf COPYING %{buildroot}%{docsdir}
%__cp -rf credits.txt %{buildroot}%{docsdir}
cd Gtk
%__cp -rf ./* %{buildroot}%{themesdir}
cd ..
cd Icons
%__cp -rf ./* %{buildroot}%{iconsdir}
cd ..
cd ..


%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{docsdir}/* 
%{themesdir}/*
%{iconsdir}/*
%{wallpapersdir}/*
%{wallpaperspropdir}/*


%changelog
* Fri Apr 29 2014 Mank <mank dot pclos at gmail dot com> 2.0.0-2mank2014
- Update

* Fri Feb 11 2011 Cristobal Lopez <lopeztobal@gmail.com> 1.5.1-1mib2010.2
- Update.

* Fri Aug 20 2010 Cristobal Lopez <lopeztobal@gmail.com> 1.4.2-1mib2010.1
- Update.

* Sat Jul 10 2010 Cristobal Lopez <lopeztobal@gmail.com> 1.4.1-1mib2010.1
- Update.
