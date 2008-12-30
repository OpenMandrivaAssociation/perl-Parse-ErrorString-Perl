
%define realname   Parse-ErrorString-Perl
%define version    0.08
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Parse error messages from the perl interpreter
Source:     http://www.cpan.org/modules/by-module/Parse/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Test::More)
BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(File::Basename)
BuildRequires: perl(Pod::Find)
BuildRequires: perl(Pod::POM)

BuildArch: noarch

%description
Module to parse error messages from the perl interpreter.


%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
#./Build test

%install
rm -rf %buildroot
./Build install --destdir %buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
/usr/bin/check_perldiag
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*


