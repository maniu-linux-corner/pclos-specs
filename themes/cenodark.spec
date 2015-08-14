Name:           cenodark
Version:        d7mq7in
Release:        1%{?dist}
Summary:        GTK2&3 and Metacity theme
BuildArch:		noarch
License:        GPL
URL:            http://vinceliuice.deviantart.com/art/Cenodark-461437583
Source0:        cenodark_by_vinceliuice-d7mq7in.zip

%description
GTK2&3 and Metacity theme

%prep
%setup -q -n Cenodark


%build


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{name}
cp -R ./ $RPM_BUILD_ROOT%{_datadir}/themes/%{name}

%files
%{_datadir}/themes/%{name}/*

%changelog
