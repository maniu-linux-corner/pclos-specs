Name: task-LO
Summary: Task for Office Suite (core)
Version: 5.1
Release: 4
License: LGPLv3
URL: http://www.libreoffice.org/
Group: Tasks
BuildArch: noarch

Requires: libreoffice5.1-freedesktop-menus
Requires: libobasis5.1-librelogo
Requires: libobasis5.1-python-script-provider
Requires: libobasis5.1-filter-data
Requires: libobasis5.1-base
Requires: libobasis5.1-calc
Requires: libobasis5.1-core
Requires: libobasis5.1-draw
Requires: libobasis5.1-en-US-base
Requires: libobasis5.1-en-US-calc
Requires: libobasis5.1-en-US-math
Requires: libobasis5.1-en-US-res
Requires: libobasis5.1-en-US-writer
Requires: libobasis5.1-en-US
Requires: libobasis5.1-extension-beanshell-script-provider
Requires: libobasis5.1-extension-javascript-script-provider
Requires: libobasis5.1-extension-mediawiki-publisher
Requires: libobasis5.1-extension-nlpsolver
Requires: libobasis5.1-extension-pdf-import
Requires: libobasis5.1-extension-report-builder
Requires: libobasis5.1-gnome-integration
Requires: libobasis5.1-graphicfilter
Requires: libobasis5.1-images
Requires: libobasis5.1-impress
Requires: libobasis5.1-kde-integration
Requires: libobasis5.1-math
Requires: libobasis5.1-ogltrans
Requires: libobasis5.1-onlineupdate
Requires: libobasis5.1-ooofonts
Requires: libobasis5.1-ooolinguistic
Requires: libobasis5.1-postgresql-sdbc
Requires: libobasis5.1-pyuno
Requires: libobasis5.1-writer
Requires: libobasis5.1-xsltfilter
Requires: libreoffice5.1-base
Requires: libreoffice5.1-calc
Requires: libreoffice5.1-dict-en
Requires: libreoffice5.1-dict-es
Requires: libreoffice5.1-dict-fr
Requires: libreoffice5.1-draw
Requires: libreoffice5.1-en-US
Requires: libreoffice5.1-impress
Requires: libreoffice5.1-math
Requires: libreoffice5.1-writer
Requires: libreoffice5.1
Requires: task-java

Conflicts: libobasis5.0-base
Conflicts: libobasis5.0-binfilter
Conflicts: libobasis5.0-calc
Conflicts: libobasis5.0-core
Conflicts: libobasis5.0-draw
Conflicts: libobasis5.0-en-US-base
Conflicts: libobasis5.0-en-US-calc
Conflicts: libobasis5.0-en-US-math
Conflicts: libobasis5.0-en-US-res
Conflicts: libobasis5.0-en-US-writer
Conflicts: libobasis5.0-en-US
Conflicts: libobasis5.0-extension-beanshell-script-provider
Conflicts: libobasis5.0-extension-javascript-script-provider
Conflicts: libobasis5.0-extension-mediawiki-publisher
Conflicts: libobasis5.0-extension-nlpsolver
Conflicts: libobasis5.0-extension-pdf-import
Conflicts: libobasis5.0-extension-presentation-minimizer
Conflicts: libobasis5.0-extension-presenter-screen
Conflicts: libobasis5.0-extension-python-script-provider
Conflicts: libobasis5.0-extension-report-builder
Conflicts: libobasis5.0-gnome-integration
Conflicts: libobasis5.0-graphicfilter
Conflicts: libobasis5.0-images
Conflicts: libobasis5.0-impress
Conflicts: libobasis5.0-javafilter
Conflicts: libobasis5.0-kde-integration
Conflicts: libobasis5.0-math
Conflicts: libobasis5.0-ogltrans
Conflicts: libobasis5.0-onlineupdate
Conflicts: libobasis5.0-ooofonts
Conflicts: libobasis5.0-ooolinguistic
Conflicts: libobasis5.0-postgresql-sdbc
Conflicts: libobasis5.0-pyuno
Conflicts: libobasis5.0-writer
Conflicts: libobasis5.0-xsltfilter
Conflicts: libreoffice5.0-base
Conflicts: libreoffice5.0-calc
Conflicts: libreoffice5.0-dict-en
Conflicts: libreoffice5.0-dict-es
Conflicts: libreoffice5.0-dict-fr
Conflicts: libreoffice5.0-draw
Conflicts: libreoffice5.0-en-US
Conflicts: libreoffice5.0-impress
Conflicts: libreoffice5.0-math
Conflicts: libreoffice5.0-stdlibs
Conflicts: libreoffice5.0-ure
Conflicts: libreoffice5.0-writer
Conflicts: libreoffice5.0
Conflicts: libreoffice5.0-mandriva-menus

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
LibreOffice is the power-packed free, libre and open source personal productivity suite for Windows, Macintosh and GNU/Linux, that gives you six feature-rich applications for all your document production and data processing needs: Writer, Calc, Impress, Draw, Math and Base. Support and documentation is free from our large, dedicated community of users, contributors and developers. You, too, can get involved!

%files

%changelog
* Sat Mar 25 2011 Mank <mank@pclinuxos.cz> 3.6-1
- initial task packages
