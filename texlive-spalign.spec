Name:		texlive-spalign
Version:	42225
Release:	1
Summary:	Typeset matrices and arrays with spaces and semicolons as delimiters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spalign
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spalign.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spalign.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spalign.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Typeset matrices and arrays with spaces and semicolons as
delimiters. The purpose of this package is to decrease the
number of keystrokes needed to typeset small amounts of aligned
material (matrices, arrays, etc.). It provides a facility for
typing alignment environments and macros with spaces as the
alignment delimiter and semicolons (by default) as the
end-of-row indicator. For instance, typeset a matrix using
\spalignmat{1 12 -3; 24 -2 2; 0 0 1}, or a vector using
\spalignvector{22 \frac{1}{2} -14}. This package also contains
utility macros for typesetting augmented matrices, vectors,
arrays, systems of equations, and more, and is easily
extendable to other situations that use alignments. People who
have to typeset a large number of matrices (like linear algebra
teachers) should find this package to be a real time saver.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/spalign
%{_texmfdistdir}/tex/latex/spalign
%doc %{_texmfdistdir}/doc/latex/spalign

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
