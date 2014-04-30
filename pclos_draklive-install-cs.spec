Name: draklive-install-kde-cs
Summary: Upravený instalátor systému pro CZ/SK LiveCD s prostředím KDE
Version: 1.0.0
Release: 3
License: GPL v2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Requires: draklive-install
Source0: draklive-install-kde-cs-%{version}.tar.xz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Upravený instalátor systému pro CZ/SK LiveCD s prostředím KDE
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
%{_bindir}/draklive-install-cs-sk
/usr/sbin/draklive-install-cs
/usr/sbin/draklive-install-sk
%{_datadir}/libDrakX/pixmaps/pclinuxos-finish-cs.png
%{_datadir}/libDrakX/pixmaps/pclinuxos-format-cs.png
%{_datadir}/libDrakX/pixmaps/pclinuxos-install-cs.png
%{_datadir}/libDrakX/pixmaps/pclinuxos-wizard-cs.png
%{_datadir}/mylivecd/halt.local
#%{_datadir}/pclinuxos/pics/cz.png
#%{_datadir}/pclinuxos/pics/exit.png
#%{_datadir}/pclinuxos/pics/sk.png
%{_datadir}/applications/draklive-install-cs-sk.desktop
/etc/pam.d/draklive-install-lock-storage-cs
/etc/pam.d/draklive-install-lock-storage-sk
%{_bindir}/draklive-install-lock-storage-cs
%{_bindir}/draklive-install-lock-storage-sk
%{_bindir}/slovensky-install
/usr/sbin/draklive-install-lock-storage-cs
/usr/sbin/draklive-install-lock-storage-sk
%{_datadir}/pclinuxos/*



%changelog
* Sat Aug 11 2012 Mank <Mank1@seznam.cz> 1.0.1-2
-
