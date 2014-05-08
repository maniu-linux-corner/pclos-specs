Name: d14tmeter-KDE-SM
Summary: A Kde Service menu for dr14tmeter
Version: 0.0.1
Release: 2
License: GPL v2
URL: https://pclinuxos.cz
Group: Applications
BuildArch: noarch
Source0: dr14tmeter-KDE.tar.gz
Requires: dr14tmeter
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A Kde Service menu for dr14tmeter

%prep
%setup -c kde

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT


%install
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/
cp ./usr/share/icons/drlogo.png $RPM_BUILD_ROOT/usr/share/icons/drlogo.png
mkdir -p $RPM_BUILD_ROOT/usr/share/kde4/services/ServiceMenus/
cp -r ./usr/share/kde4/services/ServiceMenus/ $RPM_BUILD_ROOT/usr/share/kde4/services/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_datadir}/icons/*
%{_datadir}/kde4/*


%changelog
* Sat Mar 25 2011 Mank <mank@pclinuxos.cz> 0.0.1-1
- Kde 4 service menus (autor migelo <migelo@pclinuxos.cz> )
