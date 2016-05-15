%global import_path github.com/github/git-lfs

Name:           git-lfs
Version:        1.2.0
Release:        1%{?dist}
Summary:        Git extension for versioning large files

License:        MIT
URL:            https://git-lfs.github.com/
Source0:        https://github.com/github/git-lfs/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{go_arches}
BuildRequires:  compiler(go-compiler)

BuildRequires:  golang(github.com/bgentry/go-netrc/netrc)
BuildRequires:  golang(github.com/cheggaaa/pb)
BuildRequires:  golang(github.com/kr/pretty)
BuildRequires:  golang(github.com/kr/pty)
BuildRequires:  golang(github.com/kr/text)
BuildRequires:  golang(github.com/inconshreveable/mousetrap)
BuildRequires:  golang(github.com/olekukonko/ts)
BuildRequires:  golang(github.com/rubyist/tracerx)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/ThomsonReutersEikon/go-ntlm/ntlm)

# For tests
BuildRequires:  golang(github.com/technoweenie/assert)
BuildRequires:  git >= 1.8.2

# Generate mans
BuildRequires:  /usr/bin/ronn

Requires:       git >= 1.8.2

%description
Git Large File Storage (LFS) replaces large files such as audio samples,
videos, datasets, and graphics with text pointers inside Git, while
storing the file contents on a remote server.

%prep
# If we don't create git repo testing will fail
# https://github.com/github/git-lfs/issues/1219
%autosetup -S git
# Unbundle libs
find -type f -name '*.go' -exec sed -i -e 's,".*_nuts/,",' {} ';'
rm -rf vendor

%build
mkdir -p src/github.com/github/
ln -s $(pwd) src/github.com/github/%{name}
export GOPATH=$(pwd):%{gopath}
%gobuild -o bin/git-lfs %{import_path}

# Build manpages
ronn docs/man/*.ronn

%install
install -Dpm0755 bin/git-lfs %{buildroot}%{_bindir}/%{name}
install -d -p %{buildroot}%{_mandir}/man1/
install -Dpm0644 docs/man/*.1 %{buildroot}%{_mandir}/man1/
install -d -p %{buildroot}%{_mandir}/man5/
install -Dpm0644 docs/man/*.5 %{buildroot}%{_mandir}/man5/

%check
export GOPATH=$(pwd):%{gopath}
%gotest %{import_path}/git
%gotest %{import_path}/lfs

%files
%license LICENSE.md
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}*.1*
%doc %{_mandir}/man5/%{name}*.5*

%changelog
* Sun May 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.2.0-1
- Initial package
