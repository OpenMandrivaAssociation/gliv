%define name	gliv
%define version	1.9.6
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	OpenGL image viewer
Version: 	%{version}
Release: 	%{release}

Source:		http://guichaz.free.fr/gliv/%{name}-%{version}.tar.bz2
URL:		http://guichaz.free.fr/gliv/
License:	GPL
Group:		Graphics
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig X11-devel libgtkglext-devel libgtk+2.0-devel gettext
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

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=graphics_section
Name=GLiv
Comment=OpenGL graphics viewer
Categories=Graphics;Viewer;
EOF

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
%_mandir/man1/*
%{_datadir}/applications/mandriva-%name.desktop
#%_datadir/pixmaps/*
%{_datadir}/applications/*

