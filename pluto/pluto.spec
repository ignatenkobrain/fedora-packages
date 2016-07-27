%global commit c6cab36140648828ccc72cc659d55d274508da0d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pluto
Version:        0
Release:        0.1git%{shortcommit}%{?dist}
Summary:        Small utility library for SHA1, Tiny Encryption Algorithm, and UUID4

License:        GPLv3+
URL:            https://gitlab.com/CollectiveTyranny/pluto
Source0:        %{url}/repository/archive.tar.gz?ref=%{commit}#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make

%description
%{summary}.

%package devel
Summary:        Development files and headers for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%package doc
Summary:        Documentation for %{name}-devel
BuildRequires:  doxygen
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{commit}-%{commit}
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %cmake ..
popd
%make_build -C %{_target_platform}
%make_build doc -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files doc
%license LICENSE
%doc doc/html

%changelog
* Wed Jul 27 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1gitc6cab36
- Initial package
