Summary:	numix holo theme
Name:		gtk-xfwm4-theme-numix-holo
Version:	0.3
Release:	1
Source0:	159304-Numix-Holo-0.3.tar.gz

License:	GPLv3
Group:		Graphical desktop/Xfce
URL:		http://xfce-look.org/content/show.php/Numix+Holo?content=159304
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
A Complete theme for gtk/xfce

%prep
%setup -q -c numix
%build

%install
%__install -d %{buildroot}%{_datadir}/themes/
%__cp -rf ./* %{buildroot}%{_datadir}/themes/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/themes/*
%exclude
%{_datadir}/themes/Numix Holo/.git/


%changelog
* Fri Jul 28 2013 Mank <Mank1@seznam.cz> 1.0.0-1
- Init spec

