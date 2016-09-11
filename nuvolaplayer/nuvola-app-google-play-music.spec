Name:           nuvola-app-google-play-music
Version:        master
Release:        1%{?dist}
Summary:        owncloud music support

License:        GPL
URL:            https://github.com/tiliado/nuvola-app-google-play-music
Source0:        nuvola-app-google-play-music-master.zip

%description


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
%make_install DEST=%{buildroot}%{_datadir}/nuvolaplayer3/web_apps/


%files
/usr/share/nuvolaplayer3/web_apps/google_play_music/*
 /usr/share/icons/hicolor/*


%changelog
