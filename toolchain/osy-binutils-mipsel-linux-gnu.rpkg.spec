Name: osy-binutils-mipsel-linux-gnu
Version: 2.27
Release: 1%{?dist}
Summary: Cross-build binary utilities for mipsel-linux-gnu.

License: GPL
URL: https://sourceware.org/binutils
Source: ftp://ftp.gnu.org/gnu/binutils/binutils-2.27.tar.bz2

%description
Light-weight computer simulator based on MIPS R4000.


%global debug_package %{nil}

%prep
tar xjf $RPM_SOURCE_DIR/binutils-2.27.tar.bz2

%build
cd binutils-2.27
%configure --target=mipsel-linux-gnu --program-prefix=mipsel-linux-gnu --disable-nls --disable-werror
%make_build all

%install
cd binutils-2.27
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT

%files
/usr/bin/mipsel-linux-gnu-addr2line
/usr/bin/mipsel-linux-gnu-ar
/usr/bin/mipsel-linux-gnu-as
/usr/bin/mipsel-linux-gnu-c++filt
/usr/bin/mipsel-linux-gnu-elfedit
/usr/bin/mipsel-linux-gnu-gprof
/usr/bin/mipsel-linux-gnu-ld
/usr/bin/mipsel-linux-gnu-ld.bfd
/usr/bin/mipsel-linux-gnu-nm
/usr/bin/mipsel-linux-gnu-objcopy
/usr/bin/mipsel-linux-gnu-objdump
/usr/bin/mipsel-linux-gnu-ranlib
/usr/bin/mipsel-linux-gnu-readelf
/usr/bin/mipsel-linux-gnu-size
/usr/bin/mipsel-linux-gnu-strings
/usr/bin/mipsel-linux-gnu-strip
/usr/mipsel-linux-gnu/bin/ar
/usr/mipsel-linux-gnu/bin/as
/usr/mipsel-linux-gnu/bin/ld
/usr/mipsel-linux-gnu/bin/ld.bfd
/usr/mipsel-linux-gnu/bin/nm
/usr/mipsel-linux-gnu/bin/objcopy
/usr/mipsel-linux-gnu/bin/objdump
/usr/mipsel-linux-gnu/bin/ranlib
/usr/mipsel-linux-gnu/bin/readelf
/usr/mipsel-linux-gnu/bin/strip
/usr/mipsel-linux-gnu/sys-root/
/usr/share/man/man1/mipsel-linux-gnu-addr2line.1.gz
/usr/share/man/man1/mipsel-linux-gnu-ar.1.gz
/usr/share/man/man1/mipsel-linux-gnu-as.1.gz
/usr/share/man/man1/mipsel-linux-gnu-c++filt.1.gz
/usr/share/man/man1/mipsel-linux-gnu-dlltool.1.gz
/usr/share/man/man1/mipsel-linux-gnu-elfedit.1.gz
/usr/share/man/man1/mipsel-linux-gnu-gprof.1.gz
/usr/share/man/man1/mipsel-linux-gnu-ld.1.gz
/usr/share/man/man1/mipsel-linux-gnu-ld.bfd.1.gz
/usr/share/man/man1/mipsel-linux-gnu-nlmconv.1.gz
/usr/share/man/man1/mipsel-linux-gnu-nm.1.gz
/usr/share/man/man1/mipsel-linux-gnu-objcopy.1.gz
/usr/share/man/man1/mipsel-linux-gnu-objdump.1.gz
/usr/share/man/man1/mipsel-linux-gnu-ranlib.1.gz
/usr/share/man/man1/mipsel-linux-gnu-readelf.1.gz
/usr/share/man/man1/mipsel-linux-gnu-size.1.gz
/usr/share/man/man1/mipsel-linux-gnu-strings.1.gz
/usr/share/man/man1/mipsel-linux-gnu-strip.1.gz
/usr/share/man/man1/mipsel-linux-gnu-windmc.1.gz
/usr/share/man/man1/mipsel-linux-gnu-windres.1.gz

%changelog
