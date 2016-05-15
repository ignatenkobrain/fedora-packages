%global debug_package   %{nil}

%global provider        github
%global provider_tld    com
%global project         technoweenie
%global repo            assert
# https://github.com/technoweenie/assert
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          b25ea301d127043ffacf3b2545726e79b6632139
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Asserts to Go testing
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}.

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/kr/pretty)
Requires:      golang(github.com/kr/pretty)
Provides:      golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package unit-test-devel
Summary:         Unit tests for %{name} package

# test subpackage tests code from devel subpackage
Requires:        %{name}-devel = %{version}-%{release}

%description unit-test-devel
%{summary}.

This package contains unit tests for project
providing packages with %{import_path} prefix.

%prep
%autosetup -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}%{gopath}/src/%{import_path}/
install -Dpm0644 *.go %{buildroot}%{gopath}/src/%{import_path}/

%check
export GOPATH=%{buildroot}%{gopath}:%{gopath}
%gotest %{import_path}

%files devel
%doc README.md example
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/assert.go

%files unit-test-devel
%{gopath}/src/%{import_path}/assert_test.go

%changelog
* Sun May 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-0.1.gitb25ea30
- Initial package
