Name:           gfxboot-theme-pclinuxos-cs-sk
Version:        1.0.0
Release:        1%{?dist}
Summary:        Téma pro gfxboot

License:        CC BY-SA 3.0
URL:            http://kde-look.org/content/show.php/Caledonia+Official+Wallpapers?content=143579
Source0:        %{name}.tar.xz


%description

Téma pro Live DVD https://github.com/pclinuxoscz/specs 2016

Použita tapeta z kolekce Caledoina

Odkaz: http://kde-look.org/content/show.php/Caledonia+Official+Wallpapers?content=143579

%prep
%setup -q -c %{name}

%install
cp -r * $RPM_BUILD_ROOT

%files
%{_datadir}/gfxboot/themes/https://github.com/pclinuxoscz/specs/*

%changelog
