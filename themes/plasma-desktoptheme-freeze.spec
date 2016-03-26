Name:           plasma-desktoptheme-freeze
Version:        1.3
Release:        1%{?dist}
Summary:        A Plasma Theme for the KDE 4 desktop

License:        GPL
URL:            pc.org
Source0:        plasma-desktoptheme-freeze-1.3.tar.xz

Requires:       kde-baseapps-plasma
BuildArch:		noarch
%description


%prep
%setup -q -c %{name}

%install
%__install -d %{buildroot}%{_datadir}/apps/aurorae/themes/
cd usr/share/apps/aurorae/themes/
%__cp -rf ./* %{buildroot}%{_datadir}/apps/aurorae/themes/


%files
%{_datadir}/apps/aurorae/themes/


%changelog
