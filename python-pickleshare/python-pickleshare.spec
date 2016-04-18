%global modname pickleshare

# Tests are not included in PyPI
# https://github.com/pickleshare/pickleshare/issues/22
%global with_tests 0

Name:           python-%{modname}
Version:        0.7.2
Release:        1%{?dist}
Summary:        Tiny 'shelve'-like database with concurrency support

# License is not included in PyPI
# https://github.com/pickleshare/pickleshare/issues/22
License:        MIT
URL:            https://pypi.python.org/pypi/%{modname}
Source0:        https://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
PickleShare - a small 'shelve' like datastore with concurrency support.\
\
Like shelve, a PickleShareDB object acts like a normal dictionary.\
Unlike shelve, many processes can access the database simultaneously.\
Changing a value in database is immediately visible to other processes\
accessing the same database.\
\
Concurrency is possible because the values are stored in separate files.\
Hence the "database" is a directory where all files are governed by\
PickleShare.

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if 0%{?with_tests}
BuildRequires:  python2-pytest
%endif
Requires:       python2-pathlib2

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?with_tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
rm -rf *.egg-info
# Renove shebang
sed -i -e '1{\@^#!/usr/bin/env python@d}' %{modname}.py

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%if 0%{?with_tests}
%check
py.test-%{python2_version} -v
py.test-%{python3_version} -v
%endif

%files -n python2-%{modname}
%{python2_sitelib}/%{modname}-%{version}-*.egg-info/
%{python2_sitelib}/%{modname}.py*

%files -n python3-%{modname}
%{python3_sitelib}/%{modname}-%{version}-*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Mon Apr 18 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.7.2-1
- Initial package
