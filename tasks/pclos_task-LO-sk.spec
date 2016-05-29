Name: task-LO-sk-lang
Summary: Task for Office Suite (sk lang files)
Version: 5.1
Release: 1
License: LGPLv3
URL: http://www.libreoffice.org/
Group: Tasks
BuildArch: noarch
Requires: task-LO
Requires: libobasis5.1-sk-base
Requires: libobasis5.1-sk-calc
Requires: libobasis5.1-sk-math
Requires: libobasis5.1-sk-res
Requires: libobasis5.1-sk-writer
Requires: libobasis5.1-sk
Requires: libreoffice5.1-sk
Requires: libreoffice5.1-dict-sk
Requires: libobasis5.1-sk-help

Conflicts: libobasis5.0-sk-base
Conflicts: libobasis5.0-sk-calc
Conflicts: libobasis5.0-sk-math
Conflicts: libobasis5.0-sk-res
Conflicts: libobasis5.0-sk-writer
Conflicts: libobasis5.0-sk
Conflicts: libreoffice5.0-sk
Conflicts: libreoffice5.0-dict-sk
Conflicts: libobasis5.0-sk-help

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
LibreOffice is the power-packed free, libre and open source personal productivity suite for Windows, Macintosh and GNU/Linux, that gives you six feature-rich applications for all your document production and data processing needs: Writer, Calc, Impress, Draw, Math and Base. Support and documentation is free from our large, dedicated community of users, contributors and developers. You, too, can get involved!

%files

%changelog
* Sat Mar 25 2011 Mank <mank@pclinuxos.cz> 3.6-1
- initial task packages
