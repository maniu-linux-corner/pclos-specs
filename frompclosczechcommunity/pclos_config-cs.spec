Name: config-cs
Summary: Lokalizace systému do češtiny
Version: 1.0.0
Release: 10
License: GPL v2
URL: https://https://github.com/pclinuxoscz/specs
BuildArch: noarch
Group: Applications
Conflicts: config-cs-sk
Conflicts: config-sk
Source0: config-cs.tar.xz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Lokalizace systému do češtiny

Konfigurační soubory pro úplnou lokalizaci systému do češtiny
%prep
%setup -c config-cs

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

cp -r * $RPM_BUILD_ROOT

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
echo "Uživatelé ze Slovenska, nainstalujte si balíček config-sk.";

%posttrans
#!/bin/bash
echo "Lokalizace výrazů v /etc/rc.d/init.d/functions"
mv /etc/rc.d/init.d/functions /etc/rc.d/init.d/functions.orig
sed -e "s/OUTPUT_CHARSET=UTF-8 gprintf 'Booting the system.../OUTPUT_CHARSET=UTF-8 gprintf 'Startuji systém.../" -e "s/OUTPUT_CHARSET=UTF-8 gprintf 'Shutting down the system.../OUTPUT_CHARSET=UTF-8 gprintf 'Vypínám systém.../" -e "s/OUTPUT_CHARSET=UTF-8 gprintf 'Restarting the system.../OUTPUT_CHARSET=UTF-8 gprintf 'Restartuji systém.../" /etc/rc.d/init.d/functions.orig > /etc/rc.d/init.d/functions
echo "Lokalizace výrazů v /etc/samba/smb.conf"
mv /etc/samba/smb.conf /etc/samba/smb.conf.puvodni
sed -e "s/#   dos charset = 850/ dos charset = 852/" -e "s/#   unix charset = ISO8859-1/ unix charset = ISO8859-2/" -e "s/#  guest account = pcguest/  guest account = pcguest/" /etc/samba/smb.conf.puvodni > /etc/samba/smb.conf
#> /dev/null 2>&1

%files
%defattr(-,root,root)
/etc/rc.d/init.d/repo-mank
 /etc/skel/.config/user-dirs.dirs
 /etc/skel/.config/user-dirs.locale
 /etc/sysconfig/i18n
 /etc/sysconfig/i18n_AL
 /etc/xdg/user-dirs.defaults
 %{_datadir}/applications/clementine.desktop
 %{_datadir}/applications/drakfirewall.desktop
 %{_datadir}/applications/draknetcenter.desktop
 %{_datadir}/applications/localedrake-user.desktop
 %{_datadir}/applications/pclinuxos-drakconf.desktop
 %{_datadir}/applications/synaptic-kde.desktop
 %{_datadir}/applications/synaptic.desktop
  /.directory
 %{_datadir}/desktop-directories/mandriva-system-archiving.directory
 %{_datadir}/desktop-directories/mandriva-system-configuration.directory
 %{_datadir}/desktop-directories/mandriva-system-filetools.directory
%{_datadir}/desktop-directories/mandriva-system-monitoring.directory
%{_datadir}/desktop-directories/mandriva-system-terminals.directory
%{_datadir}/applications/synaptic-aktualizace.desktop
%{_datadir}/applications/synaptic-aktualizace-kde.desktop

%changelog
* Sat Aug 11 2012 Mank <Mank dot pclos at gmail dot coms> 1.0.0-1
-
