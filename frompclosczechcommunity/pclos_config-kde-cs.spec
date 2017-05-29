Name: kde4-config-cs
Summary: Konfigurace prostředí KDE SC pro české uživatele
Version: 1.0.1
Release: 5
License: GPL v2
URL: https://https://github.com/pclinuxoscz/specs
BuildArch: noarch
Group: Applications
Conflicts: kde4-config
Conflicts: kde4-config-fm
Conflicts: kde4-config-legacy
Conflicts: kde4-config-sk
Requires: oxygen-gtk
Source0: kde4-config-cs.tar.xz
Source1: kdmrc
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Konfigurace prostředí KDE pro české uživatele

Konfigurační soubory, které lokalizují prostředí KDE do češtiny

%prep
%setup -c kde4-config-cs

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

cp -r * $RPM_BUILD_ROOT

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
sh /tmp/en-na-cs-kde.sh
rm /tmp/en-na-cs-kde.sh

%files
%defattr(-,root,root)
/usr/share/config/kdm/kdmrc
/etc/skel/.config/user-dirs.dirs
   /etc/skel/.config/user-dirs.locale
   /etc/skel/.gtkrc-2.0
   /etc/skel/.kde4/Autostart/noblank.sh
   /etc/skel/.kde4/share/apps/dolphin/dolphinui.rc
   /etc/skel/.kde4/share/apps/dolphin/view_properties/global/.directory
   /etc/skel/.kde4/share/apps/dolphinpart/dolphinpart.rc
   /etc/skel/.kde4/share/apps/katepart/katepartsimpleui.rc
   /etc/skel/.kde4/share/apps/katepart/katepartui.rc
   /etc/skel/.kde4/share/apps/konqueror/bookmarks.xml
   /etc/skel/.kde4/share/apps/konqueror/konqueror.rc
   /etc/skel/.kde4/share/apps/konqueror/kpartplugins/searchbar.rc
   /etc/skel/.kde4/share/apps/konqueror/profiles/filemanagement
   /etc/skel/.kde4/share/apps/konqueror/profiles/webbrowsing
   /etc/skel/.kde4/share/apps/konqueror/view_properties/global/.directory
   /etc/skel/.kde4/share/apps/konqueror/view_properties/local/usr/share/icons/.directory
   /etc/skel/.kde4/share/apps/konsole/Linux.colorscheme
   /etc/skel/.kde4/share/apps/konsole/Shell.profile
   /etc/skel/.kde4/share/apps/kwrite/kwriteui.rc
   /etc/skel/.kde4/share/apps/nsplugins/cache
   /etc/skel/.kde4/share/apps/nsplugins/pluginsinfo
   /etc/skel/.kde4/share/config/activitymanagerrc
   /etc/skel/.kde4/share/config/akonadi-firstrunrc
   /etc/skel/.kde4/share/config/akonadi_nepomuk_feederrc
   /etc/skel/.kde4/share/config/dirfilterrc
   /etc/skel/.kde4/share/config/dolphinrc
   /etc/skel/.kde4/share/config/emaildefaults
   /etc/skel/.kde4/share/config/filetypesrc
   /etc/skel/.kde4/share/config/gtkrc
   /etc/skel/.kde4/share/config/gtkrc-2.0
   /etc/skel/.kde4/share/config/kaddressbookmigratorrc
   /etc/skel/.kde4/share/config/kalarmrc
   /etc/skel/.kde4/share/config/kbanner.kssrc
   /etc/skel/.kde4/share/config/kcmdisplayrc
   /etc/skel/.kde4/share/config/kcminputrc
   /etc/skel/.kde4/share/config/kcmnspluginrc
   /etc/skel/.kde4/share/config/kconf_updaterc
   /etc/skel/.kde4/share/config/kdebugrc
   /etc/skel/.kde4/share/config/kdedrc
   /etc/skel/.kde4/share/config/kdeglobals
   /etc/skel/.kde4/share/config/kdeglobals_AL
   /etc/skel/.kde4/share/config/kglobalshortcutsrc
   /etc/skel/.kde4/share/config/khotkeysrc
   /etc/skel/.kde4/share/config/kickoffrc
   /etc/skel/.kde4/share/config/kiorc
   /etc/skel/.kde4/share/config/kmetainformationrc
   /etc/skel/.kde4/share/config/knfsshare
   /etc/skel/.kde4/share/config/knotifyrc
   /etc/skel/.kde4/share/config/konqsidebartngrc
   /etc/skel/.kde4/share/config/konquerorrc
   /etc/skel/.kde4/share/config/konsolerc
   /etc/skel/.kde4/share/config/kres-migratorrc
   /etc/skel/.kde4/share/config/krunnerrc
   /etc/skel/.kde4/share/config/kscreensaverrc
   /etc/skel/.kde4/share/config/kservicemenurc
   /etc/skel/.kde4/share/config/ksmserverrc
   /etc/skel/.kde4/share/config/ktimezonedrc
   /etc/skel/.kde4/share/config/kwinrc
   /etc/skel/.kde4/share/config/kwinrulesrc
   /etc/skel/.kde4/share/config/nepomukserverrc
   /etc/skel/.kde4/share/config/plasma-appletsrc
   /etc/skel/.kde4/share/config/plasma-desktop-appletsrc
   /etc/skel/.kde4/share/config/plasma-desktoprc
   /etc/skel/.kde4/share/config/plasmarc
   /etc/skel/.kde4/share/config/powerdevil2profilesrc
   /etc/skel/.kde4/share/config/powerdevilrc
   /etc/skel/.kde4/share/config/powermanagementprofilesrc
   /etc/skel/.kde4/share/config/startupconfig
   /etc/skel/.kde4/share/config/startupconfigfiles
   /etc/skel/.kde4/share/config/startupconfigkeys
   /etc/skel/.kde4/share/config/systemsettingsrc
   /etc/skel/.kde4/share/config/workspaceoptionsrc
   /etc/skel/.kde4/share/kde4/services/nsplugin.desktop
   /etc/skel/.kderc
   /etc/skel/.local/screen-configurations.xml
   /etc/skel/.local/share/applications/mimeapps.list
   /etc/skel/.local/share/mime/XMLnamespaces
   /etc/skel/.local/share/mime/aliases
   /etc/skel/.local/share/mime/application/asx.xml
   /etc/skel/.local/share/mime/application/futuresplash.xml
   /etc/skel/.local/share/mime/application/vnd.rn-realaudio.xml
   /etc/skel/.local/share/mime/application/x-drm-v2.xml
   /etc/skel/.local/share/mime/application/x-google-vlc-plugin.xml
   /etc/skel/.local/share/mime/application/x-mplayer2.xml
   /etc/skel/.local/share/mime/application/x-ms-wmp.xml
   /etc/skel/.local/share/mime/application/x-ms-wmv.xml
   /etc/skel/.local/share/mime/application/x-nsv-vp3-mp3.xml
   /etc/skel/.local/share/mime/application/x-quicktimeplayer.xml
   /etc/skel/.local/share/mime/application/x-skype.xml
   /etc/skel/.local/share/mime/audio/flac.xml
   /etc/skel/.local/share/mime/audio/mp3.xml
   /etc/skel/.local/share/mime/audio/mpeg2.xml
   /etc/skel/.local/share/mime/audio/mpeg3.xml
   /etc/skel/.local/share/mime/audio/wav.xml
   /etc/skel/.local/share/mime/audio/x-basic.xml
   /etc/skel/.local/share/mime/audio/x-mp4.xml
   /etc/skel/.local/share/mime/audio/x-mpeg.xml
   /etc/skel/.local/share/mime/audio/x-mpeg2.xml
   /etc/skel/.local/share/mime/audio/x-mpeg3.xml
   /etc/skel/.local/share/mime/audio/x-ms-wax.xml
   /etc/skel/.local/share/mime/audio/x-ms-wmv.xml
   /etc/skel/.local/share/mime/audio/x-ogg.xml
   /etc/skel/.local/share/mime/audio/x-pn-realaudio.xml
   /etc/skel/.local/share/mime/audio/x-realaudio.xml
   /etc/skel/.local/share/mime/generic-icons
   /etc/skel/.local/share/mime/globs
   /etc/skel/.local/share/mime/globs2
   /etc/skel/.local/share/mime/icons
   /etc/skel/.local/share/mime/magic
   /etc/skel/.local/share/mime/mime.cache
   /etc/skel/.local/share/mime/packages/application-asx.xml
   /etc/skel/.local/share/mime/packages/application-futuresplash.xml
   /etc/skel/.local/share/mime/packages/application-vnd.rn-realaudio.xml
   /etc/skel/.local/share/mime/packages/application-x-drm-v2.xml
   /etc/skel/.local/share/mime/packages/application-x-google-vlc-plugin.xml
   /etc/skel/.local/share/mime/packages/application-x-mplayer2.xml
   /etc/skel/.local/share/mime/packages/application-x-ms-wmp.xml
   /etc/skel/.local/share/mime/packages/application-x-ms-wmv.xml
   /etc/skel/.local/share/mime/packages/application-x-nsv-vp3-mp3.xml
   /etc/skel/.local/share/mime/packages/application-x-quicktimeplayer.xml
   /etc/skel/.local/share/mime/packages/application-x-skype.xml
   /etc/skel/.local/share/mime/packages/audio-flac.xml
   /etc/skel/.local/share/mime/packages/audio-mp3.xml
   /etc/skel/.local/share/mime/packages/audio-mpeg2.xml
   /etc/skel/.local/share/mime/packages/audio-mpeg3.xml
   /etc/skel/.local/share/mime/packages/audio-wav.xml
   /etc/skel/.local/share/mime/packages/audio-x-basic.xml
   /etc/skel/.local/share/mime/packages/audio-x-mp4.xml
   /etc/skel/.local/share/mime/packages/audio-x-mpeg.xml
   /etc/skel/.local/share/mime/packages/audio-x-mpeg2.xml
   /etc/skel/.local/share/mime/packages/audio-x-mpeg3.xml
   /etc/skel/.local/share/mime/packages/audio-x-ms-wax.xml
   /etc/skel/.local/share/mime/packages/audio-x-ms-wmv.xml
   /etc/skel/.local/share/mime/packages/audio-x-ogg.xml
   /etc/skel/.local/share/mime/packages/audio-x-pn-realaudio.xml
   /etc/skel/.local/share/mime/packages/audio-x-realaudio.xml
   /etc/skel/.local/share/mime/packages/video-divx.xml
   /etc/skel/.local/share/mime/packages/video-fli.xml
   /etc/skel/.local/share/mime/packages/video-msvideo.xml
   /etc/skel/.local/share/mime/packages/video-vnd.divx.xml
   /etc/skel/.local/share/mime/packages/video-vnd.vivo.xml
   /etc/skel/.local/share/mime/packages/video-x-fli.xml
   /etc/skel/.local/share/mime/packages/video-x-mpeg.xml
   /etc/skel/.local/share/mime/packages/video-x-mpeg2.xml
   /etc/skel/.local/share/mime/packages/video-x-ms-asf-plugin.xml
   /etc/skel/.local/share/mime/packages/video-x-ms-wm.xml
   /etc/skel/.local/share/mime/packages/video-x-ms-wvx.xml
   /etc/skel/.local/share/mime/packages/video-x-quicktime.xml
   /etc/skel/.local/share/mime/subclasses
   /etc/skel/.local/share/mime/treemagic
   /etc/skel/.local/share/mime/types
   /etc/skel/.local/share/mime/video/divx.xml
   /etc/skel/.local/share/mime/video/fli.xml
   /etc/skel/.local/share/mime/video/msvideo.xml
   /etc/skel/.local/share/mime/video/vnd.divx.xml
   /etc/skel/.local/share/mime/video/vnd.vivo.xml
   /etc/skel/.local/share/mime/video/x-fli.xml
   /etc/skel/.local/share/mime/video/x-mpeg.xml
   /etc/skel/.local/share/mime/video/x-mpeg2.xml
   /etc/skel/.local/share/mime/video/x-ms-asf-plugin.xml
   /etc/skel/.local/share/mime/video/x-ms-wm.xml
   /etc/skel/.local/share/mime/video/x-ms-wvx.xml
   /etc/skel/.local/share/mime/video/x-quicktime.xml
   /etc/skel/Dokumenty/.directory
/etc/skel/Hudba/.directory
/etc/skel/Obrázky/.directory
/etc/skel/Plocha/.directory
/etc/skel/Plocha/Home.desktop
/etc/skel/Stažené/.directory
/etc/skel/Videa/.directory
/tmp/en-na-cs-kde.sh
/usr/share/apps/color-schemes/Mdm_dust.colors
   /.directory
   /etc/skel/.bash_logout
   /etc/skel/.bash_profile
   /etc/skel/.bashrc
   /etc/skel/.config/Trolltech.conf
   /etc/skel/.config/oxygen-gtk/argb-apps.conf
   /etc/skel/.gconf/apps/gedit-2/preferences/%gconf.xml
   /etc/skel/.gconf/apps/gedit-2/preferences/ui/%gconf.xml
   /etc/skel/.gconf/apps/gedit-2/preferences/ui/statusbar/%gconf.xml
   /etc/skel/.gconf/desktop/gnome/url-handlers/http/%gconf.xml
   /etc/skel/.gconf/desktop/gnome/url-handlers/https/%gconf.xml
   /etc/skel/.gconf/desktop/gnome/url-handlers/mailto/%gconf.xml
   /etc/skel/.kde4/share/apps/activitymanager/resources/database
   /etc/skel/.kde4/share/apps/kabc/std.vcf
   /etc/skel/.kde4/share/apps/kabc/std.vcf_6
   /etc/skel/.kde4/share/config/granatierrc
   /etc/skel/.kde4/share/config/kbouncerc
   /etc/skel/.kde4/share/config/kbreakoutrc
   /etc/skel/.kde4/share/config/kded_device_automounterrc
   /etc/skel/.kde4/share/config/kdiamondrc
   /etc/skel/.kde4/share/config/kget_multisegkiofactory.rc
   /etc/skel/.kde4/share/config/kgetrc
   /etc/skel/.kde4/share/config/killbotsrc
   /etc/skel/.kde4/share/config/kio_desktoprc
   /etc/skel/.kde4/share/config/kio_httprc
   /etc/skel/.kde4/share/config/kioslaverc
   /etc/skel/.kde4/share/config/klickety
   /etc/skel/.kde4/share/config/klines
   /etc/skel/.kde4/share/config/klipperrc
   /etc/skel/.kde4/share/config/kmines
   /etc/skel/.kde4/share/config/knetwalk
   /etc/skel/.kde4/share/config/korgacrc
   /etc/skel/.kde4/share/config/kpat
   /etc/skel/.kde4/share/config/kuriikwsfilterrc
   /etc/skel/.kde4/share/config/specialmailcollectionsrc
   /etc/skel/.xbindkeysrc
   /etc/skel/Plocha/trash.desktop


%changelog
* Sat Aug 11 2012 Mank <Mank dot pclos at gmail dot coms> 1.0.0-1
-
