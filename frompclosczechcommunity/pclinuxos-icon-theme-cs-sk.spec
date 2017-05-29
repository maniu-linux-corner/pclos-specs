Name:           pclinuxos-icon-theme-cs-sk
Version:        2016
Release:        1%{?dist}
Summary:        PCLinuxOS Flat 2016 CZ / SK

License:        GPL
URL:            https://github.com/pclinuxoscz/specs
Source0:        pclinuxos-icon-theme-cs-sk-%{version}.tar.xz
BuildArch:		noarch


%description
Téma ikon pro PCLinuxOS KDE (postavené na Abridged, některé ikony dolněny z Antu a přidány ikony pro PCLinuxOS)
http://kde-look.org/content/show.php/Abridged+Icon+Theme?content=174136

%prep
%setup -q -c %{name}


%install
%__install -d %{buildroot}%{_datadir}/icons/
cd usr/share/icons/
%__cp -rf ./* %{buildroot}%{_datadir}/icons/

%files
%{_datadir}/icons/


%changelog
