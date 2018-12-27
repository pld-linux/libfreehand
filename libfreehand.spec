#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

Summary:	Library for parsing the FreeHand file format structure
Summary(pl.UTF-8):	Biblioteka do analizy struktury formatu plików FreeHand
Name:		libfreehand
Version:	0.1.2
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/libfreehand/%{name}-%{version}.tar.xz
# Source0-md5:	c3788f5686839fd097bd77d8f51c3d04
URL:		http://www.freedesktop.org/wiki/Software/libfreehand/
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	gperf >= 3.0.0
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libicu-devel
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libfreehand is library providing ability to interpret and import
Adobe/Macromedia drawings into various applications.

%description -l pl.UTF-8
Libfreehand to biblioteka umożliwiająca interpretowanie i import do
różnych aplikacji rysunków w formacie Adobe/Macromedia.

%package devel
Summary:	Header files for libfreehand library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfreehand
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel >= 6:4.7
Requires:	zlib-devel

%description devel
Header files for libfreehand library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfreehand.

%package static
Summary:	Static libfreehand library
Summary(pl.UTF-8):	Statyczna biblioteka libfreehand
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfreehand library.

%description static -l pl.UTF-8
Statyczna biblioteka libfreehand.

%package apidocs
Summary:	libfreehand API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libfreehand
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libfreehand library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libfreehand.

%package tools
Summary:	Tools to transform FreeHand drawings into other formats
Summary(pl.UTF-8):	Programy przekształcania rysunków FreeHand do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform FreeHand drawings into other formats. Currently
supported: SVG, raw.

%description tools -l pl.UTF-8
Narzędzia do przekształcania rysunków FreeHand do innych formatów.
Aktualnie obsługiwane są SVG i format surowy.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfreehand-*.la
# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libfreehand

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libfreehand-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfreehand-0.1.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfreehand-0.1.so
%{_includedir}/libfreehand-0.1
%{_pkgconfigdir}/libfreehand-0.1.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfreehand-0.1.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fh2raw
%attr(755,root,root) %{_bindir}/fh2svg
%attr(755,root,root) %{_bindir}/fh2text
