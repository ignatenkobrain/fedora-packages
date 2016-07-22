%global modname tqdm

%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        4.7.6
Release:        1%{?dist}
Summary:        A Fast, Extensible Progress Meter

License:        MPLv2.0 and MIT
URL:            https://github.com/tqdm/tqdm
Source0:        %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
tqdm (read taqadum, تقدّم) means "progress" in Arabic.\
\
Instantly make your loops show a smart progress meter - just wrap any iterable\
with "tqdm(iterable)", and you're done!

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose
BuildRequires:  python2-coverage
BuildRequires:  python2-flake8
BuildRequires:  python2-pandas
Recommends:     python2-pandas

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-coverage
BuildRequires:  python3-flake8
BuildRequires:  python3-pandas
Recommends:     python3-pandas

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{modname}
%license LICENCE
%doc README.rst examples
%{python2_sitelib}/%{modname}-*.egg-info/
%{python2_sitelib}/%{modname}/

%files -n python3-%{modname}
%license LICENCE
%doc README.rst examples
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%changelog
* Fri Jul 22 2016 Igor Gnatenko <ignatenko@redhat.com> - 4.7.6-1
- Update to 4.7.6

* Thu Jun 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 4.7.4-1
- Initial package
