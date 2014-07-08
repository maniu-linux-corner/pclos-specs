Name: config-sk
Summary: Lokalizace systému do slovenštiny
Version: 1.0.1
Release: 12
License: GPL v2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Conflicts: config-cs
Source0: config-sk-%{version}-12.tar.xz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Lokalizace systému do slovenštiny

Konfigurační soubory pro úplnou lokalizaci systému do slovenštiny
%prep
%setup -c config-sk

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

cp -r * $RPM_BUILD_ROOT

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%posttrans
#! /bin/sh

echo "Lokalizace výrazů v /etc/rc.d/init.d/functions"
mv /etc/rc.d/init.d/functions /etc/rc.d/init.d/functions.orig
sed -e "s/OUTPUT_CHARSET=UTF-8 gprintf 'Booting the system.../OUTPUT_CHARSET=UTF-8 gprintf 'Spúšťam systém.../" -e "s/OUTPUT_CHARSET=UTF-8 gprintf 'Shutting down the system.../OUTPUT_CHARSET=UTF-8 gprintf 'Vypínam systém.../" -e "s/OUTPUT_CHARSET=UTF-8 gprintf 'Restarting the system.../OUTPUT_CHARSET=UTF-8 gprintf 'Reštartujem systém.../" /etc/rc.d/init.d/functions.orig > /etc/rc.d/init.d/functions



if [ -n "`cat /etc/samba/smb.conf | grep "dos charset = 850"`" ]; then SMB=0; else SMB=1; fi
if [ $SMB -eq 0 ];then
  echo "Lokalizace výrazů v /etc/samba/smb.conf" &&
  mv /etc/samba/smb.conf /etc/samba/smb.conf.puvodni &&
  sed -e "s/#   dos charset = 850/ dos charset = 852/" -e "s/#   unix charset = ISO8859-1/ unix charset = ISO8859-2/" -e "s/#  guest account = pcguest/  guest account = pcguest/" /etc/samba/smb.conf.puvodni > /etc/samba/smb.conf
fi

ARCH=`getconf LONG_BIT` 
CMDMR1=`ls /etc/apt/sources.list.d`
CMDMR2=`cp /usr/share/pclinuxos/repo/cs-sk-$ARCH.list /etc/apt/sources.list.d && mv /etc/apt/sources.list.d/cs-sk-$ARCH.list /etc/apt/sources.list.d/cs-sk.list`

if [ "$CMDMR1" = 'cs-sk.list' ]; then REPOLIST=1 ; else REPOLIST=0 ; fi
if [ $REPOLIST -eq 0 ];then $CMDMR2 && rm -f /etc/rc.d/rc3.d/S99repo-mank /etc/rc.d/rc4.d/S99repo-mank /etc/rc.d/rc2.d/S99repo-mank /etc/rc.d/init.d/repo-mank /etc/rc.d/rc5.d/S99repo-mank; fi

if [ -n "`cat /etc/apt/sources.list | grep " czech-noarch "`" ]; then IS=0; else IS=1; fi
if [ $IS -eq 0 ]; then rm -f /etc/apt/sources.list && cp /usr/share/pclinuxos/repo/sources-$ARCH.list /etc/apt && mv /etc/apt/sources-$ARCH.list /etc/apt/sources.list; fi

exit 0

%files
%defattr(-,root,root)
%{_sysconfdir}/skel/.config/user-dirs.dirs
%{_sysconfdir}/skel/.config/user-dirs.locale
%{_sysconfdir}/sysconfig/i18n
%{_sysconfdir}/sysconfig/i18n_AL
%{_sysconfdir}/xdg/user-dirs.defaults
%{_datadir}/applications/clementine.desktop
%{_datadir}/applications/drakfirewall.desktop
%{_datadir}/applications/draknetcenter.desktop
%{_datadir}/applications/localedrake-user.desktop
%{_datadir}/applications/pclinuxos-drakconf.desktop
%{_datadir}/applications/synaptic-kde.desktop
%{_datadir}/applications/synaptic.desktop
%{_datadir}/applications/synaptic-aktualizace.desktop
/.directory
%{_datadir}/desktop-directories/mandriva-system-archiving.directory
%{_datadir}/desktop-directories/mandriva-system-configuration.directory
%{_datadir}/desktop-directories/mandriva-system-filetools.directory
%{_datadir}/desktop-directories/mandriva-system-monitoring.directory
%{_datadir}/desktop-directories/mandriva-system-terminals.directory
%{_datadir}/locale/sk/LC_MESSAGES/synaptic.mo
%{_datadir}/applications/synaptic-aktualizace-kde.desktop
%{_datadir}/pclinuxos/repo/*

%changelog
* Sat Aug 11 2012 Mank <mank@pclinuxos.cz> 1.0.1-11
-
