Name:           geteltorito
Version:        0.6
Release:        2%{?dist}
Summary:        El Torito boot image extractor

License:        GPLv2+
URL:            http://userpages.uni-koblenz.de/~krienke/ftp/noarch/geteltorito/
Source0:        %{url}/%{name}
Source1:        %{url}/gpl.txt

BuildArch:      noarch

%description
call:   geteltorito CD-image > toritoimagefile
example:geteltorito /dev/sr0  > /tmp/bootimage

The perl-script will extract the initial/default boot image from a CD if
existent. It will not extract any of other possibly existing bootimages
that are allowed by the El Torito standard.
The imagedata are written to STDOUT, all other information is written to
STDERR (eg type and size of image).
If you want to write the image to a file instead of STDOUT you can
specify the filename wanted on the commandline using option -o <filename>.

%prep
%autosetup -T -c
cp -p %{SOURCE0} %{name}
cp -p %{SOURCE1} gpl.txt

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license gpl.txt
%{_bindir}/%{name}

%changelog
* Tue Jun 28 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6-2
- Fix spelling
- Trivial fixes

* Sun Jan 31 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6-1
- Initial package
