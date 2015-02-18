%define modname	Test-NeedsDisplay
%define modver	1.07

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	6

Summary:	Ensure that tests needing a display have one
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz

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
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

#%check
#make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
