%define name gnome-bisigi-orange-theme
%define version 2.0.0
%define release %mkrel 2

%define themesdir %{_datadir}/themes
%define wallpapersdir %{_datadir}/backgrounds
%define wallpaperspropdir %{_datadir}/gnome-background-properties
%define docsdir %{_docdir}/%{name}
%define themeinside orange


Summary:	Bisigi theme
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source1:	orange-theme.tar.gz
License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://www.bisigi-project.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	murrine humanity-icon-theme

%description
Orange theme contains a full theme for GNOME based system.
It includes the following components:
   * "Orange" wallpapers
   * GTK+ theme
   * Metacity theme
   * Humanity Icons set

%prep

tar -xf %{SOURCE1}
cd orange-theme/Gtk/
tar -xf %{themeinside}.tar.gz

%build

%install

%__rm -rf %{buildroot}
%__install -d %{buildroot}%{themesdir}
%__install -d %{buildroot}%{wallpapersdir}
%__install -d %{buildroot}%{wallpaperspropdir}
%__install -d %{buildroot}%{docsdir}

ls
cd orange-theme/Wallpaper
%__cp -rf *.jpg %{buildroot}%{wallpapersdir}
%__cp -rf *.xml %{buildroot}%{wallpaperspropdir}
cd ..
%__cp -rf COPYING %{buildroot}%{docsdir}
%__cp -rf credits.txt %{buildroot}%{docsdir}
cd Gtk
%__cp -rf ./* %{buildroot}%{themesdir}
cd ..

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{docsdir}/* 
%{themesdir}/*
%{wallpapersdir}/*
%{wallpaperspropdir}/*


%changelog
* Fri Apr 29 2014 Mank <mank@pclinuxos.cz> 2.0.0-2mank2014
- Update

* Fri Feb 11 2011 Cristobal Lopez <lopeztobal@gmail.com> 1.6.1-1mib2010.2
- Update

* Fri Aug 20 2010 Cristobal Lopez <lopeztobal@gmail.com> 1.5.1-1mib2010.1
- Update.

* Sat Jul 10 2010 Cristobal Lopez <lopeztobal@gmail.com> 1.5.0-1mib2010.1
- Update.
