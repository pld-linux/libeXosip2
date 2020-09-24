Summary:	The eXtended osip library
Summary(pl.UTF-8):	Rozszerzona biblioteka osip
Name:		libeXosip2
Version:	5.1.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://download.savannah.gnu.org/releases/exosip/libexosip2-%{version}.tar.gz
# Source0-md5:	9a088539e5b83c66fec628ca9d80b323
Patch0:		%{name}-link.patch
URL:		http://savannah.nongnu.org/projects/exosip
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	c-ares-devel
BuildRequires:	libosip2-devel >= 5.0.0
BuildRequires:	libtool >= 2:2
BuildRequires:	openssl-devel >= 1.0.2
BuildRequires:	pkgconfig
Requires:	libosip2 >= 5.0.0
Requires:	openssl >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eXosip is a library that hides the complexity of using the SIP
protocol for multimedia session establishement. This protocol is
mainly to be used by VoIP telephony applications (endpoints or
conference server) but might be also usefull for any application that
wish to establish sessions like multiplayer games.

%description -l pl.UTF-8
eXosip jest biblioteką ukrywającą skomplikowane korzystanie z
protokołu SIP dla sesji multimedialnych. Protokół jest przeznaczony do
wykorzystania przez aplikacje telefoniczne korzystające z VoIP
(telefony lub serwery konferencji), ale może być również używany
przez dowolne aplikacje chcące używać sesji multimedialnych, jak np.
gry dla wielu graczy.

%package devel
Summary:	Header files for libeXosip2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libeXosip2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	c-ares-devel
Requires:	libosip2-devel >= 5.0.0
Requires:	openssl-devel >= 1.0.2

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
%setup -q -n libexosip2-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-openssl \
	--disable-silent-rules
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
%attr(755,root,root) %{_bindir}/sip_monitor
%attr(755,root,root) %{_bindir}/sip_reg
%attr(755,root,root) %{_libdir}/libeXosip2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeXosip2.so.13

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeXosip2.so
%{_libdir}/libeXosip2.la
%{_includedir}/eXosip2

%files static
%defattr(644,root,root,755)
%{_libdir}/libeXosip2.a
