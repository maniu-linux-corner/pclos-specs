Name: xfce-composite-editor
Summary: A Composite editor for The Xfce 4
Version: 2.6.6
Release: 4
License: GPLv2
URL: http://keithhedger.hostingsiteforfree.com/pages/apps.html
BuildArch: noarch
Group: Graphical desktop/Xfce
Source0: Xfce4-Composite-Editor.tar.gz
Requires: gtkdialog

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A Composite editor for The Xfce 4

%prep
%setup -q -c Xfce4-Composite-Editor

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
install -m 777 xfce4-composite-editor $RPM_BUILD_ROOT/usr/bin/xfce4-composite-editor
install -m 744 xfcecomped.desktop $RPM_BUILD_ROOT/usr/share/applications/xfcecomped.desktop

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/xfce4-composite-editor
%{_datadir}/applications/xfcecomped.desktop

%changelog
* Sat Jun 13 2015 Mank <mank@pclinuxos.cz> 2.6.6-4
-  update spec
* Sat Mar 25 2013 Mank <mank@pclinuxos.cz> 2.6.6-3
-  init spec
