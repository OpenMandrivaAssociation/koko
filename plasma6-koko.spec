#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Name:		plasma6-koko
Summary:	Image viewer for desktop and touch devices
Version:	24.12.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://invent.kde.org/graphics/koko
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/koko/-/archive/%{gitbranch}/koko-%{gitbranchd}.tar.bz2#/koko-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%(if [ $(echo %{version} |cut -d. -f3) -ge 50 ]; then echo -n un; fi)stable/release-service/%{version}/src/koko-%{version}.tar.xz
%endif
Source1:	http://download.geonames.org/export/dump/cities1000.zip
Source2:	http://download.geonames.org/export/dump/admin1CodesASCII.txt
Source3:	http://download.geonames.org/export/dump/admin2Codes.txt
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	qml(org.kde.kquickimageeditor)
BuildRequires:	cmake(KQuickImageEditor)
BuildRequires:	pkgconfig(xcb-atom)
Requires:	qml(org.kde.purpose)
Requires:	qml(org.kde.kquickimageeditor)

%description
Koko is an image viewer for desktop and touch devices.

%prep
%autosetup -p1 -n koko-%{?git:%{gitbranchd}}%{!?git:%{version}}
cp %{S:1} %{S:2} %{S:3} src/
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang koko --with-html

%files -f koko.lang
%{_bindir}/koko
# No point in libpackaging this, just internal stuff
# with no headers shipped.
%{_datadir}/applications/org.kde.koko.desktop
%{_datadir}/knotifications6/koko.notifyrc
%{_datadir}/koko
%{_datadir}/metainfo/org.kde.koko.appdata.xml
%{_datadir}/icons/*/*/*/org.kde.koko.*
