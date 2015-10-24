#
# spec file for package qutim
#
%define         _sharedir share/apps/qutim
Name:           qutim
Version:        0.3.3
Release:        117.2
License:        GPLv3
Summary:        QutIM instant messenger
Url:            http://qutim.org/
Group:          Productivity/Networking/Instant Messenger
Source0:        %{name}-%{version}.tar.xz

Requires:       %{_lib}qca2
Requires:       %{name}-icons
Obsoletes:      qutim-plugins qutim-plugins-debuginfo qutim-plugin-phononsound
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
AutoReq: no

BuildRequires:  cmake >= 2.8
BuildRequires:  %{_lib}qca2-devel
BuildRequires:  %{_lib}qt4-devel
BuildRequires:  phonon-devel
BuildRequires:  %{_lib}otr-devel >= 3.2.0
Requires:       task-qt4

%description
Multiprotocol instant messenger.

%package devel
Summary:        Development files for QutIM
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{_lib}qca2-devel
Requires:       %{_lib}qt4-devel

%description devel
Development files for QutIM

%package icons
Summary:        Icon files for QutIM
BuildArch:      noarch
Requires:       %{name} = %{version}

%description icons
Icon files for QutIM package.

%package plugin-aspeller
Summary:        Aspeller plugin for QutIM
BuildRequires:  aspell
BuildRequires:  %{_lib}aspell-devel
Requires:       %{name} = %{version}

%description plugin-aspeller
Spell checker plugin for QutIM based on aspell

%package plugin-hunspeller
Summary:        Hunspeller plugin for QutIM
Requires:       %{name} = %{version}

BuildRequires:  hunspell
BuildRequires:  %{_lib}hunspell-devel

%description plugin-hunspeller
Spell checker plugin for QutIM based on hunspell

%package plugin-kdeintegration
Summary:        KDE integration plugin for QutIM
Requires:       %{name} = %{version}
BuildRequires:  kdelibs-devel

%description plugin-kdeintegration
Plugin that provides integration with KDE

%package plugin-sdlsound
Summary:        SDL sound plugin for QutIM
Requires:       %{name} = %{version}

BuildRequires:  %{_lib}SDL_mixer-devel

%description plugin-sdlsound
Sound engine plugin based on SDL

%package plugin-plugman
Summary:       PlugMan plugin for qutim
Requires:      %{name} = %{version}
Requires:      task-qt4
BuildRequires: attica-devel

%description plugin-plugman
Plugin for downloadong additional plugins and artwork.

%prep

%setup -q -n %{name}-%{version}

%build
mkdir build
pushd build
export CXXFLAGS="-O0"
export QMAKE_CXXFLAGS="-O0"
cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DSYSTEM_JREEN=0 \
    -DSYSTEM_VREEN=0 \
    -DLIB_SUFFIX="`getconf LONG_BIT`" \
    -DBEARERMANAGER=1 \
    -DMULTIMEDIABACKEND=0 \
    -DANTIBOSS=0 \
    -DPLUGMAN=1 \
    -DQMLCHAT=0 \
    -DDBUSAPI=0 \
    -DAWN=0 \
    -DMOBILEABOUT=0 \
    -DMOBILECONTACTINFO=0 \
    -DMOBILENOTIFICATIONSSETTINGS=1 \
    -DNOTIFICATIONSSETTINGS=1 \
    -DMOBILESETTINGSDIALOG=0 \
    -DQRCICONS=0 \
    -DQUTIM_SHARE_DIR=%{_sharedir} \
    -DSYSTEM_QTDOCKTILE=0 \
    -DQUTIM_GENERATE_DOCS=0 \
    ..
make
popd #build

%install
pushd build
%make_install

popd #build

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_libdir}/qutim
%dir %{_libdir}/qutim/plugins

#{_datadir}{name}
%doc AUTHORS ChangeLog COPYING README.mediawiki

%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

#lib
%{_libdir}/libqutim.so.*
%{_libdir}/libqtdocktile.so.*
%{_libdir}/libqutim-adiumchat.so.*
%{_libdir}/libqutim-adiumwebview.so.*
%{_libdir}/libqutim-simplecontactlist.so.*

%{_libdir}/libjreen.so.1
%{_libdir}/libjreen.so.1.1.1
%{_libdir}/libqtdocktile.so
#%{_libdir}/libvreen.so
%{_libdir}/libvreen.so.0
%{_libdir}/libvreen.so.0.9.5
%{_libdir}/libqutim.so
%{_libdir}/libqutim-adiumchat.so
%{_libdir}/libqutim-adiumwebview.so
%{_libdir}/libqutim-simplecontactlist.so

%{_libdir}/qt4/imports/org/docktile/libqmldocktileplugin.so
%{_libdir}/qt4/imports/org/docktile/qmldir
%{_libdir}/qutim/plugins/libautopaster.so
%{_libdir}/qutim/plugins/libquetzal.so
%{_libdir}/qutim/plugins/libscreenshoter.so
%{_libdir}/qt4/plugins/docktile/libunityplugin.so
%{_libdir}/qutim/plugins/libnotificationssettings.so
%{_libdir}/qutim/plugins/libsdlsound.so


#app icons
%{_datadir}/pixmaps/qutim.xpm

#protocols
%{_libdir}/qutim/plugins/libirc.so
%{_libdir}/qutim/plugins/libjabber.so
%{_libdir}/qutim/plugins/libmrim.so
%{_libdir}/qutim/plugins/liboscar.so
%{_libdir}/qutim/plugins/liboscaridentify.so
%{_libdir}/qutim/plugins/liboscarxstatus.so
%{_libdir}/qutim/plugins/libvkontakte.so

#plugins
%{_libdir}/qutim/plugins/libautoreply.so
%{_libdir}/qutim/plugins/libadiumwebview.so
%{_libdir}/qutim/plugins/libaccountcreator.so
%{_libdir}/qutim/plugins/libaddcontactdlg.so
%{_libdir}/qutim/plugins/libadiumchat.so
%{_libdir}/qutim/plugins/libadiumsrvicons.so
%{_libdir}/qutim/plugins/libauthdialog.so
%{_libdir}/qutim/plugins/libbearermanager.so
%{_libdir}/qutim/plugins/libchatnotificationsbackend.so
%{_libdir}/qutim/plugins/libchatspellchecker.so
%{_libdir}/qutim/plugins/libcontactinfo.so
%{_libdir}/qutim/plugins/libdataformsbackend.so
%{_libdir}/qutim/plugins/libemoticonssettings.so
%{_libdir}/qutim/plugins/libfiletransfer.so
%{_libdir}/qutim/plugins/libfiletransfersettings.so
%{_libdir}/qutim/plugins/libidledetector.so
%{_libdir}/qutim/plugins/libidlestatuschanger.so
%{_libdir}/qutim/plugins/libjoinchatdialog.so
%{_libdir}/qutim/plugins/libjoingroupchatdlg.so
%{_libdir}/qutim/plugins/libjsonconfig.so
%{_libdir}/qutim/plugins/libjsonhistory.so
%{_libdir}/qutim/plugins/libkineticscroller.so
%{_libdir}/qutim/plugins/libkopeteemoticonsbackend.so
%{_libdir}/qutim/plugins/liblocalization.so
%{_libdir}/qutim/plugins/libmetacontacts.so
%{_libdir}/qutim/plugins/libmigration02x03.so
%{_libdir}/qutim/plugins/libnocryptoservice.so
%{_libdir}/qutim/plugins/libnotificationfilter.so
%{_libdir}/qutim/plugins/libmobilenotificationssettings.so
%{_libdir}/qutim/plugins/liboldsoundtheme.so
%{_libdir}/qutim/plugins/libpassword.so
%{_libdir}/qutim/plugins/libcontactmodel.so
%{_libdir}/qutim/plugins/libplistconfig.so
%{_libdir}/qutim/plugins/libproxysettings.so
%{_libdir}/qutim/plugins/libqticons.so
%{_libdir}/qutim/plugins/libsearchdialog.so
%{_libdir}/qutim/plugins/libservicechooser.so
%{_libdir}/qutim/plugins/libsessionhelper.so
%{_libdir}/qutim/plugins/libshortcutsettings.so
%{_libdir}/qutim/plugins/libsimpleaboutdialog.so
%{_libdir}/qutim/plugins/libsimpleactionbox.so
%{_libdir}/qutim/plugins/libsimpleactions.so
%{_libdir}/qutim/plugins/libsimplecontactlist.so
%{_libdir}/qutim/plugins/libsimplecontactlistwidget.so
%{_libdir}/qutim/plugins/libsimplecontactdelegate.so
%{_libdir}/qutim/plugins/libsimplerosterstorage.so
%{_libdir}/qutim/plugins/libsoundthemeselector.so
%{_libdir}/qutim/plugins/libstackedchatform.so
%{_libdir}/qutim/plugins/libtabbedchatform.so
%{_libdir}/qutim/plugins/libtextchat.so
%{_libdir}/qutim/plugins/libtorycontactlistwidget.so
%{_libdir}/qutim/plugins/libtrayicon.so
%{_libdir}/qutim/plugins/libxsettingsdialog.so
%{_libdir}/qutim/plugins/liblinuxintegration.so
#%{_libdir}/qutim/plugins/libphononsound.so
%{_libdir}/qutim/plugins/libcomparators.so

%{_libdir}/qutim/plugins/libaescrypto.so
%{_libdir}/qutim/plugins/libantispam.so
%{_libdir}/qutim/plugins/libbirthdayreminder.so
%{_libdir}/qutim/plugins/libclconf.so
%{_libdir}/qutim/plugins/libemoedit.so
%{_libdir}/qutim/plugins/libfloaties.so
%{_libdir}/qutim/plugins/libhistman.so
%{_libdir}/qutim/plugins/libkineticpopups.so
%{_libdir}/qutim/plugins/libmassmessaging.so
%{_libdir}/qutim/plugins/liboldcontactdelegate.so
%{_libdir}/qutim/plugins/libscriptapi.so
%{_libdir}/qutim/plugins/libunreadmessageskeeper.so
%{_libdir}/qutim/plugins/libweather.so
%{_libdir}/qutim/plugins/liblogger.so
%{_libdir}/qutim/plugins/liburlpreview.so
%{_libdir}/qutim/plugins/libyandexnarod.so
%{_libdir}/qutim/plugins/libdbusnotifications.so
%{_libdir}/qutim/plugins/libnowplaying.so
%{_libdir}/qutim/plugins/libhighlighter.so
%{_libdir}/qutim/plugins/libblogimprover.so
%{_libdir}/qutim/plugins/libupdater.so
%{_libdir}/qutim/plugins/libformula.so
%{_libdir}/qutim/plugins/libofftherecord.so
%{_libdir}/qutim/plugins/libdocktile.so

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libjreen.so
%{_libdir}/libvreen.so
%{_datadir}/cmake/Modules
%{_libdir}/pkgconfig/libjreen.pc
%{_libdir}/pkgconfig/qtdocktile.pc


%files icons
%defattr(-,root,root)
%{_datadir}/apps/qutim
%{_datadir}/icons/*

%files plugin-aspeller
%defattr(-,root,root)
%{_libdir}/qutim/plugins/libaspeller.so

%files plugin-hunspeller
%defattr(-,root,root)
%{_libdir}/qutim/plugins/libhunspeller.so

%files plugin-kdeintegration
%defattr(-,root,root)
%{_libdir}/qutim/plugins/libkdeintegration.so
%dir %{_datadir}/apps/desktoptheme/
%dir %{_datadir}/apps/desktoptheme/default
%dir %{_datadir}/apps/desktoptheme/default/icons
%{_datadir}/apps/desktoptheme/default/icons/qutim.svg

#%files plugin-sdlsound
#%defattr(-,root,root)
#%{_libdir}/qutim/plugins/libsdlsound.so

#%files plugin-plugman
#%defattr(-,root,root)
#%{_libdir}/qutim/plugins/libplugman.so

%changelog
