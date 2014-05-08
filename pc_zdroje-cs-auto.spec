Name: config-cs-sk
Summary: A Sources List for PCLOS (cs&sk)
Version: 0.0.1
Release: 1
License: GPLv2
BuildArch: noarch
URL: http://www.pclinuxos.cz
Group: Applications/System
Source0: repo.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A config cz&sk

%prep
%setup -c %{name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d/
cp repo/etc/rc.d/init.d/repo-mank $RPM_BUILD_ROOT/etc/rc.d/init.d/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%postun
if [ "$1" = 0 ]; then
rm -f /etc/init.d/repo-mank /etc/rc2.d/S99repo-mank
rm -f /etc/init.d/repo-mank /etc/rc3.d/S99repo-mank
rm -f /etc/init.d/repo-mank /etc/rc4.d/S99repo-mank
rm -f /etc/init.d/repo-mank /etc/rc5.d/S99repo-mank
fi

%post
ln -s /etc/init.d/repo-mank /etc/rc2.d/S99repo-mank
ln -s /etc/init.d/repo-mank /etc/rc3.d/S99repo-mank
ln -s /etc/init.d/repo-mank /etc/rc4.d/S99repo-mank
ln -s /etc/init.d/repo-mank /etc/rc5.d/S99repo-mank

%files
%defattr(-,root,root)
/etc/rc.d/init.d/*

%changelog
* Sat Jun 23 2012 Mank <mank@pclinuxos.cz> 0.0.1-1
- config-cs-sk Version : 0.0.1
