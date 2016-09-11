Name:           paper-icon-theme
Version:        1.0.0
Release:        1%{?dist}
Summary:        Paper Icon Theme

License:        CC-BY-SA-4.0
URL:            https://snwh.org/paper
Source0:        paper-icon-theme-%{version}.zip
BuildArch:		noarch


%description
Paper Icon Theme

%prep
%setup -q -c %{name}}

%install
%__install -d %{buildroot}%{_datadir}/icons/
%__cp -rf ./* %{buildroot}%{_datadir}/icons/

%files
%{_datadir}/icons/



%changelog
