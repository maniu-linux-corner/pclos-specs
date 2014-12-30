Name:           xfce4-notifyd
Version:        0.2.4
Release:        1%{?dist}
Summary:        Easily themable notification daemon with transparency effects
BuildRequires:  libxfce4util-devel libxfce4ui-devel gettext
License:        GPLv3
URL:            http://xfce.org
Group:          Graphical desktop/Xfce
Source0:        xfce4-notifyd-0.2.4.tar.bz2

%description
Easily themable notification daemon with transparency effects

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/xfce4-notifyd-config
%{_libdir}/xfce4/notifyd
%{_libdir}/xfce4/notifyd/xfce4-notifyd
%{_datadir}/applications/xfce4-notifyd-config.desktop
%{_datadir}/dbus-1/services/org.xfce.xfce4-notifyd.Notifications.service
%{_datadir}/icons/hicolor/48x48/apps/xfce4-notifyd.png
%{_datadir}/themes/Default/*
%{_datadir}/themes/Smoke/*
%{_datadir}/themes/ZOMG-PONIES!/
%{_mandir}/man1/xfce4-notifyd-config.1.bz2

%changelog

* Sat Aug 25 2014 Mank <mank@pclinuxos.cz> 0.2.4-1
- Init Spec file with xfce4-notifyd 0.2.4

