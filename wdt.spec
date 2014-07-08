Name: wdt
Summary: A Web Develops Tools
Version: 2.6.6
Release: 5
License: GPL v2
URL: https://launchpad.net/~petrakis/+archive/wdt-main
BuildArch: noarch
Group: Applications
Source0: WDT.tar.gz
Source1: wdt.desktop
Requires: python
Requires: python-webkitgtk
Requires: webkit-jsc
Requires: pyxdg
Requires: python-feedparser
Requires: optipng
Requires: advancecomp
Requires: libgmime2.2
Requires: gnome-menus2

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A Web Develops Tools

%prep
%setup -n WDT

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/
./installer.sh $RPM_BUILD_ROOT/usr/share/
cp start/wdt $RPM_BUILD_ROOT/usr/bin/wdt
install -D -m644 "%{SOURCE1}" "$RPM_BUILD_ROOT/usr/share/applications/wdt.desktop"

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/wdt
%{_datadir}/*

%changelog
* Sat Mar 25 2012 Mank <Mank1@seznam.cz> 2.6.6-3
- WDT Repair Desktop Icons
* Sat Mar 25 2012 Mank <Mank1@seznam.cz> 2.6.6-2
- WDT
