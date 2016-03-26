Name:           root-actions-kde
Version:        2.9
Release:        1%{?dist}
Summary:        Servisní menu pro KDE4, osahující několik funkcí s právy roota v kontextovém menu, vyvolaným pravým tlačítkem.

License:        GPL
URL:            pc.org
Source0:        Root_Actions_2.9.tar.xz

Requires:      kde-baseapps-dolphin 

%description

Root Actions servicemenu provides a convenient way to perform several actions 'as root', from the right-click context menu in KDE filemanagers.

Servisní menu pro KDE4, osahující několik funkcí s právy roota v kontextovém menu, vyvolaným pravým tlačítkem.

%prep
%setup -q -c %{name}

%install
%__install -d %{buildroot}%{_bindir}/
cd usr/bin/
%__cp rootactions-servicemenu.pl %{buildroot}%{_bindir}/
%__install -d %{buildroot}/%{_datadir}/kde4/services/*
cd ../../usr/share/kde4/services/ServiceMenus/
%__cp -r ./* %{buildroot}/%{_datadir}/kde4/services/*


%files
%{_bindir}/rootactions-servicemenu.pl
%{_datadir}/kde4/services/*


%changelog
