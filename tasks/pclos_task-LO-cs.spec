Name: task-LO-cs-lang
Summary: Task for Office Suite (cs lang files)
Version: 5.1
Release: 1
License: LGPLv3
URL: http://www.libreoffice.org/
Group: Tasks
BuildArch: noarch

Requires: task-LO
Requires: libobasis5.1-cs-base
Requires: libobasis5.1-cs-calc
Requires: libobasis5.1-cs-math
Requires: libobasis5.1-cs-res
Requires: libobasis5.1-cs-writer
Requires: libobasis5.1-cs
Requires: libreoffice5.1-cs
Requires: libreoffice5.1-dict-cs
Requires: libobasis5.1-cs-help

Conflicts: libobasis5.0-cs-base
Conflicts: libobasis5.0-cs-calc
Conflicts: libobasis5.0-cs-math
Conflicts: libobasis5.0-cs-res
Conflicts: libobasis5.0-cs-writer
Conflicts: libobasis5.0-cs
Conflicts: libreoffice5.0-cs
Conflicts: libreoffice5.0-dict-cs
Conflicts: libobasis5.0-cs-help

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
LibreOffice is the power-packed free, libre and open source personal productivity suite for Windows, Macintosh and GNU/Linux, that gives you six feature-rich applications for all your document production and data processing needs: Writer, Calc, Impress, Draw, Math and Base. Support and documentation is free from our large, dedicated community of users, contributors and developers. You, too, can get involved!

%files

%changelog
* Sat Mar 25 2011 Mank <mank@pclinuxos.cz> 3.6-1
- initial task packages.
