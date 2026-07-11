%global tl_name animate
%global tl_revision 72548

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Create PDF and SVG animations from graphics files and inline graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/animate
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/animate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/animate.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/animate.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an interface to create portable, JavaScript driven
PDF and SVG animations from sets of graphics files or from inline
graphics, such as LaTeX picture environment, PSTricks or pgf/TikZ
generated pictures, or just from typeset text.

