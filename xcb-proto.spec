Summary:	XML-XCB protocol description files
Summary(pl.UTF-8):	Pliki opisu protokołu XML-XCB
Name:		xcb-proto
Version:	1.2
Release:	2
License:	MIT
Group:		Development/Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	09f912486d8a2353bb4b99ddc28ba3c7
URL:		http://xcb.freedesktop.org/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
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

%py_comp $RPM_BUILD_ROOT
%py_ocomp $RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README TODO doc/xml-xcb.txt
%{_datadir}/xcb
%{_pkgconfigdir}/xcb-proto.pc
%{py_sitescriptdir}/xcbgen
