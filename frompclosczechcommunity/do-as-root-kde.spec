Name: DoAsRoot-cs-sk
Summary: Do As Root je servisní menu pro KDE, které usnadňuje použití práv správce pro mazání, editaci a otevírání složek a souborů.
Version: 2.1.1
Release: 1
License: GPL
URL: http://www.kde-apps.org/content/show.php/Open+Dolphin+as+Root?content=102548
Group: Applications/KDE
Source0: DoAsRoot-cs-sk-2.1.1.tar.xz
Requires: glibc
Requires: kde-baseapps-core
Requires: libstdc++6
Conflicts: DoAsRoot
BuildArch: noarch
Autoprov: No
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Do As Root je servisní menu pro KDE, které usnadňuje použití práv správce pro mazání, editaci a otevírání složek a souborů.

%prep
%setup

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%install
cp -r ./ $RPM_BUILD_ROOT/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/usr/share/kde4/services/ServiceMenus/*
/.directory
%changelog
* Sat Mar 25 2011 Mank <mank@pclinuxos.cz> 0.0.1-1
- do-as-root: Version pre: 0.0.1
