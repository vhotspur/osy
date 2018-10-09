Name: osy-binutils-mipsel-linux-gnu
Version: 2.27
Release: 1%{?dist}
Summary: Cross-build binary utilities for mipsel-linux-gnu.

License: GPL
URL: https://sourceware.org/binutils
Source: https://ftpmirror.gnu.org/binutils/binutils-2.27.tar.bz2

%description
Cross-build binary utilities for mipsel-linux-gnu.


%global debug_package %{nil}

%prep
tar xjf $RPM_SOURCE_DIR/binutils-2.27.tar.bz2

%build
cd binutils-2.27
%configure --target=mipsel-linux-gnu --program-prefix=mipsel-linux-gnu- --disable-nls --disable-werror
%make_build all

%install
cd binutils-2.27
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/usr/share/man
rm -rf $RPM_BUILD_ROOT/usr/share/info
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
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xw
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xu
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xsw
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xsc
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xs
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xr
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xn
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xdw
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xdc
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xd
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xc
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.xbn
/usr/mipsel-linux-gnu/lib/ldscripts/elf64ltsmip.x
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xw
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xu
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xsw
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xsc
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xs
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xr
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xn
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xdw
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xdc
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xd
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xc
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.xbn
/usr/mipsel-linux-gnu/lib/ldscripts/elf64btsmip.x
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xu
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xsw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xsc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xs
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xr
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xn
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xdw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xdc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xd
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.xbn
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmipn32.x
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xu
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xsw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xsc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xs
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xr
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xn
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xdw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xdc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xd
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.xbn
/usr/mipsel-linux-gnu/lib/ldscripts/elf32ltsmip.x
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xu
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xsw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xsc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xs
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xr
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xn
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xdw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xdc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xd
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.xbn
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmipn32.x
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xu
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xsw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xsc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xs
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xr
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xn
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xdw
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xdc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xd
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xc
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.xbn
/usr/mipsel-linux-gnu/lib/ldscripts/elf32btsmip.x

%changelog
