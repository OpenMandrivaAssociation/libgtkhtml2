%define req_gail_version 1.3
%define pkgname libgtkhtml
%define lib_major 0
%define api_version 2
%define libname %mklibname gtkhtml %{api_version} %{lib_major}
%define libnamedev %mklibname -d gtkhtml %{api_version}

Summary: GtkHTML 2
Name: %{pkgname}%{api_version}
Version: 2.11.1
Release: %mkrel 2
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{pkgname}/%{pkgname}-%{version}.tar.bz2

License: LGPL
Url: http://www.gnome.org/
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: gail-devel >= %{req_gail_version}
BuildRequires: gnome-vfs2-devel
BuildRequires: libsm-devel

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
Provides:	gtkhtml2-devel = %version-%release
Requires:	%{libname} = %{version}-%{release}
Requires:	gail-devel
Requires:	gnome-vfs2-devel
Obsoletes: %mklibname -d gtkhtml %{api_version} %{lib_major}

%description -n %{libnamedev}
GtkHTML2 development files

%prep
%setup -q -n %{pkgname}-%{version}

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{libname}
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{libname}
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgtkhtml-%{api_version}.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*


