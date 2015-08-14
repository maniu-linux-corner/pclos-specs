Name:           plymouth-theme-lxde-cs-sk
Version:        1.0.0
Release:        1%{?dist}
Summary:        Téma pro Plymouth

License:        GPLv3
URL:            pclinuxos.cz
Source0:       plymouth-theme-lxde-cs-sk.tar.xz 
BuildArch: noarch
Requires:  plymouth  bootsplash      

%description
Téma pro CZ/SK vydání LiveDVD LXDE 

%prep
%setup -q -n plymouth-theme-lxde-cs-sk

%build

%install
mkdir -p $RPM_BUILD_ROOT
cp -R ./ $RPM_BUILD_ROOT/

%pre
/usr/share/bootsplash/scripts/remove-theme

%post
/usr/sbin/plymouth-set-default-theme PCLinuxOS-LXDE
/usr/share/bootsplash/scripts/switch-themes PCLinuxOS-LXDE

%postun
if [ "$1" = 0 ]; then
/usr/sbin/plymouth-set-default-theme text
/usr/share/bootsplash/scripts/switch-themes text
fi

%files
%{_datadir}/plymouth/themes/PCLinuxOS-LXDE

%changelog
* Sat Jul 26 2014 Mank <mank@pclinuxos.cz> 1.0.0-1
- Version 1.0.0 
- intial version of rpm
