#
# spec file for package libvreen
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

%define soname 0

Name:           libvreen
Version:        0.9.1+git.1356900393
Release:        15.2
License:        LGPL-3.0+
Summary:        vk.com API Qt wrapper library
Url:            http://github.com/gorthauer/vreen
Group:          System/Libraries
Source:         vreen-%{version}.tar
#Patch:          obvious-fix.patch
BuildRequires:  cmake
BuildRequires:  libqt4-devel
Obsoletes:      libvkit0 libvkit-debuginfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt wrapper library for VKontakte social network (vk.com) api.

%package -n libvreen%{soname}
Summary:        vk.com API Qt wrapper library
Group:          System/Libraries

%description -n libvreen%{soname}
Qt wrapper library for VKontakte social network (vk.com) api.

%package -n libvreen-devel
Summary:        vk.com API Qt wrapper library
Group:          Development/Libraries/C and C++
Requires:       libvreen%{soname} = %{version}
Requires:       libqt4-devel
Obsoletes:      libvkit-devel
Provides:       vreen-devel = %{version}

%description -n libvreen-devel
Development files for package libvkit.

%prep
%setup -q -n vreen-%{version}

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
    -DVREEN_WITH_QMLAPI=OFF \
    ..
make %{?_smp_mflags}
popd #build

%install
pushd build
%make_install
popd #build

%post   -n libvreen%{soname} -p /sbin/ldconfig

%postun -n libvreen%{soname} -p /sbin/ldconfig

%files -n libvreen%{soname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/libvreen.so.%{soname}
%{_libdir}/libvreen.so.%{soname}.*

%files -n libvreen-devel
%defattr(-,root,root)
%{_includedir}/vreen
%{_libdir}/libvreen.so
%{_libdir}/libvreenoauth.a
%{_libdir}/pkgconfig/vreen.pc
%{_libdir}/pkgconfig/vreenoauth.pc

%changelog
