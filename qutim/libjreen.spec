#
# spec file for package libjreen
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

Name:           libjreen
Version:        1.1.1+git.1357487371
Release:        22.2
License:        GPL-2.0+
Summary:        Qt Jabber/XMPP library
Url:            http://github.com/euroelessar/jreen
Group:          System/Libraries
Source:         jreen-%{version}.tar
Requires:       libqca2-plugin-cyrus-sasl
BuildRequires:  cmake
BuildRequires:  libqca2-devel
BuildRequires:  libqt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# optional dependencies
BuildRequires:  libidn-devel

%description
Qt Jabber/XMPP extensible library.

%package -n libjreen%{soname}
Summary:        Qt Jabber/XMPP library
Group:          System/Libraries

%description -n libjreen%{soname}
Qt Jabber/XMPP extensible library.

%package -n libjreen-devel
Summary:        Qt Jabber/XMPP library
Group:          Development/Libraries/C and C++
Requires:       libjreen%{soname} = %{version}
Requires:       libqca2-devel
Requires:       libqt4-devel
Provides:       jreen-devel = %{version}

%description -n libjreen-devel
Qt Jabber/XMPP extensible library.

%prep
%setup -q -n jreen-%{version}

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
    ..
make %{?_smp_mflags}
popd #build

%install
pushd build
%make_install
popd #build

%post   -n libjreen%{soname} -p /sbin/ldconfig

%postun -n libjreen%{soname} -p /sbin/ldconfig

%files -n libjreen%{soname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libjreen.so.%{soname}
%{_libdir}/libjreen.so.%{soname}.*

%files -n libjreen-devel
%defattr(-,root,root)
%{_includedir}/jreen
%{_libdir}/libjreen.so
%{_libdir}/pkgconfig/libjreen.pc

%changelog
