#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmake
Version  : 3.1.3
Release  : 15
URL      : http://www.cmake.org/files/v3.1/cmake-3.1.3.tar.gz
Source0  : http://www.cmake.org/files/v3.1/cmake-3.1.3.tar.gz
Summary  : General purpose data compression library
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause GPL-2.0 ICU MIT Zlib bzip2-1.0.5
Requires: cmake-bin
Requires: cmake-data
BuildRequires : cmake
Patch1: build.patch

%description
To create a cmake release, make sure the "release" tag is pointing to the
expected git commit:

%package bin
Summary: bin components for the cmake package.
Group: Binaries
Requires: cmake-data

%description bin
bin components for the cmake package.


%package data
Summary: data components for the cmake package.
Group: Data

%description data
data components for the cmake package.


%package dev
Summary: dev components for the cmake package.
Group: Development
Requires: cmake-bin
Requires: cmake-data

%description dev
dev components for the cmake package.


%prep
%setup -q -n cmake-3.1.3
%patch1 -p1

%build
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir}
make V=1  %{?_smp_mflags}
popd

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd clr-build ; make test ||: ; popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/doc/cmake-3.1/Copyright.txt
/usr/doc/cmake-3.1/cmcompress/Copyright.txt
/usr/doc/cmake-3.1/cmcurl/COPYING
/usr/doc/cmake-3.1/cmexpat/COPYING
/usr/doc/cmake-3.1/cmlibarchive/COPYING
/usr/doc/cmake-3.1/cmliblzma/COPYING
/usr/doc/cmake-3.1/cmsys/Copyright.txt
/usr/doc/cmake-3.1/cmzlib/Copyright.txt

%files bin
%defattr(-,root,root,-)
/usr/bin/cmake
/usr/bin/cpack
/usr/bin/ctest

%files data
%defattr(-,root,root,-)
/usr/share/cmake-3.1/*

%files dev
%defattr(-,root,root,-)
/usr/share/aclocal/*.m4
