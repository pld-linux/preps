Summary:	PRepS is a simple Problem Reporting System
Summary(pl): PRepS to uproszczony system do kontroli i zarz±dzania b³êdami
Name:		preps
Version:	1.3.2
Release:	1
Copyright:	Artistic
Group:		Development/Tools
Source:		http://www.execpc.com/~stuffle/linux/%{name}-%{version}.tar.gz 
Patch:		%{name}-DESTDIR.patch
BuildRequires:	postgresql-static >= 6.5
BuildRequires:	gtk+-devel >= 1.2
Requires:	gtk+ >= 1.2
Requires:	postgresql >= 6.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PRepS is a simple Problem Reporting System.  PRepS is designed around the
bug tracking needs of small to medium sized software projects.  However, 
PRepS may be flexible enough to be used for other types of problem or
status tracking.  For example, PRepS could be setup to track things 
that need fixing around the house.  Be creative.

%description -l pl
PRepS to s³u¿y do kontroli i zarz±dzania b³êdami. PRepS zosta³
zaprojektowany do ma³ych i ¶rednich projektów. Mimo to jest na tyle
elestyczny, ¿e mo¿e byæ u¿ywany przy innych rodzajach problemów
wymagaj±cych kontroli postêpów. Mo¿e byæ na przyk³ad u¿yty w domu
do nadzoru rzeczy wymagaj±cych naprawy. 

%prep
%setup -q
%patch0 -p1

%build
automake -v
%configure
make 

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog COPYING INSTALL NEWS README TODO \
	doc/*html $RPM_BUILD_ROOT/%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,COPYING,INSTALL,NEWS,README,TODO}.gz
%doc doc/*.html.gz
%{_mandir}/man1/*.gz
%{_datadir}/%{name}
# %attr(755,root,root) %{_libdir}/*
%attr(755,root,root) %{_bindir}/*
