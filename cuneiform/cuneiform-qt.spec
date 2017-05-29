%define version		0.1.2
%define release		%mkrel 1

Name:		cuneiform-qt
Summary:	A graphical interface for Cuneiform OCR
Version:	%{version}
Release:	%{release}
License:	GPLv2
URL:		http://sourceforge.net/projects/cuneiform-qt/
Group:		Text tools
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	desktop-file-utils
BuildRequires:	qt4-devel

Requires:	cuneiform-linux

%description
cuneiform-qt is GUI frontend for Cuneiform (OCR system originally developed and
open sourced by Cognitive technologies). It allow to open scanned image, view
this one in preview pane, recornize text via Cuneiform and save result in HTML
file.

%prep
%setup -q
# Fix hardcoded installation-path:
sed -i 's!/usr/local!%{_prefix}!' %{name}.pro

%build
# "PREFIX=...." has no effect- but it should have:
%qmake_qt4 -o Makefile "PREFIX=%{_prefix}" %{name}.pro
%make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}

# Remove extension of icon name in *.desktop-file:
sed -i 's!%{name}.png!%{name}!' %{buildroot}%{_datadir}/applications/%{name}.desktop
# Fix wrong localestring in *.desktop-file:
sed -i 's!uл!uk!' %{buildroot}%{_datadir}/applications/%{name}.desktop

# *.desktop-file modification (XDG-Menu):
desktop-file-install --vendor="" \
  --remove-category="Office" \
  --add-category="Qt" \
  --add-category="Graphics" \
  --add-category="Scanning" \
  --add-category="OCR" \
  --dir %{buildroot}%{_datadir}/applications/ %{buildroot}%{_datadir}/applications/*.desktop

%clean
rm -rf %{buildroot}


%files
%doc AUTHORS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/apps/%{name}/*.qm
%{_datadir}/pixmaps/*.png

%changelog
* Thu Apr 29 2014 Mank <Mank dot pclos at gmail dot com> 0.1.2-1pclos2012
- Build for PCLinuxOS

* Fri Jul 16 2010 Doktor5000 <rpm@mandrivauser.de> 0.1.2-1mud2010.1
- rebuild for Mandrivalinux 2010.1

* Sat Apr 03 2010 Doktor5000 <rpm@mandrivauser.de> 0.1.2-1mud2010.0
- rebuild for Mandrivalinux 2010.0

* Sat Feb 20 2010 MaxiPunkt <email@domain.de> 0.1.2-1max
- First built for Mandriva
