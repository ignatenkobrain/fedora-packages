%global modname fuzzyfinder

Name:           python-%{modname}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Fuzzy Finder implemented in Python

License:        BSD
URL:            https://github.com/amjith/fuzzyfinder
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{modname}; echo ${n:0:1})/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
%{summary}. Matches partial string entries from a list of strings.\
Works similar to fuzzy finder in SublimeText and Vim's Ctrl-P plugin.

%description
%{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
rm -rf %{modname}.egg-info/

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-2 -v
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-3 -v

%files -n python2-%{modname}
%{python2_sitelib}/%{modname}-*.egg-info/
%{python2_sitelib}/%{modname}/

%files -n python3-%{modname}
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Sat Aug 06 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-1
- Initial package
