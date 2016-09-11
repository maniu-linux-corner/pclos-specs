Name:           protobuf-c
Version:        1.2.1
Release:        1%{?dist}
Summary:        protobuf-c

License:        GPL
URL:            https://github.com/protobuf-c/protobuf-c
Source0:        protobuf-c-%{version}.tar.gz

%description
...

%prep
%setup -q


%build
sh autogen.sh --prefix=/usr
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
/usr/bin/protoc-c
   /usr/include/google/protobuf-c/protobuf-c.h
   /usr/include/protobuf-c/protobuf-c.h
   /usr/lib64/libprotobuf-c.a
   /usr/lib64/libprotobuf-c.la
   /usr/lib64/libprotobuf-c.so
   /usr/lib64/libprotobuf-c.so.1
   /usr/lib64/libprotobuf-c.so.1.0.0
   /usr/lib64/pkgconfig/libprotobuf-c.pc




%changelog
