Name:           nuvola-app-soundcloud
Version:        master
Release:        1%{?dist}
Summary:        deezer support

License:        GPL
URL:            https://github.com/tiliado/nuvola-app-soundcloud
Source0:        nuvola-app-soundcloud-master.zip

%description


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
%make_install DEST=%{buildroot}%{_datadir}/nuvolaplayer3/web_apps/


%files
/usr/share/nuvolaplayer3/web_apps/soundcloud/*
 /usr/share/icons/hicolor/*


%changelog
