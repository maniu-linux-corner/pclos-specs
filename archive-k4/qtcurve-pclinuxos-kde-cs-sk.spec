Name:           qtcurve-pclinuxos-kde-cs-sk
Version:       1.0.0 
Release:        1%{?dist}
Summary:        Téma pro QtCurve
BuildArch:	noarch
License:        GPLv3
URL:            https://github.com/pclinuxoscz/specs
Source0:        qtcurve-pclinuxos-kde-cs-sk.tar.xz

Requires:   kde4-style-qtcurve qtcurve-gtk2

%description
Téma stylu QtCurve vybrané na komunitní LiveDVD CS/SK pro grafické prostředí KDE4 SC

- Appows http://kde-look.org/content/show.php/appows+for+kde?content=156778

%prep
%setup -q -n qtcurve-pclinuxos-kde-cs-sk
%build

%install
mkdir -p $RPM_BUILD_ROOT/
cp -R ./ $RPM_BUILD_ROOT/
%files
%{_datadir}/apps/QtCurve/*

%changelog
