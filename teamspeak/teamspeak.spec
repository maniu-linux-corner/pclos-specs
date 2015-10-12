Name: teamspeak3
Summary: TeamSpeak is software for quality voice communication via the Internet
Version: 3.0.18.1
Release: 1
License: custom
URL: http://www.teamspeak.com/
Group: Applications/Internet
Source0: TeamSpeak3-Client-linux_amd64-%{version}.run.tar.xz
Source1: teamspeak3.desktop
Source2: icon.xpm
Source3: teamspeak3.launcher
Source4: lagos_cs.qm
Source5: lagos_sk.qm
Requires: task-qt4
Requires: quazip
AutoReqProv: no
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
TeamSpeak is software for quality voice communication via the Internet
Lokalizace Licence:
Přeložil: Herní Hosting, s.r.o. - http://www.hernihosting.cz
Česko-slovenská podpora: http://forum.hernihosting.cz

%prep
%setup -c teamspeak3

%build

%install

  # Create Destination Directories
  install -d $RPM_BUILD_ROOT/{usr/bin/,opt/}

  # Make Installer Executable
  chmod +x TeamSpeak3-Client-linux_amd64-%{version}.run

  # Run Installer
  ./TeamSpeak3-Client-linux_amd64-%{version}.run --noexec --target teamspeak3

  # Move Program Data to Package Directory
  mv teamspeak3/ $RPM_BUILD_ROOT/opt/

  # Install Desktop File
  install -D -m644 %{SOURCE1} $RPM_BUILD_ROOT/usr/share/applications/teamspeak3.desktop

  # Install Icon File
  install -D -m644 %{SOURCE2} $RPM_BUILD_ROOT/usr/share/pixmaps/teamspeak3.xpm

  # Install Client Launcher
  install -D -m755 %{SOURCE3} $RPM_BUILD_ROOT/usr/bin/teamspeak3
  install -D -m755 %{SOURCE4} $RPM_BUILD_ROOT/opt/teamspeak3/translations/lagos_cs.qm
  install -D -m755 %{SOURCE5} $RPM_BUILD_ROOT/opt/teamspeak3/translations/lagos_sk.qm	

#1st is arch based 
# fix perm
  %__chmod +x	$RPM_BUILD_ROOT/opt/teamspeak3/ts3client_linux_amd64
  %__chmod 777	$RPM_BUILD_ROOT/opt/teamspeak3/ts3client_runscript.sh
  %__chmod +x	$RPM_BUILD_ROOT/opt/teamspeak3/ts3client_runscript.sh
  %__chmod -R 777 $RPM_BUILD_ROOT/opt/teamspeak3/ 	
 	

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/opt/teamspeak3/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_bindir}/teamspeak3


%changelog
* Sat Mar 25 2011 Mank <mank@pclinuxos.cz> 3.0.18.1-1
- Update

