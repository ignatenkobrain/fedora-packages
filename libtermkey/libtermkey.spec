%global libname termkey

# Unibilium by default, otherwise ncurses
%bcond_without unibilium

Name:           lib%{libname}
Version:        0.18
Release:        1%{?dist}
Summary:        Library for easy processing of keyboard entry from terminal-based programs

License:        MIT
URL:            http://www.leonerd.org.uk/code/libtermkey/
Source0:        %{url}/%{name}-%{version}.tar.gz

Patch0:         fix-test-compile.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
%if %{with unibilium}
BuildRequires:  pkgconfig(unibilium)
%else
BuildRequires:  pkgconfig(tinfo)
%endif
# For tests
BuildRequires:  /usr/bin/prove

%description
This library allows easy processing of keyboard entry from terminal-based
programs. It handles all the necessary logic to recognise special keys, UTF-8
combining, and so on, with a simple interface.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1
echo '#!/bin/sh' > ./configure
chmod +x ./configure

%build
%configure
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%check
make test CFLAGS="%{optflags}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{libname}.h
%{_libdir}/pkgconfig/%{libname}.pc
%{_mandir}/man3/%{libname}_*.3*
%{_mandir}/man7/%{libname}.7*

%changelog
* Thu Apr 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.18-1
- Initial package
