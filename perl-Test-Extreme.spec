#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Extreme
Summary:	Test::Extreme - A perlish unit testing framework
Summary(pl):	Test::Extreme - perlowy szkielet do testowania w stylu unit
Name:		perl-Test-Extreme
Version:	0.12
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Extreme is a perlish port of the xUnit testing framework. It is
in the spirit of JUnit, the unit testing framework for Java, by Kent
Beck and Erich Gamma. Instead of porting the implementation of JUnit
we have ported its spirit to Perl.

%description -l pl
Test::Extreme to perlowy port szkieletu testuj±cego xUnit. Jest w
duchu JUnit, szkieletu testowego dla Javy, autorstwa Kenta Becka i
Ericha Gammy. Zamiast portowania implementacji Junit zosta³ sportowany
do Perla jego duch.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
