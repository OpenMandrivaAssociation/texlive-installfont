# revision 31205
# category Package
# catalog-ctan /support/installfont
# catalog-date 2013-07-15 19:52:10 +0200
# catalog-license lppl
# catalog-version v1.7
Name:		texlive-installfont
Version:	v1.7
Release:	1
Summary:	A bash script for installing a LaTeX font family
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/installfont
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/installfont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/installfont.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-installfont.bin = %{EVRD}

%description
With this script you can install a LaTeX font family
(PostScript Type 1, TrueType and OpenType formats are
supported). Font series from light to ultra bold, and (faked)
small caps and (faked) slanted shapes are supported, but not
expert fonts. The script will rename the fonts automatically
(optional) or will otherwise expect the *.afm files and the
font files (in PostScript Type1 format) named in the Karl Berry
scheme (e.g. 5bbr8a.pfb). After running the script, you should
have a working font installation in your local TeX tree.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/installfont-tl
%{_texmfdistdir}/scripts/installfont/installfont-tl
%doc %{_texmfdistdir}/doc/support/installfont/LICENSE
%doc %{_texmfdistdir}/doc/support/installfont/README
%doc %{_texmfdistdir}/doc/support/installfont/installfont
%doc %{_texmfdistdir}/doc/support/installfont/installfont.pdf
%doc %{_texmfdistdir}/doc/support/installfont/installfont.tex
%doc %{_texmfdistdir}/doc/support/installfont/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}	 
pushd %{buildroot}%{_bindir}	 
    ln -sf %{_texmfdistdir}/scripts/installfont/installfont-tl installfont-tl
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
