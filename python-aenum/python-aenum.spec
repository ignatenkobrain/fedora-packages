%global modname aenum

%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        1.4.5
Release:        1%{?dist}
Summary:        Advanced Enumerations (compatible with Python's stdlib Enum), NamedTuples, and NamedConstants

License:        BSD
URL:            https://bitbucket.org/stoneleaf/%{modname}
Source0:        %{url}/get/%{version}.tar.gz#/%{modname}-%{version}.tar.gz

BuildArch:      noarch

# for docs
BuildRequires:  /usr/bin/rst2pdf

%global _description \
aenum includes a Python stdlib Enum-compatible data type, as well as a\
metaclass-based NamedTuple implementation and a NamedConstant class.\
\
An Enum is a set of symbolic names (members) bound to unique, constant values.\
Within an enumeration, the members can be compared by identity, and the\
enumeration itself can be iterated over. If using Python 3 there is built-in\
support for unique values, multiple values, auto-numbering, and suspension of\
aliasing (members with the same value are not identical), plus the ability to\
have values automatically bound to attributes.\
\
\
A NamedTuple is a class-based, fixed-length tuple with a name for each possible\
position accessible using attribute-access notation as well as the standard\
index notation.\
\
\
A NamedConstant is a class whose members cannot be rebound; it lacks all other\
Enum capabilities, however; consequently, it can have duplicate values.\
\
\
Utility functions include:\
* skip: class that prevents attributes from being converted to a\
        constant or enum member\
* module: inserts NamedConstant and Enum classes into sys.modules\
          where it will appear to be a module whose top-level names cannot be\
          rebound\
* extend_enum: add new members to enumerations after creation\
* enum: helper class for creating members with keywords\
* constant: helper class for creating constant members

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Recommends:     python-enum34

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -c
mv stoneleaf-%{modname}-* python2
cp -ai python2 python3
rm -f python2/%{modname}/test_v3.py

%build
pushd python2
  %py2_build
popd
pushd python3
  %py3_build
popd
rst2pdf python2/%{modname}/doc/%{modname}.rst -o %{modname}.pdf

%install
pushd python2
  %py2_install
  rm -vrf %{buildroot}%{python2_sitelib}/%{modname}/{CHANGES,LICENSE}
popd
pushd python3
  %py3_install
  rm -vrf %{buildroot}%{python3_sitelib}/%{modname}/{CHANGES,LICENSE}
popd

%check
PYTHONPATH=%{buildroot}%{python2_sitelib} %{__python2} python2/%{modname}/test.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} python3/%{modname}/test.py
PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} python3/%{modname}/test_v3.py

%files -n python2-%{modname}
%license python2/%{modname}/LICENSE
%doc python2/README python2/%{modname}/CHANGES
%doc %{modname}.pdf
%exclude %{python2_sitelib}/%{modname}/doc/
%exclude %{python2_sitelib}/%{modname}/test*.py
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-*.egg-info/

%files -n python3-%{modname}
%license python3/%{modname}/LICENSE
%doc python3/README python3/%{modname}/CHANGES
%doc %{modname}.pdf
%exclude %{python3_sitelib}/%{modname}/doc/
%exclude %{python3_sitelib}/%{modname}/test*.py
%exclude %{python3_sitelib}/%{modname}/__pycache__/test*
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-*.egg-info/

%changelog
* Sat Jul 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.4.5-1
- Initial package
