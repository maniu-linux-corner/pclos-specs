%define name elementary-usu-icon-theme
%define version 8.0.7
%define release %mkrel 3

%define iconsdir %{_datadir}/icons

Summary:	Elementary usu for KDE
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source1:	elementary_usu-8.0.7.tar.bz2

License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://opendesktop.org/content/show.php?content=148128
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Elementary usu for KDE

%prep

tar --bzip2 -xf %{SOURCE1}

%build

%install

%__rm -rf %{buildroot}
%__install -d %{buildroot}%{iconsdir}/%{name}
cd elementary_usu
%__cp -rf ./* %{buildroot}%{iconsdir}/%{name}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{iconsdir}/*

%changelog
* Sat Jul 10 2014 Mank <Mank1@seznam.cz> 8.0.7-3
- Update.
