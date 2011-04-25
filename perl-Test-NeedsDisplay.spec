%define upstream_name    Test-NeedsDisplay
%define upstream_version 1.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Ensure that tests needing a display have one
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)
BuildRequires: x11-server-xvfb
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Requires: x11-server-xvfb

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

#%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*

