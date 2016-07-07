%global modname marshmallow_enum
%global srcname marshmallow-enum
%global _docdir_fmt %{name}

# Actually this should be tagged (as this version uploaded to PyPI)
# https://github.com/justanr/marshmallow_enum/issues/3
%global commit a023565774d9c052eac2e7c2d00c210a48f823f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        1.0
Release:        1%{?dist}
Summary:        Enum serializer/deserializer for use with Marshmallow
License:        MIT
URL:            https://github.com/justanr/%{modname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# for tests
BuildRequires:  python2-pytest
BuildRequires:  python2-marshmallow
BuildRequires:  python-enum34
Requires:       python2-marshmallow
Requires:       python-enum34

%description -n python2-%{srcname}
%{summary}.

Python 2 version.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-marshmallow
Requires:       python3-marshmallow

%description -n python3-%{srcname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{modname}-%{commit}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v

%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-*.egg-info/

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-*.egg-info/

%changelog
* Thu Jul 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0-1
- Initial package
