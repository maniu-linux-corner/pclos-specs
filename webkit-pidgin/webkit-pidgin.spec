Name: pidgin-webkit
Summary: A Webkit Plugin for pidgin
Version: 69
Release: 1
License: GPLv2
URL: https://code.launchpad.net/pidgin-webkit
Group: Applications/IM
Source0: pidgin-webkit.tar.xz
Source1: adium-pidgin
Source5: pidgin-webkit-tempfile-2.patch
BuildRequires:	libgtk+2.0_0-devel
BuildRequires: libwebkitgtk1.0-devel
BuildRequires: pidgin-devel
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A Webkit-based and adium styles conversion for pidgin

%prep
%setup -n pidgin-webkit

%build
patch -i %{SOURCE5}
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/pidgin/
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/bin/adium-pidgin
mv -Tf webkit.so $RPM_BUILD_ROOT/usr/lib/pidgin/webkit.so


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_libdir}/pidgin/webkit.so
%{_bindir}/adium-pidgin

%changelog
* Sat Mar 25 2013 Maniu <me  at maniu dot eu> 69-1
- pidgin-webkit: Version pre: 69
