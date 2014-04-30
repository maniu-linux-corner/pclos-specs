Name: screenfetch
Summary: A Screenshots Info Utility
Version: 1git30032014
Release: 1
License: GPL
URL: http://git.silverirc.com/cgit.cgi/screenfetch-dev.git/plain/screenfetch-dev
Group: Applications
Source0: screenFetch.tar.xz
BuildArch: noarch

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A Screenshots Info Utility

%prep
%setup -n screenFetch

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/screenfetch/
cp screenfetch-dev $RPM_BUILD_ROOT/usr/bin/screenfetch-dev
cp COPYING $RPM_BUILD_ROOT/usr/share/doc/screenfetch/COPYING
cp CHANGELOG $RPM_BUILD_ROOT/usr/share/doc/screenfetch/CHANGELOG
cp README.mkdn $RPM_BUILD_ROOT/usr/share/doc/screenfetch/README.mkdn


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_datadir}/doc/screenfetch/*
%{_bindir}/screenfetch-dev

%changelog
* Sat Mar 25 2013 Mank <Mank1@seznam.cz> 1git14072013-1
- Init Spec
