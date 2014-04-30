Name: task-LO
Summary: Task for Office Suite (core)
Version: 3.6
Release: 1
License: LGPLv3
URL: http://www.libreoffice.org/
Group: Tasks
Source0: README_en-US.tar
BuildArch: noarch
Requires: libobasis3.6-base
Requires: libobasis3.6-binfilter
Requires: libobasis3.6-calc
Requires: libobasis3.6-core01
Requires: libobasis3.6-core02
Requires: libobasis3.6-core03
Requires: libobasis3.6-core04
Requires: libobasis3.6-core05
Requires: libobasis3.6-core06
Requires: libobasis3.6-core07
Requires: libobasis3.6-draw
Requires: libobasis3.6-en-US-base
Requires: libobasis3.6-en-US-calc
Requires: libobasis3.6-en-US-math
Requires: libobasis3.6-en-US-res
Requires: libobasis3.6-en-US-writer
Requires: libobasis3.6-en-US
Requires: libobasis3.6-extension-beanshell-script-provider
Requires: libobasis3.6-extension-javascript-script-provider
Requires: libobasis3.6-extension-mediawiki-publisher
Requires: libobasis3.6-extension-nlpsolver
Requires: libobasis3.6-extension-pdf-import
Requires: libobasis3.6-extension-presentation-minimizer
Requires: libobasis3.6-extension-presenter-screen
Requires: libobasis3.6-extension-python-script-provider
Requires: libobasis3.6-extension-report-builder
Requires: libobasis3.6-gnome-integration
Requires: libobasis3.6-graphicfilter
Requires: libobasis3.6-images
Requires: libobasis3.6-impress
Requires: libobasis3.6-javafilter
Requires: libobasis3.6-kde-integration
Requires: libobasis3.6-math
Requires: libobasis3.6-ogltrans
Requires: libobasis3.6-onlineupdate
Requires: libobasis3.6-ooofonts
Requires: libobasis3.6-ooolinguistic
Requires: libobasis3.6-postgresql-sdbc
Requires: libobasis3.6-pyuno
Requires: libobasis3.6-writer
Requires: libobasis3.6-xsltfilter
Requires: libreoffice3.6-base
Requires: libreoffice3.6-calc
Requires: libreoffice3.6-dict-en
Requires: libreoffice3.6-dict-es
Requires: libreoffice3.6-dict-fr
Requires: libreoffice3.6-draw
Requires: libreoffice3.6-en-US
Requires: libreoffice3.6-impress
Requires: libreoffice3.6-math
Requires: libreoffice3.6-stdlibs
Requires: libreoffice3.6-ure
Requires: libreoffice3.6-writer
Requires: libreoffice3.6
Requires: libreoffice3.6-mandriva-menus
Requires: task-java

Conflicts: libobasis3.5-base
Conflicts: libobasis3.5-binfilter
Conflicts: libobasis3.5-calc
Conflicts: libobasis3.5-core01
Conflicts: libobasis3.5-core02
Conflicts: libobasis3.5-core03
Conflicts: libobasis3.5-core04
Conflicts: libobasis3.5-core05
Conflicts: libobasis3.5-core06
Conflicts: libobasis3.5-core07
Conflicts: libobasis3.5-draw
Conflicts: libobasis3.5-en-US-base
Conflicts: libobasis3.5-en-US-calc
Conflicts: libobasis3.5-en-US-math
Conflicts: libobasis3.5-en-US-res
Conflicts: libobasis3.5-en-US-writer
Conflicts: libobasis3.5-en-US
Conflicts: libobasis3.5-extension-beanshell-script-provider
Conflicts: libobasis3.5-extension-javascript-script-provider
Conflicts: libobasis3.5-extension-mediawiki-publisher
Conflicts: libobasis3.5-extension-nlpsolver
Conflicts: libobasis3.5-extension-pdf-import
Conflicts: libobasis3.5-extension-presentation-minimizer
Conflicts: libobasis3.5-extension-presenter-screen
Conflicts: libobasis3.5-extension-python-script-provider
Conflicts: libobasis3.5-extension-report-builder
Conflicts: libobasis3.5-gnome-integration
Conflicts: libobasis3.5-graphicfilter
Conflicts: libobasis3.5-images
Conflicts: libobasis3.5-impress
Conflicts: libobasis3.5-javafilter
Conflicts: libobasis3.5-kde-integration
Conflicts: libobasis3.5-math
Conflicts: libobasis3.5-ogltrans
Conflicts: libobasis3.5-onlineupdate
Conflicts: libobasis3.5-ooofonts
Conflicts: libobasis3.5-ooolinguistic
Conflicts: libobasis3.5-postgresql-sdbc
Conflicts: libobasis3.5-pyuno
Conflicts: libobasis3.5-writer
Conflicts: libobasis3.5-xsltfilter
Conflicts: libreoffice3.5-base
Conflicts: libreoffice3.5-calc
Conflicts: libreoffice3.5-dict-en
Conflicts: libreoffice3.5-dict-es
Conflicts: libreoffice3.5-dict-fr
Conflicts: libreoffice3.5-draw
Conflicts: libreoffice3.5-en-US
Conflicts: libreoffice3.5-impress
Conflicts: libreoffice3.5-math
Conflicts: libreoffice3.5-stdlibs
Conflicts: libreoffice3.5-ure
Conflicts: libreoffice3.5-writer
Conflicts: libreoffice3.5
Conflicts: libreoffice3.5-mandriva-menus

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
LibreOffice is the power-packed free, libre and open source personal productivity suite for Windows, Macintosh and GNU/Linux, that gives you six feature-rich applications for all your document production and data processing needs: Writer, Calc, Impress, Draw, Math and Base. Support and documentation is free from our large, dedicated community of users, contributors and developers. You, too, can get involved!

%prep
%setup -c

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/task-lo/
cp $RPM_SOURCE_DIR/README_en-US $RPM_BUILD_ROOT/usr/share/doc/task-lo/


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/usr/share/doc/task-lo/README_en-US


%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 3.6-1
- initial task packages
