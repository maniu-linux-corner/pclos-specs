Name: dr14tmeter
Version: 0.8.5
Release: 1
Summary: Compute the dynamic range DR14 value of the givens audio files
BuildArch: noarch

Group: Applications/Sound
License: GPLv3
URL: http://simon-r.github.com/dr14_t.meter
Source: https://github.com/downloads/simon-r/dr14_t.meter/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python
BuildRequires: bash
Requires: python
Requires: python-numpy
Requires: python-scipy
Requires: flac
Requires: lame
Requires: faad2
Requires: ffmpeg
Requires: vorbis-tools

%description
Compute the DR14 value of the given audio files according to the algorithm decribed by the Pleasurize Music Foundation

%prep
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
zcat $RPM_SOURCE_DIR/%{name}-%{version}.tar.gz | tar -xvf -

%build
cd $RPM_BUILD_DIR/%{name}-%{version}
python setup.py build

%install
cd $RPM_BUILD_DIR/%{name}-%{version}
python setup.py install --root=%{buildroot} --prefix=usr --optimize=1

%clean

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_mandir}/man7/*


%changelog
* Sat Jun 23 2012 Mank <mank@pclinuxos.cz> 0.8.5-1
- dr1tmeter 0.8.5: Init Packages for pclinuxos
