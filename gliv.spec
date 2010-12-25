%define name	gliv
%define version	1.9.7
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	OpenGL image viewer
Version: 	%{version}
Release: 	%{release}

Source:		http://guichaz.free.fr/gliv/files/%{name}-%{version}.tar.bz2
Patch0:		gliv-1.9.7-fix-link.patch
URL:		http://guichaz.free.fr/gliv/
License:	GPL
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	mesaglu-devel
BuildRequires:	libx11-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgtkglext-devel
BuildRequires:	gettext-devel
Requires:	imagemagick

%description
GLiv is an OpenGL image viewer. It performs image loading via Gdk-pixbuf
(which is bundled with GTK+-2.2) and rendering with OpenGL. The graphical
user interface uses GTK+ with GtkGLExt. If Gdk-pixbuf cannot load your image,
it uses ImageMagick to convert it to PNG. GLiv is very fast and smooth at
rotating, panning, and zooming if you have an OpenGL accelerated graphics
board.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING THANKS
%{_bindir}/%name
%lang(de) %{_mandir}/de/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%{_datadir}/pixmaps/gliv.png
%_mandir/man1/*
%{_datadir}/applications/*
