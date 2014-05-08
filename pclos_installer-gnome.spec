Name: installer-gnome
Summary: A Installer for CZ&SK Community (Gnome Edition)
Version: 1.0.4
Release: 3
License: GPL v2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Conflicts: installer-kde
Source0: installer-gnome-%{version}.tar.xz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A Installer for CZ&SK Community (Gnome Edition)

%prep
%setup

%build
mkdir -p $RPM_BUILD_ROOT/usr/
./install.sh $RPM_BUILD_ROOT/usr/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/installer
%{_sbindir}/*
%{_datadir}/*
%{_docdir}/*

%changelog
* Sat Aug 11 2012 Mank <mank@pclinuxos.cz> 1.0.1-2
- Installer (Gnome)
