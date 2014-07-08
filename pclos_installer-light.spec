Name: installer-lxde
Summary: Jednoduchý Instaler pro CZ&SK (Light)
Version: 1.0.12
Release: 1
License: GPL v2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Requires: xterm
Conflicts: installer-kde
Conflicts: installer-gnome
Source0: installer-lxde-%{version}.tar.xz 
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Jednoduhy Instaler pro CZ&SK (Lxde)

%prep
%setup -c installer-lxde -n installer-lxde-%{version}

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
cp -r * $RPM_BUILD_ROOT

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/*
%{_bindir}/test-repo-mank
%{_sbindir}/*
%{_datadir}/*

%changelog
* Sat Aug 11 2012 Mank <mank@pclinuxos.cz> 1.0.4-1
- Installer (Gnome)
