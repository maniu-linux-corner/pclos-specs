Name: task-LO-cs-lang
Summary: Task for Office Suite (cs lang files)
Version: 4.3
Release: 1
License: LGPLv3
URL: http://www.libreoffice.org/
Group: Tasks
BuildArch: noarch
Requires: task-LO
Requires: libobasis4.3-cs-base
Requires: libobasis4.3-cs-calc
Requires: libobasis4.3-cs-math
Requires: libobasis4.3-cs-res
Requires: libobasis4.3-cs-writer
Requires: libobasis4.3-cs
Requires: libreoffice4.3-cs
Requires: libreoffice4.3-dict-cs
Requires: libobasis4.3-cs-help

Obsoletes: libobasis4.2-cs-base
Obsoletes: libobasis4.2-cs-calc
Obsoletes: libobasis4.2-cs-math
Obsoletes: libobasis4.2-cs-res
Obsoletes: libobasis4.2-cs-writer
Obsoletes: libobasis4.2-cs
Obsoletes: libreoffice4.2-cs
Obsoletes: libreoffice4.2-dict-cs
Obsoletes: libobasis4.2-cs-help

Obsoletes: libobasis4.1-cs-base
Obsoletes: libobasis4.1-cs-calc
Obsoletes: libobasis4.1-cs-math
Obsoletes: libobasis4.1-cs-res
Obsoletes: libobasis4.1-cs-writer
Obsoletes: libobasis4.1-cs
Obsoletes: libreoffice4.1-cs
Obsoletes: libreoffice4.1-dict-cs
Obsoletes: libobasis4.1-cs-help

Obsoletes: libobasis3.5-cs-base
Obsoletes: libobasis3.5-cs-calc
Obsoletes: libobasis3.5-cs-math
Obsoletes: libobasis3.5-cs-res
Obsoletes: libobasis3.5-cs-writer
Obsoletes: libobasis3.5-cs
Obsoletes: libreoffice3.5-cs
Obsoletes: libreoffice3.5-dict-cs
Obsoletes: libobasis3.5-cs-help

Obsoletes: libobasis3.6-cs-base
Obsoletes: libobasis3.6-cs-calc
Obsoletes: libobasis3.6-cs-math
Obsoletes: libobasis3.6-cs-res
Obsoletes: libobasis3.6-cs-writer
Obsoletes: libobasis3.6-cs
Obsoletes: libreoffice3.6-cs
Obsoletes: libreoffice3.6-dict-cs
Obsoletes: libobasis3.6-cs-help

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
LibreOffice is the power-packed free, libre and open source personal productivity suite for Windows, Macintosh and GNU/Linux, that gives you six feature-rich applications for all your document production and data processing needs: Writer, Calc, Impress, Draw, Math and Base. Support and documentation is free from our large, dedicated community of users, contributors and developers. You, too, can get involved!

%files

%changelog
* Sat Mar 25 2011 Mank <Mank dot pclos at gmail dot com> 4.0-1
- initial task packages.
