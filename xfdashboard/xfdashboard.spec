Name:           xfdashboard
Version:        0.4.1
Release:        1%{?dist}
Summary: Maybe a Gnome shell like dashboard for Xfce       

License: GPLv3       
URL:  http://goodies.xfce.org/projects/applications/xfdashboard/start
Source0: xfdashboard-%{version}.tar.bz2      

BuildRequires: garcon-devel clutter glib xfconf dbus-glib %{_lib}wnck3-devel gettext clutter-devel
Requires: garcon %{_lib}wnck1_22

%description
xfdashboard provides a GNOME shell dashboard like interface for use with Xfce desktop. It can be configured to run to any keyboard shortcut and when executed provides an overview of applications currently open enabling the user to switch between different applications. The search feature works like Xfce's app finder which makes it convenient to search for and start applications.


%prep
%setup -q

%build
%configure2_5x
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}-settings
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_datadir}/appdata/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_datadir}/icons/*
%{_datadir}/themes/%{name}/*
%{_datadir}/%{name}/bindings.xml
%{_datadir}/%{name}/preferences.ui
%{_datadir}/themes/%{name}-*/*

%changelog
* Fri Aug 14 2015 Mank <mank at pclinuxos.cz> 0.4.1-1mank2015
- 0.4.1
* Fri Jun 8 2014 Mank <mank at pclinuxos.cz> 0.2.4-1mank2014
- 0.2.4
