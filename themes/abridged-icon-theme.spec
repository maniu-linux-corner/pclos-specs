Name:           abridged-icon-theme
Version:        1.0.0
Release:        1%{?dist}
Summary:        KDE Icon Theme - A simple and clean icon theme forked from Breeze.

License:        GPL
URL:            http://kde-look.org/content/show.php/Abridged+Icon+Theme?content=174136
Source0:        abridged.tar.gz
BuildArch:		noarch


%description
KDE Icon Theme - A simple and clean icon theme forked from Breeze.

%prep
%setup -q -c abridged

%install
%__install -d %{buildroot}%{_datadir}/icons/
%__cp -rf ./* %{buildroot}%{_datadir}/icons/

%files
%{_datadir}/icons/



%changelog
