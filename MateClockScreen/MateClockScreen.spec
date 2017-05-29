Name: mate-clock-screensaver
Summary: A Screensaver with Analog clock
Version: 1.0.1
Release: 3
License: GPLv3
Group: Graphical desktop/MATE
Source0: gnome-clock-screensaver-%{version}.tar.gz
Source5: anclock.desktop
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

%description
A ScreenSaver with Analog Clock

%prep
%setup -q -n gnome-clock-screensaver-1.0.1

%build
%{__make}

%install
%{makeinstall}
rm $RPM_BUILD_ROOT/%{_datadir}/applications/screensavers/anclock.desktop
cp -f %{SOURCE5} $RPM_BUILD_ROOT/%{_datadir}/applications/screensavers/anclock.desktop
%clean

make clean

%files

%defattr(-,root,root)
%{_libdir}/mate-screensaver/anclock
%{_datadir}/applications/screensavers/anclock.desktop

%changelog
* Sat Dec 12 2013 Mank <Mank dot pclos at gmail dot com> 1.0.1-2
- anclock: Version 1.0.1
