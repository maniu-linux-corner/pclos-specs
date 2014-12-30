Name:           zonColor-themes
Version:        1.6.5
Release:        1%{?dist}
Summary:		zonColor Themes        

License:        GPLv3
URL:            http://www.fandigital.com/p/zoncolor.html
Source0:        zoncolor-themes-pack_%{version}.tar.gz
BuildArch:		noarch

%description
Zon Colors Themes Pack ( Gnome, Mate ,Xfce ,LXDE and RazorQT)
( without scripts)

%prep
%setup -q -n zoncolor-themes


%build
cd zoncolor/
cd icon-themes/
%__install -d $RPM_BUILD_ROOT/usr/share/icons/
%__cp icon-themes.tar.gz $RPM_BUILD_ROOT/usr/share/icons/
cd ..
cd gtk-themes/
%__install -d $RPM_BUILD_ROOT/usr/share/themes/
%__cp gtk-themes.tar.gz $RPM_BUILD_ROOT/usr/share/themes/
cd ..
%__install -d $RPM_BUILD_ROOT/usr/share/wallpapers/zonColors/
%__cp -R wallpapers/ $RPM_BUILD_ROOT/usr/share/wallpapers/zonColors/
cd ..
cd xtra
cd xtra
install -d $RPM_BUILD_ROOT/usr/share/razor/themes/
cd razor-qt-theme
%__cp -r ./ $RPM_BUILD_ROOT/usr/share/razor/themes/

cd $RPM_BUILD_ROOT/usr/share/icons/
tar -xf icon-themes.tar.gz
%__rm icon-themes.tar.gz
cd $RPM_BUILD_ROOT/usr/share/themes/
tar -xf gtk-themes.tar.gz
%__rm gtk-themes.tar.gz

%install


%files
%{_datadir}/icons/*
%{_datadir}/themes/*
%{_datadir}/razor/themes/*
%{_datadir}/wallpapers/zonColors/*



%changelog
* Tue Dec 30 2014 mank <mank@pclinuxos.cz>
- built

