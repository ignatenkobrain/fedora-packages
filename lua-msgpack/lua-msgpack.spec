%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}

Name:           lua-msgpack
Version:        0.3.4
Release:        1%{?dist}
Summary:        Lua binary-based efficient object serialization library

License:        MIT
URL:            http://fperrad.github.io/lua-MessagePack/
Source0:        https://github.com/fperrad/lua-MessagePack/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  lua >= %{luaver}
# For tests
#BuildRequires:  /usr/bin/prove
# TODO: lua-testmore is not packaged, only after this we can run tests
#BuildRequires:  lua-testmore
Requires:       lua(abi) >= %{luaver}

BuildArch:      noarch

%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is Lua MessagePack, a pure Lua implementation of MessagePack binary
serialization format.

%prep
%autosetup -n lua-MessagePack-%{version}

%build
# Nothing to build

%install
%make_install INSTALL="install -p" PREFIX="%{_prefix}" LUAVER="%{luaver}"

%check
#make test

%files
%license COPYRIGHT
%{_datadir}/lua/%{luaver}/MessagePack.lua

%changelog
* Thu Apr 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.3.4-1
- Update to 0.3.4
- Add license
- Add %%check section (doesn't work yet)
- BuildArch: noarch
- Improve description

* Wed Jul 09 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Initial package
