Name:           nuvola-app-soundcloud
Version:        master
Release:        2%{?dist}
Summary:        soundcloud support

License:        GPL
URL:            https://github.com/tiliado/nuvola-app-soundcloud
Source0:        nuvola-app-soundcloud-1.1.tar.gz

%description


%prep
%setup -q -n nuvola-app-soundcloud-1.1


%build
make %{?_smp_mflags}


%install
%make_install DEST=%{buildroot}%{_datadir}/nuvolaplayer3/web_apps/


%files
%{_datadir}/nuvolaplayer3/web_apps/soundcloud/*
%{_datadir}/icons/hicolor/*


%changelog
