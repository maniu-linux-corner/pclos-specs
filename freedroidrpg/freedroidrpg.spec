%define name	freedroidrpg
%define	oname	freedroidRPG
%define version	0.16.0
%define mversion 0.16
%define release	%mkrel 1
%define	Summary	A Diablo clone with the Tux as hero in a world of rampaging robots

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://freedroid.sourceforge.net/
Source0:	%{oname}-%{mversion}.tar.gz
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png

License:	GPLv2
Group:		Games/Adventure
BuildRequires:	libSDL_image-devel libSDL_net-devel libSDL_mixer-devel
BuildRequires:	%{_lib}gtk+2.0_0-devel mesa-common-devel
BuildRequires:	%{_lib}jpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	gettext-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	%{oname}
Provides:	%{oname} = %{version}-%{release}

%description
FreeDroidRPG is a free isometric RPG game inspired by elements of Diablo and
Fallout. Originally based on FreeDroid Classic, this project now has vastly deviated
from its parent.

This game tells the story of a world destroyed by a conflict between the bots
and their human masters. Play as Tux in a quest to save the world from the murderous
rebel bots who know no mercy. You get to choose which path you wish to follow, and
freedom of choice is everywhere in the game.

FreeDroidRPG features a complete real time combat system with melee and ranged
weapons, fairly similar to the proprietary game Diablo. There also is an 
innovative system of magic, with features such as forced casting and over 20 spells.
You can use over 50 different kinds of items and fight countless enemies on
your way to your destiny.

We have an advanced dialogue system, which aims at being at least on par with
Fallout's. The dialogues in the game represent a large part of the gameplay.
Finally, if guns are too inaccurate and blades too messy, you can always take
over your enemies and have them fight on your side."



%prep
%setup -q -n %{name}-%{mversion}
# %patch0 -p1 -b .strfmt
rm -rf `find -name .xvpics`

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
make clean
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=FreedroidRPG
Comment=%{Summary}
Exec=%{_gamesbindir}/%{oname}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;AdventureGame;
EOF

install %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -n %{name}
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/applications/mandriva*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%dir %{_gamesdatadir}/%{name}
%dir %{_gamesdatadir}/%{name}/sound
%{_gamesdatadir}/%{name}/sound/*
%{_gamesdatadir}/%{name}/graphics
%{_gamesdatadir}/%{name}/map
%{_gamesdatadir}/%{name}/dialogs
%defattr(755,root,root,755)
%{_gamesbindir}/*
%{_gamesdatadir}/appdata/freedroidRPG.appdata.xml
%{_gamesdatadir}/applications/freedroidRPG.desktop
%{_gamesdatadir}/freedroidrpg/*
%{_gamesdatadir}/icons/HighContrast/*
%{_gamesdatadir}/icons/hicolor/*
%{_mandir}/man6/freedroidRPG.6.bz2




%changelog
* Wed May 25 2011 Mank <mank dot pclos@gmail.com> 0.14.1-1pclinux2011.1
-	Build for PCLinuxOS
* Sat Nov 27 2010 Zombie Ryushu <ryushu@mandriva.org> 0.14.1-1mdv2011.0
+ Revision: 601736
- Upgrade to 0.14.1

* Sat Nov 20 2010 Zombie Ryushu <ryushu@mandriva.org> 0.14rc3-1mdv2011.0
+ Revision: 599316
- Remove string format patch
- Upgrade to 0.14rc3
- Upgrade to 0.14rc3

* Sat Jan 23 2010 Frederik Himpe <fhimpe@mandriva.org> 0.13-1mdv2010.1
+ Revision: 495306
- Update to new version 0.13
- Rediff string format patch

* Sat May 02 2009 Frederik Himpe <fhimpe@mandriva.org> 0.12.1-1mdv2010.0
+ Revision: 370395
- BuildRequires: gettext-devel
- Update to new version 0.12.1

* Wed Mar 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.12-1mdv2009.1
+ Revision: 354014
- Update to new version 0.12
- Add patch fixing build with -Werror=format-security

* Tue Dec 16 2008 Zombie Ryushu <ryushu@mandriva.org> 0.11.1-2mdv2009.1
+ Revision: 314888
- Correct description by request of Authur Huillet
- Correct description by request of Authur Huillet

* Sun Dec 07 2008 Zombie Ryushu <ryushu@mandriva.org> 0.11.1-1mdv2009.1
+ Revision: 311660
- Version bump to fix map errors
- Bump to Version 0.11.1 to fix map errors

  + Funda Wang <fwang@mandriva.org>
    - New version 0.11

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.10.3-3mdv2009.0
+ Revision: 245362
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 22 2007 Jérôme Soyer <saispo@mandriva.org> 0.10.3-1mdv2008.1
+ Revision: 101330
- New release
- New release

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sat Jul 07 2007 Olivier Blin <oblin@mandriva.com> 0.10.2-1mdv2008.0
+ Revision: 49398
- 0.10.2 (from Zombie Ryushu)

* Mon May 28 2007 Olivier Blin <oblin@mandriva.com> 0.10.1-2mdv2008.0
+ Revision: 31941
- add back menu post scripts

* Sat May 26 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.10.1-1mdv2008.0
+ Revision: 31562
- update to 0.10.1 (fixes #28932)
- remove old debian menu
- voice samples seems to have disappeared..


* Sun Dec 31 2006 Olivier Blin <oblin@mandriva.com> 0.10.0-1mdv2007.0
+ Revision: 102975
- 0.10.0
- Import freedroidrpg

* Thu Aug 24 2006 Götz Waschk <waschk@mandriva.org> 0.9.13-3mdv2007.0
- fix buildrequires

* Thu Aug 03 2006 Götz Waschk <waschk@mandriva.org> 0.9.13-2mdv2007.0
- xdg menu

* Sat May 13 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.9.13-1mdk
- 0.9.13 (closes #22291)
- %%mkrel

* Fri Aug 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.12-2mdk
- rebuild for new menu

* Thu Apr 15 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.12-1mdk
- 0.9.12

* Wed Feb 11 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.10-2mdk
- fix command in menu item
- compile with gtk+ and opengl support

* Sat Jan 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.10-1mdk
- 0.9.10
- convert name to lowercase

