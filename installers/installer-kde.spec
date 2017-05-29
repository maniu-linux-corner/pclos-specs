Name: installer-kde
Summary: Rychlá instalace programů
Version: 1.0.16.01
Release: 3
License: GPL v2
URL: https://https://github.com/pclinuxoscz/specs
BuildArch: noarch
Group: Applications
Requires: konsole
Source0: installer-kde-%{version}.tar.xz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

Requires: inxi

%description
Rychlá instalace programů

Aplikace zjednodušující instalaci vybraných programů, které jsou instalovány nejčastěji

%prep
%setup -c %{name}

%build
mkdir -p $RPM_BUILD_ROOT
cp -r * $RPM_BUILD_ROOT

%clean


%post

%files
%defattr(-,root,root)
%{_datadir}/polkit-1/actions/org.pclinuxos.installer.policy
%{_bindir}/installer
%{_bindir}/test-repo-mank
%{_sbindir}/*
%{_datadir}/*
%{_datadir}/pclinuxos/installer/icons/*
%{_datadir}/pclinuxos/repo/*
%{_docdir}/*
/root/.kde4/share/apps/konsole/installer.profile
%{_bindir}/inst-ver
/usr/libexec/installer

%changelog
* Sat Mar 13 2015 Mank <Mank dot pclos at gmail dot com> 1.0.9-1
- Installer updates
* Sat Mar 25 2013 Mank <Mank dot pclos at gmail dot com> 1.0.9-1
- Installer updates
