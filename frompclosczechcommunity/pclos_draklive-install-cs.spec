Name: draklive-install-cs
Summary: A Live install for cs/sk locales
Version: 1.0.0
Release: 1
License: GPL v2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Requires: draklive-install
Source0: draklive-install-cs.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A Installer for CZ&SK Community (Gnome Edition)

%prep
%setup -c draklive-install-cs

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

cp -r * $RPM_BUILD_ROOT


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/etc/draklive-install.d/sysconfig/desktop
/etc/draklive-install.d/sysconfig/drakauth
/etc/draklive-install.d/sysconfig/finish-install
/etc/draklive-install.d/sysconfig/i18n
/etc/draklive-install.d/sysconfig/printing
/etc/draklive-install.d/sysconfig/system
/etc/draklive-install.d/sysconfig/userdrake
/etc/sysconfig/i18n
/etc/sysconfig/i18n_AL
/etc/xdg/user-dirs.defaults
/usr/bin/draklive-install-cs-sk
/usr/sbin/draklive-install-cs
/usr/sbin/draklive-install-sk
/usr/share/libDrakX/pixmaps/pclinuxos-finish-cs.png
/usr/share/libDrakX/pixmaps/pclinuxos-format-cs.png
/usr/share/libDrakX/pixmaps/pclinuxos-install-cs.png
/usr/share/libDrakX/pixmaps/pclinuxos-wizard-cs.png
/usr/share/mylivecd/halt.local
/usr/share/pclinuxos/pics/cz.png
/usr/share/pclinuxos/pics/exit.png
/usr/share/pclinuxos/pics/sk.png
/usr/share/applications/draklive-install-cs-sk.desktop




%changelog
* Sat Aug 11 2012 Mank <mank@pclinuxos.cz> 1.0.1-2
- 
