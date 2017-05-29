Name:           kde-color-schemes-pclinuxos-cs-sk
Version:        1.0.0
Release:        1%{?dist}
Summary:	Schéma barev pro KDE        

License:        GPLv3
URL:            http://https://github.com/pclinuxoscz/specs
BuildArch:	noarch
Source0:        kde-color-schemes-pclinuxos-cs-sk.tar.xz
Requires:    kde-baseapps-core   



%description
Schéma barev pro KDE

Barevná schémata vybraná na komunitní LiveDVD CS/SK pro grafické prostředí KDE4 SC. Balíček obsahuje 

- Caledonia 6
- LuckyEyes http://kde-look.org/content/show.php/LuckyEyes?content=101360


%prep
%setup -q -n kde-color-schemes-pclinuxos-cs-sk


%build

%install
mkdir -p $RPM_BUILD_ROOT/
cp -R ./ $RPM_BUILD_ROOT/

%files
%{_datadir}/apps/color-schemes/

%changelog
