Name: task-LO-sk-lang
Summary: Task for Office Suite (sk lang files)
Version: 4.3
Release: 1
License: LGPLv3
URL: http://www.libreoffice.org/
Group: Tasks
BuildArch: noarch
Requires: task-LO

Requires: libobasis4.3-sk-base
Requires: libobasis4.3-sk-calc
Requires: libobasis4.3-sk-math
Requires: libobasis4.3-sk-res
Requires: libobasis4.3-sk-writer
Requires: libobasis4.3-sk
Requires: libreoffice4.3-sk
Requires: libreoffice4.3-dict-sk
Requires: libobasis4.3-sk-help

Obsoletes: libobasis4.2-sk-base
Obsoletes: libobasis4.2-sk-calc
Obsoletes: libobasis4.2-sk-math
Obsoletes: libobasis4.2-sk-res
Obsoletes: libobasis4.2-sk-writer
Obsoletes: libobasis4.2-sk
Obsoletes: libreoffice4.2-sk
Obsoletes: libreoffice4.2-dict-sk
Obsoletes: libobasis4.2-sk-help

Obsoletes: libobasis4.1-sk-base
Obsoletes: libobasis4.1-sk-calc
Obsoletes: libobasis4.1-sk-math
Obsoletes: libobasis4.1-sk-res
Obsoletes: libobasis4.1-sk-writer
Obsoletes: libobasis4.1-sk
Obsoletes: libreoffice4.1-sk
Obsoletes: libreoffice4.1-dict-sk
Obsoletes: libobasis4.1-sk-help


Obsoletes: libobasis3.6-sk-base
Obsoletes: libobasis3.6-sk-calc
Obsoletes: libobasis3.6-sk-math
Obsoletes: libobasis3.6-sk-res
Obsoletes: libobasis3.6-sk-writer
Obsoletes: libobasis3.6-sk
Obsoletes: libreoffice3.6-sk
Obsoletes: libreoffice3.6-dict-sk
Obsoletes: libobasis3.6-sk-help

Obsoletes: libobasis3.5-sk-base
Obsoletes: libobasis3.5-sk-calc
Obsoletes: libobasis3.5-sk-math
Obsoletes: libobasis3.5-sk-res
Obsoletes: libobasis3.5-sk-writer
Obsoletes: libobasis3.5-sk
Obsoletes: libreoffice3.5-sk
Obsoletes: libreoffice3.5-dict-sk
Obsoletes: libobasis3.5-sk-help



Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
LibreOffice is the power-packed free, libre and open source personal productivity suite for Windows, Macintosh and GNU/Linux, that gives you six feature-rich applications for all your document production and data processing needs: Writer, Calc, Impress, Draw, Math and Base. Support and documentation is free from our large, dedicated community of users, contributors and developers. You, too, can get involved!

%files

%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 4.0-1
- initial task packages
