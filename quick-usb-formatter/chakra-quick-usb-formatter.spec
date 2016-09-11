%define git_ver 1622737

Name:           chakra-quick-usb-formatter
Version:        0.0.1
Release:        1%{?dist}
Summary:        This software it's for format usb sticks,

License:        GPL
URL:            https://gitorious.org/chakra/quick-usb-formatter
Source0:        chakraquick-usb-formatter-%{git_ver}.tar.gz

BuildRequires:  cmake
   

%description
Quick Usb Formatter
This software it's for format usb sticks,
it's designed for being simple, so if you need
a more specialized format you should use instead
a more advanced tool.


%prep
%setup -n chakraquick-usb-formatter-1622737 

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
%make

%install
cd build
%make_install


%files
%{_sysconfdir}/dbus-1/system.d/org.kde.auth.quf.conf
%{_bindir}/quickusbformatter
%{_libdir}/kde4/libexec/helper
%{_datadir}/applications/kde4/quickusbformatter.desktop
%{_datadir}/apps/solid/actions/quickusbformatter_solid.desktop
%{_datadir}/dbus-1/system-services/org.kde.auth.quf.service
%{_datadir}/locale/*
%{_datadir}/polkit-1/actions/org.kde.auth.quf.policy


%changelog
