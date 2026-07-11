%global tl_name pdftosrc
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Extract source file or stream from PDF file
Group:		Publishing
URL:		https://www.ctan.org/pkg/pdftosrc
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftosrc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftosrc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pdftosrc.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Extracts an embedded source file, or extracts and uncompresses a PDF
stream given by object number. Developed as part of the pdfTeX source
tree.

