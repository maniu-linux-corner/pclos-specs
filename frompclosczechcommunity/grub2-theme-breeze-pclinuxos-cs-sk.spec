Name:           kdm-theme-pclinuxos-cs-sk
Version:        1.0.0
Release:        1%{?dist}
Summary:        Téma pro GRUB

License:        CC BY-SA 3.0
URL:            http://kde-look.org/content/show.php/Breeze+GRUB2+theme?content=171217
Source0:        %{name}.tar.xz


%description

Upravené téma Breeze pro Live DVD https://github.com/pclinuxoscz/specs 2016

Odkaz: http://kde-look.org/content/show.php/Breeze+GRUB2+theme?content=171217

Licence: Creative Commons BY-SA 3.0

Použita tapeta z kolekce Caledoina

Odkaz: http://kde-look.org/content/show.php/Caledonia+Official+Wallpapers?content=143579

Licence: Creative Commons BY-SA 3.0

%prep
%setup -q -c %{name}

%install
cp -r * $RPM_BUILD_ROOT

%files
/boot/grub2/themes/breeze.pclos/

%changelog
