%include	/usr/lib/rpm/macros.perl
Summary:	HTML-TableLayout perl module
Summary(pl):	Modu³ perla HTML-TableLayout
Name:		perl-HTML-TableLayout
Version:	1.001008
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-TableLayout-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/TableLayout
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README RELEASE_NOTES *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,RELEASE_NOTES,Component_Heirarchy.txt}.gz

%{perl_sitelib}/HTML/TableLayout.pm
%{perl_sitelib}/HTML/TableLayout/*.pm
%{perl_sitearch}/auto/HTML/TableLayout

%{_mandir}/man3/*
