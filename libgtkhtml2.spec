%define url_ver %(echo %{version}|cut -d. -f1,2)

%define pkgname libgtkhtml
%define api	2
%define major	0
%define libname %mklibname gtkhtml %{api} %{major}
%define devname %mklibname -d gtkhtml %{api}

Summary:	GtkHTML 2
Name:		%{pkgname}%{api}
Version:	2.11.1
Release:	10
License:	LGPLv2
Url:		http://www.gnome.org/
Group:		System/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgtkhtml/%{url_ver}/%{pkgname}-%{version}.tar.bz2
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

%package -n %{devname}
Summary:	Static libraries, include files for GtkHTML2
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
GtkHTML2 development files

%prep
%setup -qn %{pkgname}-%{version}
%apply_patches

%build
%configure2_5x --disable-static

%make LIBS="-lm"

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgtkhtml-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

