%global modname multidict

#global rctag b4

Name:           python-%{modname}
Version:        1.1.0
Release:        1%{?rctag:%{rctag}}%{?dist}
Summary:        MultiDict implementation

License:        ASL 2.0
URL:            https://github.com/aio-libs/%{modname}
Source0:        %{url}/archive/v%{version}%{?rctag:%{rctag}}/%{modname}-%{version}%{?rctag:%{rctag}}.tar.gz

BuildRequires:  gcc

%global _description \
Multidicts are useful for working with HTTP headers, URL query args etc.\
\
The code was extracted from aiohttp library.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest

%description -n python3-%{modname} %{_description}

%prep
%autosetup -n %{modname}-%{version}%{?rctag:%{rctag}}
rm -f %{modname}/*.c

%build
%py3_build

%install
%py3_install
rm -f %{buildroot}%{python3_sitearch}/%{modname}/*.{c,pyx}

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-3 -v

%files -n python3-%{modname}
%license LICENSE
%doc README.rst CHANGES.rst
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/

%changelog
* Thu Jul 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.0-1
- Update to 1.1.0
- Trivial fixes

* Thu Jun 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.0-0.1b4
- Initial package
