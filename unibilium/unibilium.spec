Name:           unibilium
Version:        1.2.0
Release:        1%{?dist}
Summary:        Terminfo parsing library

License:        LGPLv3+
URL:            https://github.com/mauke/unibilium
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
# For docs
BuildRequires:  /usr/bin/pod2man
# For tests
BuildRequires:  /usr/bin/prove

%description
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup
echo '#!/bin/sh' > ./configure
chmod +x ./configure

%build
%configure
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%check
make test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LGPLv3
%doc Changes
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_mandir}/man3/unibi_*.3*
%{_mandir}/man3/%{name}.h.3*

%changelog
* Thu Apr 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.2.0-1
- Initial package
