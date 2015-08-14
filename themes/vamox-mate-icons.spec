Name:           vamox-mate-icons
Version:        1
Release:        1%{?dist}
Summary:        Icon Pack for Xfce/Mate 

License:        CC-AA-BY-SA
URL:            http://gnome-look.org/content/show.php/Vamox+MATE+%28green%29?content=166332
Source0:        vamox-mate-icons-1-1.tar.gz
BuildArch:	noarch

%description
 Icon Pack for Xfce/Mate 

%prep
%setup -q -n vamox-mate


%build


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/vamox-mate-icons/
cp -R ./ $RPM_BUILD_ROOT%{_datadir}/icons/vamox-mate-icons/
rm $RPM_BUILD_ROOT%{_datadir}/icons/vamox-mate-icons/.icon-theme.cache

%files
%{_datadir}/icons/vamox-mate-icons/*

%changelog
