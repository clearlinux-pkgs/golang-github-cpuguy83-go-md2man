#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-cpuguy83-go-md2man
Version  : 1.0.8
Release  : 15
URL      : https://github.com/cpuguy83/go-md2man/archive/v1.0.8.tar.gz
Source0  : https://github.com/cpuguy83/go-md2man/archive/v1.0.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: golang-github-cpuguy83-go-md2man-bin = %{version}-%{release}
Requires: golang-github-cpuguy83-go-md2man-license = %{version}-%{release}
Requires: golang-github-cpuguy83-go-md2man-man = %{version}-%{release}
BuildRequires : buildreq-golang
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Rework-directory-structure-to-build-from-tar.patch

%description
go-md2man
=========
** Work in Progress **
This still needs a lot of help to be complete, or even usable!

%package bin
Summary: bin components for the golang-github-cpuguy83-go-md2man package.
Group: Binaries
Requires: golang-github-cpuguy83-go-md2man-license = %{version}-%{release}
Requires: golang-github-cpuguy83-go-md2man-man = %{version}-%{release}

%description bin
bin components for the golang-github-cpuguy83-go-md2man package.


%package license
Summary: license components for the golang-github-cpuguy83-go-md2man package.
Group: Default

%description license
license components for the golang-github-cpuguy83-go-md2man package.


%package man
Summary: man components for the golang-github-cpuguy83-go-md2man package.
Group: Default

%description man
man components for the golang-github-cpuguy83-go-md2man package.


%prep
%setup -q -n go-md2man-1.0.8
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export GOPATH="$PWD"
go build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/golang-github-cpuguy83-go-md2man
cp LICENSE.md %{buildroot}/usr/share/package-licenses/golang-github-cpuguy83-go-md2man/LICENSE.md
cp vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/golang-github-cpuguy83-go-md2man/vendor_github.com_russross_blackfriday_LICENSE.txt

## install_append content
install -d -m0755 %{buildroot}/usr/bin
install -m0755 go-md2man-1.0.8 %{buildroot}/usr/bin/go-md2man
./go-md2man-1.0.8 -in go-md2man.1.md -out go-md2man.1
install -d -m0755 %{buildroot}/usr/share/man/man1
install -m0644 go-md2man.1 %{buildroot}/usr/share/man/man1/go-md2man.1
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/go-md2man

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/golang-github-cpuguy83-go-md2man/LICENSE.md
/usr/share/package-licenses/golang-github-cpuguy83-go-md2man/vendor_github.com_russross_blackfriday_LICENSE.txt

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/go-md2man.1
