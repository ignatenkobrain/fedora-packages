%global debug_package   %{nil}

%global provider        github
%global provider_tld    com
%global project         ThomsonReutersEikon
%global repo            go-ntlm
# https://github.com/ThomsonReutersEikon/go-ntlm
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          b00ec39bbdd04f845950f4dbb4fd0a2c3155e830
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Native implementation of NTLM for Go
License:        BSD with advertising
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

Provides:      golang(%{import_path}/ntlm) = %{version}-%{release}
Provides:      golang(%{import_path}/ntlm/md4) = %{version}-%{release}

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
# source codes for building projects
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done

# testing files for this project
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list
done

sort -u -o devel.file-list devel.file-list

%check
export GOPATH=%{buildroot}/%{gopath}:%{gopath}

%gotest %{import_path}/ntlm
%gotest %{import_path}/ntlm/md4

%files devel -f devel.file-list
%license License
%doc README.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}

%files unit-test-devel -f unit-test-devel.file-list

%changelog
* Sun May 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-0.1.gitb00ec39
- Initial package
