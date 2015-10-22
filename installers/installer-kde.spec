Name: installer-kde
Summary: Rychlá instalace programů
Version: 1.0.12
Release: 1
License: GPL v2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Requires: xterm
Source0: installer-kde-%{version}.tar.xz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Rychlá instalace programů

Aplikace zjednodušující instalaci vybraných programů, které jsou instalovány nejčastěji

%prep
%setup -c installer-kde

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
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
%{_datadir}/pclinuxos/installer/icons/internet/*
%{_datadir}/pclinuxos/repo/*
%{_docdir}/*


%changelog
* Sat Mar 25 2013 Mank <mank@pclinuxos.cz> 1.0.9-1
- Installer updates
