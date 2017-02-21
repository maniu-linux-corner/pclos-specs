Name:           wildfire-icons
Version:        1.0.0
Release:        1
Summary:        Minimalism And Realism Mix and match, Meego And iOS icon Style"

License:        GPL
URL:            https://xenlism.github.io/wildfire
Source0:        wildfire.tar.xz

%description


%prep
%setup -q -n wildfire

%install
install -dm755 "%{buildroot}/usr/share/icons"
cd "icons/"
cp -r * "%{buildroot}/usr/share/icons/";
find "%{buildroot}/usr/share/icons" -type d -exec chmod 755 '{}' \;
find "%{buildroot}/usr/share/icons" -type f -exec chmod 644 '{}' \;
install -dm755 "%{buildroot}/usr/share/backgrounds/gnome/"
cd "../wallpapers/";
install -dm755 "%{buildroot}/usr/share/backgrounds/xenlism/";
cp -r * "%{buildroot}/usr/share/backgrounds/xenlism/";
find "%{buildroot}/usr/share/backgrounds/xenlism/" -type d -exec chmod 755 '{}' \;
find "%{buildroot}/usr/share/backgrounds/xenlism/" -type f -exec chmod 644 '{}' \;
cd "../background-properties/";
install -dm755 "%{buildroot}/usr/share/gnome-background-properties/";
cp -r * "%{buildroot}/usr/share/gnome-background-properties/";
find "%{buildroot}/usr/share/gnome-background-properties/" -type d -exec chmod 755 '{}' \;
find "%{buildroot}/usr/share/gnome-background-properties/" -type f -exec chmod 644 '{}' \;

%post
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-Day'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-FriDay'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-MidNight'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-MonDay'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-Night'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-SaturDay'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-SunDay'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-ThursDay'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-TuesDay'
/usr/bin/gtk-update-icon-cache -f '/usr/share/icons/Xenlism-Wildfire-WednesDay'

%files
%{_datadir}/icons/*
%{_datadir}/backgrounds/xenlism/*
%{_datadir}/gnome-background-properties/*


%changelog
* Sun Feb 19 2017 mank
- 
