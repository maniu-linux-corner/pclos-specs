Name:           nuvola-app-plex
Version:        master
Release:        1%{?dist}
Summary:        music support

License:        GPL
URL:            https://github.com/tiliado/nuvola-app-spotify
Source0:        nuvola-app-plex-master.zip

%description


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
%make_install DEST=%{buildroot}%{_datadir}/nuvolaplayer3/web_apps/


%files
/usr/share/nuvolaplayer3/web_apps/plex/*


%changelog
