# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-calendar
# catalog-date 2009-03-30 10:35:07 +0200
# catalog-license lppl
# catalog-version 0.47
Name:		texlive-pst-calendar
Version:	0.47
Release:	4
Summary:	Plot calendars in "fancy" ways
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-calendar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calendar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calendar.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/pst-calendar/pst-calendar.sty
%doc %{_texmfdistdir}/doc/latex/pst-calendar/Changes
%doc %{_texmfdistdir}/doc/latex/pst-calendar/README
%doc %{_texmfdistdir}/doc/latex/pst-calendar/pst-calendar-docDE.ltx
%doc %{_texmfdistdir}/doc/latex/pst-calendar/pst-calendar-docDE.pdf
%doc %{_texmfdistdir}/doc/latex/pst-calendar/pst-calendar-docDE.tex
%doc %{_texmfdistdir}/doc/latex/pst-calendar/pst-calendar-docFR.pdf
%doc %{_texmfdistdir}/doc/latex/pst-calendar/pst-calendar-docFR.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.47-2
+ Revision: 755225
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.47-1
+ Revision: 719338
- texlive-pst-calendar
- texlive-pst-calendar
- texlive-pst-calendar
- texlive-pst-calendar

