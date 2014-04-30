Name: task-skype
Summary: Task for Skype
Version: 2.2.0.35
Release: 1
License: LGPLv3
URL: http://www.skype.com/
Group: Tasks
BuildArch: noarch
Requires: skype_static
Requires: skype-i18n
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Task for Skype The p2p VoIP application.

%files

%changelog
* Sat Mar 25 2012 Mank <Mank1@seznam.cz> 2.2.0.35-1
- initial task packages
