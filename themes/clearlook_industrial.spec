Summary:	Clearlook-industrial
Name:		gtk-theme-clearlook-industrial
Version:	1.0.0
Release:	2
Source0:	34253-Clearlooks-Industrial.tar.bz2
License:	GPLv2
Group:		Graphical desktop/Xfce
URL:		http://gnome-look.org/content/show.php?content=34253
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
A gtk theme ClearLook Industrial

%prep
%setup -q -c Clearlook_industrial
%build

%install
%__install -d %{buildroot}%{_datadir}/themes/
%__cp -rf ./* %{buildroot}%{_datadir}/themes/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/themes/*


%changelog
* Fri Apr 28 2014 Mank <mank dot pclos at gmail dot com> 1.0.0-2
- Init spec

