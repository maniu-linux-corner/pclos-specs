Name:           breeze-icons
Version:        1.0.0
Release:        1%{?dist}
Summary:        breeze-icons

License:        GPL
URL:            kde.org
Source0:        breeze-icons-1.0.0.tar.xz
BuildArch:		noarch
BuildRequires:  cmake extra-cmake-modules
 

%description
breeze

%prep
%setup -q


%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}


%install
%make_install


%files
%{_iconsdir}/*



%changelog
