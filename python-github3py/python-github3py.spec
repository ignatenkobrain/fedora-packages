%global modname github3py
%global srcname github3.py
%global altname github3

# Tests require internet connection to github.com
%bcond_with tests

%global rctag a4

Name:           python-%{modname}
Version:        1.0.0
Release:        0.1%{?rctag:%{rctag}}%{?dist}
Summary:        Python wrapper for the GitHub API

License:        BSD
URL:            https://github3py.readthedocs.org
Source0:        https://github.com/sigmavirus24/%{srcname}/archive/%{version}%{?rctag:%{rctag}}/%{modname}-%{version}%{?rctag:%{rctag}}.tar.gz

BuildArch:      noarch

%global _description \
github3.py is a comprehensive, actively developed and extraordinarily stable\
wrapper around the GitHub API (v3).

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
%{?python_provide:%python_provide python2-%{srcname}}
%{?python_provide:%python_provide python2-%{altname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with tests}
BuildRequires:  python2-pytest
BuildRequires:  python2-betamax
BuildRequires:  python2-betamax-matchers
BuildRequires:  python2-unittest2
BuildRequires:  python2-mock
BuildRequires:  python2-requests
BuildRequires:  python2-uritemplate
%endif
Requires:       python2-requests
# FIXME: use uritemplate.py https://bugzilla.redhat.com/show_bug.cgi?id=1351136
Requires:       python2-uritemplate
# TODO: handle SNI_requires
# ignatenkobrain: no idea how it is used for now

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{srcname}}
%{?python_provide:%python_provide python3-%{altname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-betamax
BuildRequires:  python3-betamax-matchers
BuildRequires:  python3-requests
BuildRequires:  python3-uritemplate
%endif
Requires:       python3-requests
Requires:       python3-uritemplate

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}%{?rctag:%{rctag}}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%if %{with tests}
%check
# Some of tests are failing: https://github.com/sigmavirus24/github3.py/issues/624
py.test-%{python2_version} -v
py.test-%{python3_version} -v
%endif

%files -n python2-%{modname}
%license LICENSE
%doc README.rst HISTORY.rst
%{python2_sitelib}/%{srcname}-*.egg-info/
%{python2_sitelib}/%{altname}/

%files -n python3-%{modname}
%license LICENSE
%doc README.rst HISTORY.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{altname}/

%changelog
* Wed Jun 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-0.1a4
- Initial package
