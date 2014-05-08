Summary:	Axe theme
Name:		xfwm4-axe-theme
Version:	1.0.0
Release:	2
Source0:	73291-axe.tar.gz
License:	GPLv2
Group:		Graphical desktop/Xfce
URL:		http://xfce-look.org/content/show.php/axe?content=73291
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
A xfwm4 theme axe

%prep
%setup -q -c axe_theme
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
* Fri Apr 29 2014 Mank <mank@pclinuxos.cz> 1.0.0-2
- Init spec
* Fri Jul 28 2013 Mank <mank@pclinuxos.cz> 1.0.0-1
- Init spec

