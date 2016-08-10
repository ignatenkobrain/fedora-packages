%global srcname keyrings.alt
%global modname %(n=%{srcname}; echo ${n//./-})

Name:           python-%{modname}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Alternate keyring implementations for python-keyring

# No license in archive nor in repo
# https://github.com/jaraco/keyrings.alt/issues/6
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{srcname}; echo ${n:0:1})/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Alternate keyring backend implementations for use with the python-keyring\
package.

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python-gdata
BuildRequires:  python-keyczar
BuildRequires:  python2-crypto
Recommends:     python-gdata
Recommends:     python-keyczar
Requires:       python2-crypto

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-crypto
Requires:       python3-crypto

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
py.test-2 -v
py.test-3 -v

%files -n python2-%{modname}
%doc README.txt
%{python2_sitelib}/%{srcname}-nspkg.pth
%{python2_sitelib}/%{srcname}-*.egg-info/
%dir %{python2_sitelib}/keyrings/
%{python2_sitelib}/keyrings/alt/

%files -n python3-%{modname}
%doc README.txt
%{python3_sitelib}/%{srcname}-nspkg.pth
%{python3_sitelib}/%{srcname}-*.egg-info/
%dir %{python3_sitelib}/keyrings/
%{python3_sitelib}/keyrings/alt/

%changelog

