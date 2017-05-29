Name: deadbeef-mpris
Summary: A dbus-plugin for deadbeef
Version: 2.1.5
Release: 3
License: GPLv2
URL: http://code.google.com/p/deadbeef-mpris-plugin/
Group: Sound/Players
Source0: deadbeef-MPRIS-plugin-2.1.5.tar.gz
Source1: deadbeef-MPRIS-plugin-2.1.5-glibfix.patch
BuildRequires:	libgtk+2.0_0-devel
BuildRequires: deadbeef-devel
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A dbus-plugin for deadbeef

%prep
%setup -q -n deadbeef-2.1.5

%build
patch -i %{SOURCE1}
%configure --prefix=/usr --libdir=%{_libdir}
make

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_libdir}/deadbeef/*

%changelog
* Sat Apr 25 2014 Mank <Mank dot pclos at gmail dot com> 2.1.5-3
- deadbeef-mpris: Version : 2.1.5
