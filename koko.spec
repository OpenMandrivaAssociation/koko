%define snapshot 20201015

Name:		koko
Summary:	Image viewer for desktop and touch devices
Version:	0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://invent.kde.org/graphics/koko
Source0:	https://invent.kde.org/graphics/koko/-/archive/master/koko-master.tar.bz2
Source1:	http://download.geonames.org/export/dump/cities1000.zip
Source2:	http://download.geonames.org/export/dump/admin1CodesASCII.txt
Source3:	http://download.geonames.org/export/dump/admin2Codes.txt
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:	pkgconfig(exiv2)
Requires:	qml(org.kde.purpose)

%description
Koko is an image viewer for desktop and touch devices.

%prep
%autosetup -p1 -n %{name}-master
cp %{S:1} %{S:2} %{S:3} src/
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_bindir}/koko
# No point in libpackaging this, just internal stuff
# with no headers shipped.
%{_libdir}/libkokocommon.so*
%{_libdir}/qt5/qml/org/kde/koko
%{_datadir}/applications/org.kde.koko.desktop
%{_datadir}/icons/hicolor/128x128/apps/koko.png
%{_datadir}/knotifications5/koko.notifyrc
%{_datadir}/koko
%{_datadir}/metainfo/org.kde.koko.appdata.xml
