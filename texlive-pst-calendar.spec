%global tl_name pst-calendar
%global tl_revision 60480

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.48
Release:	%{tl_revision}.1
Summary:	Plot calendars in fancy ways
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-calendar
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calendar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calendar.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses pstricks and pst-3d to draw tabular calendars, or
calendars on dodecahedra with a month to each face (the package also
requires the multido and pst-xkey packages). The package works for years
2000-2099, and has options for calendars in French German and English,
but the documentation is not available in English.

