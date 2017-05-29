%define name gdm-themes-simply-grace
%define version 0.1
%define release %mkrel 1

Summary:	Theme for Gnome Display Manager (CZ)
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	Simply_Grace.tar.gz
License:	GPL
Group:		Graphical desktop/GNOME
URL:		http://https://github.com/pclinuxoscz/specs/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
Requires:	gdm

%description
This package contains the Simple Grace (with Changes background) for PCLOS Gnome) theme for gdm, the Gnome Display Manager.

%prep
%setup -q -n Simply_Grace

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdm/themes/
tar -xzf %{SOURCE0} -C $RPM_BUILD_ROOT/%{_datadir}/gdm/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/gdm/themes/*


%changelog
* Tue Jun 2 2011 Mank <Mank dot pclos at gmail dot com> 0.1-1pclos2011
- first build
