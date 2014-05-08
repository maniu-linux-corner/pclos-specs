Name: installer-kde
Summary: Rychlá instalace progamů
Version: 1.0.8
Release: 1
License: GPLv2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Source0: installer-kde-%{version}.tar.xz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Rychlá instalace programů

Aplikace zjednodušující instalaci vybraných programů, které jsou instalovány nejčastěji

%prep
%setup -c installer-kde

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
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
* Sat Mar 25 2013 Mank <mank@pclinuxos.cz> 1.0.8-1
- Installer
