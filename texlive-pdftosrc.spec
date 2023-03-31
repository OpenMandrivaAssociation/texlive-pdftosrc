Name:		texlive-pdftosrc
Version:	62387
Release:	2
Summary:	Extract source file or stream from PDF file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdftosrc
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftosrc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftosrc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Extracts an embedded source file, or extracts and uncompresses
a PDF stream given by object number. Developed as part of the
pdfTeX source tree.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdftosrc.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdftosrc.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
