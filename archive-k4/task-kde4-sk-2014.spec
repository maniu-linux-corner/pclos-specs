Name: task-kde4-sk-2014
Summary: Task pro KDE SC SK
Version: 2014
Release: 4
License: LGPLv3
URL: http://www.https://github.com/pclinuxoscz/specs/
Group: Tasks
BuildArch: noarch
Requires: DoAsRoot-cs-sk kde4-config-sk-2014 config-sk akonadi kde-smooth-tasks kde-baseapps-core kde-baseapps-dolphin 
Requires: kde-runtime kde-workspace-core kdelibs  kde-multimedia-kmix  kde-pimlibs  kdm  kwebkitpart  
Requires: oxygen-icon-theme   plasma-desktoptheme-Elly  soprano  soprano-plugin-common
Requires: strigi  virtuoso-opensource  xsettings-kde  kde-graphics-libs  kde-plasma-addons  kwrite  konsole  kde-baseapps-plasma
Requires: installer-kde iso-codes transcode rarlinux lm_sensors detox
Conflicts: kde4-config-sk kde4-config-cs task-kde4-sk task-kde4-cs task-kde4-cs-2014
Requires: kde-smooth-tasks 
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Task pro SK KDE

%post
yes "" | sensors-detect

%files

%changelog
* Sat Mar 25 2012 Mank <Mank dot pclos at gmail dot com> 2.2.0.35-1
- initial task packages
