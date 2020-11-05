#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kbounce
Version  : 20.08.3
Release  : 24
URL      : https://download.kde.org/stable/release-service/20.08.3/src/kbounce-20.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.3/src/kbounce-20.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.3/src/kbounce-20.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: kbounce-bin = %{version}-%{release}
Requires: kbounce-data = %{version}-%{release}
Requires: kbounce-license = %{version}-%{release}
Requires: kbounce-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kbounce package.
Group: Binaries
Requires: kbounce-data = %{version}-%{release}
Requires: kbounce-license = %{version}-%{release}

%description bin
bin components for the kbounce package.


%package data
Summary: data components for the kbounce package.
Group: Data

%description data
data components for the kbounce package.


%package doc
Summary: doc components for the kbounce package.
Group: Documentation

%description doc
doc components for the kbounce package.


%package license
Summary: license components for the kbounce package.
Group: Default

%description license
license components for the kbounce package.


%package locales
Summary: locales components for the kbounce package.
Group: Default

%description locales
locales components for the kbounce package.


%prep
%setup -q -n kbounce-20.08.3
cd %{_builddir}/kbounce-20.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604596841
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604596841
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kbounce
cp %{_builddir}/kbounce-20.08.3/COPYING %{buildroot}/usr/share/package-licenses/kbounce/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kbounce-20.08.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/kbounce/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/kbounce-20.08.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/kbounce/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd
%find_lang kbounce

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kbounce

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kbounce.desktop
/usr/share/icons/hicolor/128x128/apps/kbounce.png
/usr/share/icons/hicolor/16x16/apps/kbounce.png
/usr/share/icons/hicolor/22x22/apps/kbounce.png
/usr/share/icons/hicolor/32x32/apps/kbounce.png
/usr/share/icons/hicolor/48x48/apps/kbounce.png
/usr/share/icons/hicolor/64x64/apps/kbounce.png
/usr/share/kbounce/sounds/death.wav
/usr/share/kbounce/sounds/reflect.wav
/usr/share/kbounce/sounds/seconds.wav
/usr/share/kbounce/sounds/timeout.wav
/usr/share/kbounce/sounds/wallend.wav
/usr/share/kbounce/sounds/wallstart.wav
/usr/share/kbounce/themes/default.desktop
/usr/share/kbounce/themes/egyptian_bounce.png
/usr/share/kbounce/themes/egyptian_bounce.svgz
/usr/share/kbounce/themes/geometry.desktop
/usr/share/kbounce/themes/geometry.png
/usr/share/kbounce/themes/kbounce.svg
/usr/share/kbounce/themes/oxygen.desktop
/usr/share/kbounce/themes/oxygen.png
/usr/share/kbounce/themes/oxygen.svgz
/usr/share/kbounce/themes/roads.desktop
/usr/share/kbounce/themes/roads.svgz
/usr/share/kbounce/themes/roads_preview.png
/usr/share/kbounce/themes/the_beach.desktop
/usr/share/kbounce/themes/the_beach.svgz
/usr/share/kbounce/themes/thebeach_preview.png
/usr/share/kxmlgui5/kbounce/kbounceui.rc
/usr/share/metainfo/org.kde.kbounce.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kbounce/button-new.png
/usr/share/doc/HTML/de/kbounce/button-pause.png
/usr/share/doc/HTML/de/kbounce/index.cache.bz2
/usr/share/doc/HTML/de/kbounce/index.docbook
/usr/share/doc/HTML/de/kbounce/kbounce_corridor1.png
/usr/share/doc/HTML/de/kbounce/kbounce_corridor2.png
/usr/share/doc/HTML/de/kbounce/menu-game.png
/usr/share/doc/HTML/de/kbounce/menu-help.png
/usr/share/doc/HTML/de/kbounce/menu-settings.png
/usr/share/doc/HTML/de/kbounce/toolbar.png
/usr/share/doc/HTML/en/kbounce/document-new.png
/usr/share/doc/HTML/en/kbounce/index.cache.bz2
/usr/share/doc/HTML/en/kbounce/index.docbook
/usr/share/doc/HTML/en/kbounce/kbounce_corridor1.png
/usr/share/doc/HTML/en/kbounce/kbounce_corridor2.png
/usr/share/doc/HTML/en/kbounce/media-playback-pause.png
/usr/share/doc/HTML/es/kbounce/index.cache.bz2
/usr/share/doc/HTML/es/kbounce/index.docbook
/usr/share/doc/HTML/et/kbounce/index.cache.bz2
/usr/share/doc/HTML/et/kbounce/index.docbook
/usr/share/doc/HTML/fr/kbounce/index.cache.bz2
/usr/share/doc/HTML/fr/kbounce/index.docbook
/usr/share/doc/HTML/fr/kbounce/jezball_corridor1.png
/usr/share/doc/HTML/fr/kbounce/jezball_corridor2.png
/usr/share/doc/HTML/fr/kbounce/jezball_newWall.png
/usr/share/doc/HTML/it/kbounce/index.cache.bz2
/usr/share/doc/HTML/it/kbounce/index.docbook
/usr/share/doc/HTML/nl/kbounce/index.cache.bz2
/usr/share/doc/HTML/nl/kbounce/index.docbook
/usr/share/doc/HTML/pt/kbounce/index.cache.bz2
/usr/share/doc/HTML/pt/kbounce/index.docbook
/usr/share/doc/HTML/pt_BR/kbounce/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kbounce/index.docbook
/usr/share/doc/HTML/pt_BR/kbounce/kbounce_corridor1.png
/usr/share/doc/HTML/pt_BR/kbounce/kbounce_corridor2.png
/usr/share/doc/HTML/sv/kbounce/index.cache.bz2
/usr/share/doc/HTML/sv/kbounce/index.docbook
/usr/share/doc/HTML/uk/kbounce/index.cache.bz2
/usr/share/doc/HTML/uk/kbounce/index.docbook
/usr/share/doc/HTML/uk/kbounce/kbounce_corridor1.png
/usr/share/doc/HTML/uk/kbounce/kbounce_corridor2.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kbounce/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kbounce/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/kbounce/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kbounce.lang
%defattr(-,root,root,-)

