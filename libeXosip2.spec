Summary:	The eXtended osip library
Summary(pl.UTF-8):	Rozszerzona biblioteka osip
Name:		libeXosip2
Version:	3.3.0
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://download.savannah.nongnu.org/releases/exosip/%{name}-%{version}.tar.gz
# Source0-md5:	a2739067b51c1e417c5aef9606b285b2
Patch0:		%{name}-openssl_link.patch
URL:		http://savannah.nongnu.org/projects/exosip
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libosip2-devel >= 3.0.3
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eXosip is a library that hides the complexity of using the SIP
protocol for multimedia session establishement. This protocol is
mainly to be used by VoIP telephony applications (endpoints or
conference server) but might be also usefull for any application that
wish to establish sessions like multiplayer games.

%description -l pl.UTF-8
eXosip jest biblioteką ukrywającą skomplikowane korzystanie z
protokołu SIP dla multimedialnych sesji. Prokokół jest przeznaczony do
wykorzystania przez aplikacje telefoniczne korzystające z
VoIP(telefony lub serwery konferencji), ale może być równiez używany
przez dowolne aplikacje chcące uzywać multimedialnych sesji, jak np
gry dla wielu graczy.

%package devel
Summary:	Header files for libeXosip2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libeXosip2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libeXosip2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libeXosip2.

%package static
Summary:	Static libeXosip2 library
Summary(pl.UTF-8):	Statyczna biblioteka libeXosip2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libeXosip2 library.

%description static -l pl.UTF-8
Statyczna biblioteka libeXosip2.

%prep
%setup -q
%patch0

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-openssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/eXosip2/

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
