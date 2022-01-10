#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Standard Jane Street ppx rewriters
Summary(pl.UTF-8):	Standardowe moduły przepisujące ppx Jane Street
Name:		ocaml-ppx_jane
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_jane/tags
Source0:	https://github.com/janestreet/ppx_jane/archive/v%{version}/ppx_jane-%{version}.tar.gz
# Source0-md5:	8bd0b705e790bdc8da939afab8a7f0bf
URL:		https://github.com/janestreet/ppx_jane
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-base_quickcheck-devel >= 0.14
BuildRequires:	ocaml-base_quickcheck-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_assert-devel >= 0.14
BuildRequires:	ocaml-ppx_assert-devel < 0.15
BuildRequires:	ocaml-ppx_base-devel >= 0.14
BuildRequires:	ocaml-ppx_base-devel < 0.15
BuildRequires:	ocaml-ppx_bench-devel >= 0.14
BuildRequires:	ocaml-ppx_bench-devel < 0.15
BuildRequires:	ocaml-ppx_bin_prot-devel >= 0.14
BuildRequires:	ocaml-ppx_bin_prot-devel < 0.15
BuildRequires:	ocaml-ppx_custom_printf-devel >= 0.14
BuildRequires:	ocaml-ppx_custom_printf-devel < 0.15
BuildRequires:	ocaml-ppx_expect-devel >= 0.14
BuildRequires:	ocaml-ppx_expect-devel < 0.15
BuildRequires:	ocaml-ppx_fields_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_fields_conv-devel < 0.15
BuildRequires:	ocaml-ppx_fixed_literal-devel >= 0.14
BuildRequires:	ocaml-ppx_fixed_literal-devel < 0.15
BuildRequires:	ocaml-ppx_here-devel >= 0.14
BuildRequires:	ocaml-ppx_here-devel < 0.15
BuildRequires:	ocaml-ppx_inline_test-devel >= 0.14
BuildRequires:	ocaml-ppx_inline_test-devel < 0.15
BuildRequires:	ocaml-ppx_let-devel >= 0.14
BuildRequires:	ocaml-ppx_let-devel < 0.15
BuildRequires:	ocaml-ppx_module_timer-devel >= 0.14
BuildRequires:	ocaml-ppx_module_timer-devel < 0.15
BuildRequires:	ocaml-ppx_optcomp-devel >= 0.14
BuildRequires:	ocaml-ppx_optcomp-devel < 0.15
BuildRequires:	ocaml-ppx_optional-devel >= 0.14
BuildRequires:	ocaml-ppx_optional-devel < 0.15
BuildRequires:	ocaml-ppx_pipebang-devel >= 0.14
BuildRequires:	ocaml-ppx_pipebang-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_message-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_message-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_value-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_value-devel < 0.15
BuildRequires:	ocaml-ppx_stable-devel >= 0.14
BuildRequires:	ocaml-ppx_stable-devel < 0.15
BuildRequires:	ocaml-ppx_string-devel >= 0.14
BuildRequires:	ocaml-ppx_string-devel < 0.15
BuildRequires:	ocaml-ppx_typerep_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_typerep_conv-devel < 0.15
BuildRequires:	ocaml-ppx_variants_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_variants_conv-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ppx_jane is a ppx driver including all standard ppx rewriters.

This package contains files needed to run bytecode executables using
ppx_jane library.

%description -l pl.UTF-8
ppx_jane to sterownik ppx zawierający wszystkie standardowe moduły
przepisujące ppx.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_jane.

%package devel
Summary:	Standard Jane Street ppx rewriters - development part
Summary(pl.UTF-8):	Standardowe moduły przepisujące ppx Jane Street - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-base_quickcheck-devel >= 0.14
Requires:	ocaml-ppx_assert-devel >= 0.14
Requires:	ocaml-ppx_base-devel >= 0.14
Requires:	ocaml-ppx_bench-devel >= 0.14
Requires:	ocaml-ppx_bin_prot-devel >= 0.14
Requires:	ocaml-ppx_custom_printf-devel >= 0.14
Requires:	ocaml-ppx_expect-devel >= 0.14
Requires:	ocaml-ppx_fields_conv-devel >= 0.14
Requires:	ocaml-ppx_fixed_literal-devel >= 0.14
Requires:	ocaml-ppx_here-devel >= 0.14
Requires:	ocaml-ppx_inline_test-devel >= 0.14
Requires:	ocaml-ppx_let-devel >= 0.14
Requires:	ocaml-ppx_module_timer-devel >= 0.14
Requires:	ocaml-ppx_optcomp-devel >= 0.14
Requires:	ocaml-ppx_optional-devel >= 0.14
Requires:	ocaml-ppx_pipebang-devel >= 0.14
Requires:	ocaml-ppx_sexp_message-devel >= 0.14
Requires:	ocaml-ppx_sexp_value-devel >= 0.14
Requires:	ocaml-ppx_stable-devel >= 0.14
Requires:	ocaml-ppx_string-devel >= 0.14
Requires:	ocaml-ppx_typerep_conv-devel >= 0.14
Requires:	ocaml-ppx_variants_conv-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_jane library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_jane.

%prep
%setup -q -n ppx_jane-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_jane/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_jane/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_jane

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%attr(755,root,root) %{_bindir}/ppx-jane
%dir %{_libdir}/ocaml/ppx_jane
%attr(755,root,root) %{_libdir}/ocaml/ppx_jane/ppx.exe
%{_libdir}/ocaml/ppx_jane/META
%{_libdir}/ocaml/ppx_jane/*.cma
%dir %{_libdir}/ocaml/ppx_jane/kernel
%attr(755,root,root) %{_libdir}/ocaml/ppx_jane/kernel/ppx.exe
%{_libdir}/ocaml/ppx_jane/kernel/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_jane/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_jane/kernel/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_jane/*.cmi
%{_libdir}/ocaml/ppx_jane/*.cmt
%{_libdir}/ocaml/ppx_jane/kernel/*.cmi
%{_libdir}/ocaml/ppx_jane/kernel/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_jane/ppx_jane.a
%{_libdir}/ocaml/ppx_jane/*.cmx
%{_libdir}/ocaml/ppx_jane/*.cmxa
%{_libdir}/ocaml/ppx_jane/kernel/ppx_jane_kernel.a
%{_libdir}/ocaml/ppx_jane/kernel/*.cmx
%{_libdir}/ocaml/ppx_jane/kernel/*.cmxa
%endif
%{_libdir}/ocaml/ppx_jane/dune-package
%{_libdir}/ocaml/ppx_jane/opam
