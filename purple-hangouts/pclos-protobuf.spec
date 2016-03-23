# 32/64bit spec-file
#
%define name protobuf
%define version 2.6.1
%define rel %mkrel 4
%define major 9

%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d

Summary:	Protocol Buffers - Google's data interchange format
Summary(de):	Protocol Buffers - Googles Datenaustauschformat
Name:		%{name}
Version:	%{version}
Release:	%{rel}
License:	new BSD
Group:		Networking/Other
URL:		https://code.google.com/p/protobuf/
Source0:	https://protobuf.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	glibc >= 2.16
Requires:	libstdc++6 >= 4.7.2
Obsoletes:	protobuf < %version
Obsoletes:	protobuf-compiler < %version
Obsoletes:	protobuf-devel < %version
Obsoletes:	protobuf-lite < %version
Obsoletes:	protobuf-lite-devel < %version
Obsoletes:	protobuf-lite-static < %version
Obsoletes:	protobuf-python < %version
Obsoletes:	protobuf-static < %version
Obsoletes:	protobuf-vim < %version

%description
Protocol Buffers are a way of encoding structured data in an efficient 
yet extensible format. Google uses Protocol Buffers for almost all of 
its internal RPC protocols and file formats. 

%description -l de
Protocol Buffers sind ein Weg zum Kodieren von strukturierten Daten, in 
einem effizienten jedoch erweiterbaren Format. Google nutzt Protocol 
Buffers für fast alle seine internen RPC Protokolle und Dateiformate.

%package -n %{libname}
Summary:	Protocol Buffers - Google's data interchange format
Summary(de):	Protocol Buffers - Googles Datenaustauschformat
Group:		Networking/Other
License:	new BSD
Provides:	lib%{name} = %{version}
Obsoletes:	protobuf < %version
Obsoletes:	protobuf-compiler < %version
Provides:	protobuf = %version-%release
Provides:	protobuf-compiler = %version-%release

%description -n %{libname}
Protocol Buffers are a way of encoding structured data in an efficient 
yet extensible format. Google uses Protocol Buffers for almost all of 
its internal RPC protocols and file formats.

%description -n %{libname} -l de
Protocol Buffers sind ein Weg zum Kodieren von strukturierten Daten, in 
einem effizienten jedoch erweiterbaren Format. Google nutzt Protocol 
Buffers für fast alle seine internen RPC Protokolle und Dateiformate.

%package -n %{libnamedev}
Summary:	Protocol Buffers - Google's data interchange format
Summary(de):	Protocol Buffers - Googles Datenaustauschformat
Group:		Networking/Other
License:	new BSD
Requires:	lib%{name} = %{version}
Obsoletes:	protobuf-devel < %version
Provides:	protobuf-devel = %version-%release

%description -n %{libnamedev}
Protocol Buffers are a way of encoding structured data in an efficient 
yet extensible format. Google uses Protocol Buffers for almost all of 
its internal RPC protocols and file formats.

This package contains the development headers and libraries for
protobuf.

%description -n %{libnamedev} -l de
Protocol Buffers sind ein Weg zum Kodieren von strukturierten Daten, in 
einem effizienten jedoch erweiterbaren Format. Google nutzt Protocol 
Buffers für fast alle seine internen RPC Protokolle und Dateiformate.

Dieses Paket enthält die Header-Dateien und Bibliotheken für protobuf.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall_std

find %{buildroot} -name '*.la' -delete

%post -n %{libname}
ldconfig

%postun -n %{libname}
ldconfig

%files -n %{libname}
%defattr(-,root,root)
%doc CHANGES.txt CONTRIBUTORS.txt
%{_bindir}/protoc
%{_libdir}/lib%{name}.so.%{major}*
%{_libdir}/lib%{name}-lite.so.%{major}*
%{_libdir}/libprotoc.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/google/protobuf
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-lite.so
%{_libdir}/libprotoc.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-lite.pc

%changelog
* Sun May 12 2013 Texstar <texstar at gmail.com> 2.5.0-4pclos2013
- add more obsoletes

* Sun May 12 2013 Texstar <texstar at gmail.com> 2.5.0-3pclos2013
- obsolete old version of protobuf

* Sun May 12 2013 Texstar <texstar at gmail.com> 2.5.0-2pclos2013
- rebuild against glibc 2.16

* Sun Mar 17 2013 ghostbunny <hmhaase at pclinuxosusers dot de> 2.5.0-1pclos2013
- initial import for pclos
