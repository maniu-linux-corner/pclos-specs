Summary: 	PCLinuxOS 2012 theme
Name:    	pclos-2012-theme
Version: 	2012
Release: 	6
Source0: 	pclos-2012-theme.tar.xz

License: 	GPL
Group: 		Graphical desktop/KDE
URL:   	   	http://www.pclinuxos.com
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires(pre): plymouth
Requires(pre): bootsplash

%description
PCLinuxOS 2012 theme

%prep
%setup -n pclos-2012-theme
%build

%install
%__install -d %{buildroot}%{_datadir}/apps/
%__install -d %{buildroot}%{_datadir}/mcc/
%__install -d %{buildroot}%{_datadir}/plymouth/
%__cp -rf ./* %{buildroot}

%clean
%__rm -rf %{buildroot}

%pre
cd /boot
cp gfxmenu gfxmenu.orig
/usr/share/bootsplash/scripts/remove-theme

%post
/usr/sbin/plymouth-set-default-theme PCLinuxOS-2012
/usr/share/bootsplash/scripts/switch-themes PCLinuxOS-2012
SYSUSERS=`cat /etc/passwd | grep "/home/.*/bash" |grep "[0-9][0-9][0-9]" |cut -d: -f1`
for idx in $SYSUSERS; do cp /tmp/ksplashrc /home/$idx/.kde4/share/config/; done
rm /tmp/ksplashrc;

%postun
if [ "$1" = 0 ]; then
/usr/sbin/plymouth-set-default-theme text
/usr/share/bootsplash/scripts/switch-themes text
fi
%preun
if [ "$1" = 0 ]; then
cd /boot
cp gfxmenu.orig gfxmenu
#cd /usr/share/mcc/themes/
#cp -r default.orig default
fi
%files
%defattr(-,root,root)
%{_datadir}/apps/
%config %{_datadir}/mcc/
%{_datadir}/plymouth/
%config %{_datadir}/config/kdm/kdmrc
%config /boot/gfxmenu
%config /tmp/ksplashrc
%config /etc/mcc.conf

%changelog
* Fri Jul 28 2013 Mank <Mank dot pclos at gmail dot com> 2012-1
- Init spec

