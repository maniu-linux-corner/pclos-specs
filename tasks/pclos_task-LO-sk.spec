Name: task-LO-sk-lang
Summary: Task for Office Suite (sk lang files)
Version: 3.6
Release: 1
License: LGPLv3
URL: http://www.libreoffice.org/
Group: Tasks
BuildArch: noarch
Requires: task-LO
Requires: libobasis3.6-sk-base
Requires: libobasis3.6-sk-calc
Requires: libobasis3.6-sk-math
Requires: libobasis3.6-sk-res
Requires: libobasis3.6-sk-writer
Requires: libobasis3.6-sk
Requires: libreoffice3.6-sk
Requires: libreoffice3.6-dict-sk
Requires: libobasis3.6-sk-help

Conflicts: libobasis3.5-sk-base
Conflicts: libobasis3.5-sk-calc
Conflicts: libobasis3.5-sk-math
Conflicts: libobasis3.5-sk-res
Conflicts: libobasis3.5-sk-writer
Conflicts: libobasis3.5-sk
Conflicts: libreoffice3.5-sk
Conflicts: libreoffice3.5-dict-sk
Conflicts: libobasis3.5-sk-help

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
LibreOffice is the power-packed free, libre and open source personal productivity suite for Windows, Macintosh and GNU/Linux, that gives you six feature-rich applications for all your document production and data processing needs: Writer, Calc, Impress, Draw, Math and Base. Support and documentation is free from our large, dedicated community of users, contributors and developers. You, too, can get involved!

%files

%changelog
* Sat Mar 25 2011 Mank <mank@pclinuxos.cz> 3.6-1
- initial task packages
