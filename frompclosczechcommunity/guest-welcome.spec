Name: guest_uvitani
Summary: Uvitani na Live CD/DVD pro KDE
Version: 0.0.1
Release: 1
License: GPL
URL: http://pclinuxos.cz
Group: Applications/KDE
Source0: guest_uvitani.tar.xz
Requires: glibc
Requires: libstdc++6
Autoprov: No
BuildArch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Uvitani na Live CD/DVD pro KDE

%prep
%setup

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%install
cp -r ./ $RPM_BUILD_ROOT/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/usr/share/pclinuxos/pics/*
/home/guest/.kde4/*
%changelog
* Sat Mar 25 2011 Mank <mank@pclinuxos.cz> 0.0.1-1
- guest-welccome: Version pre: 0.0.1
