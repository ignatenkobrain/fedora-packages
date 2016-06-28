%global modname qrencode

%global commit a58d28a4988676d20e204a9937972528cdffc381
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          python-%{modname}
Version:       0
Release:       1.git.%{shortcommit}%{?dist}
Summary:       A simple wrapper for the C qrencode

# No LICENSE file in repo: https://github.com/Arachnid/pyqrencode/issues/9
License:       ASL 2.0
URL:           https://github.com/Arachnid/pyqrencode
Source0:       %{url}/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz

BuildRequires: qrencode-devel

%description
A simple wrapper for the C qrencode.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
Requires:       python2-pillow%{?_isa}

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
Requires:       python3-pillow%{?_isa}

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -n py%{modname}-%{commit}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{modname}
%{python2_sitearch}/%{modname}/
%{python2_sitearch}/%{modname}-*.egg-info

%files -n python3-%{modname}
%{python3_sitearch}/%{modname}/
%{python3_sitearch}/%{modname}-*.egg-info

%changelog
* Tue Jun 28 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-1.git.a58d28a
- Initial package
