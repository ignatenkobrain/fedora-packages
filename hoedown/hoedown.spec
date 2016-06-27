%bcond_without tests

Name:           hoedown
Version:        3.0.7
Release:        1%{?dist}
Summary:        Standards compliant, fast, secure markdown processing library in C

License:        MIT
URL:            https://github.com/hoedown/hoedown
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# https://github.com/hoedown/hoedown/pull/194
Patch0:         0001-Fix-misleading-intentation-warning.patch
# https://github.com/hoedown/hoedown/pull/195
Patch1:         0001-add-CMake-build-definitions.patch
Patch2:         0002-test-runner-add-support-for-getting-executable-from-.patch

BuildRequires:  gcc
BuildRequires:  cmake
# For regeneration of one of sources
BuildRequires:  /usr/bin/gperf
%if %{with tests}
BuildRequires:  /usr/bin/tidy
BuildRequires:  /usr/bin/python
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(Getopt::Long)
%endif

%description
Hoedown is a revived fork of Sundown, the Markdown parser based on the original
code of the Upskirt library by Natacha Porté. Features:
* Fully standards compliant
* Massive extension support
* UTF-8 aware
* Tested & Ready to be used on production
* Customizable renderers
* Optimized for speed
* Zero-dependency

%package devel
Summary:        Development files and headers for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development files and headers for %{name}.

%prep
%autosetup -p1
mkdir build

%build
pushd build
  %cmake .. \
    -DENABLE_TESTS=%{?with_tests:TRUE}%{!?with_tests:FALSE}
  %make_build
popd

%install
pushd build
  %make_install
popd

%if %{with tests}
%check
pushd build
  ctest -VV
popd
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/smartypants
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/

%changelog
* Thu Jun 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.0.7-1
- Initial package
