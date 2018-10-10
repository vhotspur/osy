Name: osy-gcc-mipsel-linux-gnu
Version: 8.2.0
Release: 1%{?dist}
Summary: Cross-build GCC for mipsel-linux-gnu.

License: GPL
URL: http://gcc.gnu.org
Source: https://ftpmirror.gnu.org/gcc/gcc-8.2.0/gcc-8.2.0.tar.gz

Requires: gmp
Requires: isl
Requires: libmpc
BuildRequires: gmp-devel
BuildRequires: isl-devel
BuildRequires: libmpc-devel
BuildRequires: gcc-c++

%description
Cross-build GCC for mipsel-linux-gnu.


%global debug_package %{nil}

%prep
tar xzf $RPM_SOURCE_DIR/gcc-8.2.0.tar.gz

%build
mkdir build
cd build
../gcc-8.2.0/configure \
    --prefix=/usr \
    --target=mipsel-linux-gnu --program-prefix=mipsel-linux-gnu- \
    --with-gnu-as --with-gnu-ld --disable-nls --disable-threads \
    --enable-languages=c,c++ \
    --disable-multilib --disable-libgcj --without-headers \
    --disable-shared --enable-lto --disable-werror
%make_build all-gcc

%install
cd build
rm -rf $RPM_BUILD_ROOT
make install-gcc DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/share/man
rm -rf $RPM_BUILD_ROOT/usr/share/info
find $RPM_BUILD_ROOT/

%files
/usr/bin/mipsel-linux-gnu-gcc-nm
/usr/bin/mipsel-linux-gnu-gcc-ranlib
/usr/bin/mipsel-linux-gnu-gcov-tool
/usr/bin/mipsel-linux-gnu-cpp
/usr/bin/mipsel-linux-gnu-gcc-ar
/usr/bin/mipsel-linux-gnu-g++
/usr/bin/mipsel-linux-gnu-c++
/usr/bin/mipsel-linux-gnu-gcc
/usr/bin/mipsel-linux-gnu-gcc-8.2.0
/usr/bin/mipsel-linux-gnu-gcov
/usr/bin/mipsel-linux-gnu-gcov-dump
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/

%changelog
