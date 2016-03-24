%define qmakeqt5 /usr/lib64/qt5/bin/qmake
Name: kvantum
Version: 0.9.5.git.1458057296.bce024b
Release: 117.1
Summary: Kvantum is an SVG-based theme engine for Qt4/Qt5 and KDE
Group:   System/GUI/KDE
Packager: Konstantin Voinov <konstantin.voinov@gmail.com>

License: GPL-3.0
URL: https://github.com/tsujan/Kvantum
Source0: kvantum-%{version}.tar.gz
Patch0: kvantum.patch
BuildRequires: pkgconfig(QtCore)

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Svg)

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: kde-style-kvantum

%description

Kvantum is an SVG-based theme engine for Qt4/Qt5 and KDE.
It has a default dark theme but goes far beyond it: you could make themes with very different looks and feels
for it and Kvantum will let you control almost every aspect of Qt widgets.

%package qt4

Summary: Kvantum is an SVG-based theme engine for Qt4 and KDE4
Group:   System/GUI/KDE
Obsoletes: kde-style-kvantum


%package qt5
Summary: Kvantum is an SVG-based theme engine for Qt5 and KF5
Group:   System/GUI/KDE

%description qt5
Kvantum is an SVG-based theme engine for Qt4/Qt5 and KDE.
It has a default dark theme but goes far beyond it: you could make themes with very different looks and feels
for it and Kvantum will let you control almost every aspect of Qt widgets.

This package provides Kvantum theme engine for Qt5.



%description qt4
Kvantum is an SVG-based theme engine for Qt4/Qt5 and KDE.
It has a default dark theme but goes far beyond it: you could make themes with very different looks and feels
for it and Kvantum will let you control almost every aspect of Qt widgets.
Kvantum theme engine for Qt5

This package provides Kvantum theme engine for Qt4.



%package qt5-manager
Summary:        Configuration manager for Kvantum style
Group:          System/GUI/KDE
Requires:       %{name}-qt5 = %{version}
Obsoletes:	kde-style-kvantum-manager

%description qt5-manager
Kvantum is an SVG-based theme engine for Qt4/Qt5 and KDE.
It has a default dark theme but goes far beyond it: you could make themes with very different looks and feels
for it and Kvantum will let you control almost every aspect of Qt widgets.

This package provides Qt5-based configuration manager for Kvantum style.


%package themes
Summary: Themes for Kvantum style
Group:   System/GUI/KDE
BuildArch: noarch

%description themes
Kvantum is an SVG-based theme engine for Qt4/Qt5 and KDE.
It has a default dark theme but goes far beyond it: you could make themes with very different looks and feels
for it and Kvantum will let you control almost every aspect of Qt widgets.

This package provides some themes for Kvantum style.

%package openbox-themes
Summary: Openbox themes for Kvantum style
Group:   System/GUI/
BuildArch: noarch

%description openbox-themes
Kvantum is an SVG-based theme engine for Qt4/Qt5 and KDE.
It has a default dark theme but goes far beyond it: you could make themes with very different looks and feels
for it and Kvantum will let you control almost every aspect of Qt widgets.

This package provides some Openbox themes for Kvantum style.

%package doc

Summary: Documentation for Kvantum, SVG-based theme engine for Qt4 and Qt5
Group:   System/GUI/KDE
BuildArch: noarch

%description doc
Kvantum is an SVG-based theme engine for Qt4/Qt5 and KDE.
It has a default dark theme but goes far beyond it: you could make themes with very different looks and feels
for it and Kvantum will let you control almost every aspect of Qt widgets.

This package provides documentation for Kvantum style engine.

%prep
%setup -n kvantum-%{version}
mv Kvantum/* .
rmdir Kvantum
%patch0

%build

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

#qmake
#make %{?_smp_mflags}
#strip style/libkvantum.so
#%install
#make INSTALL_ROOT=%{buildroot} PREFIX=%{_prefix} install




make distclean
%qmakeqt5
make %{?_smp_mflags}
strip style/libkvantum.so
make INSTALL_ROOT=%{buildroot} PREFIX=%{_prefix} install



mkdir -p %{buildroot}/usr/share/doc/packages/%{name}-doc
cp -r doc/* %{buildroot}/usr/share/doc/packages/%{name}-doc/

%files qt4
%defattr(-,root,root)
%dir %{_libdir}/qt4/plugins/styles
%{_libdir}/qt4/plugins/styles/*


%files qt5
%doc ChangeLog COPYING NEWS README
%defattr(-,root,root)
%dir %{_libdir}/qt5/plugins/styles
%{_libdir}/qt5/plugins/styles/*



%files themes
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/apps
%dir %{_datadir}/kde4/apps/color-schemes
%{_datadir}/kde4/apps/color-schemes/*

%dir %{_datadir}/color-schemes/
%dir %{_datadir}/Kvantum
%dir %{_datadir}/Kvantum/KvantumAlt
%dir %{_datadir}/Kvantum/KvCurves
%dir %{_datadir}/Kvantum/KvDark
%dir %{_datadir}/Kvantum/KvFlat
%dir %{_datadir}/Kvantum/KvFlatLight
%dir %{_datadir}/Kvantum/KvGray
%dir %{_datadir}/Kvantum/KvDynamo
%dir %{_datadir}/Kvantum/KvDarkRed
%dir %{_datadir}/Kvantum/KvBeige
%dir %{_datadir}/Kvantum/KvCurves3d
%dir %{_datadir}/Kvantum/KvCurvesLight
%dir %{_datadir}/Kvantum/KvGnome
%dir %{_datadir}/Kvantum/KvSimplicity
%dir %{_datadir}/Kvantum/KvFlatRed
%dir %{_datadir}/Kvantum/KvGnomeDark
%{_datadir}/color-schemes/*
%{_datadir}/Kvantum/KvantumAlt/*
%{_datadir}/Kvantum/KvCurves/*
%{_datadir}/Kvantum/KvDark/*
%{_datadir}/Kvantum/KvFlat/*
%{_datadir}/Kvantum/KvFlatLight/*
%{_datadir}/Kvantum/KvGray/*
%{_datadir}/Kvantum/KvDynamo/*
%{_datadir}/Kvantum/KvDarkRed/*
%{_datadir}/Kvantum/KvBeige/*
%{_datadir}/Kvantum/KvCurves3d/*
%{_datadir}/Kvantum/KvCurvesLight/*
%{_datadir}/Kvantum/KvGnome/*
%{_datadir}/Kvantum/KvSimplicity/*
%{_datadir}/Kvantum/KvFlatRed/*
%{_datadir}/Kvantum/KvGnomeDark/*


%files openbox-themes
%defattr(-,root,root)
%dir %{_datadir}/themes/KvBeige
%dir %{_datadir}/themes/Kvantum
%dir %{_datadir}/themes/KvCurvesLight
%dir %{_datadir}/themes/KvDynamo
%dir %{_datadir}/themes/KvFlatLight
%dir %{_datadir}/themes/KvGnome
%dir %{_datadir}/themes/KvGray
%dir %{_datadir}/themes/KvSimplicity
%dir %{_datadir}/themes/KvDarkRed
%dir %{_datadir}/themes/KvGnomeDark
%dir %{_datadir}/themes/KvBeige/openbox-3
%dir %{_datadir}/themes/Kvantum/openbox-3
%dir %{_datadir}/themes/KvCurvesLight/openbox-3
%dir %{_datadir}/themes/KvDynamo/openbox-3
%dir %{_datadir}/themes/KvFlatLight/openbox-3
%dir %{_datadir}/themes/KvGnome/openbox-3
%dir %{_datadir}/themes/KvGray/openbox-3
%dir %{_datadir}/themes/KvSimplicity/openbox-3
%dir %{_datadir}/themes/KvDarkRed/openbox-3
%dir %{_datadir}/themes/KvGnomeDark/openbox-3
%{_datadir}/themes/KvBeige/openbox-3/*
%{_datadir}/themes/Kvantum/openbox-3/*
%{_datadir}/themes/KvCurvesLight/openbox-3/*
%{_datadir}/themes/KvDynamo/openbox-3/*
%{_datadir}/themes/KvFlatLight/openbox-3/*
%{_datadir}/themes/KvGnome/openbox-3/*
%{_datadir}/themes/KvGray/openbox-3/*
%{_datadir}/themes/KvSimplicity/openbox-3/*
%{_datadir}/themes/KvDarkRed/openbox-3/*
%{_datadir}/themes/KvGnomeDark/openbox-3/*

%files doc

%defattr(-,root,root)
%{_docdir}/%{name}-qt5/*
%{_docdir}/packages/%{name}-doc/*
%{_docdir}/packages/%{name}-doc/Glassy/*


%files qt5-manager
%defattr(-,root,root)
%{_bindir}/*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/applications/kvantummanager.desktop
%{_datadir}/icons/hicolor/scalable/apps/kvantum.svg




#%clean

%changelog
* Wed Mar 16 2016 kill_it@mail.ru git
- Added three extra themes (KvSimplicity, KvGnomeDark and KvFlatRed), polished some themes and modified KvDarkRed.
- At last a workaround for the Qt5 "hover bug", because of which, comboboxes and buttons remain in the mouseover state after their menus are closed and without the cursor being over them.
- Use the pressed state for focused non-editable comboboxes.
- Don't enforce darkness on text editors.
- Moved the Kvantum icon to the standard hicolor directory.
* Sat Feb 20 2016 kill_it@mail.ru
- Verion 0.9.5
- Added Openbox themes for use with the included Kvantum themes (under LXQT).
- Added a new extra theme (KvSimplicity).
- Patch kvantum.pro allows build themes for openSUSE 13.1
* Wed Feb 10 2016 konstantin.voinov@gmail.com git
- Version 0.9.4
- Added a hacking key for not styling any toolbar other than the top one.
- Added a hacking key for tinting label icons on mouseover.
- Added a hacking key for setting the opacity of disabled icons.
- Draw each spinbox indicator only once.
- Draw framed spin buttons vertically if a null widget is fed into the related methods.
- Show all menu-items in the case of too big menus.
- A little overlap for submenus.
- Fixes for tabbar base panel.
- Added KvGnome, with a Gnome like look and feel, to the extra themes.
- The interior used in partial frame expansion should have the frame name.
- Workaround for bad hard-coded slider styling.
- Swap left and right text margins in RTL.
- Added a general key for submenu overlap with -1 (automatic) as default.
- Take frame vertical asymmetry into account when drawing labels of push buttons and comboboxes.
* Tue Dec 22 2015 konstantin.voinov@gmail.com git
- Version 0.9.3
- Support high DPI displays (when QT_DEVICE_PIXEL_RATIO > 1 and even when AA_UseHighDpiPixmaps isn't set).
- Draw subwindow titlebar buttons on menubars exactly as on MDI titlebars.
- Added a hacking key for not styling any toolbar other than the top one.
- Calculate the height of problematic fonts like Noto Sans correctly.
- Corrected a typo in SE_TabWidgetRightCorner.
- Force progressbar roundness on KCapacityBar in all circumstances.
- Always show text in KisSliderSpinBox.
- Removed the redundant key "textless_progressbar".
- Group toolbar buttons based on their heights (not their iconlessness).
* Wed Nov 25 2015 konstantin.voinov@gmail.com git
- Version 0.9.2
- Added '$DATADIR/themes/$THEME_NAME/Kvantum/', '~/.themes/$THEME_NAME/Kvantum/' and '~/.local/share/themes/$THEME_NAME/Kvantum/' to the installation paths but with lower priority (the second directory ha
- Added a hacking key for not using bold font for the text of a default push button.
- Added a general key for layout spacing, with a value between 2 and 10px.
- Added another extra theme (KvCurves3d).
- Used a more reliable boolean for determining whether a slider is horizontal.
- Support the #RRGGBBAA format for color names.
- Use the combobox indicator element if its normal state exists.
- Respect darkness only when the window color is dark enough.
- Don't group toolbar buttons on a vertical toolbar because they wouldn't look elegant, especially with frame expansion.
- Don't rotate toolbar buttons by 90 degrees on a vertical toolbar.
* Thu Nov 12 2015 konstantin.voinov@gmail.com git
- A workaround for the rare occasion when the background of a Qt5 composited tooltip is filled by the window background color.
- In the case of menus and tooltips, check compositing at the moment of their creaton (this fixes shadowless menus of KF5 desktop and panel).
- Always show text in KCapacityBar.
- Added a general key for setting tooltip display delay.
- Consider the possibility of color gradients in the case of view-items with hard-coded backgrounds when setting their texts.
- Gave priority to the new location of kdeglobals.
* Thu Oct  1 2015 konstantin.voinov@gmail.com git
- Added two extra themes (KvDarkRed and KvBeige).
- Minor modifications to Kvantum Manager (to recognize KF5 and LXQT more).
* Tue Aug 25 2015 konstantin.voinov@gmail.com git
- Move ChangeLog COPYING NEWS README to main package.
- Use the generic frame for combo menus.
- Added a key for drawing editable comboboxes as lineedits.
- Use the generic frame for combo menus.
- Check iconlessness when grouping toolbar buttons.
- Added a hacking key for merging PCManFM-qt's sidepane with its surroundings (to Kvantum Manager).
- It's time to have a decent icon for Kvantum.
* Mon Aug 24 2015 konstantin.voinov@gmail.com git
- Version 0.8.25
- Added a key for drawing editable comboboxes as lineedits.
- V0.8.24
- Added some of my themes, that don't need special titlebars, to the project for Kvantum to have extra themes by default. They're installed as root with Qt5 installation.
- Fixed Kvantum Managers's comment tooltip for root themes.
- Fixed a miscalculation when the text has shadow.
- Took care of buttonless spinboxes.
- Don't move the cursor out of the window and back for x11 dragging with Qt5. This workaround not only isn't needed anymore but also creates artifacts with Openbox.
* Fri Aug 14 2015 konstantin.voinov@gmail.com git
- Version 0.8.24
- Added some of my themes, that don't need special titlebars, to the project for Kvantum to have extra themes by default. They're installed as root with Qt5 installation.
- Fixed Kvantum Managers's comment tooltip for root themes.
* Mon Jul 13 2015 konstantin.voinov@gmail.com git
- Version 0.8.23
- Added two new sections for opaque and translucent dialogs. The fallbacks are the sections "WindowTranslucent" and "Window".
- Added KF5 system and user color scheme paths to "style.pro" and "KvantumManager.cpp", respectively. The system path is used with the Qt5 compilation.
- Added a hacking key for removing the icons of pushbuttons as far as possible.
- Another hacking key for removing menu icons.
- A lot of subtle changes that together guarantee a more logical look under unusual circumstances.
- Corrected some miscalculations.
- When calculating spinbox size, consider the case where only QAbstractSpinBox is subclassed.
- Fixed a compilation error with Qt5-5.5.0.
- Took care of textless menuitems.
- Forced KCalcDisplay's text color.
- Let the size grip be just an indicator and added one to the default theme.
- Draw the size grip relative to the corner.
- Don't allow windows to have custom background colors if they have different window and base colors. As for their text color, it's the responsibility of developers to use QStyle correctly.
- Another criterion for giving shadow/translucency to menus.
- Changed the toggled and pressed buttons of the default theme.
- To get the spinbox maximum-length text, use the real width of the text, not the number of its characters.
- Version 0.8.22
- Added an experimental hacking key to force size grips of dialogs and statusbars.
- Partially rounded view-items (in some places) and headers.
- How did I forget namespace in such a program?!
- Take care of transparent line-edits in comboboxes (I've seen them only in Qt5 Cantata).
- Added a key for the minimum scrollbar extent and gave a 1px space to scrollbars of very thin widgets.
- Set lower/upper limits for some integer keys.
- If "mirror_doc_tabs" is false, don't mirror tabs when "attach_active_tab" is also false.
* Tue Jul  7 2015 konstantin.voinov@gmail.com git
- Version 0.8.21
- If the interior element of the "expand-" objects exists, make borders rounded even when the widget height is greater than the value of frame expansion.
- Now it's possible to have clean borders with maximally rounded corners (without a new key and when the "border-" elements exist).
- Added a configuration section for distinguishing between opaque and translucent window backgrounds if needed.
- Added a key for not mirroring the top/left tab shape to draw the bottom/right tab in the document mode.
- Set the pressed state for a combobox if its line-edit has focus.
- Compile kvantumpreview and kventummanager against Qt5 by default.
- Workaround for the nasty behavior of Qt5 QSettings, which reorders keys on writing.
- A little more space for centered toolbar handles.
- Added a hacking key to force size grips of dialogs and statusbars.
* Wed Mar  4 2015 konstantin.voinov@gmail.com git
- first line at changelog
