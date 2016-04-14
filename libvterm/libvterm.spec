%global libname vterm

%global revision 681

Name:           lib%{libname}
Version:        0
Release:        0.1.bzr%{revision}%{?dist}
Summary:        An abstract library implementation of a VT220/xterm/ECMA-48 terminal emulator

License:        MIT
URL:            https://launchpad.net/libvterm
Source0:        http://bazaar.launchpad.net/~leonerd/libvterm/trunk/tarball/%{revision}/%{name}-%{revision}.tgz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool

%description
An abstract C99 library which implements a VT220 or xterm-like
terminal emulator. It does not use any particular graphics toolkit or
output system. Instead, it invokes callback function pointers that
its embedding program should provide it to draw on its behalf.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%package tools
Summary:        Tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
%{summary}.

%prep
%autosetup -n ~leonerd/libvterm/trunk
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
%{_includedir}/%{libname}_*.h
%{_libdir}/pkgconfig/%{libname}.pc

%files tools
%{_bindir}/unterm
%{_bindir}/%{libname}-ctrl
%{_bindir}/%{libname}-dump

%changelog
* Thu Apr 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1.bzr681
- Initial package
