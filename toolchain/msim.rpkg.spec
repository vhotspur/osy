Name: msim
Version: 1.3.8.5
Release: 1%{?dist}
Summary: Light-weight computer simulator based on MIPS R4000.

License: GPL
URL: http://d3s.mff.cuni.cz/~holub/sw/msim/
Source: http://d3s.mff.cuni.cz/~holub/sw/msim/msim-1.3.8.5.tar.bz2

Requires: readline
BuildRequires: imake
BuildRequires: readline-devel

%description
Light-weight computer simulator based on MIPS R4000.


%global debug_package %{nil}

%prep
tar xjf $RPM_SOURCE_DIR/msim-1.3.8.5.tar.bz2

%build
cd msim-1.3.8.5
%configure
%make_build

%install
cd msim-1.3.8.5
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
/usr/bin/msim

%changelog
