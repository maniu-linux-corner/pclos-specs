%define url_ver %(echo %{version} | cut -d "." -f -2)

Summary:	A GNOME filemanager similar to the Norton Commander(TM)
Name:		gnome-commander
Version:	1.4.3
Release:	%mkrel 1
URL:		http://www.freesoftware.fsf.org/gcmd/
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.gz
Patch3:		gnome-commander-1.2.8.15-staticlib.patch
License:	GPLv2+
Group:		File tools
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libgnome-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	python-devel
BuildRequires:	libchm-devel
BuildRequires:	intltool gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	libxslt-proc
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	gnome-common

%description
Gnome Commander is a filemanager that just like the classical Norton
commander (TM) lets you do everything with the keyboard. It can
perform all standard file operations and some extra features like ftp
support.

%prep
%setup -q
%apply_patches

%build
autoreconf -fi
sh autogen.sh --prefix=/usr
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome
for omf in %{buildroot}%{_datadir}/omf/*/*[_-]??.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%{buildroot}!!)" >> %{name}.lang
done

desktop-file-install --vendor="" \
  --add-category="System" \
  --add-category="FileTools" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%files -f %{name}.lang
%doc README TODO ChangeLog
%{_bindir}/%{name}
%{_bindir}/gcmd-block
%{_libdir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/omf/%{name}
%{_datadir}/omf/%{name}/%{name}-C.omf
%{_datadir}/appdata/gnome-commander.appdata.xml

%changelog
* Fri May 30 2014 Mank <MMank dot pclos at gmail dot com> 1.4.3-1
+ Build for PCLOS
- new version 1.4.3
* Fri May 30 2014 ovitters <ovitters> 1.4.2-1.mga5
+ Revision: 627816
- new version 1.4.2

* Sat Apr 05 2014 ovitters <ovitters> 1.4.1-1.mga5
+ Revision: 611814
- new version 1.4.1

* Mon Mar 17 2014 dams <dams> 1.4.0-1.mga5
+ Revision: 604430
- new version 1.4.0
- enable back 'gsf build'
- rediff patch

* Mon Feb 10 2014 dams <dams> 1.2.8.17-3.mga5
+ Revision: 589008
- rebuild for new exiv2

* Sat Feb 08 2014 fwang <fwang> 1.2.8.17-2.mga5
+ Revision: 586085
- rebuild for new poppler

* Tue Feb 04 2014 dams <dams> 1.2.8.17-1.mga5
+ Revision: 580929
- new version 1.2.8.17
- remove useless patches (merged upstream)

* Sat Oct 19 2013 umeabot <umeabot> 1.2.8.15-14.mga4
+ Revision: 530975
- Mageia 4 Mass Rebuild

* Wed Jul 31 2013 fwang <fwang> 1.2.8.15-13.mga4
+ Revision: 461353
- rebuild for new poppler

* Sat Jul 20 2013 fwang <fwang> 1.2.8.15-12.mga4
+ Revision: 456569
- force use new api
- patch against latest poppler
- rebuild for new poppler

* Sun Jun 23 2013 fwang <fwang> 1.2.8.15-11.mga4
+ Revision: 445914
- cast variable
- disable gsf build, as it failed building
- rebuild for new poppler

* Sat Jan 12 2013 umeabot <umeabot> 1.2.8.15-10.mga3
+ Revision: 352063
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Mon Dec 31 2012 fwang <fwang> 1.2.8.15-9.mga3
+ Revision: 336474
- fix build with automake 1.13
- rebuild for new poppler

* Mon Nov 12 2012 fwang <fwang> 1.2.8.15-8.mga3
+ Revision: 317122
- rebuild for new poppler

* Wed Oct 10 2012 tv <tv> 1.2.8.15-7.mga3
+ Revision: 304200
- rebuild with new poppler

* Tue Sep 11 2012 fwang <fwang> 1.2.8.15-6.mga3
+ Revision: 292151
- rebuild for new poppler

* Sat Sep 01 2012 fwang <fwang> 1.2.8.15-5.mga3
+ Revision: 286956
- do not add libadd to static libs
- build libgcmd as static lib

* Thu Aug 30 2012 fwang <fwang> 1.2.8.15-4.mga3
+ Revision: 285813
- add fedora patch to build with gcc 4.7
- rebuild for new poppler

* Mon Jun 18 2012 fwang <fwang> 1.2.8.15-3.mga3
+ Revision: 261638
- rebuild for new exiv

* Wed Jun 13 2012 fwang <fwang> 1.2.8.15-2.mga3
+ Revision: 260250
- br gettext
- regenerate configure
- add fedora patch to build with latest poppler
- rebuild for new poppler

* Wed Dec 07 2011 fwang <fwang> 1.2.8.15-1.mga2
+ Revision: 178084
- new version 1.2.8.15

* Fri Oct 28 2011 fwang <fwang> 1.2.8.14-3.mga2
+ Revision: 158961
- rebuild for new poppler

* Sun Oct 09 2011 fwang <fwang> 1.2.8.14-2.mga2
+ Revision: 153419
- rebuild for new exiv2

* Wed Oct 05 2011 wally <wally> 1.2.8.14-1.mga2
+ Revision: 152012
- new version 1.2.8.14

* Tue Sep 27 2011 ovitters <ovitters> 1.2.8.13-4.mga2
+ Revision: 149375
- rebuild for new poppler

* Tue Sep 27 2011 fwang <fwang> 1.2.8.13-3.mga2
+ Revision: 149368
- rebuild for new poppler

* Wed Sep 21 2011 fwang <fwang> 1.2.8.13-2.mga2
+ Revision: 146438
- drop .la files
- new version 1.2.8.13

  + ahmad <ahmad>
    - Change libpoppler-*-devel BR to pkgconfig style

* Sat Jul 02 2011 wally <wally> 1.2.8.12-1.mga2
+ Revision: 117515
- new version 1.2.8.12
- disable static build
- fix desktop-file-validate warnings
- clean .spec a bit

* Thu Apr 14 2011 ennael <ennael> 1.2.8.10-2.mga1
+ Revision: 85263
- clean spec file
- imported package gnome-commander


* Fri Mar 11 2011 Funda Wang <fwang@mandriva.org> 1.2.8.10-2mdv2011.0
+ Revision: 643738
- rebuild for new poppler

* Sat Jan 15 2011 Götz Waschk <waschk@mandriva.org> 1.2.8.10-1
+ Revision: 631125
- update to new version 1.2.8.10

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 1.2.8.9-3mdv2011.0
+ Revision: 626160
- rebuild for new poppler

* Fri Dec 03 2010 Götz Waschk <waschk@mandriva.org> 1.2.8.9-2mdv2011.0
+ Revision: 607147
- use new 1.2.8.9 tarball

* Fri Dec 03 2010 Götz Waschk <waschk@mandriva.org> 1.2.8.9-1mdv2011.0
+ Revision: 606926
- update to new version 1.2.8.9

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 1.2.8.8-3mdv2011.0
+ Revision: 604405
- rebuild for new exiv2

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 1.2.8.8-2mdv2011.0
+ Revision: 593007
- rebuild for new python 2.7

* Fri Sep 10 2010 Götz Waschk <waschk@mandriva.org> 1.2.8.8-1mdv2011.0
+ Revision: 577027
- update to new version 1.2.8.8

* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 1.2.8.7-4mdv2011.0
+ Revision: 571804
- rebuild for new poppler

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 1.2.8.7-3mdv2011.0
+ Revision: 566254
- rebuild for new poppler

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 1.2.8.7-2mdv2011.0
+ Revision: 565539
- rebuild for new exiv2

* Tue Jul 27 2010 Götz Waschk <waschk@mandriva.org> 1.2.8.7-1mdv2011.0
+ Revision: 562083
- update to new version 1.2.8.7

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 1.2.8.6-1mdv2011.0
+ Revision: 550776
- update to new version 1.2.8.6

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 1.2.8.5-2mdv2010.1
+ Revision: 537373
- rebuild

* Sun Feb 14 2010 Götz Waschk <waschk@mandriva.org> 1.2.8.5-1mdv2010.1
+ Revision: 505793
- new version
- update the patch

* Wed Jan 13 2010 Götz Waschk <waschk@mandriva.org> 1.2.8.4-3mdv2010.1
+ Revision: 490559
- rebuild for new libjpeg

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2.8.4-2mdv2010.1
+ Revision: 484196
- Rebuild for new libexiv2

* Thu Dec 03 2009 Götz Waschk <waschk@mandriva.org> 1.2.8.4-1mdv2010.1
+ Revision: 473092
- update to new version 1.2.8.4

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 1.2.8.3-1mdv2010.1
+ Revision: 460928
- update to new version 1.2.8.3

* Tue Sep 22 2009 Götz Waschk <waschk@mandriva.org> 1.2.8.2-1mdv2010.0
+ Revision: 447526
- update to new version 1.2.8.2

* Sun Aug 16 2009 Götz Waschk <waschk@mandriva.org> 1.2.8.1-2mdv2010.0
+ Revision: 416882
- rebuild for new libjpeg

* Tue Aug 11 2009 Götz Waschk <waschk@mandriva.org> 1.2.8.1-1mdv2010.0
+ Revision: 414694
- update to new version 1.2.8.1

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 1.2.8-1mdv2010.0
+ Revision: 390583
- new version
- rediff the patch
- update file list
- update build deps

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 1.2.7-3mdv2009.1
+ Revision: 320291
- fix str fmt

* Sat Nov 08 2008 Götz Waschk <waschk@mandriva.org> 1.2.7-2mdv2009.1
+ Revision: 301106
- rebuild for new libxcb

* Mon Jul 28 2008 Götz Waschk <waschk@mandriva.org> 1.2.7-1mdv2009.0
+ Revision: 252057
- new version

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Mon Jun 02 2008 Götz Waschk <waschk@mandriva.org> 1.2.6-1mdv2009.0
+ Revision: 214208
- new version
- disable --as-needed and --no-undefined to make it build

* Sat Mar 01 2008 Götz Waschk <waschk@mandriva.org> 1.2.5-1mdv2008.1
+ Revision: 177245
- new version
- update buildrequires

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - replace %%{_datadir}/man by %%{_mandir}!

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jun 09 2007 Götz Waschk <waschk@mandriva.org> 1.2.4-1mdv2008.0
+ Revision: 37667
- new version
- fix buildrequires


* Tue Dec 12 2006 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdv2007.0
+ Revision: 95200
- new version

* Mon Dec 11 2006 Götz Waschk <waschk@mandriva.org> 1.2.2-2mdv2007.1
+ Revision: 94777
- fix buildrequires

* Mon Dec 11 2006 Götz Waschk <waschk@mandriva.org> 1.2.2-1mdv2007.1
+ Revision: 94666
- new version

* Wed Oct 18 2006 Götz Waschk <waschk@mandriva.org> 1.2.1-1mdv2007.0
+ Revision: 65795
- new version
- new version

* Sun Oct 15 2006 Götz Waschk <waschk@mandriva.org> 1.2.1-0.20061010.1mdv2006.0
+ Revision: 64777
- Import gnome-commander

* Sat Oct 14 2006 G�tz Waschk <waschk@mandriva.org> 1.2.1-0.20061010.1mdv2007.1
- fix buildrequires
- new snapshot

* Sat Aug 05 2006 Götz Waschk <waschk@mandriva.org> 1.2.0-1mdv2007.0
- rebuild for new dbus

* Fri Jul 21 2006 G�tz Waschk <waschk@mandriva.org> 1.2.0-3mdv2007.0
- xdg menu

* Thu May 11 2006 G�tz Waschk <waschk@mandriva.org> 1.2.0-2mdk
- fix buildrequires

* Mon May 08 2006 Jerome Soyer <saispo@mandriva.org> 1.2.0-1mdk
- New release 1.2.0

* Mon Feb 13 2006 G�tz Waschk <waschk@mandriva.org> 1.1.7-1mdk
- drop patches
- new version
- new source URL

* Wed Aug 10 2005 G�tz Waschk <waschk@mandriva.org> 1.1.6-6mdk
- fix build

* Wed Jun 08 2005 G�tz Waschk <waschk@mandriva.org> 1.1.6-5mdk
- fix buildrequires

* Tue Jun 07 2005 G�tz Waschk <waschk@mandriva.org> 1.1.6-4mdk
- patch for gcc 4

* Sat May 07 2005 G�tz Waschk <waschk@mandriva.org> 1.1.6-3mdk
- fix build on x86_64

* Wed May 05 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.1.6-2mdk
- patch from CVS to make it compile with gtk 2.4

* Tue Jan 20 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.1.6-1mdk
- new version

* Mon Jan 12 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.1.5-1mdk
- update file list
- new version
