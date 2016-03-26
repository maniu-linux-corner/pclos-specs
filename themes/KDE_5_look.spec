%define iconsdir %{_datadir}/icons


Name:           KDE_5_look
Version:        1.0.0
Release:        2%{?dist}
Summary:    	kde 5 look for K4    

License:        GPL
URL:            wedontknow.org
Source0:        KDE_5_look.tar.gz
BuildArch:		noarch
%description


%prep
%setup -q -c KDE_5_look -n KDE_5_look


%build

%install
cd KDE_5_look
%__install -d %{buildroot}%{iconsdir}/
%__cp -rf Icons %{buildroot}%{iconsdir}/

%__install -d %{buildroot}%{_datadir}/themes/
%__cp -rf ./GTK2.3_theme/* %{buildroot}%{_datadir}/themes/

%__install -d %{buildroot}%{_datadir}/apps/QtCurve/
%__cp Breeze.qtcurve %{buildroot}%{_datadir}/apps/QtCurve/

%__install -d %{buildroot}%{_datadir}/apps/aurorae/themes/
%__cp -rf ./Breeze-Light-0.036 %{buildroot}%{_datadir}/apps/aurorae/themes/
%__cp -rf ./Breeze-0.034 %{buildroot}%{_datadir}/apps/aurorae/themes/

%__install -d %{buildroot}%{_datadir}/apps/color-schemes/
%__cp BreezeLight.colors %{buildroot}%{_datadir}/apps/color-schemes/

%__install -d %{buildroot}%{_datadir}/wallpapers/
%__cp *.jpg %{buildroot}%{_datadir}/wallpapers/
%__cp *.png %{buildroot}%{_datadir}/wallpapers/

%__install -d %{buildroot}%{_datadir}/apps/desktoptheme/
%__cp -rf Plasma_desktop_theme/* %{buildroot}%{_datadir}/apps/desktoptheme/

%files
%{_datadir}/themes/
%{iconsdir}/
%{_datadir}/apps/QtCurve/*
%{_datadir}/apps/aurorae/themes/*
%{_datadir}/apps/color-schemes/*
%{_datadir}/wallpapers/*
%{_datadir}/apps/desktoptheme/*


%changelog
