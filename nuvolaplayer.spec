Name: nuvolaplayer
Summary: Nuvola Player runs a web interface of cloud music services in its own window and provides integration with a Linux desktop .
Version: 2.3.1
Release: 3
License: 2 Cause BSD Licence/Mixed with Adobe's flash Licence
URL: http://nuvolaplayer.fenryxo.cz/home.html
Group: Sound/Players
Source0: nuvolaplayer-%{version}.tar.gz
Source100: http://archive.canonical.com/pool/partner/a/adobe-flashplugin/adobe-flashplugin_11.2.202.346.orig.tar.gz
BuildRequires: vala
BuildRequires: %{_lib}rsvg2-devel
BuildRequires: libgee0.6-devel webkitgtk3-devel %{_lib}gtk+3.0-devel
Requires: nspluginwrapper glib-networking

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Nuvola Player runs a web interface of cloud music services in its own window and provides integration with a Linux desktop (multimedia keys, system tray, media player applets, dock menu, notifications and more). Learn more about features of Nuvola Player and supported streaming services.

Nuvola Player is an open-source project licensed under 2-Clause BSD license and written in Vala (the core) and JavaScript (service integrations). Learn more about how to contribute to the project.

%prep
%setup -q

%build
./waf configure --prefix=%{_prefix}/usr --no-unity-quick-list --skip-tests --experimental
#work around aroudn faulty waf
xvfb-run -a dbus-launch ./waf build
%install
cd ..
mkdir -p %{_prefix}/opt/nuvolaplayer/flash/
tar -xvzf %{SOURCE100}
cd adobe-flashplugin-11.2.202.346/i386
%__install -d %{buildroot}/opt/nuvolaplayer/flash/
%__cp libflashplayer.so %{buildroot}/opt/nuvolaplayer/flash/

./waf install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
SYSUSERS=`cat /etc/passwd | grep "/home/.*/bash" |grep "[0-9][0-9][0-9]" |cut -d: -f1`
for idx in $SYSUSERS;do
	su $idx;	
	nspluginwrapper -v -n -i /opt/nuvolaplayer/flash/libflashplayer.so
done


%files
%defattr(-,root,root)
%{_bindir}//%{name}
%{_bindir}/%{name}-client
%{_libdir}/lib%{name}private.so
%{_libdir}/%{name}/lib%{name}private.so
%{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/%{name}.tsocks
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome-control-center/default-apps/%{name}.xml
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/locale/ar/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/bg/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/ca/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/cs/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/el/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/es/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/et/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/eu/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/fi/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/hu/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/ia/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/it/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/ja/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/ms/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/nl/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/oc/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/pl/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/pt/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/pt_BR/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/ru/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/sl/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/sq/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/sv/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/te/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/tr/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.mo
   %{_datadir}/locale/zh_TW/LC_MESSAGES/%{name}.mo
   %{_datadir}/%{name}/audio/audiotest.mp3
   %{_datadir}/%{name}/dev/newservicetemplate/description.html
   %{_datadir}/%{name}/dev/newservicetemplate/integration.js
   %{_datadir}/%{name}/dev/newservicetemplate/metadata.conf
   %{_datadir}/%{name}/html/Audio.html
   %{_datadir}/%{name}/html/Flash.html
   %{_datadir}/%{name}/html/Service.html
   %{_datadir}/%{name}/html/Settings.html
   %{_datadir}/%{name}/html/_resources/screen.css
   %{_datadir}/%{name}/js/audio.js
   %{_datadir}/%{name}/js/compat-1.x.js
   %{_datadir}/%{name}/js/flash_detect.js
   %{_datadir}/%{name}/js/flash_support.js
   %{_datadir}/%{name}/js/forms.js
   %{_datadir}/%{name}/js/main.js
   %{_datadir}/%{name}/services/amazon/description.html
   %{_datadir}/%{name}/services/amazon/home.html
   %{_datadir}/%{name}/services/amazon/icon.png
   %{_datadir}/%{name}/services/amazon/integration.js
   %{_datadir}/%{name}/services/amazon/metadata.conf
   %{_datadir}/%{name}/services/amazon/settings.js
   %{_datadir}/%{name}/services/bandcamp/description.html
   %{_datadir}/%{name}/services/bandcamp/integration.js
   %{_datadir}/%{name}/services/bandcamp/metadata.conf
   %{_datadir}/%{name}/services/deezer/description.html
   %{_datadir}/%{name}/services/deezer/icon.png
   %{_datadir}/%{name}/services/deezer/integration.js
   %{_datadir}/%{name}/services/deezer/metadata.conf
   %{_datadir}/%{name}/services/eighttracks/description.html
   %{_datadir}/%{name}/services/eighttracks/icon.png
   %{_datadir}/%{name}/services/eighttracks/integration.js
   %{_datadir}/%{name}/services/eighttracks/metadata.conf
   %{_datadir}/%{name}/services/googleplay/description.html
   %{_datadir}/%{name}/services/googleplay/icon.png
   %{_datadir}/%{name}/services/googleplay/integration.js
   %{_datadir}/%{name}/services/googleplay/metadata.conf
   %{_datadir}/%{name}/services/googleplay/settings.js
   %{_datadir}/%{name}/services/grooveshark/description.html
   %{_datadir}/%{name}/services/grooveshark/icon.png
   %{_datadir}/%{name}/services/grooveshark/integration.js
   %{_datadir}/%{name}/services/grooveshark/metadata.conf
   %{_datadir}/%{name}/services/hypem/description.html
   %{_datadir}/%{name}/services/hypem/icon.png
   %{_datadir}/%{name}/services/hypem/integration.js
   %{_datadir}/%{name}/services/hypem/metadata.conf
   %{_datadir}/%{name}/services/pandora/description.html
   %{_datadir}/%{name}/services/pandora/icon.png
%{_datadir}/%{name}/services/pandora/integration.js
%{_datadir}/%{name}/services/pandora/metadata.conf
%{_datadir}/%{name}/services/rdio/description.html
%{_datadir}/%{name}/services/rdio/icon.png
%{_datadir}/%{name}/services/rdio/integration.js
%{_datadir}/%{name}/services/rdio/metadata.conf
%{_datadir}/%{name}/ui/menubar.xml
%{_datadir}/%{name}/ui/popup_menu.xml
/opt/nuvolaplayer/flash/libflashplayer.so



%changelog
* Sat Mar 25 2014 Mank <Mank1@seznam.cz> 2.3.1-1
- Init Spec
