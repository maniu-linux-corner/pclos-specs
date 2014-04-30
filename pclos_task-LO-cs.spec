Name: task-LO-cs-lang
Summary: Task for Office Suite (cs lang files)
Version: 3.6
Release: 1
License: LGPLv3
URL: http://www.libreoffice.org/
Group: Tasks
BuildArch: noarch
Requires: task-LO
Requires: libobasis3.6-cs-base
Requires: libobasis3.6-cs-calc
Requires: libobasis3.6-cs-math
Requires: libobasis3.6-cs-res
Requires: libobasis3.6-cs-writer
Requires: libobasis3.6-cs
Requires: libreoffice3.6-cs
Requires: libreoffice3.6-dict-cs
Requires: libobasis3.6-cs-help

Conflicts: libobasis3.5-cs-base
Conflicts: libobasis3.5-cs-calc
Conflicts: libobasis3.5-cs-math
Conflicts: libobasis3.5-cs-res
Conflicts: libobasis3.5-cs-writer
Conflicts: libobasis3.5-cs
Conflicts: libreoffice3.5-cs
Conflicts: libreoffice3.5-dict-cs
Conflicts: libobasis3.5-cs-help

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
LibreOffice is the power-packed free, libre and open source personal productivity suite for Windows, Macintosh and GNU/Linux, that gives you six feature-rich applications for all your document production and data processing needs: Writer, Calc, Impress, Draw, Math and Base. Support and documentation is free from our large, dedicated community of users, contributors and developers. You, too, can get involved!

%files

%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 3.6-1
- initial task packages.
