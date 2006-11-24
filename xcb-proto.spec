Summary:	XML-XCB protocol description files
Summary(pl):	Pliki opisu protoko³u XML-XCB
Name:		xcb-proto
Version:	1.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	d31407eaae7e52d100645217767a41aa
URL:		http://xcb.freedesktop.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcb-proto provides the XML-XCB protocol descriptions that libxcb uses
to generate the majority of its code and API. They are provided
separately from libxcb to allow reuse by other projects, such as
additional language bindings, protocol dissectors, or documentation
generators.

%description -l pl
xcb-proto zawiera opisy protoko³u XML-XCB u¿ywane przez libxcb do
generowania wiêkszo¶ci swojego kodu i API. S± dostarczane osobno, aby
umo¿liwiæ wykorzystanie przez inne projekty, takie jak dodatkowe
dowi±zania dla innych jêzyków, analizatory protoko³u czy generatory
dokumentacji.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README TODO doc/xml-xcb.txt
%{_datadir}/xcb
%{_pkgconfigdir}/xcb-proto.pc
