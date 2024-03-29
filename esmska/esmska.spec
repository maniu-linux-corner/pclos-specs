Name: esmska
Summary: A program to send sms via Internet Gateways
Version: 1.8
Release: 1
License: AGPL
URL: http://code.google.com/p/esmska/wiki/Download?tm=2
Group: Applications/Java
Source0: esmska-%{version}.tar.gz
Source1: esmska.desktop
Requires: java-1.7.0-sun
BuildArch:	noarch
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A program to send sms via Gateways

%prep
%setup

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%install

%__install -d "$RPM_BUILD_ROOT/usr/share/java/esmska"
%__cp -a * "$RPM_BUILD_ROOT/usr/share/java/esmska"

	#.desktop + icon files
%__install -D -m644 "%{SOURCE1}" \
		"$RPM_BUILD_ROOT/usr/share/applications/esmska.desktop"
	%__install -D -m644 "%{_builddir}/esmska-%{version}/icons/esmska.png" \
		"$RPM_BUILD_ROOT/usr/share/pixmaps/esmska.png"

	#executable file
	%__install -d -m755 "$RPM_BUILD_ROOT/usr/bin"
	ln -s "/usr/share/java/esmska/esmska.sh" \
		"$RPM_BUILD_ROOT/usr/bin/$_name"

	#license
	%__install -D -m644 %{_builddir}/%{name}-%{version}/license/license.txt \
		$RPM_BUILD_ROOT/usr/share/licenses/$_name/LICENSE
	%__install -D -m644 %{_builddir}/%{name}-%{version}/license/gnu-agpl.txt \
		$RPM_BUILD_ROOT/usr/share/licenses/$_name/AGPL

	#removing unneeded
	%__rm $RPM_BUILD_ROOT/usr/share/java/esmska/esmska.exe

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/esmska.sh
%{_datadir}/applications/esmska.desktop
%{_datadir}/java/esmska/*
%{_datadir}/licenses/AGPL
%{_datadir}/licenses/LICENSE
%{_datadir}/pixmaps/esmska.png

%changelog
* Sat Jul 29 2013 MManiu <me+pclosgit@maniu.eu> 1.4-1
- esmska: Version: 1.4
