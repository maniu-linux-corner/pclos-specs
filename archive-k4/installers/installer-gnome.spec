Name: installer-gnome
Summary: Jednoduchý Instaler pro CZ&SK (Gnome)
Version: 1.0.12
Release: 2
License: GPL v2
URL: https://https://github.com/pclinuxoscz/specs
BuildArch: noarch
Group: Applications
Requires: xterm
Conflicts: installer-kde
Source0: installer-gnome-%{version}.tar.xz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Jednoduhy Instaler pro CZ&SK (Gnome)

%prep
%setup -c installer-gnome

%build
cp -r * $RPM_BUILD_ROOT

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/installer
%{_bindir}/test-repo-mank
%{_sbindir}/*
%{_datadir}/*

%changelog
* Sat Aug 11 2014 Mank <Mank dot pclos at gmail dot com 1.0.11-1
- Installer (Gnome)
