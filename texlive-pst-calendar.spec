Name:		texlive-pst-calendar
Version:	60480
Release:	2
Summary:	Plot calendars in "fancy" ways
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-calendar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calendar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calendar.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The pst-calendar package uses pstricks and pst-3d to draw
tabular calendars, or calendars on dodecahedra with a month to
each face (the package also requires the multido and pst-xkey
packages). The package works for years 2000-2099, and has
options for calendars in French German and English, but the
documentation is not available in English.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-calendar
%doc %{_texmfdistdir}/doc/latex/pst-calendar

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
