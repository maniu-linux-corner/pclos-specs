Name:           kdm-theme-pclinuxos-kde-cs-sk
Version:        1.0.0
Release:        1%{?dist}
Summary:        Téma pro KDM

License:        GPLv3
URL:            https://github.com/pclinuxoscz/specs
Source0:        kdm-theme-pclinuxos-kde-cs-sk.tar.xz
BuildArch: noarch
Requires:    kdm   

%description
Téma pro CZ/SK vydání LiveDVD KDE a KDE Plus 

%prep
%setup -q -n kdm-theme-pclinuxos-kde-cs-sk


%build

%install
cp -R . $RPM_BUILD_ROOT/

%files
%config %{_datadir}/config/kdm/kdmrc
%{_datadir}/apps/kdm/themes/*


%changelog
