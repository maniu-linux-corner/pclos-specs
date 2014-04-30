Name: task-kde4-cs
Summary: Task for Live CZ KDE env
Version: 1.0
Release: 1
License: LGPLv3
URL: http://www.pclinuxos.cz/
Group: Tasks
BuildArch: noarch
Requires: kde4-config-cs
Requires: config-cs

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Task for CZ Live env

%files

%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 4.0-1
- initial task packages.
