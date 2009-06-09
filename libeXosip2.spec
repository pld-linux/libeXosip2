Summary:	The eXtended osip library
Summary(pl.UTF-8):	Rozszerzona biblioteka osip
Name:		libeXosip2
Version:	3.3.0
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.savannah.nongnu.org/releases/exosip/%{name}-%{version}.tar.gz
# Source0-md5:	a2739067b51c1e417c5aef9606b285b2
URL:		http://savannah.nongnu.org/projects/exosip
BuildRequires:	libosip2-devel >= 3.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eXosip is a library that hides the complexity of using the SIP
protocol for multimedia session establishement. This protocol is
mainly to be used by VoIP telephony applications (endpoints or
conference server) but might be also usefull for any application that
wish to establish sessions like multiplayer games.

%description -l pl.UTF-8
eXosip jest biblioteką ukrywającą skomplikowane korzystanie z
protokołu SIP dla multimedialnych sesji. Prokokół jest przeznaczony
do wykorzystania przez aplikacje telefoniczne korzystające z
VoIP(telefony lub serwery konferencji), ale może być równiez
używany przez dowolne aplikacje chcące uzywać multimedialnych
sesji, jak np gry dla wielu graczy.

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
#%patch0 -p1

%build
%configure
# disable ssl support - need fresh openssl and isn't necessary - no way to
# disable it at configure level - see
# http://www.atosc.org/pipermail/osip/2007-September/007975.html
sed -e 's@#define HAVE_OPENSSL_SSL_H 1@#undef HAVE_OPENSSL_SSL_H@g' -i config.h
%{__make} -j1

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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/eXosip2/

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
