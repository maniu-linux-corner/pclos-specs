%define name	Xfce-Theme-Manager
%define version	0.1.18
%define release	%mkrel 1
%define	Summary	A Xfce Theme Manager

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://keithhedger.hostingsiteforfree.com/pages/apps.html#themeed
Source0:	xfce-theme-manager-0.1.18.tar.gz
License:	GPLv2
Group:		Desktop Enviroment/Xfce
BuildRequires:	glib2-devel >= 2.4
BuildRequires:	gtk+2-devel >= 2.6
BuildRequires:  libxcursor-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
..

%prep
%setup -n %{name}-%{version}

%install
  install -d $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/share/applications $RPM_BUILD_ROOT/usr/share/doc/xfce-theme-manager
  cd %{_builddir}/Xfce-Theme-Manager-%{version}
  sed 's/Name=Xfce-Theme-Manager/Name=Xfce Theme Manager/g;s/^Comment.*/Comment=Control Xfce4 Themes, Icons, Cursors, Wallpapers and more/g' Xfce-Theme-Manager.desktop > xfce-theme-manager.desktop
  mv Makefile Makefile.old
  sed 's/Xfce-Theme-Manager.desktop/xfce-theme-manager.desktop/g' Makefile.old > Makefile
  make CXXFLAGS="$CXXFLAGS -O3 -Wall `pkg-config --cflags --libs glib-2.0` `pkg-config --cflags --libs gdk-2.0` `pkg-config --cflags --libs gtk+-2.0` `pkg-config --cflags --libs xcursor` `pkg-config --cflags --libs gthread-2.0`" PREFIX="$RPM_BUILD_ROOT/usr" install
  install -m 644 README* $RPM_BUILD_ROOT/usr/share/doc/xfce-theme-manager/
  install -m 644 ChangeLog* $RPM_BUILD_ROOT/usr/share/doc/xfce-theme-manager/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/applications/xfce-theme-manager.desktop
%{_bindir}/xfce-theme-manager
%{_datadir}/pixmaps/xfce-theme-manager.png
%{_datadir}/doc/xfce-theme-manager/*

%changelog
* Wed Sep 27 2012 Mank <mank@pclinuxos.cz> %{version}-%{release}
-	Build for PCLinuxOS

