%include	/usr/lib/rpm/macros.perl
Summary:	HTML-TableLayout perl module
Summary(pl):	Modu³ perla HTML-TableLayout
Name:		perl-HTML-TableLayout
Version:	1.001008
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-TableLayout-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML-TableLayout is a HTML-generating package for making graphical
user interfaces via a web browser.

%description -l pl
HTML-TableLayout jest pakietem generuj±cym graficzne interfejsy
u¿ytkownika w HTMLu przez przegl±darkê www.

%prep
%setup -q -n HTML-TableLayout-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README RELEASE_NOTES *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTML/TableLayout.pm
%dir %{perl_sitelib}/HTML/TableLayout
%{perl_sitelib}/HTML/TableLayout/*.pm
%{_mandir}/man3/*
