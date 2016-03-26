%define nname nuvolaplayer3
Name: nuvolaplayer
Summary: Nuvola Player runs a web interface of cloud music services in its own window and provides integration with a Linux desktop .
Version: 3.0.1
Release: 1
License: 2 Cause BSD Licence/Mixed with Adobe's flash Licence
URL: http://nuvolaplayer.fenryxo.cz/home.html
Group: Sound/Players
Source0: nuvolaplayer-%{version}.tar.gz
#Source100: http://archive.canonical.com/pool/partner/a/adobe-flashplugin/adobe-flashplugin_11.2.202.346.orig.tar.gz
BuildRequires: vala
BuildRequires: %{_lib}rsvg2-devel
BuildRequires: libgee0.6-devel webkitgtk3-devel %{_lib}gtk+3.0-devel
Requires: glib-networking
#nspluginwrapper 

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Nuvola Player runs a web interface of cloud music services in its own window and provides integration with a Linux desktop (multimedia keys, system tray, media player applets, dock menu, notifications and more). Learn more about features of Nuvola Player and supported streaming services.

Nuvola Player is an open-source project licensed under 2-Clause BSD license and written in Vala (the core) and JavaScript (service integrations). Learn more about how to contribute to the project.

%prep
%setup -q

%build
./waf configure --prefix=/usr  --no-system-hooks --libdir %{_libdir}
#work around aroudn faulty waf
xvfb-run -a dbus-launch ./waf build
%install
#cd ..
#mkdir -p %{_prefix}/opt/nuvolaplayer/flash/
#tar -xvzf %{SOURCE100}
#cd adobe-flashplugin-11.2.202.346/i386
#%__install -d %{buildroot}/opt/nuvolaplayer/flash/
#%__cp libflashplayer.so %{buildroot}/opt/nuvolaplayer/flash/

./waf install --no-system-hooks --destdir=%{buildroot}

%clean

%post
#SYSUSERS=`cat /etc/passwd | grep "/home/.*/bash" |grep "[0-9][0-9][0-9]" |cut -d: -f1`
#for idx in $SYSUSERS;do
#	su $idx;	
#	nspluginwrapper -v -n -i /opt/nuvolaplayer/flash/libflashplayer.so
#done
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/nuvolaplayer3ctl
%{_bindir}/%{nname}
%{_libdir}/*
%{_datadir}/applications/%{nname}.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/%{nname}/*
%{_includedir}/nuvolaplayer3-1.0/*
%{_datadir}/appdata/nuvolaplayer3.appdata.xml
%{_datadir}/vala/vapi/*

%changelog
* Sat Mar 25 2014 Mank <mank@pclinuxos.cz> 2.3.1-1
- Init Spec
