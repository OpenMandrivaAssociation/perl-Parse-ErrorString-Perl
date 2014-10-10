%define upstream_name    Parse-ErrorString-Perl
%define upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Parse error messages from the perl interpreter
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/Parse-ErrorString-Perl-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(Pod::Find)
BuildRequires:	perl(Pod::POM)
BuildArch:	noarch

%description
Module to parse error messages from the perl interpreter.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc  Changes
%{_bindir}/check_perldiag
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.150.0-2mdv2011.0
+ Revision: 657820
- rebuild for updated spec-helper

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 622927
- new version

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 401617
- rebuild using %%perl_convert_version
- fixed license field

* Tue Feb 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.13-1mdv2009.1
+ Revision: 339096
- update to new version 0.13

* Mon Feb 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.12-1mdv2009.1
+ Revision: 338704
- update to new version 0.12

* Sat Jan 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.11-1mdv2009.1
+ Revision: 323993
- update to new version 0.11

* Fri Jan 02 2009 Jérôme Quelin <jquelin@mandriva.org> 0.09-1mdv2009.1
+ Revision: 323339
- update to new version 0.09

* Tue Dec 30 2008 Jérôme Quelin <jquelin@mandriva.org> 0.08-1mdv2009.1
+ Revision: 321397
- import perl-Parse-ErrorString-Perl


* Tue Dec 30 2008 jquelin 0.08-1mdv
- initial mdv release



