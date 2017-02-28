Name:           xdwaita-icons
Version:        1.0.0
Release:        1%{?dist}
Summary:        Xdwaita icon from xenlism project

License:        GPL
URL:            https://xenlism.github.io/
Source0:        Xdwaita-master.zip

%description


%prep
%setup -q -c xdwaita-icons -n xdwaita-icons

%install
install -dm755 "%{buildroot}/usr/share/icons"
cd "Xdwaita-master/icons/"
cp -r * "%{buildroot}/usr/share/icons/";
find "%{buildroot}/usr/share/icons" -type d -exec chmod 755 '{}' \;
find "%{buildroot}/usr/share/icons" -type f -exec chmod 644 '{}' \;

%files
%{_datadir}/icons/


%changelog
* Sun Feb 26 2017 mank
- intial
