%define module	    DBIx-Class-Schema-Loader
%define name	    perl-%{module}
%define version     0.04002
%define release     %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Dynamic definition of a DBIx::Class::Schema
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/DBIx/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(DBI) >= 1.56
BuildRequires:	perl(DBIx::Class) >= 0.07006
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(Lingua::EN::Inflect::Number)
BuildRequires:	perl(Class::Data::Accessor)
BuildRequires:	perl(DBD::mysql)
BuildRequires:	perl(DBD::Pg)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBD::SQLite2)
BuildRequires:	perl(Data::Dump)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
DBIx::Class::Schema::Loader automates the definition of a DBIx::Class::Schema
by scanning database table definitions and setting up the columns, primary
keys, and relationships.

DBIx::Class::Schema::Loader currently supports only the DBI storage type. It
has explicit support for DBD::Pg, DBD::mysql, DBD::DB2, DBD::SQLite, and
DBD::Oracle. Other DBI drivers may function to a greater or lesser degree with
this loader, depending on how much of the DBI spec they implement, and how
standard their implementation is.

Patches to make other DBDs work correctly welcome.

See DBIx::Class::Schema::Loader::DBI::Writing for notes on writing your own
vendor-specific subclass for an unsupported DBD driver.

This module requires DBIx::Class 0.07006 or later, and obsoletes the older
DBIx::Class::Loader.

This module is designed more to get you up and running quickly against an
existing database, or to be effective for simple situations, rather than to be
what you use in the long term for a complex database/project.

That being said, transitioning your code from a Schema generated by this module
to one that doesn't use this module should be straightforward and painless, so
don't shy away from it just for fears of the transition down the road.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl}  -pi -e "s/('DBD::(DB2|Oracle))/#$1/g" Makefile.PL
%{__perl} Makefile.PL INSTALLDIRS=vendor <</dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/DBIx
%{_mandir}/*/*

