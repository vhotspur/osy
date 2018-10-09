Name: osy-gcc-mipsel-linux-gnu
Version: 6.2.0
Release: 1%{?dist}
Summary: Cross-build GCC for mipsel-linux-gnu.

License: GPL
URL: http://gcc.gnu.org
Source: https://ftpmirror.gnu.org/gcc/gcc-6.2.0/gcc-6.2.0.tar.bz2

%description
Cross-build GCC for mipsel-linux-gnu.


%global debug_package %{nil}

%prep
tar xjf $RPM_SOURCE_DIR/gcc-6.2.0.tar.bz2

%build
cd gcc-6.2.0
%configure --target=mipsel-linux-gnu --program-prefix=mipsel-linux-gnu- --disable-nls --disable-werror
%make_build all

%install
cd gcc-6.2.0
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/share/man
rm -rf $RPM_BUILD_ROOT/usr/share/info
find $RPM_BUILD_ROOT

%files
/usr/bin/mipsel-linux-gnu-gcc

%changelog
