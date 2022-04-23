#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kbounce
Version  : 22.04.0
Release  : 38
URL      : https://download.kde.org/stable/release-service/22.04.0/src/kbounce-22.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.0/src/kbounce-22.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.0/src/kbounce-22.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 LGPL-2.0
Requires: kbounce-bin = %{version}-%{release}
Requires: kbounce-data = %{version}-%{release}
Requires: kbounce-license = %{version}-%{release}
Requires: kbounce-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev

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
%setup -q -n kbounce-22.04.0
cd %{_builddir}/kbounce-22.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650672641
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1650672641
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kbounce
cp %{_builddir}/kbounce-22.04.0/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kbounce/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kbounce-22.04.0/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kbounce/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kbounce-22.04.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kbounce/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kbounce-22.04.0/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kbounce/7697008f58568e61e7598e796eafc2a997503fde
cp %{_builddir}/kbounce-22.04.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kbounce/a4c60b3fefda228cd7439d3565df043192fef137
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
/usr/share/metainfo/org.kde.kbounce.appdata.xml
/usr/share/qlogging-categories5/kbounce.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kbounce/index.cache.bz2
/usr/share/doc/HTML/ca/kbounce/index.docbook
/usr/share/doc/HTML/ca/kbounce/kbounce_corridor1.png
/usr/share/doc/HTML/ca/kbounce/kbounce_corridor2.png
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
/usr/share/package-licenses/kbounce/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kbounce/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kbounce/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kbounce/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kbounce/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f kbounce.lang
%defattr(-,root,root,-)

