Summary:	PRepS is a simple Problem Reporting System
Summary(pl):	PRepS to uproszczony system do kontroli i zarz±dzania b³êdami
Name:		preps
Version:	1.9.6
Release:	3
License:	GPL
Group:		X11/Development/Tools
Source0:	http://webpages.charter.net/stuffle/preps/download/files/%{name}-%{version}.tar.gz
# Source0-md5:	a09990786e183ed83695037a029cad54
Patch0:		%{name}-with_shared_libpq.patch
Patch1:		%{name}-gtk24.patch
Patch2:		%{name}-desktop.patch
URL:		http://webpages.charter.net/stuffle/preps/preps.html
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	postgresql-devel >= 7.2
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
# to get paths
BuildRequires:	tetex
BuildRequires:	tetex-dvips
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	tetex
Requires:	tetex-dvips
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
elastyczny, ¿e mo¿e byæ u¿ywany przy innych rodzajach problemów
wymagaj±cych kontroli postêpu prac. Mo¿e byæ na przyk³ad u¿yty w domu
do nadzoru rzeczy wymagaj±cych naprawy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_desktopdir} \
	GCONFTOOL=/bin/true

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install preps.schema

%preun
%gconf_schema_uninstall preps.schema

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/preps
%{_sysconfdir}/gconf/schemas/*.schema
%{_omf_dest_dir}/preps
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
