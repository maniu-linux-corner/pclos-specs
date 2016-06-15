Name:           plymouth-theme-pclinuxos-kde-cs-sk
Version:        1.0.0
Release:        1%{?dist}
Summary:        Téma pro Plymouth

License:        GPLv3
URL:            pclinuxos.cz
Source0:       plymouth-theme-pclinuxos-cs-sk.tar.xz 
BuildArch: noarch
Requires:  plymouth  bootsplash      

%description
Téma pro CZ/SK vydání LiveDVD KDE a KDE Plus 

%prep
%setup -q -c plymouth-theme-pclinuxos-cs-sk

%build

%install
mkdir -p $RPM_BUILD_ROOT
cp -R ./ $RPM_BUILD_ROOT/

%pre
/usr/share/bootsplash/scripts/remove-theme

%post
/usr/sbin/plymouth-set-default-theme caledonia-pclos.
/usr/share/bootsplash/scripts/switch-themes caledonia-pclos

%postun
if [ "$1" = 0 ]; then
/usr/sbin/plymouth-set-default-theme text
/usr/share/bootsplash/scripts/switch-themes text
fi

%files
%{_datadir}/plymouth/themes/caledonia.pclos/*

%changelog
* Sat Jul 26 2014 Mank <mank@pclinuxos.cz> 1.0.0-1
- Version 1.0.0 
- intial version of rpm
