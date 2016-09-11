#
# spec file for package imagewriter
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define breq libqt4-devel
%define backend udisks2
%define qmake /usr/lib64/qt4/bin/qmake
%define lrelease /usr/lib/qt4/bin/lrelease
%define definedbackend USEUDISKS2


Name:           imagewriter
Version:        1.10.1396965491.1d253d9
Release:        2
Summary:        Utility for writing disk images to USB keys
License:        GPL-2.0
Group:          Hardware/Other
Url:            https://github.com/openSUSE/imagewriter
Source0:        imagewriter-%{version}.zip
Source1:		org.pclinuxos.imagewriter.policy
Source10:		%{name}
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  %{breq} %{backend}
BuildRequires:  xz
Requires:       xdg-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A graphical utility for writing raw disk images & hybrid ISOs to USB keys.

%prep
%setup -q -n imagewriter-master

%build
# -DKIOSKHACK
# Create qmake cache file for building and use optflags.
cat > .qmake.cache <<EOF
PREFIX=%{_prefix}
QMAKE_CXXFLAGS_RELEASE += "%{optflags}"
DEFINES=%{definedbackend}
EOF
%{qmake}
make

%install
make INSTALL_ROOT=%{buildroot} install
%if 0%{?suse_version}
    %suse_update_desktop_file imagewriter
%endif
%__mkdir -p %{buildroot}/usr/libexec/
%__mv %{buildroot}/usr/bin/%{name} %{buildroot}/usr/libexec/
%__mkdir -p %{buildroot}/%{_bindir}/
%__mkdir -p %{buildroot}/%{_datadir}/polkit-1/actions/
install -D %{SOURCE10} %{buildroot}/%{_bindir}/
install -Dm644 %{SOURCE1} %{buildroot}/%{_datadir}/polkit-1/actions/org.pclinuxos.imagewriter.policy

%if 0%{?suse_version} >= 1140
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/%{name}
/usr/libexec/%{name}
%{_datadir}/applications/imagewriter.desktop
%{_datadir}/icons/hicolor/*/apps/imagewriter.*
%{_datadir}/polkit-1/actions/org.pclinuxos.imagewriter.policy
%{_mandir}/man1/imagewriter.1.*


%changelog
