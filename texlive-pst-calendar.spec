# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-calendar
# catalog-date 2009-03-30 10:35:07 +0200
# catalog-license lppl
# catalog-version 0.47
Name:		texlive-pst-calendar
Version:	0.47
Release:	1
Summary:	Plot calendars in "fancy" ways
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-calendar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calendar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-calendar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The pst-calendar package uses pstricks and pst-3d to draw
tabular calendars, or calendars on dodecahedra with a month to
each face (the package also requires the multido and pst-xkey
packages). The package works for years 2000-2099, and has
options for calendars in French German and English, but the
documentation is not available in English.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
