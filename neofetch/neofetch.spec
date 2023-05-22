Name:           neofetch
Version:        3.0.1
Release:        1
Summary:        Neofetch

License:        MIT
URL:            https://github.com/dylanaraps/neofetch
Source0:        neofetch-3.0.1.tar.gz

Requires:       ImageMagick 
Requires:       caca-utils w3m

%description


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%config(noreplace) %{_sysconfdir}/neofetch/config
%{_bindir}/neofetch
%{_datadir}/man/man1/neofetch.1.bz2
%{_datadir}/neofetch/ascii/distro/*

%changelog
* Thu Feb  2 2017 Maniu <me  at maniu dot eu>
- 
