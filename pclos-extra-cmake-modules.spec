Name:           extra-cmake-modules
Version: 	5.20.0
Release: %mkrel 2
Summary:        Extra modules and scripts for CMake
Group:          Development/Libraries
License:        MIT
URL:            http://www.kde.org/
Source0:        %name-%version.tar.xz
BuildRequires:  cmake
BuildRequires:  python-sphinx
BuildRequires:  python-sphinx_rtd_theme
BuildRequires:  qt5help-devel

%description
Extra modules and scripts for CMake.

%prep
%setup -q
%apply_patches

%build
%cmake
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%files
%_datadir/ECM
%doc %_docdir/ECM
%_mandir/man?/*.*


%changelog
* Sun Feb 28 2016 daniel <meisssw01 at gmail.com> 5.16.0-2pclos2016
- rebuild for 32 bit

* Tue Nov 10 2015 bb <bb> 5.16.0-1pclos2015
- update for lxqt

* Thu Apr 02 2015 bb <bb> 1.8.0-2pclos2015
- rebuild for cmake 3.0.2

* Fri Mar 13 2015 bb <bb> 1.8.0-1pclos2015
- update

* Sat Mar 07 2015 bb <bb> 1.5.0-1pclos2015
- import from france
