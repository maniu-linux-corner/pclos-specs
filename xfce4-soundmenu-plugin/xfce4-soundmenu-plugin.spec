Name:           xfce4-soundmenu-plugin
Version:        0.7.0
Release:        2%{?dist}
Summary:        A very basic xfce4-panel plugin to control any players MPRIS2 compatible.

License:        GPLv2
URL:            https://github.com/matiasdelellis/xfce4-soundmenu-plugin
Source0:        xfce4-soundmenu-plugin-%{version}.tar.bz2

BuildRequires: xfce4-panel-devel %{_lib}xfce4util-devel %{_lib}xfce4ui-devel %{_lib}notify-devel libmpris2client-devel
Requires: xfce4-panel

%description
A very basic xfce4-panel plugin to control any players MPRIS2 compatible.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%{_libdir}/xfce4/panel/plugins/libsoundmenu.so
%{_datadir}/icons/hicolor/128x128/apps/xfce4-soundmenu-plugin.png
%{_datadir}/locale/es/LC_MESSAGES/xfce4-soundmenu-plugin.mo
%{_datadir}/xfce4/panel/plugins/soundmenu.desktop


%changelog
* Sat Jun 13 2015 Mank <mank dot pclos at gmail dot com> 0.7.0-2
- Init Spec
