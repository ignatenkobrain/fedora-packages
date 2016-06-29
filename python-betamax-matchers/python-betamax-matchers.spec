%global modname betamax-matchers
%global altname betamax_matchers

%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Group of experimental matchers for Betamax

License:        ASL 2.0
URL:            https://github.com/sigmavirus24/%{altname}
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Experimental set of Matchers for Betamax that may possibly end up in the main\
package.

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
BuildRequires:  python2-betamax
BuildRequires:  python2-requests-toolbelt
Requires:       python2-betamax
Requires:       python2-requests-toolbelt

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-pytest
BuildRequires:  python3-betamax
BuildRequires:  python3-requests-toolbelt
Requires:       python2-betamax
Requires:       python2-requests-toolbelt

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{altname}-%{version}

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
%{python2_sitelib}/%{altname}/
%{python2_sitelib}/%{altname}-*.egg-info/

%files -n python3-%{modname}
%license LICENSE
%doc HISTORY.rst README.rst
%{python3_sitelib}/%{altname}/
%{python3_sitelib}/%{altname}-*.egg-info/

%changelog
* Wed Jun 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.0-1
- Initial package
