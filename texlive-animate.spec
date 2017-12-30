Name:		texlive-animate
Version:	20170930
Release:	1
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
%{_texmfdistdir}/tex/latex/animate
%doc %{_texmfdistdir}/doc/latex/animate

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
