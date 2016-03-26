Name:           libdiorite
Version:        0.2.1
Release:        1%{?dist}
Summary:        Diorite is a a grey to dark-grey intermediate intrusive igneous rock. Diorite library is a utility and widget library for Nuvola Player project based on GLib, GIO and GTK.

License:        GPL
URL:            http://nuvolaplayer.fenryxo.cz/home.html
Source0:        diorite-0.2.1.tar.gz

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n diorite-%{version}


%build
./waf configure --prefix=/usr --destdir=%{_prefix} --with-experimental-api --libdir %{_libdir} --platform=LINUX
./waf build


%install
./waf install --destdir=%{buildroot}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc
%{_bindir}/diorite-testgen-0.2
%{_libdir}/libdioritedb-0.2.so
%{_libdir}/libdioriteglib-0.2.so
%{_libdir}/libdioritegtk-0.2.so
%{_datadir}/vala/vapi/*

%files devel
%{_libdir}/pkgconfig
%{_includedir}/diorite-1.0
%changelog
