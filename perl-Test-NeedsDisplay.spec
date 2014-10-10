%define upstream_name    Test-NeedsDisplay
%define upstream_version 1.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Ensure that tests needing a display have one
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildRequires:	x11-server-xvfb
BuildArch:	noarch
Requires:	x11-server-xvfb

%description
When testing GUI applications, sometimes applications or modules absolutely
insist on a display, even just to load a module without actually showing
any objects.

Regardless, this makes GUI applications pretty much impossible to build and
test on headless or automated systems. And it fails to the point of not
even running the Makefile.PL script because a dependency needs a display so
it can be loaded to find a version.

In these situations, what is needed is a fake display.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.70.0-2mdv2011.0
+ Revision: 658889
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 401520
- rebuild using %%perl_convert_version
- fixed license field

* Mon Jan 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.07-1mdv2009.1
+ Revision: 325081
- removing tests for this package
- update to new version 1.07

* Wed Nov 12 2008 Jérôme Quelin <jquelin@mandriva.org> 1.05-1mdv2009.1
+ Revision: 302526
- adding missing prereqs
- import perl-Test-NeedsDisplay


* Wed Nov 12 2008 cpan2dist 1.05-1mdv
- initial mdv release, generated with cpan2dist

