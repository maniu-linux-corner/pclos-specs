Name:           purple-facebook
Version:        92885e0456ed
Release:        1%{?dist}
Summary:        Facebook's messenger chat support for libpurple

License:        GPL
URL:            https://github.com/jgeboski/purple-facebook/wiki
Source0:        purple-facebook-%{version}.tar.gz

%description
Facebook's messenger chat support for libpurple


%prep
%setup -q -n purple-facebook-%{version}


%build
sh autogen.sh --prefix=/usr
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm $RPM_BUILD_ROOT/usr/lib64/purple-2/libfacebook.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%{_libdir}/purple-2/libfacebook.so



%changelog
