#
# Conditional build:
%bcond_without	python3 # CPython 3.x module

Summary:	XML-XCB protocol description files
Summary(pl.UTF-8):	Pliki opisu protokołu XML-XCB
Name:		xcb-proto
Version:	1.14
Release:	2
License:	MIT
Group:		Development/Libraries
#Source0:	https://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
Source0:	https://xorg.freedesktop.org/releases/individual/proto/%{name}-%{version}.tar.xz
# Source0-md5:	4a053ca2456007a343024a0452dbf13b
URL:		https://xcb.freedesktop.org/
BuildRequires:	libxml2-progs
BuildRequires:	python >= 1:2.5
%{?with_python3:BuildRequires:	python3}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python >= 1:2.5
Requires:	python-xcbgen = %{version}-%{release}
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

%description -n python-xcbgen
Python 2 xcbgen module.

%description -n python-xcbgen -l pl.UTF-8
Moduł xcbgen dla Pythona 2.

%package -n python3-xcbgen
Summary:	Python 3 xcbgen module
Summary(pl.UTF-8):	Moduł xcbgen dla Pythona 3
Group:		Libraries/Python

%description -n python3-xcbgen
Python 3 xcbgen module.

%description -n python3-xcbgen -l pl.UTF-8
Moduł xcbgen dla Pythona 3.

%prep
%setup -q
%if %{with python3}
mkdir build3
%endif
mkdir build2

%build
%if %{with python3}
cd build3
PYTHON=%{__python3} \
../%configure
%{__make}
cd ..
%endif

cd build2
PYTHON=%{__python} \
../%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
cd build3
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..
%endif

cd build2
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT
%py_ocomp $RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md TODO doc/xml-xcb.txt
%{_datadir}/xcb
%{_pkgconfigdir}/xcb-proto.pc

%files -n python-xcbgen
%defattr(644,root,root,755)
%{py_sitescriptdir}/xcbgen

%if %{with python3}
%files -n python3-xcbgen
%defattr(644,root,root,755)
%{py3_sitedir}/xcbgen
%endif
