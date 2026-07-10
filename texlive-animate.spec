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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an interface to create portable, JavaScript driven
PDF and SVG animations from sets of graphics files or from inline
graphics, such as LaTeX picture environment, PSTricks or pgf/TikZ
generated pictures, or just from typeset text.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/animate
%dir %{_datadir}/texmf-dist/source/latex/animate
%dir %{_datadir}/texmf-dist/tex/latex/animate
%dir %{_datadir}/texmf-dist/source/latex/animate/files
%doc %{_datadir}/texmf-dist/doc/latex/animate/ChangeLog
%doc %{_datadir}/texmf-dist/doc/latex/animate/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/animate/animate.pdf
%doc %{_datadir}/texmf-dist/source/latex/animate/animate.tex
%doc %{_datadir}/texmf-dist/source/latex/animate/files/bye_0.eps
%doc %{_datadir}/texmf-dist/source/latex/animate/files/bye_1.eps
%doc %{_datadir}/texmf-dist/source/latex/animate/files/bye_2.eps
%doc %{_datadir}/texmf-dist/source/latex/animate/files/bye_3.eps
%doc %{_datadir}/texmf-dist/source/latex/animate/files/click.mp3
%doc %{_datadir}/texmf-dist/source/latex/animate/files/exp.mp
%doc %{_datadir}/texmf-dist/source/latex/animate/files/pstmetronome.tex
%doc %{_datadir}/texmf-dist/source/latex/animate/files/scarab.mp
%{_datadir}/texmf-dist/tex/latex/animate/animate.sty
