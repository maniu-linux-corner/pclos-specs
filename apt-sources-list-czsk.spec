Summary: Sources List for the apt-rpm package manager
Name: sources-cz-sk
Version: 1.0.0
Release: %mkrel 2
License: GPL
Group: System/Configuration/Packaging
URL: https://github.com/pclinuxoscz/
Source:      %name-%version.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains apt sources list for the apt-rpm
package manager for cz-sk repo

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/apt/sources.list.d/


%ifarch x86_64
install -m 0644 cs-sk64.list %{buildroot}%{_sysconfdir}/apt/sources.list.d/cs-sk.list
%endif
%ifarch %{ix86}
install -m 0644 cs-sk32.list %{buildroot}%{_sysconfdir}/apt/sources.list.d/cs-sk.list
%endif


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sysconfdir}/apt/sources.list.d/cs-sk.list

%changelog
* Wed Oct 02 2016 Mank <mank at void . cet> 1.0.0-1pclos2016
- create
