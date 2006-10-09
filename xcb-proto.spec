Summary:	XCB protocol files
Summary(pl):	Pliki opisu protoko³u XCB
Name:		xcb-proto
Version:	0.9.92
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	dc05c33ae1efc3e59d725887de9fc1a6
URL:		http://xcb.freedesktop.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCB protocol files.

%description -l pl
Pliki opisu protoko³u XCB.

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
%doc COPYING TODO doc/xml-xcb.txt
%{_datadir}/xcb
%{_pkgconfigdir}/xcb-proto.pc
