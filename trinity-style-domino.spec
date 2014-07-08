Name:           trinity-style-domino
Version:        0.4
Release:        1%{?dist}
Summary:        Styl pro Trinity

License: CC-BY-AA       
URL:     http://kde-look.org/usermanager/search.php?username=psychydyl&PHPSESSID=9703870edf9fb13f9498c4cc60ad3c1f       
Source0:    trinity-style-domino-%{version}.tar.xz    

Requires: trinity-twin      

%description
Styl a dekorace pro prostředí Trinity. Umožní vám použít desítky přednastavených stylů pro vaše prostředí
Pro Trinity upravil psychydyl

%prep
%setup -q


%build
mkdir -p $RPM_BUILD_ROOT/opt/
cp -r opt/* $RPM_BUILD_ROOT/opt/

%install

%files
/opt/trinity/*

%changelog

* Fri Jun 8 2014 Mank <mank at pclinuxos.cz> 0.4-1mank2014
- 0.4

