#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	LibXML-XPathContext
Summary:	XML::LibXML::XPathContext - Perl interface to libxml2's xmlXPathContext
Summary(pl.UTF-8):	XML::LibXML::XPathContext - interfejs perlowy do xmlXPathContext z libxml2
Name:		perl-XML-LibXML-XPathContext
Version:	0.07
Release:	3
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e7fca6fe476f933b4afba82add465d3
URL:		http://search.cpan.org/dist/XML-LibXML-XPathContext/
BuildRequires:	libxml2-devel >= 2.4.25
%if %{with tests}
BuildRequires:	perl-XML-LibXML >= 0.51
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	libxml2 >= 2.4.25
Requires:	perl-XML-LibXML >= 0.51
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module augments XML::LibXML by providing Perl interface to
libxml2's xmlXPathContext structure. Besides just performing xpath
statements on XML::LibXML's node trees it allows redefining certaint
aspects of XPath engine. This modules allows:
- registering namespace prefixes,
- defining XPath functions in Perl,
- defining variable lookup functions in Perl,
- cheating the context about current proximity position and context
  size.

%description -l pl.UTF-8
Ten moduł rozszerza XML::LibXML dostarczając perlowy interfejs do
struktury xmlXPathContext z libxml2. Oprócz samego wykonywania
instrukcji xpath na drzewach węzłów XML::LibXML pozwala redefiniować
niektóre aspekty silnika XPath:
- rejestrować prefiksy przestrzeni nazw,
- definiować funkcje XPath w Perlu,
- definiować funkcje wyszukiwania zmiennych w Perlu,
- oszukiwać kontekst co do bieżącej bliskości pozycji i rozmiaru
  kontekstu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%{perl_vendorarch}/XML/LibXML/XPathContext.pm
%dir %{perl_vendorarch}/auto/XML/LibXML/XPathContext
%attr(755,root,root) %{perl_vendorarch}/auto/XML/LibXML/XPathContext/XPathContext.so
%{_mandir}/man3/*
