Name:           profile-sync-daemon 
Version:        5.75
Release:        5%{?dist}
Summary:        Offload browser profiles to RAM for speed a wear reduction
License:        MIT
URL:            https://github.com/graysky2/profile-sync-daemon 
Source0:        https://github.com/graysky2/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        rc.psd
Source2:        tmp-fstab
Source3:        psd.conf
BuildArch:      noarch
Requires:       rsync
Requires:       zenity

%description
Symlinks and syncs browser profiles to RAM via tmpfs which will reduce HDD/SDD
calls and speed-up browsers.

%prep
%setup -q

%build

%install
make install-bin install-man install-cron DESTDIR=%{buildroot}
%__mkdir -p $RPM_BUILD_ROOT/etc/rc.d/
%__mkdir -p $RPM_BUILD_ROOT/tmp/
%__cp %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/rc.psd
%__cp %{SOURCE2} $RPM_BUILD_ROOT/tmp/tmp-fstab
%__cp %{SOURCE3} $RPM_BUILD_ROOT/etc/psd.conf

%post
#!/bin/sh
ln -sf /etc/rc.d/rc.psd /etc/init.d/psd
ln -s /etc/rc.d/rc.psd /etc/rc0.d/K99psd
ln -s /etc/rc.d/rc.psd /etc/rc6.d/K99psd

zenity --question --text "Přidat do /etc/fstab ramdisk?";
if [ $? == 1 ]; then exit 0; fi

if [ -n "`cat /etc/fstab | grep " tmpfs "`" ]; then exit 0; else cd /tmp && cat tmp-fstab >> /etc/fstab; fi
	rm /tmp/tmp-fstab;

if [ -n "`cat /etc/fstab | grep "#tmpfs "`" ]; then
cp /etc/fstab /etc/fstab.zalohapsd
mv /etc/fstab /etc/fstab-psd
sed -e "s/#tmpfs/tmpfs/" /etc/fstab-psd > /etc/fstab ;
fi
exit 0

%preun
/etc/init.d/psd stop

%postun
#!/bin/sh
cp /etc/fstab /etc./fstab.zalohapsd
mv /etc/fstab /etc/fstab-psdrm
sed -e "s/tmpfs/#tmpfs/" /etc/fstab-psdrm > /etc/fstab


%files
%doc README*
%config(noreplace) %{_sysconfdir}/psd.conf
%{_bindir}/*
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_psd
%{_mandir}/man1/*.1*
/etc/rc.d/rc.psd
/etc/cron.hourly/psd-update
/tmp/tmp-fstab


%changelog
* Wed May 29 2015 Mank <mank@pclinuxos.cz> - 5.35-5
- Initial Package.
