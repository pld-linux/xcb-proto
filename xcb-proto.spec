#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	XML-XCB protocol description files
Summary(pl.UTF-8):	Pliki opisu protokołu XML-XCB
Name:		xcb-proto
Version:	1.17.0
Release:	3
License:	MIT
Group:		Development/Libraries
#Source0:	https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
Source0:	https://xorg.freedesktop.org/releases/individual/proto/%{name}-%{version}.tar.xz
# Source0-md5:	c415553d2ee1a8cea43c3234a079b53f
URL:		https://xcb.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.12.6
BuildRequires:	libxml2-progs
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.043
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{without python3}
Requires:	python >= 1:2.5
Requires:	python-xcbgen = %{version}-%{release}
%else
Requires:	python3 >= 1:3.2
Requires:	python3-xcbgen = %{version}-%{release}
%endif
BuildArch:	noarch
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

%package -n python-xcbgen
Summary:	Python 2 xcbgen module
Summary(pl.UTF-8):	Moduł xcbgen dla Pythona 2
Group:		Libraries/Python
Requires:	python-modules >= 1:2.5

%description -n python-xcbgen
Python 2 xcbgen module.

%description -n python-xcbgen -l pl.UTF-8
Moduł xcbgen dla Pythona 2.

%package -n python3-xcbgen
Summary:	Python 3 xcbgen module
Summary(pl.UTF-8):	Moduł xcbgen dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch

%description -n python3-xcbgen
Python 3 xcbgen module.

%description -n python3-xcbgen -l pl.UTF-8
Moduł xcbgen dla Pythona 3.

%prep
%setup -q

%build
# rebuild ac/am to use python3 sitescriptdir (apply automake/revert-debian-python-hacks.patch)
%{__aclocal}
%{__autoconf}
%{__automake}

%define	configuredir	..
%if %{with python3}
install -d build3
cd build3
%configure \
	PYTHON=%{__python3}
%{__make}
cd ..
%endif

%if %{with python2}
install -d build2
cd build2
%configure \
	PYTHON=%{__python}
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__make} -C build2 install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__make} -C build3 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md TODO doc/xml-xcb.txt
%{_datadir}/xcb
%{_npkgconfigdir}/xcb-proto.pc

%if %{with python2}
%files -n python-xcbgen
%defattr(644,root,root,755)
%{py_sitescriptdir}/xcbgen
%endif

%if %{with python3}
%files -n python3-xcbgen
%defattr(644,root,root,755)
%{py3_sitescriptdir}/xcbgen
%endif
