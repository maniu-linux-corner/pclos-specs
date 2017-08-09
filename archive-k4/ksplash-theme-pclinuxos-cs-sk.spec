Name:           ksplash-theme-pclinuxos-cs-sk
Version:        1.0.0
Release:        1%{?dist}
Summary:        Téma pro KSplash

License:        CC BY-SA 3.0 and GPL
URL:            http://kde-look.org/content/show.php/KStarboard+Splash?content=119216
Source0:        %{name}.tar.xz


%description
Téma pro KSPlash

Upravené téma KStarboard Splash pro Live DVD https://github.com/pclinuxoscz/specs 2016

Odkaz: http://kde-look.org/content/show.php/KStarboard+Splash?content=119216

Licence: GPL

Použita tapeta z kolekce Caledoina

Odkaz: http://kde-look.org/content/show.php/Caledonia+Official+Wallpapers?content=143579

Licence: Creative Commons BY-SA 3.0


%prep
%setup -q -c %{name}

%install
cp -r * $RPM_BUILD_ROOT

%files
%{_datadir}/apps/ksplash/Themes/kstarboard.pclos/*

%changelog
