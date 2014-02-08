# revision 25205
# category Package
# catalog-ctan /support/installfont
# catalog-date 2012-01-26 12:26:54 +0100
# catalog-license lppl
# catalog-version v1.6b
Name:		texlive-installfont
Version:	v1.6b
Release:	3
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


%changelog
* Wed Feb 01 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.6b-2
+ Revision: 770348
- Correct provides of installfont.bin

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.6b-1
+ Revision: 770187
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.6-2
+ Revision: 752797
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.6-1
+ Revision: 718723
- texlive-installfont
- texlive-installfont
- texlive-installfont
- texlive-installfont

