Summary:	PRepS is a simple Problem Reporting System
Summary(pl):	PRepS to uproszczony system do kontroli i zarz�dzania b��dami
Name:		preps
Version:	1.2.4
Release:	4
Copyright:	Artistic
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	http://www.execpc.com/~stuffle/linux/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-login_pwd_entry.patch
Patch2:		%{name}-responsible_on_list.patch
BuildRequires:	postgresql-static >= 6.5
BuildRequires:	gtk+-devel >= 1.2
Requires:	gtk+ >= 1.2
Requires:	postgresql >= 6.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PRepS is a simple Problem Reporting System. PRepS is designed around
the bug tracking needs of small to medium sized software projects.
However, PRepS may be flexible enough to be used for other types of
problem or status tracking. For example, PRepS could be setup to track
things that need fixing around the house. Be creative.

%description -l pl
PRepS s�u�y do kontroli i zarz�dzania b��dami. PRepS zosta�
zaprojektowany do ma�ych i �rednich projekt�w. Mimo to jest na tyle
elestyczny, �e mo�e by� u�ywany przy innych rodzajach problem�w
wymagaj�cych kontroli postepu prac. Mo�e by� na przyk�ad u�yty w domu
do nadzoru rzeczy wymagaj�cych naprawy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
