%define tname QtSpell
%define oname %(echo %{tname} | tr [:upper:] [:lower:])

Summary:	A spell checking for Qt text widgets
Name:		%{oname}
Version:	1.0.1
Release:	1
License:	GPLv3+
Group:		Development/KDE and Qt
URL:		https://github.com/manisandro/%{name}
Source0:	https://github.com/manisandro/%{name}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	doxygen
BuildRequires:	pkgconfig(enchant)
# qt5
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	qmake5
BuildRequires:	qt5-linguist-tools
# qt6
BuildRequires:	cmake(Qt6Tools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qttools-linguist-tools

Requires:	iso-codes

%description
QtSpell adds spell-checking functionality to Qt's text widgets, using the
enchant spell-checking library.

#----------------------------------------------------------------------------

%package qt5
Summary:	A spell checking for Qt5 text widgets
Group:		Development/KDE and Qt

%description qt5
QtSpell-qt5 adds spell-checking functionality to Qt's text widgets, using the
enchant spell-checking library.

%files qt5
%license COPYING
%{_libdir}/libqtspell-qt5.so.*

#----------------------------------------------------------------------------

%package qt5-devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name}-qt5 = %{EVRD}

%description qt5-devel
This package contains libraries and header files for developing applications
that use %{name}-qt5.

%files qt5-devel
%license COPYING
%doc AUTHORS ChangeLog README.md NEWS
%{_includedir}/QtSpell-qt5/
%{_libdir}/libqtspell-qt5.so
%{_libdir}/pkgconfig/QtSpell-qt5.pc

#----------------------------------------------------------------------------

%package qt5-translations
Summary:	Translations for %{name}-qt5
BuildArch:	noarch

Requires:	%{name}-qt5 = %{EVRD}
Requires:	qt5-qttranslations

%description qt5-translations
The %{name}-qt5-translations contains translations for %{name}-qt5.

%files qt5-translations
%{_datadir}/qt5/translations/QtSpell_*.qm

#----------------------------------------------------------------------------

%package qt6
Summary:	A spell checking for Qt6 text widgets
Group:		Development/KDE and Qt

%description qt6
QtSpell-qt6 adds spell-checking functionality to Qt's text widgets, using the
enchant spell-checking library.

%files qt6
%license COPYING
%{_libdir}/libqtspell-qt6.so.*

#----------------------------------------------------------------------------

%package qt6-devel
Summary:	Development files for %{name}-qt6
Group:		Development/KDE and Qt
Requires:	%{name}-qt6 = %{EVRD}

%description qt6-devel
This package contains libraries and header files for developing applications
that use %{name}-qt6.

%files qt6-devel
%license COPYING
%doc AUTHORS ChangeLog README.md NEWS
%{_includedir}/QtSpell-qt6/
%{_libdir}/libqtspell-qt6.so
%{_libdir}/pkgconfig/QtSpell-qt6.pc

#----------------------------------------------------------------------------

%package qt6-translations
Summary:	Translations for %{name}-qt6
BuildArch:	noarch

Requires:	%{name}-qt6 = %{EVRD}
Requires:	qt6-qttranslations

%description qt6-translations
The %{name}-qt6-translations contains translations for %{name}-qt6.

%files qt6-translations
%{_datadir}/qt6/translations/QtSpell_*.qm

#----------------------------------------------------------------------------

%package doc
Summary:	Developer documentation for %{name}
BuildArch:	noarch

%description doc
The %{name}-doc package contains the documentation for developing applications
that use %{name}.

%files doc
%license COPYING
%doc build-qt6/doc/html/

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}

%build
for i in 5 6
do
	CMAKE_BUILD_DIR=build-qt$i \
	%cmake \
		-DQT_VER=$i \
		-GNinja
	%ninja_build
	%ninja_build doc
	cd ..
done

%install
%ninja_install -C build-qt5
%ninja_install -C build-qt6

