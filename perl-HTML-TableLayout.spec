%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	TableLayout
Summary:	HTML::TableLayout perl module
Summary(pl):	Modu³ perla HTML::TableLayout
Name:		perl-HTML-TableLayout
Version:	1.001008
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::TableLayout is a HTML-generating package for making graphical
user interfaces via a web browser.

%description -l pl
HTML::TableLayout jest pakietem generuj±cym graficzne interfejsy
u¿ytkownika w HTMLu przez przegl±darkê www.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README RELEASE_NOTES *txt
%{perl_vendorlib}/HTML/TableLayout.pm
%dir %{perl_vendorlib}/HTML/TableLayout
%{perl_vendorlib}/HTML/TableLayout/*.pm
%{_mandir}/man3/*
