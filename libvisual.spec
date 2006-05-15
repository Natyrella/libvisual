Summary:	Abstraction library that comes between applications and audio visualisation plugins
Summary(pl):	Abstrakcyjna biblioteka pomi�dzy aplikacjami a wtyczkami wizualizacji audio
Name:		libvisual
Version:	0.4.0
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libvisual/%{name}-%{version}.tar.bz2
# Source0-md5:	d0f987abd0845e725743605fd39ef73f
URL:		http://libvisual.sourceforge.net/
Patch0:		%{name}-link.patch
Patch1:		%{name}-ppc.patch
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.14
Obsoletes:	libvisual-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Abstraction library that comes between applications and audio
visualisation plugins.

%description -l pl
Abstrakcyjna biblioteka pomi�dzy aplikacjami a wtyczkami wizualizacji
audio.

%package devel
Summary:	Header files for libvisual library
Summary(pl):	Pliki nag��wkowe biblioteki libvisual
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvisual library.

%description devel -l pl
Pliki nag��wkowe biblioteki libvisual.

%package static
Summary:	Static libvisual library
Summary(pl):	Statyczna biblioteka libvisual
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvisual library.

%description static -l pl
Statyczna biblioteka libvisual.

%prep
%setup -q
%patch0 -p1
%ifarch ppc ppc64
%patch1 -p1
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}-0.4

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-0.4.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libvisual-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvisual-*.so
%{_libdir}/libvisual-*.la
%{_includedir}/libvisual-*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvisual-*.a
