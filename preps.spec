Summary:	PRepS is a simple Problem Reporting System
Summary(pl):	PRepS to uproszczony system do kontroli i zarz�dzania b��dami
Name:		preps
Version:	1.4.5
Release:	2
License:	Artistic
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	http://www.execpc.com/~stuffle/linux/%{name}-%{version}.tar.gz
Patch0:		%{name}-login_pwd_entry.patch
Patch1:		%{name}-responsible_on_list.patch
Patch2:		%{name}-with_shared_libpq.patch
Patch3:		%{name}-macros.patch
Patch4:		%{name}-shell.patch
Patch5:		%{name}-plpgsql.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	postgresql-devel >= 6.5
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:  tetex
BuildRequires:  tetex-dvips
BuildRequires:  glib-devel
BuildRequires:  gtk+-devel
BuildRequires:  XFree86-devel
Requires:       postgresql-module-plpgsql
Requires:       tetex
Requires:       tetex-dvips
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
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
aclocal -I macros
autoconf
automake -a -c
%configure --with-pgsqldir=%{_libdir}/modules
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog INSTALL NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html
%attr(755,root,root) %{_libdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/*.sql
%{_datadir}/%{name}/*.xpm
%{_datadir}/%{name}/*.msg
%{_mandir}/man1/*
