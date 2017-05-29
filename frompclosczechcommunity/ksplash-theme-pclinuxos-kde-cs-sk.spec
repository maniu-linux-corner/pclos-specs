Name:           ksplash-theme-pclinuxos-kde-cs-sk
Version:        1.0.0
Release:        2%{?dist}
Summary:      Téma pro KSplash  

License:        GPLv3
URL:            https://github.com/pclinuxoscz/specs
Source0:        ksplash-theme-pclinuxos-kde-cs-sk.tar.xz
BuildArch: noarch
Requires:  kde-baseapps     

%description
Téma pro CZ/SK vydání LiveDVD KDE a KDE Plus 

%prep
%setup -q -n ksplash-theme-pclinuxos-kde-cs-sk


%build

%install
mkdir -p $RPM_BUILD_ROOT
cp -R ./ $RPM_BUILD_ROOT/

#%post
#SYSUSERS=`cat /etc/passwd | grep "/home/.*/bash" |grep "[0-9][0-9][0-9]" |cut -d: -f1`
#for idx in $SYSUSERS; do cp /tmp/ksplashrc /home/$idx/.kde4/share/config/;chown $idx:$idx /home/$idx/.kde4/share/config/;chmod 777 /home/$idx/.kde4/share/config/;  done
#rm /tmp/ksplashrc;

%files
%{_datadir}/apps/ksplash/*

%changelog
