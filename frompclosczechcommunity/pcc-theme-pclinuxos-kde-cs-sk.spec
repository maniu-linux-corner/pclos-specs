Name:           pcc-theme-pclinuxos-kde-cs-sk
Version:        1.0.0
Release:        1%{?dist}
Summary:        Téma pro PCC

License:      	GPLv3  
URL:            https://github.com/pclinuxoscz/specs
Source0:        pcc-theme-pclinuxos-kde-cs-sk.tar.xz
BuildArch:	noarch 
Requires:       drakconf

%description
Téma vybrané na komunitní LiveDVD CS/SK pro aplikaci Nastavit váš počítač (PCLinuxOS Control Center) pro grafické prostředí KDE4 SC

%prep
%setup -q -n pcc-theme-pclinuxos-kde-cs-sk

%build

%install
mkdir -p $RPM_BUILD_ROOT/
cp -R ./ $RPM_BUILD_ROOT/

%files
%{_datadir}/mcc/themes/KDE/*

%changelog
