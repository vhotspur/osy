Name: MSIM
Version: 1.3.8.5
Release: 1%{?dist}
Summary: Light-weight computer simulator based on MIPS R4000.

License: GPL
URL: http://d3s.mff.cuni.cz/~holub/sw/msim/

Source: https://yankee.ms.mff.cuni.cz/msim-1.3.8.5.tar.bz2

Requires: readline

%description
Light-weight computer simulator based on MIPS R4000.


%global debug_package %{nil}

%prep
{{{ git_setup_macro }}}

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
usr/bin/msim
usr/share/doc/msim-1.3.8.5/reference.html
usr/share/doc/msim-1.3.8.5/default.css

%changelog
