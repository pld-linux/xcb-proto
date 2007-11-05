Summary:	XML-XCB protocol description files
Summary(pl.UTF-8):	Pliki opisu protokołu XML-XCB
Name:		xcb-proto
Version:	1.1
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	dd34acc58c0a438e812f72a9afe7b2a0
URL:		http://xcb.freedesktop.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcb-proto provides the XML-XCB protocol descriptions that libxcb uses
to generate the majority of its code and API. They are provided
separately from libxcb to allow reuse by other projects, such as
additional language bindings, protocol dissectors, or documentation
generators.

%description -l pl.UTF-8
xcb-proto zawiera opisy protokołu XML-XCB używane przez libxcb do
generowania większości swojego kodu i API. Są dostarczane osobno, aby
umożliwić wykorzystanie przez inne projekty, takie jak dodatkowe
dowiązania dla innych języków, analizatory protokołu czy generatory
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
