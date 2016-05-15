%global debug_package   %{nil}

%global provider        github
%global provider_tld    com
%global project         bgentry
%global repo            go-netrc
# https://github.com/bgentry/go-netrc
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          9fd32a8b3d3d3f9d43c341bfe098430e07609480
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        netrc file parser for Go programming language
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
A Golang package for reading and writing netrc files. This package can parse
netrc files, make changes to them, and then serialize them back to netrc
format, while preserving any whitespace that was present in the source file.

%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}/netrc) = %{version}-%{release}

%description devel
A Golang package for reading and writing netrc files. This package can parse
netrc files, make changes to them, and then serialize them back to netrc
format, while preserving any whitespace that was present in the source file.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package unit-test-devel
Summary:         Unit tests for %{name} package

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%description unit-test-devel
A Golang package for reading and writing netrc files. This package can parse
netrc files, make changes to them, and then serialize them back to netrc
format, while preserving any whitespace that was present in the source file.

This package contains unit tests for project
providing packages with %{import_path} prefix.

%prep
%autosetup -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}%{gopath}/src/%{import_path}/netrc/
install -Dpm0644 netrc/*.go %{buildroot}%{gopath}/src/%{import_path}/netrc/
install -d -p %{buildroot}%{gopath}/src/%{import_path}/netrc/examples/
install -Dpm0644 netrc/examples/*.netrc %{buildroot}%{gopath}/src/%{import_path}/netrc/examples/

%check
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%gotest %{import_path}/netrc

%files devel
%license LICENSE
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%dir %{gopath}/src/%{import_path}/netrc
%{gopath}/src/%{import_path}/netrc/netrc.go

%files unit-test-devel
%{gopath}/src/%{import_path}/netrc/netrc_test.go
%{gopath}/src/%{import_path}/netrc/examples/

%changelog
* Sun May 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-0.1.git9fd32a8
- Initial package
