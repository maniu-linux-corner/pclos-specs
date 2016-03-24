%define iconsdir %{_datadir}/icons


Name:           KDE_5_look
Version:        1.0.0
Release:        1%{?dist}
Summary:    	kde 5 look for K4    

License:        GPL
URL:            wedontknow.org
Source0:        KDE_5_look.tar.gz
BuildArch:		noarch
%description


%prep
%setup -q -c KDE_5_look -n KDE_5_look


%build

%install
cd KDE_5_look
%__install -d %{buildroot}%{iconsdir}/%{name}
%__cp -rf Icons %{buildroot}%{iconsdir}/%{name}/
%__install -d %{buildroot}%{_datadir}/themes/%{name}
%__cp -rf ./GTK2.3_theme/* %{buildroot}%{_datadir}/themes/%{name}


%files
%{_datadir}/themes/%{name}
%{iconsdir}/%{name}/*


%changelog
