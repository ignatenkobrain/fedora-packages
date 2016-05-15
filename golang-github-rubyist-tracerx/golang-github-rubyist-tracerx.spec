%global debug_package   %{nil}

%global provider        github
%global provider_tld    com
%global project         rubyist
%global repo            tracerx
# https://github.com/rubyist/tracerx
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          d7bcc0bc315bed2a841841bee5dbecc8d7d7582f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Output tracing information in your Go app based on environment variables
License:        MIT
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

%description
Tracerx is a simple tracing package that logs messages depending on environment
variables. It is very much inspired by git's GIT_TRACE mechanism.

%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides:      golang(%{import_path}) = %{version}-%{release}

%description devel
Tracerx is a simple tracing package that logs messages depending on environment
variables. It is very much inspired by git's GIT_TRACE mechanism.

This package contains library source intended for building other packages which
use import path with %{import_path} prefix.

%prep
%autosetup -n %{repo}-%{commit}

%build

%install
install -d -p %{buildroot}%{gopath}/src/%{import_path}/
install -pm0644 %{repo}.go %{buildroot}%{gopath}/src/%{import_path}/

%files devel
%license LICENSE
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%{gopath}/src/%{import_path}/%{repo}.go

%changelog
* Sun May 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-0.1.gitd7bcc0b
- Initial package
