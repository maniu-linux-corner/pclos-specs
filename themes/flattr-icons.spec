Name:           flattr-icons
Version:        master
Release:        1%{?dist}
Summary:        Icon Theme Flatr

License:        GPLv3
URL:            https://github.com/NitruxSA/flattr-icons
Source0:        flattr-icons-master.zip
BuildArch:	noarch
%description


%prep
%setup -q -c flattr-icons-master


%build
mv flattr-icons-master flattr-icons
%__install -d %{buildroot}%{_datadir}/icons/
%__cp -rf ./* %{buildroot}%{_datadir}/icons/
%__rm %{buildroot}%{_datadir}/icons/flattr-icons/.gitignore
%__mv %{buildroot}%{_datadir}/icons/flattr-icons/
%install

%files
%{_datadir}/icons/flattr-icons/*

%changelog
