Name: mate-clock-screensaver
Summary: A Screensaver with Analog clock
Version: 1.0.1
Release: 3
License: GPLv3
Group: Applications/Mate
Source0: gnome-clock-screensaver-1.0.1.tar.gz
Source5: anclock.desktop
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

%description
A ScreenSaver with Analog Clock

%prep
%setup -n gnome-clock-screensaver-1.0.1

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%{__make}

%install
%{makeinstall}
rm $RPM_BUILD_ROOT/%{_datadir}/applications/screensavers/anclock.desktop
cp -f %{SOURCE5} $RPM_BUILD_ROOT/%{_datadir}/applications/screensavers/anclock.desktop
%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make clean

%files

%defattr(-,root,root)
%{_libdir}/mate-screensaver/anclock
%{_datadir}/applications/screensavers/anclock.desktop

%changelog
* Sat Dec 12 2013 Mank <Mank1@seznam.cz> 1.0.1-2
- anclock: Version 1.0.1
