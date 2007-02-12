#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Extreme
Summary:	Test::Extreme - a perlish unit testing framework
Summary(pl.UTF-8):   Test::Extreme - perlowy szkielet do testowania w stylu unit
Name:		perl-Test-Extreme
Version:	0.12
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	008505ccc3d31a46cc89dc5883ba2d14
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Extreme is a perlish port of the xUnit testing framework. It is
in the spirit of JUnit, the unit testing framework for Java, by Kent
Beck and Erich Gamma. Instead of porting the implementation of JUnit
we have ported its spirit to Perl.

%description -l pl.UTF-8
Test::Extreme to perlowy port szkieletu testującego xUnit. Jest w
duchu JUnit, szkieletu testowego dla Javy, autorstwa Kenta Becka i
Ericha Gammy. Zamiast portowania implementacji Junit został sportowany
do Perla jego duch.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
