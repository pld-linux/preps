Summary:	PRepS is a simple Problem Reporting System
Summary(pl):	PRepS to uproszczony system do kontroli i zarz±dzania b³êdami
Name:		preps
Version:	1.6.3
# devel
# Version:	1.7.4
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://webpages.charter.net/stuffle/linux/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-postgresql_include_path.patch
Patch1:		%{name}-nostatic.patch
# Patch0:	%{name}-login_pwd_entry.patch
# Patch1:	%{name}-responsible_on_list.patch
Patch2:		%{name}-with_shared_libpq.patch
Patch3:		%{name}-DESTDIR.patch
# Patch3:	%{name}-macros.patch
URL:		http://webpages.charter.net/stuffle/linux/preps/preps.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	postgresql-devel >= 6.5
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:  tetex
BuildRequires:  tetex-dvips
BuildRequires:  glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libpreps-devel
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
PRepS s³u¿y do kontroli i zarz±dzania b³êdami. PRepS zosta³
zaprojektowany do ma³ych i ¶rednich projektów. Mimo to jest na tyle
elestyczny, ¿e mo¿e byæ u¿ywany przy innych rodzajach problemów
wymagaj±cych kontroli postepu prac. Mo¿e byæ na przyk³ad u¿yty w domu
do nadzoru rzeczy wymagaj±cych naprawy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
aclocal -I macros
autoconf
rm -f missing
automake -a -c
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
rm -f doc/C/images/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%doc doc/C/preps-manual
%doc doc/C/images
%attr(755,root,root) %{_bindir}/*
%{_datadir}/preps/*.xpm
%{_mandir}/man1/*
