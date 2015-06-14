Name:           libmpris2client
Version:        0.1.0
Release:        2%{?dist}
Summary:        A glib library for controlling any mpris2 compatible player.

License:        GPLv2
URL:            https://github.com/matiasdelellis/libmpris2client
Source0:        libmpris2client-%{version}.tar.bz2
BuildRequires: %{_lib}glib2.0-devel
Requires: %{_lib}glib2.0_0

%description
A glib library for controlling any mpris2 compatible player.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc
%{_libdir}/*.so.*
%{_bindir}/mpris2-status-icon
%{_datadir}/icons/hicolor/128x128/apps/mpris2-status-icon.png

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmpris2client.pc


%changelog
* Sat Jun 13 2015 Mank <mank@pclinuxos.cz> 0.1.0
- Init spec file
