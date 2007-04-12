%define req_gail_version 1.3
%define pkgname libgtkhtml
%define lib_major 0
%define api_version 2
%define lib_name %mklibname gtkhtml %{api_version} %{lib_major}

Summary: GtkHTML 2
Name: %{pkgname}%{api_version}
Version: 2.11.0
Release: %mkrel 3
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

%package -n %{lib_name}
Summary:	%{summary}
Group:		%{group}

%description -n %{lib_name}
GtkHTML 2 shared library

%package -n %{lib_name}-devel
Summary:	Static libraries, include files for GtkHTML2
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	gtkhtml2-devel = %version-%release
Requires:	%{lib_name} = %{version}-%{release}
Requires:	gail-devel
Requires:	gnome-vfs2-devel

%description -n %{lib_name}-devel
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

%post -p /sbin/ldconfig -n %{lib_name}

%postun -p /sbin/ldconfig -n %{lib_name}

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*


