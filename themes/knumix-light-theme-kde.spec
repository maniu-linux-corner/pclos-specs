Name:           knumix-light-theme-kde
Version:        1.0.0
Release:        1%{?dist}
Summary:        Theme for GTK 2 & 3, Cinnamon, Xfce and Openbox (KDE)

License:        GPL
URL:            http://kde-look.org/content/show.php/KNumix+Light+-+Flat+Theme?content=165849
Source0:        KNumix-1.0.0.tar.xz
BuildArch:		noarch


%description
Theme for GTK 2 & 3, Cinnamon, Xfce and Openbox

%prep
%setup -q -n KNumix-1.0.0


%install
%__install -d %{buildroot}%{_datadir}/themes/
cd GTK_Theme
%__cp -rf ./* %{buildroot}%{_datadir}/themes/
%__install -d %{buildroot}%{_datadir}/icons/
cd ../Cursor
%__cp -rf ./* %{buildroot}%{_datadir}/icons/

%__install -d %{buildroot}%{_datadir}/apps/QtCurve/
cd ../QtCurve-Color/
%__cp -rf ./* %{buildroot}%{_datadir}/apps/QtCurve/

%__install -d %{buildroot}%{_datadir}/apps/aurorae/themes/
cd ../Decorations
%__cp -rf ./* %{buildroot}%{_datadir}/apps/aurorae/themes/


%files
%{_datadir}/apps/aurorae/themes/
%{_datadir}/apps/QtCurve/
%{_datadir}/icons/
%{_datadir}/themes/


%changelog
