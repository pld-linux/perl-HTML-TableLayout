%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	TableLayout
Summary:	HTML::TableLayout - "Layout Manager" for CGI-based web applications
Summary(pl):	HTML::TableLayout - "Zarz�dca opcji" dla opartych na CGI aplikacji WWW
Name:		perl-HTML-TableLayout
Version:	1.001008
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f1cd36c0fb77ef8a53255f40ffb457a0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::TableLayout is a HTML-generating package for making graphical
user interfaces via a web browser using a "Layout Manager" paradigm
such as in Tk/Tcl or Java.  It includes a component hierarchy for
making new "widgets".

%description -l pl
HTML::TableLayout jest pakietem generuj�cym graficzne interfejsy
u�ytkownika w HTML-u przez przegl�dark� WWW za pomoc� paradygmatu
"Zarz�dcy opcji" ("Layout Manager"), takiego jak w Tk/Tcl lub Javie.
Zawiera on hierarchie komponent�w tworz�cych nowe kontrolki.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README RELEASE_NOTES *txt
%{perl_vendorlib}/HTML/TableLayout.pm
%dir %{perl_vendorlib}/HTML/TableLayout
%{perl_vendorlib}/HTML/TableLayout/*.pm
%{_mandir}/man3/*
