Name: 	 	gliv
Summary: 	OpenGL image viewer
Version: 	1.9.7
Release: 	5

Source:		http://guichaz.free.fr/gliv/files/%{name}-%{version}.tar.bz2
Patch0:		gliv-1.9.7-fix-link.patch
URL:		https://guichaz.free.fr/gliv/
License:	GPL
Group:		Graphics
BuildRequires:	mesaglu-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
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
export LDFLAGS="-lm"
autoreconf -fi
%configure2_5x
%make
										
%install
%makeinstall

%find_lang %name

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


%changelog
* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 1.9.7-1mdv2011.0
+ Revision: 624828
- new version 1.9.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.9.6-3mdv2009.0
+ Revision: 246202
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Mar 03 2008 Austin Acton <austin@mandriva.org> 1.9.6-1mdv2008.1
+ Revision: 177842
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - auto-convert XDG menu entry
    - do not compile on gliv
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - use %%mkrel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Mar 20 2006 Austin Acton <austin@mandriva.org> 1.9.5-1mdk
- New release 1.9.5

* Thu Nov 17 2005 Lenny Cartier <lenny@mandriva.com> 1.9.4-1mdk
- 1.9.4

* Wed Aug 24 2005 Austin Acton <austin@mandriva.org> 1.9.3-1mdk
- 1.9.3
- source URL
- configure 2.5

* Thu Jan 06 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.9.1-1mdk
- 1.9.1

* Thu Aug 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.8.4-1mdk
- 1.8.4

* Fri Jun 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.8.3-1mdk
- 1.8.3

* Fri Apr 04 2003 Austin Acton <aacton@yorku.ca> 1.7.1-1mdk
- initial package

