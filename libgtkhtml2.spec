%define pkgname libgtkhtml
%define lib_major 0
%define api_version 2
%define libname %mklibname gtkhtml %{api_version} %{lib_major}
%define libnamedev %mklibname -d gtkhtml %{api_version}

Summary:	GtkHTML 2
Name:		%{pkgname}%{api_version}
Version:	2.11.1
Release:	10
License:	LGPL
Url:		http://www.gnome.org/
Group:		System/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2
Patch0:		libgtkhtml-2.11.1-wformat.patch
BuildRequires:	pkgconfig(gail)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
GtkHTML 2

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
GtkHTML 2 shared library

%package -n %{libnamedev}
Summary:	Static libraries, include files for GtkHTML2
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	gtkhtml2-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{libnamedev}
GtkHTML2 development files

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1 -b .wformat

%build
%configure2_5x --disable-static

%make LIBS="-lm"

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgtkhtml-%{api_version}.so.%{lib_major}*

%files -n %{libnamedev}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.11.1-7mdv2011.0
+ Revision: 661471
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2.11.1-6mdv2011.0
+ Revision: 602557
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.11.1-5mdv2010.1
+ Revision: 520865
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.11.1-4mdv2010.0
+ Revision: 425563
- rebuild
- fix -Wformat warnings

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.11.1-3mdv2009.0
+ Revision: 222884
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.11.1-1mdv2008.0
+ Revision: 63329
- new version
- new devel name


* Thu Oct 19 2006 Götz Waschk <waschk@mandriva.org> 2.11.0-3mdv2007.1
- fix buildrequires

* Fri Jul 14 2006 Frederic Crozat <fcrozat@mandriva.com> 2.11.0-2mdv2007.0
- Rebuild with latest libgail

* Sat Oct 08 2005 Frederic Crozat <fcrozat@mandriva.com> 2.11.0-1mdk
- Release 2.11.0
- Remove patch0 (no longer needed)

* Sat Sep 03 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.6.3-3mdk
- rebuild to remove glitz dep

* Thu Aug 18 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.6.3-2mdk
- built-in libtool 1.4 fixes

* Sun Feb 13 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.6.3-1mdk
- New release 2.6.3

* Wed Jun 09 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- reenable libtoolize
- New release 2.6.2

* Tue Apr 20 2004 Goetz Waschk <goetz@mandrakesoft.com> 2.6.1-1mdk
- New release 2.6.1

* Wed Apr 07 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- Release 2.6.0 (with Götz help)

* Tue Jan 06 2004 Götz Waschk <waschk@linux-mandrake.com> 2.4.1-2mdk
- the devel package provides gtkhtml2-devel for compatibility

* Wed Nov 05 2003 Götz Waschk <waschk@linux-mandrake.com> 2.4.1-1mdk
- new version

