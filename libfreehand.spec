#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Library for parsing the FreeHand file format structure
Summary(pl.UTF-8):	Biblioteka do analizy struktury formatu plików FreeHand
Name:		libfreehand
Version:	0.0.0
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
# Source0-md5:	d143a9c72164350b332d058fc5a3f16c
URL:		http://www.freedesktop.org/wiki/Software/libfreehand/
BuildRequires:	doxygen
BuildRequires:	gperf >= 3.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libwpd-devel >= 0.9
BuildRequires:	libwpg-devel >= 0.2
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
Requires:	libstdc++-devel
Requires:	libwpd-devel >= 0.9
Requires:	libwpg-devel >= 0.2

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

%description apidocs
API documentation for libfreehand library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libfreehand.

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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/fh2raw
%attr(755,root,root) %{_bindir}/fh2svg
%attr(755,root,root) %{_libdir}/libfreehand-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfreehand-0.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfreehand-0.0.so
%{_includedir}/libfreehand-0.0
%{_pkgconfigdir}/libfreehand-0.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libfreehand-0.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*
