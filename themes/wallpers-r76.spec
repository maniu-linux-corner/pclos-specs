Name:           wallpapers-r76
Version:        1.0.0
Release:        1%{?dist}
Summary:        Wallpers r76

License:        CC-BY-NC-ND
URL:            https://snwh.org/paper
Source0:        wallpapers-r76.tar.xz
BuildArch:		noarch


%description

Tapety pro Live DVD https://github.com/pclinuxoscz/specs

Wallpapers for Live DVD https://github.com/pclinuxoscz/specs

Author: Miroslav Řehulka
Email: rehulkamirek@seznam.cz
License: Creative Commons BY-NC-ND

https://creativecommons.org/licenses/by-nc-nd/3.0/

%prep
%setup -q -c %{name}

%install
cd usr/share/wallpapers/
%__install -d %{buildroot}%{_datadir}/wallpapers/
%__cp -rf ./* %{buildroot}%{_datadir}/wallpapers/

%files
%{_datadir}/wallpapers/



%changelog
