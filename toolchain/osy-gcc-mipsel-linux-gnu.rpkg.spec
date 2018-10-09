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
tar xzf $RPM_SOURCE_DIR/gcc-6.2.0.tar.gz

%build
mkdir build
cd build
../gcc-8.2.0/%configure \
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
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/liblto_plugin.la
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/plugin/gengtype
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/lto-wrapper
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/install-tools/mkinstalldirs
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/install-tools/fixincl
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/install-tools/fixinc.sh
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/install-tools/mkheaders
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/collect2
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/cc1plus
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/lto1
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/liblto_plugin.so.0.0.0
/usr/libexec/gcc/mipsel-linux-gnu/8.2.0/cc1
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/gtype.state
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/opts-diagnostic.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/addresses.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-dump.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimplify-me.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/attribs.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-coalesce.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/stringpool.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dwarf2asm.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gcov-io.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ansidecl.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/insn-addr.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-cfgcleanup.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/safe-ctype.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cpplib.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dbxout.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/debug.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/wide-int-print.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gtype-desc.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-builder.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/filenames.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/brig-builtins.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/optabs-tree.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/lto-streamer.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-phinodes.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfghooks.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/xcoff.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/rtlhooks-def.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/glimits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-scalar-evolution.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/rtx-vector-builder.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-expr.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/profile.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/streamer-hooks.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-address.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/objc/objc-tree.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/file-prefix-map.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-prop.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfgcleanup.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/chkp-builtins.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-iterator.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gcse-common.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/options.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-affine.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/xcoffout.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfg.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/bb-reorder.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/omp-general.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gcc.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/omp-grid.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ubsan.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-live.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/diagnostic-core.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-nested.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/typed-splay-tree.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/timevar.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/auto-host.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ira.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cppbuiltin.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sched-int.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/wide-int-bitmask.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/insn-modes-inline.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/value-prof.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gstab.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/collect2.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-stdarg.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/substring-locations.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-check.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sel-sched.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/read-rtl-function.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/coverage.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dominance.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/diagnostic-color.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-param-manipulation.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sbitmap.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/memory-block.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/vec-perm-indices.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gsyms.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/output.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hw-doloop.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/is-a.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/flags.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-reference.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-icf-gimple.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gtm-builtins.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/basic-block.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/int-vector-builder.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-dfa.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hard-reg-set.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ifcvt.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/optabs-libfuncs.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gcc-plugin.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/spellcheck.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/symbol-summary.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/diagnostic.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfgexpand.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gcse.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/graphite.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/calls.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-outof-ssa.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/intl.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hash-table.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-strlen.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/wide-int.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-eh.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/predict.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-iterator.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-walk.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/context.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/libiberty.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-sccvn.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-object-size.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dwarf2out.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-vrp.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hsa-builtins.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/read-md.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/omp-offload.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/statistics.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sreal.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gsstruct.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-icf.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/regcprop.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-dom.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/stmt.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/selftest-rtl.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/omp-expand.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/builtins.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/params-options.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-ssa.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ccmp.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/params-enum.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dbgcnt.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/auto-profile.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-loop-manip.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-diagnostic.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/fibonacci_heap.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/rtl-chkp.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/fixed-value.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/configargs.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sparseset.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/lto-compress.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/realmpfr.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/lto-section-names.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cselib.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/lra.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gcov-counter.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/pass-instances.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gensupport.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/domwalk.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/internal-fn.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-inline.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-low.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/plugin-version.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hash-set.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/poly-int-types.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/optabs.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/all-tree.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/pass_manager.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hsa-common.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/lower-subreg.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-threadupdate.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/target-def.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/inchash.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-threadedge.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/c-tree.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-pass.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/target.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/langhooks.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/rtl.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/except.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-chrec.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/signop.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/optabs-query.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/bitmap.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ggc.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/b-header-vars
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/treestruct.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-chkp.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/passes.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-vectorizer.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gengtype.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tm-preds.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/alias.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/stab.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-propagate.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/params.list
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/system.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/print-rtl.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/predict.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/profile-count.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/expr.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-vector-builder.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/insn-flags.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/params.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/builtins.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/c-family/c-objc.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/c-family/c-pretty-print.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/c-family/c-pragma.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/c-family/c-common.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/c-family/c-common.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/generic-match.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/mem-stats-traits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-utils.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/spellcheck-tree.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/graphds.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-cfg.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfganal.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/regrename.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/toplev.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ssa.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/md5.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-predicate.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cif-code.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/fold-const-call.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/pretty-print.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/graph.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/rtlhash.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/plugin-api.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/vtable-verify.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/rtl.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/mem-stats.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfgloopmanip.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/regs.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ada/gcc-interface/ada-tree.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-alias.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hash-traits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/diagnostic.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/incpath.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfgloop.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/omp-builtins.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/defaults.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfgbuild.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/conditions.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/insn-notes.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/file-find.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ssa-iterators.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-scopedtables.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/poly-int.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tm_p.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/langhooks-def.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/errors.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-data-ref.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cgraph.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/rtl-error.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-parloops.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/target.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-pretty-print.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-predict.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tracer.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-chkp.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gcc-symtab.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-hasher.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/selftest.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/stor-layout.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-if-conv.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-inline.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/trans-mem.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-pretty-print.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/coretypes.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/builtin-types.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ddg.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/mode-classes.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gsyslimits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/run-rtl-passes.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/shrink-wrap.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-dce.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/opts.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-loop-niter.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/highlev-plugin-common.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/limity.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/bversion.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/print-tree.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tsystem.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/collect-utils.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tsan.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ggc-internal.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/params.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/vr-values.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-ref.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cp/cp-tree.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cp/type-utils.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cp/name-lookup.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cp/cxx-pretty-print.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cp/operators.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cp/cp-tree.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-streamer.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/double-int.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sanitizer.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hosthooks.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dbgcnt.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/version.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/splay-tree.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/df.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hashtab.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dfp.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-ter.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/line-map.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/rtl-iter.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/builtin-attrs.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssanames.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-core.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/selftest-diagnostic.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-hash-traits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/libfuncs.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/genrtl.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/lcm.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/params-list.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-streamer.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/recog.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/loop-unroll.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/plugin.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-ccp.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/vector-builder.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/omp-low.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/input.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/collect2-aix.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hooks.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/typeclass.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfgrtl.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/target-insns.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hwint.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/machmode.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/convert.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/flag-types.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sel-sched-dump.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-operands.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-match.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/prefix.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-ssa-warn-restrict.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-loop-ivopts.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/asan.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa-loop.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/memmodel.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/regset.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ipa-fnsummary.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/real.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/vec.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dce.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/target-globals.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/internal-fn.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/gnu-user.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/linux-android.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/dbxelf.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/elfos.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/linux.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/initfini-array.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/mips/mips-opts.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/mips/gnu-user.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/mips/mips.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/mips/mips-protos.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/mips/linux.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/mips/linux-common.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/glibc-stdint.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/linux-protos.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/config/vxworks-dummy.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sync-builtins.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/edit-context.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/timevar.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/insn-constants.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/varasm.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/fold-const.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-ssa.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/emit-rtl.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sese.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/sel-sched-ir.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/et-forest.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hash-map-traits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/lra-int.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/insn-modes.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gcc-rich-location.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/symtab.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/targhooks.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/color-macros.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/plugin.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/reload.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-fold.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/expmed.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dojump.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/vmsdbg.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cppdefault.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/alloc-pool.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/valtrack.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/insn-codes.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hsa-brig-format.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/dumpfile.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/resource.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/optabs.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/machmode.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/obstack.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/limitx.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/reg-notes.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/omp-simd-clone.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/data-streamer.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/backend.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/ira-int.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/cfg-flags.def
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/function.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimple-ssa-evrp-analyze.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/target-hooks-macros.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tree-into-ssa.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/gimplify.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hosthooks-def.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/explow.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/tm.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/plugin/include/hash-map.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include-fixed/limits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include-fixed/syslimits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include-fixed/README
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/install-tools/macro_list
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/install-tools/fixinc_list
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/install-tools/gsyslimits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/install-tools/mkheaders.conf
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/install-tools/include/limits.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/install-tools/include/README
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/stdarg.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/stdatomic.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/float.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/msa.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/iso646.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/stdint.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/varargs.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/stddef.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/stdfix.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/stdbool.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/stdalign.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/stdnoreturn.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/stdint-gcc.h
/usr/lib/gcc/mipsel-linux-gnu/8.2.0/include/loongson.h

%changelog
