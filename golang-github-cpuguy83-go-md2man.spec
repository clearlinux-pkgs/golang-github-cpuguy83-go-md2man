#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-cpuguy83-go-md2man
Version  : 2.0.1
Release  : 45
URL      : https://github.com/cpuguy83/go-md2man/archive/v2.0.1/go-md2man-2.0.1.tar.gz
Source0  : https://github.com/cpuguy83/go-md2man/archive/v2.0.1/go-md2man-2.0.1.tar.gz
Summary  : Markdown to man page converter
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: golang-github-cpuguy83-go-md2man-bin = %{version}-%{release}
Requires: golang-github-cpuguy83-go-md2man-license = %{version}-%{release}
Requires: golang-github-cpuguy83-go-md2man-man = %{version}-%{release}
BuildRequires : buildreq-golang
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Converts markdown into roff (man pages). Uses blackfriday to process markdown
into man pages.

%package bin
Summary: bin components for the golang-github-cpuguy83-go-md2man package.
Group: Binaries
Requires: golang-github-cpuguy83-go-md2man-license = %{version}-%{release}

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
%setup -q -n go-md2man-2.0.1
cd %{_builddir}/go-md2man-2.0.1

%build
## build_prepend content
export BUILD_FLAGS="-mod vendor"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626999080
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
## make_prepend content
export GO111MODULE="auto"
## make_prepend end
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1626999080
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/golang-github-cpuguy83-go-md2man
cp %{_builddir}/go-md2man-2.0.1/LICENSE.md %{buildroot}/usr/share/package-licenses/golang-github-cpuguy83-go-md2man/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/go-md2man-2.0.1/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/golang-github-cpuguy83-go-md2man/da34754c05d40ff81f91de8c1b85ea6e5503e21d
true
## install_append content
install -d -m0755 %{buildroot}/usr/bin
install -m0755 ./bin/go-md2man %{buildroot}/usr/bin/
./bin/go-md2man -in go-md2man.1.md -out go-md2man.1
install -d -m0755 %{buildroot}/usr/share/man/man1
install -m0644 go-md2man.1 %{buildroot}/usr/share/man/man1/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/go-md2man

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/golang-github-cpuguy83-go-md2man/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/golang-github-cpuguy83-go-md2man/da34754c05d40ff81f91de8c1b85ea6e5503e21d

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/go-md2man.1
