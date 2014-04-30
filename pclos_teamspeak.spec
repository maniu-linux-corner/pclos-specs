Name: teamspeak3
Summary: TeamSpeak is software for quality voice communication via the Internet
Version: 3.0.9.2
Release: 2
License: custom
URL: http://www.teamspeak.com/
Group: Applications/Internet
Source0: TeamSpeak3-Client-linux_x86-3.0.9.2.run.tar.xz
Source1: teamspeak3.desktop
Source2: icon.xpm
Source3: teamspeak3.launcher
Source4: lagos_cs.qm
Source5: lagos_sk.qm
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
TeamSpeak is software for quality voice communication via the Internet
Lokalizace Licence:
Přeložil: Herní Hosting, s.r.o. - http://www.hernihosting.cz
Česko-slovenská podpora: http://forum.hernihosting.cz

%prep
%setup -c teamspeak3

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%install

  # Create Destination Directories
  install -d $RPM_BUILD_ROOT/{usr/bin/,opt/}

  # Make Installer Executable
  chmod +x TeamSpeak3-Client-linux_x86-3.0.9.2.run

  # Run Installer
  ./TeamSpeak3-Client-linux_x86-3.0.9.2.run --noexec --target teamspeak3

  # Move Program Data to Package Directory
  mv teamspeak3/ $RPM_BUILD_ROOT/opt/

  # Remove Bundled Qt Libraries and Symlink system libraries to TS3 Directory
#  rm /opt/teamspeak3/libQt*
#  ln -s /usr/lib/libQtCore.so.4    $RPM_BUILD_ROOT/opt/teamspeak3/libQtCore.so.4
#  ln -s /usr/lib/libQtGui.so.4     $RPM_BUILD_ROOT/opt/teamspeak3/libQtGui.so.4
#  ln -s /usr/lib/libQtNetwork.so.4 $RPM_BUILD_ROOT/opt/teamspeak3/libQtNetwork.so.4

  # Install Desktop File
  install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/applications/teamspeak3.desktop

  # Install Icon File
  install -D -m644 %{SOURCE2} $RPM_BUILD_ROOT/usr/share/pixmaps/teamspeak3.xpm

  # Install Client Launcher
  install -D -m755 %{SOURCE3} $RPM_BUILD_ROOT/usr/bin/teamspeak3
  install -D -m755 %{SOURCE4} $RPM_BUILD_ROOT/opt/teamspeak3/translations/lagos_cs.qm
  install -D -m755 %{SOURCE5} $RPM_BUILD_ROOT/opt/teamspeak3/translations/lagos_sk.qm	 	

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/opt/teamspeak3/*
/usr/share/pixmaps/*
/usr/share/applications/*
/usr/bin/teamspeak3


%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 3.0.9.2-1
---

