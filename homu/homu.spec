%global commit c62396ea373bd41b1f5ea0f6022afba63f53b542
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           homu
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Bot that integrates with GitHub and your favorite continuous integration service

License:        MIT
URL:            http://%{name}.io
Source0:        https://github.com/servo/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-github3py
Requires:       python3-toml
Requires:       python3-jinja2
Requires:       python3-requests
Requires:       python3-bottle
Requires:       python3-waitress

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n %{name}-%{commit}
# Replace shebang
sed -i -e '1s|.*|#!%{__python3}|' %{name}/git_helper.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md cfg.sample.toml
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

%changelog
* Wed Jun 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1.gitc62396e
- Initial package
