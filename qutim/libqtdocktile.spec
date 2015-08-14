#
# spec file for package libqtdocktile
#
# Copyright (c) 2012 Sergei Lopatin <magist3r@gmail.com> 
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define soname 1

Name:           libqtdocktile
Version:        1.0.0+git.1356607878
Release:        17.2
License:        LGPL-3.0+
Summary:        Qt dock integration library
Url:            http://github.com/gorthauer/QtDockTile
Group:          System/Libraries
Source:         libqtdocktile-%{version}.tar
#Patch:          obvious-fix.patch
BuildRequires:  cmake
BuildRequires:  libqt4-devel
BuildRequires:  libdbusmenu-qt-devel >= 0.8.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt dock integration library.

%package -n libqtdocktile%{soname}
Summary:        Qt dock integration library
Group:          System/Libraries

%description -n libqtdocktile%{soname}
Qt dock integration library.

%package -n libqtdocktile-devel
Summary:        Qt dock integration library
Group:          Development/Libraries/C and C++
Requires:       libqtdocktile%{soname} = %{version}
Requires:       libdbusmenu-qt-devel
Requires:       libqt4-devel
Provides:       QtDockTile-devel = %{version}

%description -n libqtdocktile-devel
Development files for package libqtdocktile.

%prep
%setup -q -n libqtdocktile-%{version}

#patch

%build
LIBSUFFIX=$(echo "%{_lib}"|sed 's/^lib//')
mkdir build
pushd build
export CXXFLAGS="%{optflags}"
export QMAKE_CXXFLAGS="%{optflags}"
cmake \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_VERBOSE_MAKEFILE=TRUE \
    -DCMAKE_SKIP_RPATH=TRUE \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
    -DLIB_SUFFIX="$LIBSUFFIX" \
    -DQT_QTDOCKTILE_WITH_QMLAPI=OFF \
    ..
make %{?_smp_mflags}
popd #build

%install
pushd build
%make_install
popd #build

%post   -n libqtdocktile%{soname} -p /sbin/ldconfig

%postun -n libqtdocktile%{soname} -p /sbin/ldconfig

%files -n libqtdocktile%{soname}
%defattr(-,root,root)
%doc README
%{_libdir}/libqtdocktile.so.%{soname}
%{_libdir}/libqtdocktile.so.%{soname}.*
%{_libdir}/qt4/plugins/docktile/

%defattr(-,root,root)
%files -n libqtdocktile-devel
%{_includedir}/QtDockTile
%{_libdir}/libqtdocktile.so
%{_libdir}/pkgconfig/qtdocktile.pc

%changelog
