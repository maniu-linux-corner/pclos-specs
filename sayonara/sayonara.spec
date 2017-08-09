%global gitrev  20170509

Name:           sayonara
Version:        0.9.3
Release:        1.git%{gitrev}%{?dist}
Summary:        A lightweight Qt Audio player

License:        GPLv3+
URL:            http://sayonara-player.com
# download instructions
# git clone https://git.sayonara-player.com/sayonara.git --branch 0.9.3-git2-20170509 sayonara-player
# tar cfz sayonara-player-0.9.3-git2-20170509.tar.gz sayonara-player
Source0:        sayonara-player-0.9.3-git2-20170509.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
# BuildRequires:  %{_lib}appstream-glib-devel
BuildRequires:  %{_lib}qt5core-devel
BuildRequires:  qttools5
BuildRequires:  %{_lib}gstreamer1.0-devel
BuildRequires:  taglib-devel
BuildRequires:	%{_lib}mtp-devel
BuildRequires:  zlib-devel
Requires:       hicolor-icon-theme
Requires:		task-multimedia

%description
%{name} is a small, clear, not yet platform-independent music player. Low 
CPU usage, low memory consumption and no long loading times are only three 
benefits of this player. Sayonara should be easy and intuitive to use and 
therefore it should be able to compete with the most popular music players.

%prep
%setup -q -n %{name}-player
rm -rf .git*

%build
cmake . -DCMAKE_BUILD_TYPE=[Release] -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# remove menu dir, because it's not necessary
rm -rf %{buildroot}/%{_datadir}/menu

find %{buildroot}%{_datadir}/%{name}/translations -name "*.qm" | sed 's:'%{buildroot}'::
s:.*/\([a-zA-Z]\{2\}\).qm:%lang(\1) \0:' > %{name}.lang

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
# %%license license.txt
%doc MANUAL README.txt
%doc %{_datadir}/man/*
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
# %%{_libdir}/%{name}/*.so
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.xpm
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/*/%{name}.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/%{name}/translations/icons
%{_datadir}/%{name}/translations/icons/*.png
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.ico
%{_datadir}/%{name}/*.css
%{_datadir}/%{name}/player.db
%{_datadir}/%{name}/soundcloud.db

%changelog
* Tue May 09 2017 Lucio Carreras <luciocarreras@gmail.com> - 0.9.3-3.git20170509
- Rebuild for sayonara (git tag 0.9.3-git2-20170509)

* Tue May 02 2017 Lucio Carreras <luciocarreras@gmail.com> - 0.9.3-2.git20170502
- Rebuild for sayonara (git tag 0.9.3-git1-20170502)

* Mon May 01 2017 Lucio Carreras <luciocarreras@gmail.com> - 0.9.3-1.git20170501
- Rebuild for sayonara (git tag 0.9.3-git0-20170501)

* Mon May 01 2017 Lucio Carreras <luciocarreras@gmail.com> - 0.9.3-3.git20170501
- Rebuild for sayonara (git tag 0.9.3-git2-20170501)

* Sun Oct 30 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.2-12.git20161030
- Rebuild for sayonara (git tag 0.9.2-git11-20161030)

* Thu Oct 13 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.2-9.git20161013
- Rebuild for sayonara (git tag 0.9.2-git8-20161013)

* Mon Oct 10 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.2-7.git20161010
- Rebuild for sayonara (git tag 0.9.2-git6-20161010)

* Sun Oct 09 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.2-6.git20161009
- Rebuild for sayonara (git tag 0.9.2-git5-20161009)

* Tue Sep 20 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.2-5.git20160920
- Rebuild for sayonara (git tag 0.9.2-git4-20160920)

* Tue Sep 20 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.2-3.git20160920
- Rebuild for sayonara (git tag 0.9.2-git2-20160920)

* Tue Sep 20 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.2-2.git20160919
- Rebuild for sayonara (git tag 0.9.2-git1-20160919)

* Tue Sep 13 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.1-3.git20160913
- Rebuild for sayonara (git tag 0.9.1-git2-20160913)

* Mon Sep 12 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.1-1.git20160913
- Rebuild for sayonara (git tag 0.9.1-git0-20160913)

* Mon Sep 12 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.1-1.git20160913
- Rebuild for sayonara (git tag 0.9.1-git0-20160913)

* Tue Jun 07 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.0-4.git20160607
- Rebuild for sayonara (git tag 0.9.0-git3-20160607)

* Mon Jun 06 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.0-4.git20160606
- Rebuild for sayonara (git tag 0.9.0-git3-20160606)

* Mon May 16 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.0-2.git20160516
- Rebuild for sayonara (git tag 0.9.0-git1-20160516)

* Sat May 14 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.9.0-1.git20160514
- Rebuild for sayonara (git tag 0.9.0-git0-20160514)

* Sun May 01 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.3-3.git20160501
- Rebuild for sayonara (git tag 0.8.3-git2-20160501)

* Sun May 01 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.3-3.git20160501
- Rebuild for sayonara (git tag 0.8.3-git2-20160501)

* Sun Apr 24 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.3-1.git20160424
- Rebuild for sayonara (git tag 0.8.3-git0-20160424)

* Sun Apr 24 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.3-1.git20160424
- Rebuild for sayonara (git tag 0.8.3-git0-20160424)

* Sun Apr 24 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.3-1.git20160424
- Rebuild for sayonara (git tag 0.8.3-git0-20160424)

* Fri Feb 26 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.2-3.git20160226
- Rebuild for sayonara (git tag 0.8.2-git2-20160226)

* Fri Feb 19 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.2-2.git20160219
- Rebuild for sayonara (git tag 0.8.2-git1-20160219)

* Fri Feb 19 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.2-2.git20160219
- Rebuild for sayonara (git tag 0.8.2-git1-20160219)

* Sun Feb 14 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.2-1.git20160214
- Rebuild for sayonara (git tag 0.8.2-git0-20160214)

* Sun Feb 14 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.2-1.git20160214
- Rebuild for sayonara (git tag 0.8.2-git0-20160214)

* Sun Feb 14 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.2-1.git-20160214
- Rebuild for sayonara (git tag 0.8.2-git0-20160214)

* Sun Jan 10 2016 Lucio Carreras <luciocarreras@gmail.com> - 0.8.1-1.svn319
- Rebuild for sayonara revision 319

* Fri Dec 18 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.8.0-3.svn293
- Rebuild for sayonara revision 293

* Fri Dec 18 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.8.0-2.svn292
- Rebuild for sayonara revision 292

* Wed Dec 16 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.8.0-1.svn286
- Rebuild for sayonara revision 286

* Fri Oct 16 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.1-9.svn211
- Rebuild for sayonara revision 211

* Fri Oct 16 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.1-8.svn211
- Rebuild for sayonara revision 211

* Mon Oct 05 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.1-7.svn195
- Rebuild for sayonara revision 195

* Sun Oct 04 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.1-6.svn189
- Rebuild for sayonara revision 189

* Sat Oct 03 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.1-5.svn188
- Rebuild for sayonara revision 188

* Sat Oct 03 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.1-4.svn188
- Rebuild for sayonara revision 188

* Sat Oct 03 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.1-3.svn188
- Rebuild for sayonara revision 188

* Sat Oct 03 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.1-2.svn188
- Rebuild for sayonara revision 188

* Sat Oct 03 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.1-1.svn188
- Rebuild for sayonara revision 188

* Sun Sep 13 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.0-4.svn155
- Rebuild for sayonara revision 155

* Sun Sep 13 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.0-3.svn154
- Rebuild for sayonara revision 154

* Mon Aug 24 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.7.0-2.svn148
- fixed trailing spaces in Helper/MetaData/LibraryItem.cpp
- fixed soundcloud install dir issues
- fixed QObject dependencies neccessary under Fedora 22 in certain source files
- made Gstreamer mandatory

* Sat Aug 22 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-1.svn144
- rebuild for new svn release

* Fri Aug 14 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.6-6.svn119
- rebuild for new svn release

* Fri Jul 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.6-5.svn80
- rebuild for new svn release

* Thu Jul 16 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.6-4.svn73
- rebuild for new svn release

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-3.svn62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.6.6-2.svn62
- added new CMake Build type option: RelWithDebInfo
- removed screenshots from sayonara.appdata.xml

* Sun May 24 2015 Lucio Carreras <luciocarreras@gmail.com> - 0.6.6-1.svn52
- changed server adress
- changed cmake call
- added -fPIC compiler flag for debug mode in CMakeLists.txt
- added sayonara.appdata.xml on SVN

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.5-2.svn1037
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.5-1.svn1037
- rebuild for new svn release
- added 'if' conditions to fix f23 build

* Tue Feb 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2-4.svn1021
- rebuild for new svn release

* Mon Feb 16 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2-3.svn1018
- rebuild for new svn release
- cosmetic changes
- take ownership of unowned directory %%{_datadir}/%%{name}/translations
- take ownership of unowned directory %%{_datadir}/%%{name}/translations/icons

* Mon Feb 16 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2-2.svn1016
- deleted BR  gstreamer1-devel because its redundant
- deleted RR svn isn't needed
- corrected license tag to GPLv3+
- added RR hicolor-icon-theme
- mark license files as %%license where available
- added appdata.xml file
- modified desktop file Categories
- removed java stuff
- addd BR libappstream-glib

* Fri Feb 13 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.2-1.svn1016
- rebuild for new svn release
- cleanup spec file

* Mon Sep 01 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-1.4.svn878
- enabled debugging informations
- rebuild for new svn release
- set correct file permisson

* Fri Aug 29 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.1-1.3.svn870
- rebuild for new svn release
- added more comments

* Tue Jun 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-1.2.svn851
- removed unecessary BR glib2-devel
- removed unecessary BR alsa-lib-devel
- removed unecessary BR libxml2-devel

* Tue Jun 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-1.2.svn851
- rebuild for new svn release
- added svn Requirement
- corrected svn path

* Mon Jun 09 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-1.1.svn850
- added download instructions
- rebuild for new svn release

* Tue Oct 29 2013 Brendan Jones <brendan.jones.it@gmail.com> - 0.4.0-1.0.svn695
- Inital release.
