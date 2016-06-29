%global modname uritemplate
%global altname uritemplate.py

%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Simple python library to deal with URI Templates (RFC 6570)

License:        BSD
URL:            https://%{modname}.readthedocs.io
Source0:        https://github.com/sigmavirus24/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
%{?python_provide:%python_provide python2-%{altname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{altname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n uritemplate-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
py.test-%{python2_version} -v
py.test-%{python3_version} -v

%files -n python2-%{modname}
%license LICENSE
%doc HISTORY.rst README.rst
%{python2_sitelib}/%{altname}-*.egg-info
%{python2_sitelib}/%{modname}/

%files -n python3-%{modname}
%license LICENSE
%doc HISTORY.rst README.rst
%{python3_sitelib}/%{altname}-*.egg-info
%{python3_sitelib}/%{modname}/

%changelog
* Wed Jun 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.0-1
- Initial package
