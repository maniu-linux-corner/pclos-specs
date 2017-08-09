Name: installer-lxde
Summary: Jednoduhy Instaler pro CZ&SK (Light)
Version: 1.0.10
Release: 1
License: GPL v2
URL: https://https://github.com/pclinuxoscz/specs
BuildArch: noarch
Group: Applications
Conflicts: installer-kde
Conflicts: installer-gnome
Source0: installer-light-%{version}.tar.xz 
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Jednoduhy Instaler pro CZ&SK (Lxde)

%prep
%setup -c installer-light -n installer-lxde-%{version}

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
cp -r * $RPM_BUILD_ROOT

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/*
#%{_docdir}/*

%changelog
* Sat Aug 11 2012 Mank <Mank dot pclos at gmail dot com> 1.0.4-1
- Installer (Gnome)
