Name:		texlive-animate
Version:	20110916
Release:	1
Summary:	Create PDF animations from graphics files and inline graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/animate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/animate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/animate.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides an interface to create portable,
JavaScript driven PDF animations from sets of graphics files or
from inline graphics, such as LaTeX picture environment,
PSTricks or pgf/TikZ generated pictures, or just from typeset
text.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%doc %{_texmfdistdir}/doc/latex/animate/files/exp.mp
%doc %{_texmfdistdir}/doc/latex/animate/files/mailto.eps
%doc %{_texmfdistdir}/doc/latex/animate/files/scarab.mp
%doc %{_texmfdistdir}/doc/latex/animate/files/timeline.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}