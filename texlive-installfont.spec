%global tl_name installfont
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	A bash script for installing a LaTeX font family
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/installfont
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/installfont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/installfont.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(installfont.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
With this script you can install a LaTeX font family (PostScript Type 1,
TrueType and OpenType formats are supported). Font series from light to
ultra bold, and (faked) small caps and (faked) slanted shapes are
supported, but not expert fonts. The script will rename the fonts
automatically (optional) or will otherwise expect the *.afm files and
the font files (in PostScript Type1 format) named in the Karl Berry
scheme (e.g. 5bbr8a.pfb). After running the script, you should have a
working font installation in your local TeX tree.

