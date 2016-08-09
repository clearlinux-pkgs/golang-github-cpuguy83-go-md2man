#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-cpuguy83-go-md2man
Version  : 1.0.5
Release  : 2
URL      : https://github.com/cpuguy83/go-md2man/archive/v1.0.5.tar.gz
Source0  : https://github.com/cpuguy83/go-md2man/archive/v1.0.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : go
BuildRequires : golang-github-russross-blackfriday

%description
go-md2man
=========
** Work in Progress **
This still needs a lot of help to be complete, or even usable!

%prep
%setup -q -n go-md2man-1.0.5

%build
export LANG=C

%install
gopath="/usr/lib/golang"
library_path="github.com/cpuguy83/go-md2man"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done


%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/cpuguy83/go-md2man/md2man.go
/usr/lib/golang/src/github.com/cpuguy83/go-md2man/md2man/md2man.go
/usr/lib/golang/src/github.com/cpuguy83/go-md2man/md2man/roff.go
