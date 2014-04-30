Name: task-kde4-sk
Summary: Task pro KDE SC SK
Version: 1.0.2
Release: 1
License: LGPLv3
URL: http://www.pclinuxos.cz/
Group: Tasks
BuildArch: noarch
Requires: DoAsRoot-cs-sk kde4-config-sk config-sk akonadi kde-smooth-tasks kde-baseapps-core kde-baseapps-dolphin 
Requires: kde-runtime kde-workspace-core kdelibs  kde-multimedia-kmix  kde-pimlibs  kdm  kwebkitpart  libsoprano4  
Requires: oxygen-gtk oxygen-icon-theme  plasma-desktoptheme-glassified  
Requires: strigi  virtuoso-opensource  xsettings-kde  kde-graphics-libs  kde-plasma-addons  kwrite  konsole  kde-baseapps-plasma
Requires: installer-kde iso-codes transcode rarlinux lm_sensors

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Task pro CZ KDE

%files

%changelog
* Sat Mar 25 2012 Mank <Mank1@seznam.cz> 2.2.0.35-1
- initial task packages
