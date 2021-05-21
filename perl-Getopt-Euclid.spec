#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Getopt-Euclid
Version  : 0.4.5
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/F/FA/FANGLY/Getopt-Euclid-0.4.5.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/F/FA/FANGLY/Getopt-Euclid-0.4.5.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgetopt-euclid-perl/libgetopt-euclid-perl_0.4.5-2.debian.tar.xz
Summary  : 'Executable Uniform Command-Line Interface Descriptions'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Getopt-Euclid-license = %{version}-%{release}
Requires: perl-Getopt-Euclid-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)
BuildRequires : perl(Pod::PlainText)
BuildRequires : perl(Pod::Select)

%description
NAME
Getopt::Euclid - Executable Uniform Command-Line Interface Descriptions
VERSION
This document describes Getopt::Euclid version 0.4.5

%package dev
Summary: dev components for the perl-Getopt-Euclid package.
Group: Development
Provides: perl-Getopt-Euclid-devel = %{version}-%{release}
Requires: perl-Getopt-Euclid = %{version}-%{release}

%description dev
dev components for the perl-Getopt-Euclid package.


%package license
Summary: license components for the perl-Getopt-Euclid package.
Group: Default

%description license
license components for the perl-Getopt-Euclid package.


%package perl
Summary: perl components for the perl-Getopt-Euclid package.
Group: Default
Requires: perl-Getopt-Euclid = %{version}-%{release}

%description perl
perl components for the perl-Getopt-Euclid package.


%prep
%setup -q -n Getopt-Euclid-0.4.5
cd %{_builddir}
tar xf %{_sourcedir}/libgetopt-euclid-perl_0.4.5-2.debian.tar.xz
cd %{_builddir}/Getopt-Euclid-0.4.5
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Getopt-Euclid-0.4.5/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Getopt-Euclid
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Getopt-Euclid/fb5c9d1c927eb97797bffdffd5c04e08e9bcd546
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Getopt::Euclid.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Getopt-Euclid/fb5c9d1c927eb97797bffdffd5c04e08e9bcd546

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Getopt/Euclid.pm
