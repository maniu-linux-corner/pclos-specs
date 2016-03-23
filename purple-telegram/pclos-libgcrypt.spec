# 32/64bit spec
#
%define major 20
%define libname %mklibname gcrypt %{major}
%define develname %mklibname gcrypt -d



Summary:	GNU Cryptographic library
Name:		libgcrypt
Version:	1.6.4
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnupg.org/
Source0:	ftp://ftp.gnupg.org/gcrypt/libgcrypt/%{name}-%{version}.tar.gz
#Patch1:		libgcrypt-1.2.0-libdir.patch
#Patch2:		libgcrypt-1.5.4-CVE-2014-3591.patch
#Patch3:		libgcrypt-1.5.4-CVE-2015-0837.patch
BuildRequires:	libgpg-error-devel >= 0.5
BuildRequires:  libgpgme-devel
BuildRequires:	%{_lib}pth-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Obsoletes: 	%{name} < %version

%description
Libgcrypt is a general purpose cryptographic library
based on the code from GNU Privacy Guard.  It provides functions for all
cryptograhic building blocks: symmetric ciphers
(AES,DES,Blowfish,CAST5,Twofish,Arcfour), hash algorithms (MD5,
RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all hash algorithms),
public key algorithms (RSA, ElGamal, DSA), large integer functions,
random numbers and a lot of supporting functions.

%package -n %{libname}
Summary:	GNU Cryptographic library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Libgcrypt is a general purpose cryptographic library
based on the code from GNU Privacy Guard.  It provides functions for all
cryptograhic building blocks: symmetric ciphers
(AES,DES,Blowfish,CAST5,Twofish,Arcfour), hash algorithms (MD5,
RIPE-MD160, SHA-1, TIGER-192), MACs (HMAC for all hash algorithms),
public key algorithms (RSA, ElGamal, DSA), large integer functions,
random numbers and a lot of supporting functions.

%package -n %{develname}
Summary:	Development files for GNU cryptographic library
Group:		Development/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d gcrypt 11

%description -n %{develname}
Libgcrypt is a general purpose cryptographic library
based on the code from GNU Privacy Guard.
This package contains files needed to develop
applications using libgcrypt. ( For example Ägypten project )

%prep
%setup -q
#%patch1 -p1 -b .libdir
#%patch2 -p1 -b .CVE-2014-3591
#%patch3 -p1 -b .CVE-2015-0837

%build
autoreconf -fi
%configure2_5x --enable-dev-random \
	--disable-random-daemon \
	--enable-random=linux \
	--disable-static \
	--enable-m-guard

%make

%install
rm -rf %{buildroot}
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%clean
rm -rf %{buildroot}

%post -n %{libname}
/sbin/ldconfig

%postun -n %{libname}
/sbin/ldconfig

%post -n %{develname}
%_install_info %{name}.info

%postun -n %{develname}
%_remove_install_info %{name}.info

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS README NEWS THANKS TODO
%{_bindir}/*
%{_libdir}/lib*.so.%{major}
%{_libdir}/lib*.so.%{major}.*
%{_mandir}/man1/hmac256.1.bz2

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog README.*
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_datadir}/aclocal/*
%{_infodir}/gcrypt.info*


%changelog
* Fri Apr 03 2015 bb <bb> 1.5.4-1pclos2015
- 1.5.4 plus security update

* Tue Aug 20 2013 ghostbunny <hmhaase at pclinuxosusers dot de> 1.5.3-1pclos2013
- 1.5.3

* Fri Jun 07 2013 ghostbunny <hmhaase at pclinuxosusers dot de> 1.5.2-1pclos2013
- 1.5.2
- removed signature source, it does not fit the recompressed source

