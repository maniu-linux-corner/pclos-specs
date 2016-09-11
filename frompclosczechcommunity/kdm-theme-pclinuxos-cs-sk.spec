Name:           ksplash-theme-pclinuxos-cs-sk
Version:        1.0.0
Release:        1%{?dist}
Summary:        Téma pro KDM

License:        CC BY-SA 3.0
URL:            http://kde-look.org/content/show.php/Caledonia+KDM?content=143130
Source0:        %{name}.tar.xz


%description

Téma Caledonia KDM pro Live DVD PCLinuxOS.cz 2016

Odkaz: http://kde-look.org/content/show.php/Caledonia+KDM?content=143130



%prep
%setup -q -c %{name}

%install
cp -r * $RPM_BUILD_ROOT

%files
%{_datadir}/apps/kdm/themes/Caledonia.KDM/*

%changelog
