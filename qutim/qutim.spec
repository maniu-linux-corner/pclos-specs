#
# spec file for package qutim
#
# Copyright (c) 2012 Sergei Lopatin <magist3r@gmail.com>
%define         _sharedir share/apps/qutim
Name:           qutim
Version:        0.3.1+git.1357659068
Release:        117.1
License:        GPLv3
Summary:        QutIM instant messenger
Url:            http://qutim.org/
Group:          Productivity/Networking/Instant Messenger
Source0:        %{name}-%{version}.tar
#Patch0:        150.patch
#Patch1:        6.patch
Requires:       libjreen1 >= 1.1.0
Requires:       libvreen0 >= 0.9.1
Requires:       libqtdocktile1 >= 1.0.0
Requires:       libqca1-sasl
Requires:       %{name}-icons
Obsoletes:      qutim-plugins qutim-plugins-debuginfo qutim-plugin-phononsound
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version}
BuildRequires:  update-desktop-files
BuildRequires:  fdupes
%define         _sharedir share/kde4/apps/qutim
%endif

BuildRequires:  cmake >= 2.8
BuildRequires:  libqca2-devel
#BuildRequires:  qt-webkit-devel
BuildRequires:  libjreen-devel >= 1.1.0
BuildRequires:  libvreen-devel >= 0.9.1
BuildRequires:  libqtdocktile-devel >= 1.0.0
BuildRequires:  libqt4-devel
BuildRequires:  phonon-devel
BuildRequires:  libotr2-devel >= 3.2.0

%description
Multiprotocol instant messenger.

%package devel
Summary:        Development files for QutIM
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libjreen-devel >= 1.1.0
Requires:       libvreen-devel >= 0.9.1
Requires:       libdocktile-devel >= 1.0.0
Requires:       qca2-devel
Requires:       libqt4-devel

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
BuildRequires:  libaspell-devel
Requires:       %{name} = %{version}
%if 0%{?suse_version}
Supplements:  packageand(qutim:aspell)
%endif

%description plugin-aspeller
Spell checker plugin for QutIM based on aspell

%package plugin-hunspeller
Summary:        Hunspeller plugin for QutIM
Requires:       %{name} = %{version}

BuildRequires:  hunspell
BuildRequires:  libhunspell-devel
%if 0%{?suse_version}
Supplements:  packageand(qutim:hunspell)
%endif

%description plugin-hunspeller
Spell checker plugin for QutIM based on hunspell

%package plugin-kdeintegration
Summary:        KDE integration plugin for QutIM
Requires:       %{name} = %{version}
%if 0%{?suse_version}
BuildRequires:  kdelibs-devel
Supplements:    packageand(qutim:libkde4)
%kde4_runtime_requires
%endif

%if 0%{?mandriva_version}
BuildRequires: kdelibs-devel
%endif

%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires: kdelibs-devel
%endif

%description plugin-kdeintegration
Plugin that provides integration with KDE

%package plugin-sdlsound
Summary:        SDL sound plugin for QutIM
Requires:       %{name} = %{version}
%if 0%{?suse_version}
BuildRequires:  libSDL_mixer-devel
Supplements:    packageand(qutim:libSDL_mixer-1_2-0)
%endif

%if 0%{?fedora_version}
BuildRequires: SDL_mixer-devel
%endif

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

#patch0
#patch1

%build
mkdir build
pushd build
export CXXFLAGS="-O0"
export QMAKE_CXXFLAGS="-O0"
cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DSYSTEM_JREEN=1 \
    -DSYSTEM_VREEN=1 \
    -DLIB_SUFFIX="$LIBSUFFIX" \
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
    -DNOTIFICATIONSSETTINGS=0 \
    -DMOBILESETTINGSDIALOG=0 \
    -DQRCICONS=0 \
    -DQUTIM_SHARE_DIR=%{_sharedir} \
    -DSYSTEM_QTDOCKTILE=1 \
    -DQUTIM_GENERATE_DOCS=0 \
    ..
make
popd #build

%install
pushd build
%make_install
%if 0%{?suse_version}
  %suse_update_desktop_file qutim
%endif
popd #build

# Link duplicate files
%if 0%{?suse_version}
  %fdupes %{buildroot}/%{_datadir}/apps
%endif

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
#{_libdir}/libqtdocktile.so.*
%{_libdir}/libqutim-adiumchat.so.*
%{_libdir}/libqutim-adiumwebview.so.*
%{_libdir}/libqutim-simplecontactlist.so.*

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
%{_libdir}/qutim/plugins/libphononsound.so
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
%{_libdir}/libqutim.so
#{_libdir}/libqtdocktile.so
%{_libdir}/libqutim-adiumchat.so
%{_libdir}/libqutim-adiumwebview.so
%{_libdir}/libqutim-simplecontactlist.so
%{_datadir}/cmake/Modules

%files icons
%defattr(-,root,root)
%if 0%{?suse_version}
   %{_datadir}/kde4/apps/qutim
%else
   %{_datadir}/apps/qutim
%endif
%{_datadir}/icons/*
#%%{_datadir}/apps/*

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

%files plugin-sdlsound
%defattr(-,root,root)
%{_libdir}/qutim/plugins/libsdlsound.so

%files plugin-plugman
%defattr(-,root,root)
%{_libdir}/qutim/plugins/libplugman.so

%changelog
