Name:           cursor-theme-breeze-black
Version:        1.0
Release:        1%{?dist}
Summary:        Breeze Black - X11 Mouse Theme

License:        GPL
URL:            https://opendesktop.org/content/show.php?content=174535
Source0:        cursor-theme-breeze-black-1.0.tar.xz
BuildArch:		noarch

%description
Breeze Black - X11 Mouse Theme

%prep
%setup -q -c cursor-theme-breeze-black-%{version}


%install
%__install -d %{buildroot}%{_datadir}/icons/
cd usr/share/icons/
%__cp -rf ./* %{buildroot}%{_datadir}/icons/

%files
%{_datadir}/icons/breeze-black/



%changelog
