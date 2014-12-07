# revision 33287
# category Package
# catalog-ctan /macros/latex/contrib/animate
# catalog-date 2014-03-25 20:37:10 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-animate
Version:	20140325
Release:	3
Summary:	Create PDF animations from graphics files and inline graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/animate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/animate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/animate.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an interface to create portable,
JavaScript driven PDF animations from sets of graphics files or
from inline graphics, such as LaTeX picture environment,
PSTricks or pgf/TikZ generated pictures, or just from typeset
text.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/animate/animate.sty
%{_texmfdistdir}/tex/latex/animate/animfp.sty
%doc %{_texmfdistdir}/doc/latex/animate/ChangeLog
%doc %{_texmfdistdir}/doc/latex/animate/README
%doc %{_texmfdistdir}/doc/latex/animate/animate.pdf
%doc %{_texmfdistdir}/doc/latex/animate/animate.tex
%doc %{_texmfdistdir}/doc/latex/animate/files/bye_0.eps
%doc %{_texmfdistdir}/doc/latex/animate/files/bye_1.eps
%doc %{_texmfdistdir}/doc/latex/animate/files/bye_2.eps
%doc %{_texmfdistdir}/doc/latex/animate/files/bye_3.eps
%doc %{_texmfdistdir}/doc/latex/animate/files/click.mp3
%doc %{_texmfdistdir}/doc/latex/animate/files/exp.mp
%doc %{_texmfdistdir}/doc/latex/animate/files/mailto.eps
%doc %{_texmfdistdir}/doc/latex/animate/files/pstmetronome.tex
%doc %{_texmfdistdir}/doc/latex/animate/files/scarab.mp

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
