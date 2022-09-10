AC_PREREQ(2.52)

AC_INIT([Apertium Ancient Hebrew-English], [0.1.0], [https://github.com/apertium/apertium-hbo-eng/issues], [apertium-hbo-eng], [https://wiki.apertium.org/wiki/Apertium-hbo-eng])
AM_INIT_AUTOMAKE
AC_PROG_AWK

PKG_CHECK_MODULES(APERTIUM, apertium >= 3.8.1)
PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox >= 3.6.9)


PKG_CHECK_MODULES(HFST, hfst >= 3.16.0)

PKG_CHECK_MODULES(CG3, cg3 >= 1.3.6)
PKG_CHECK_MODULES(APERTIUM_LEX_TOOLS, apertium-lex-tools >= 0.4.0)



PKG_CHECK_MODULES(APERTIUM_RECURSIVE, apertium-recursive >= 1.1.0)

AC_PATH_PROGS(ZCAT, [gzcat zcat], [false])
AS_IF([test x$ZCAT = xfalse], [AC_MSG_ERROR([You don't have zcat nor gzcat installed])])

m4_ifdef([AP_CHECK_LING],[],[AC_MSG_ERROR([AP_CHECK_LING not defined, is apertium.m4 in ACLOCAL_PATH? See: https://wiki.apertium.org/wiki/Installation_troubleshooting])])


AP_CHECK_LING([1], [apertium-hbo])

AP_CHECK_LING([2], [apertium-eng])

PKG_CHECK_MODULES(REGTEST, apertium-regtest >= 0.9.1, [],
                  [AC_MSG_WARN([Running tests requires apertium-regtest])])

AP_MKINCLUDE

AC_CONFIG_FILES([Makefile])
AC_OUTPUT
