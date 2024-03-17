import sys
# system configuration generated and used by the sysconfig module
build_time_vars = {'ABI3DLLLIBRARY': 'libpython3.dll',
 'ABI3LDLIBRARY': 'libpython3.dll.a',
 'ABIFLAGS': '',
 'AC_APPLE_UNIVERSAL_BUILD': 0,
 'AIX_BUILDDATE': 0,
 'AIX_GENUINE_CPLUSPLUS': 0,
 'ALIGNOF_LONG': 4,
 'ALIGNOF_SIZE_T': 8,
 'ALT_SOABI': 0,
 'ANDROID_API_LEVEL': 0,
 'AR': 'ar',
 'ARFLAGS': 'rcs',
 'BASECFLAGS': '',
 'BASECPPFLAGS': '-IObjects -IInclude -IPython',
 'BASEMODLIBS': '',
 'BINDIR': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/bin',
 'BINLIBDEST': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11',
 'BLDLIBRARY': '-L. -lpython3.11',
 'BLDSHARED': 'x86_64-w64-mingw32-gcc -shared -Wl,--enable-auto-image-base '
              '-pipe -fno-ident '
              '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
              '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
              '-L/c/buildroot/prerequisites/x86_64-w64-mingw32-static/lib '
              '-LC:/buildroot/prerequisites/x86_64-zlib-static/lib '
              '-LC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib',
 'BOOTSTRAP_HEADERS': '\\',
 'BUILDEXE': '.exe',
 'BUILDPYTHON': 'python.exe',
 'BUILDPYTHONW': 'pythonw.exe',
 'BUILDVENVLAUNCHER': 'venvlauncher.exe',
 'BUILDVENVWLAUNCHER': 'venvwlauncher.exe',
 'BUILD_GNU_TYPE': 'x86_64-w64-mingw32',
 'BYTESTR_DEPS': '\\',
 'CC': 'x86_64-w64-mingw32-gcc',
 'CCSHARED': '',
 'CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -O2 -pipe -fno-ident '
           '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
           '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
           '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
           '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
           '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
           '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
           '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC',
 'CFLAGSFORSHARED': '',
 'CFLAGS_ALIASING': '',
 'CONFIGFILES': 'configure configure.ac acconfig.h pyconfig.h.in '
                'Makefile.pre.in',
 'CONFIGURE_CFLAGS': '-O2 -pipe -fno-ident '
                     '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                     '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                     '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                     '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                     '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                     '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                     '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC',
 'CONFIGURE_CFLAGS_NODIST': '-fno-semantic-interposition -std=c11 '
                            '-Werror=implicit-function-declaration '
                            '-fvisibility=hidden -D_WIN32_WINNT=0x0602 '
                            '-DPY3_DLLNAME=\'L"libpython3.11.dll"\' '
                            '-DMS_DLL_ID=\'"3.11"\'',
 'CONFIGURE_CPPFLAGS': '-I../../../src/Python-3.11.6/PC  '
                       '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                       '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                       '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                       '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                       '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                       '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                       '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC -I.',
 'CONFIGURE_LDFLAGS': '-pipe -fno-ident '
                      '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
                      '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
                      '-L/c/buildroot/prerequisites/x86_64-w64-mingw32-static/lib '
                      '-LC:/buildroot/prerequisites/x86_64-zlib-static/lib '
                      '-LC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib',
 'CONFIGURE_LDFLAGS_NODIST': '-fno-semantic-interposition',
 'CONFIGURE_LDFLAGS_NOLTO': '',
 'CONFIG_ARGS': "'--host=x86_64-w64-mingw32' '--build=x86_64-w64-mingw32' "
                "'--prefix=C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt' "
                "'--enable-shared' '--with-system-expat' '--with-system-ffi' "
                "'--enable-loadable-sqlite-extensions' '--without-ensurepip' "
                "'--without-c-locale-coercion' '--enable-optimizations' "
                "'LIBFFI_INCLUDEDIR=C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include' "
                "'PKG_CONFIG_PATH=/c/buildroot/prerequisites/x86_64-zlib-static/lib/pkgconfig:/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/pkgconfig' "
                "'CFLAGS=-O2 -pipe -fno-ident "
                '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                "-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC' 'CPPFLAGS= "
                '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                "-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC' 'LDFLAGS=-pipe "
                '-fno-ident '
                '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
                '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
                '-L/c/buildroot/prerequisites/x86_64-w64-mingw32-static/lib '
                '-LC:/buildroot/prerequisites/x86_64-zlib-static/lib '
                "-LC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib' "
                "'LIBS=-lffi -ltcl -ltk -lole32 -loleaut32 -luuid' "
                "'build_alias=x86_64-w64-mingw32' "
                "'host_alias=x86_64-w64-mingw32'",
 'CONFINCLUDEDIR': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include',
 'CONFINCLUDEPY': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/python3.11',
 'COREPYTHONPATH': '',
 'COVERAGE_INFO': '/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/build/Python-3.11.6/coverage.info',
 'COVERAGE_LCOV_OPTIONS': '--rc lcov_branch_coverage=1',
 'COVERAGE_REPORT': '/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/build/Python-3.11.6/lcov-report',
 'COVERAGE_REPORT_OPTIONS': '--rc lcov_branch_coverage=1 --branch-coverage '
                            '--title "CPython 3.11 LCOV report [commit $(shell '
                            'git --git-dir ../../../src/Python-3.11.6/.git '
                            'rev-parse --short HEAD)]"',
 'CPPFLAGS': '-IObjects -IInclude -IPython -I. '
             '-I../../../src/Python-3.11.6/Include '
             '-I../../../src/Python-3.11.6/PC  '
             '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
             '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
             '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
             '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
             '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
             '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
             '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC -I.',
 'CXX': 'x86_64-w64-mingw32-c++',
 'DECIMAL_CFLAGS': '-I../../../src/Python-3.11.6/Modules/_decimal/libmpdec '
                   '-DCONFIG_64=1 -DANSI=1 -DHAVE_UINT128_T=1',
 'DECIMAL_LDFLAGS': '-lm Modules/_decimal/libmpdec/libmpdec.a',
 'DEEPFREEZE_C': 'Python/deepfreeze/deepfreeze.c',
 'DEEPFREEZE_DEPS': '../../../src/Python-3.11.6/Tools/scripts/deepfreeze.py '
                    '_bootstrap_python '
                    '../../../src/Python-3.11.6/Programs/_freeze_module.py \\',
 'DEEPFREEZE_OBJS': 'Python/deepfreeze/deepfreeze.o',
 'DESTDIR': '',
 'DESTDIRFINAL': '/',
 'DESTDIRS': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt '
             'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
             'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11 '
             'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11/lib-dynload',
 'DESTLIB': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11',
 'DESTPATH': '',
 'DESTSHARED': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11/lib-dynload',
 'DFLAGS': '',
 'DIRMODE': 755,
 'DIST': 'README.rst ChangeLog configure configure.ac acconfig.h pyconfig.h.in '
         'Makefile.pre.in Include Lib Misc Ext-dummy',
 'DISTDIRS': 'Include Lib Misc Ext-dummy',
 'DISTFILES': 'README.rst ChangeLog configure configure.ac acconfig.h '
              'pyconfig.h.in Makefile.pre.in',
 'DLINCLDIR': '.',
 'DLLLIBRARY': 'libpython3.11.dll',
 'DOUBLE_IS_ARM_MIXED_ENDIAN_IEEE754': 0,
 'DOUBLE_IS_BIG_ENDIAN_IEEE754': 0,
 'DOUBLE_IS_LITTLE_ENDIAN_IEEE754': 1,
 'DTRACE': '',
 'DTRACE_DEPS': '\\',
 'DTRACE_HEADERS': '',
 'DTRACE_OBJS': '',
 'DYNLOADFILE': 'dynload_win.o',
 'ENABLE_IPV6': 0,
 'ENSUREPIP': 'no',
 'EXE': '.exe',
 'EXEMODE': 755,
 'EXPAT_CFLAGS': '',
 'EXPAT_LDFLAGS': '-lexpat',
 'EXPORTSFROM': '',
 'EXPORTSYMS': '',
 'EXTRATESTOPTS': '',
 'EXTRA_CFLAGS': '',
 'EXT_SUFFIX': '.cp311-mingw_x86_64_ucrt.pyd',
 'FILEMODE': 644,
 'FLOAT_WORDS_BIGENDIAN': 0,
 'FREEZE_MODULE': './_bootstrap_python '
                  '../../../src/Python-3.11.6/Programs/_freeze_module.py',
 'FREEZE_MODULE_BOOTSTRAP': './Programs/_freeze_module',
 'FREEZE_MODULE_BOOTSTRAP_DEPS': 'Programs/_freeze_module',
 'FREEZE_MODULE_DEPS': '_bootstrap_python '
                       '../../../src/Python-3.11.6/Programs/_freeze_module.py',
 'FROZEN_FILES_IN': '\\',
 'FROZEN_FILES_OUT': '\\',
 'GETPGRP_HAVE_ARG': 0,
 'GITBRANCH': 'git --git-dir ../../../src/Python-3.11.6/.git name-rev '
              '--name-only HEAD',
 'GITTAG': 'git --git-dir ../../../src/Python-3.11.6/.git describe --all '
           '--always --dirty',
 'GITVERSION': 'git --git-dir ../../../src/Python-3.11.6/.git rev-parse '
               '--short HEAD',
 'GNULD': 'yes',
 'HAVE_ACCEPT': 1,
 'HAVE_ACCEPT4': 0,
 'HAVE_ACOSH': 1,
 'HAVE_ADDRINFO': 1,
 'HAVE_ALARM': 0,
 'HAVE_ALIGNED_REQUIRED': 0,
 'HAVE_ALLOCA_H': 0,
 'HAVE_ALTZONE': 0,
 'HAVE_ASINH': 1,
 'HAVE_ASM_TYPES_H': 0,
 'HAVE_ATANH': 1,
 'HAVE_BIND': 1,
 'HAVE_BIND_TEXTDOMAIN_CODESET': 0,
 'HAVE_BLUETOOTH_BLUETOOTH_H': 0,
 'HAVE_BLUETOOTH_H': 0,
 'HAVE_BROKEN_MBSTOWCS': 0,
 'HAVE_BROKEN_NICE': 0,
 'HAVE_BROKEN_PIPE_BUF': 0,
 'HAVE_BROKEN_POLL': 0,
 'HAVE_BROKEN_POSIX_SEMAPHORES': 0,
 'HAVE_BROKEN_PTHREAD_SIGMASK': 0,
 'HAVE_BROKEN_SEM_GETVALUE': 0,
 'HAVE_BROKEN_UNSETENV': 0,
 'HAVE_BUILTIN_ATOMIC': 1,
 'HAVE_BZLIB_H': 0,
 'HAVE_CHFLAGS': 0,
 'HAVE_CHMOD': 1,
 'HAVE_CHOWN': 0,
 'HAVE_CHROOT': 0,
 'HAVE_CLOCK': 1,
 'HAVE_CLOCK_GETRES': 0,
 'HAVE_CLOCK_GETTIME': 0,
 'HAVE_CLOCK_NANOSLEEP': 0,
 'HAVE_CLOCK_SETTIME': 0,
 'HAVE_CLOSE_RANGE': 0,
 'HAVE_COMPUTED_GOTOS': 1,
 'HAVE_CONFSTR': 0,
 'HAVE_CONIO_H': 1,
 'HAVE_CONNECT': 1,
 'HAVE_COPY_FILE_RANGE': 0,
 'HAVE_CRYPT_H': 0,
 'HAVE_CRYPT_R': 0,
 'HAVE_CTERMID': 0,
 'HAVE_CTERMID_R': 0,
 'HAVE_CURSES_FILTER': 1,
 'HAVE_CURSES_H': 1,
 'HAVE_CURSES_HAS_KEY': 1,
 'HAVE_CURSES_IMMEDOK': 1,
 'HAVE_CURSES_IS_PAD': 1,
 'HAVE_CURSES_IS_TERM_RESIZED': 1,
 'HAVE_CURSES_RESIZETERM': 1,
 'HAVE_CURSES_RESIZE_TERM': 1,
 'HAVE_CURSES_SYNCOK': 1,
 'HAVE_CURSES_TYPEAHEAD': 1,
 'HAVE_CURSES_USE_ENV': 1,
 'HAVE_CURSES_WCHGAT': 1,
 'HAVE_DB_H': 0,
 'HAVE_DECL_RTLD_DEEPBIND': 0,
 'HAVE_DECL_RTLD_GLOBAL': 0,
 'HAVE_DECL_RTLD_LAZY': 0,
 'HAVE_DECL_RTLD_LOCAL': 0,
 'HAVE_DECL_RTLD_MEMBER': 0,
 'HAVE_DECL_RTLD_NODELETE': 0,
 'HAVE_DECL_RTLD_NOLOAD': 0,
 'HAVE_DECL_RTLD_NOW': 0,
 'HAVE_DECL_TZNAME': 1,
 'HAVE_DEVICE_MACROS': 0,
 'HAVE_DEV_PTC': 0,
 'HAVE_DEV_PTMX': 0,
 'HAVE_DIRECT_H': 1,
 'HAVE_DIRENT_D_TYPE': 0,
 'HAVE_DIRENT_H': 1,
 'HAVE_DIRFD': 0,
 'HAVE_DLFCN_H': 0,
 'HAVE_DLOPEN': 0,
 'HAVE_DUP': 1,
 'HAVE_DUP2': 1,
 'HAVE_DUP3': 0,
 'HAVE_DYLD_SHARED_CACHE_CONTAINS_PATH': 0,
 'HAVE_DYNAMIC_LOADING': 1,
 'HAVE_ENDIAN_H': 0,
 'HAVE_EPOLL': 0,
 'HAVE_EPOLL_CREATE1': 0,
 'HAVE_ERF': 1,
 'HAVE_ERFC': 1,
 'HAVE_ERRNO_H': 1,
 'HAVE_EVENTFD': 0,
 'HAVE_EXECV': 1,
 'HAVE_EXPLICIT_BZERO': 0,
 'HAVE_EXPLICIT_MEMSET': 0,
 'HAVE_EXPM1': 1,
 'HAVE_FACCESSAT': 0,
 'HAVE_FCHDIR': 0,
 'HAVE_FCHMOD': 0,
 'HAVE_FCHMODAT': 0,
 'HAVE_FCHOWN': 0,
 'HAVE_FCHOWNAT': 0,
 'HAVE_FCNTL_H': 1,
 'HAVE_FDATASYNC': 0,
 'HAVE_FDOPENDIR': 0,
 'HAVE_FDWALK': 0,
 'HAVE_FEXECVE': 0,
 'HAVE_FLOCK': 0,
 'HAVE_FORK': 0,
 'HAVE_FORK1': 0,
 'HAVE_FORKPTY': 0,
 'HAVE_FPATHCONF': 0,
 'HAVE_FSEEK64': 0,
 'HAVE_FSEEKO': 1,
 'HAVE_FSTATAT': 0,
 'HAVE_FSTATVFS': 0,
 'HAVE_FSYNC': 0,
 'HAVE_FTELL64': 0,
 'HAVE_FTELLO': 1,
 'HAVE_FTIME': 1,
 'HAVE_FTRUNCATE': 0,
 'HAVE_FUTIMENS': 0,
 'HAVE_FUTIMES': 0,
 'HAVE_FUTIMESAT': 0,
 'HAVE_GAI_STRERROR': 0,
 'HAVE_GCC_ASM_FOR_MC68881': 0,
 'HAVE_GCC_ASM_FOR_X64': 1,
 'HAVE_GCC_ASM_FOR_X87': 1,
 'HAVE_GCC_UINT128_T': 1,
 'HAVE_GDBM_DASH_NDBM_H': 0,
 'HAVE_GDBM_H': 1,
 'HAVE_GDBM_NDBM_H': 0,
 'HAVE_GETADDRINFO': 0,
 'HAVE_GETC_UNLOCKED': 0,
 'HAVE_GETEGID': 0,
 'HAVE_GETENTROPY': 0,
 'HAVE_GETEUID': 0,
 'HAVE_GETGID': 0,
 'HAVE_GETGRGID': 0,
 'HAVE_GETGRGID_R': 0,
 'HAVE_GETGRNAM_R': 0,
 'HAVE_GETGROUPLIST': 0,
 'HAVE_GETGROUPS': 0,
 'HAVE_GETHOSTBYADDR': 1,
 'HAVE_GETHOSTBYNAME': 1,
 'HAVE_GETHOSTBYNAME_R': 0,
 'HAVE_GETHOSTBYNAME_R_3_ARG': 0,
 'HAVE_GETHOSTBYNAME_R_5_ARG': 0,
 'HAVE_GETHOSTBYNAME_R_6_ARG': 0,
 'HAVE_GETHOSTNAME': 1,
 'HAVE_GETITIMER': 0,
 'HAVE_GETLOADAVG': 0,
 'HAVE_GETLOGIN': 1,
 'HAVE_GETNAMEINFO': 0,
 'HAVE_GETPAGESIZE': 0,
 'HAVE_GETPEERNAME': 1,
 'HAVE_GETPGID': 0,
 'HAVE_GETPGRP': 0,
 'HAVE_GETPID': 1,
 'HAVE_GETPPID': 0,
 'HAVE_GETPRIORITY': 0,
 'HAVE_GETPROTOBYNAME': 1,
 'HAVE_GETPWENT': 0,
 'HAVE_GETPWNAM_R': 0,
 'HAVE_GETPWUID': 0,
 'HAVE_GETPWUID_R': 0,
 'HAVE_GETRANDOM': 0,
 'HAVE_GETRANDOM_SYSCALL': 0,
 'HAVE_GETRESGID': 0,
 'HAVE_GETRESUID': 0,
 'HAVE_GETRUSAGE': 0,
 'HAVE_GETSERVBYNAME': 1,
 'HAVE_GETSERVBYPORT': 1,
 'HAVE_GETSID': 0,
 'HAVE_GETSOCKNAME': 1,
 'HAVE_GETSPENT': 0,
 'HAVE_GETSPNAM': 0,
 'HAVE_GETUID': 0,
 'HAVE_GETWD': 0,
 'HAVE_GLIBC_MEMMOVE_BUG': 0,
 'HAVE_GRP_H': 0,
 'HAVE_HSTRERROR': 0,
 'HAVE_HTOLE64': 0,
 'HAVE_IEEEFP_H': 1,
 'HAVE_IF_NAMEINDEX': 0,
 'HAVE_INET_ATON': 0,
 'HAVE_INET_NTOA': 1,
 'HAVE_INET_PTON': 1,
 'HAVE_INITGROUPS': 0,
 'HAVE_INTTYPES_H': 1,
 'HAVE_IO_H': 1,
 'HAVE_IPA_PURE_CONST_BUG': 0,
 'HAVE_KILL': 0,
 'HAVE_KILLPG': 0,
 'HAVE_KQUEUE': 0,
 'HAVE_LANGINFO_H': 0,
 'HAVE_LARGEFILE_SUPPORT': 1,
 'HAVE_LCHFLAGS': 0,
 'HAVE_LCHMOD': 0,
 'HAVE_LCHOWN': 0,
 'HAVE_LIBB2': 0,
 'HAVE_LIBDB': 0,
 'HAVE_LIBDL': 0,
 'HAVE_LIBDLD': 0,
 'HAVE_LIBGDBM_COMPAT': 1,
 'HAVE_LIBIEEE': 0,
 'HAVE_LIBINTL_H': 0,
 'HAVE_LIBNDBM': 0,
 'HAVE_LIBREADLINE': 1,
 'HAVE_LIBRESOLV': 0,
 'HAVE_LIBSENDFILE': 0,
 'HAVE_LIBSQLITE3': 1,
 'HAVE_LIBUTIL_H': 0,
 'HAVE_LINK': 0,
 'HAVE_LINKAT': 0,
 'HAVE_LINUX_AUXVEC_H': 0,
 'HAVE_LINUX_CAN_BCM_H': 0,
 'HAVE_LINUX_CAN_H': 0,
 'HAVE_LINUX_CAN_J1939_H': 0,
 'HAVE_LINUX_CAN_RAW_FD_FRAMES': 0,
 'HAVE_LINUX_CAN_RAW_H': 0,
 'HAVE_LINUX_CAN_RAW_JOIN_FILTERS': 0,
 'HAVE_LINUX_LIMITS_H': 0,
 'HAVE_LINUX_MEMFD_H': 0,
 'HAVE_LINUX_NETLINK_H': 0,
 'HAVE_LINUX_QRTR_H': 0,
 'HAVE_LINUX_RANDOM_H': 0,
 'HAVE_LINUX_SOUNDCARD_H': 0,
 'HAVE_LINUX_TIPC_H': 0,
 'HAVE_LINUX_VM_SOCKETS_H': 0,
 'HAVE_LINUX_WAIT_H': 0,
 'HAVE_LISTEN': 1,
 'HAVE_LOCKF': 0,
 'HAVE_LOG1P': 1,
 'HAVE_LOG2': 1,
 'HAVE_LOGIN_TTY': 0,
 'HAVE_LONG_DOUBLE': 1,
 'HAVE_LSTAT': 0,
 'HAVE_LUTIMES': 0,
 'HAVE_LZMA_H': 0,
 'HAVE_MADVISE': 0,
 'HAVE_MAKEDEV': 0,
 'HAVE_MBRTOWC': 1,
 'HAVE_MEMFD_CREATE': 0,
 'HAVE_MEMORY_H': 1,
 'HAVE_MEMRCHR': 0,
 'HAVE_MKDIRAT': 0,
 'HAVE_MKFIFO': 0,
 'HAVE_MKFIFOAT': 0,
 'HAVE_MKNOD': 0,
 'HAVE_MKNODAT': 0,
 'HAVE_MKTIME': 1,
 'HAVE_MMAP': 0,
 'HAVE_MREMAP': 0,
 'HAVE_NANOSLEEP': 0,
 'HAVE_NCURSES_H': 1,
 'HAVE_NDBM_H': 1,
 'HAVE_NDIR_H': 0,
 'HAVE_NETCAN_CAN_H': 0,
 'HAVE_NETDB_H': 0,
 'HAVE_NETINET_IN_H': 0,
 'HAVE_NETPACKET_PACKET_H': 0,
 'HAVE_NET_IF_H': 0,
 'HAVE_NICE': 0,
 'HAVE_NON_UNICODE_WCHAR_T_REPRESENTATION': 0,
 'HAVE_OPENAT': 0,
 'HAVE_OPENDIR': 1,
 'HAVE_OPENPTY': 0,
 'HAVE_PATHCONF': 0,
 'HAVE_PAUSE': 0,
 'HAVE_PIPE': 0,
 'HAVE_PIPE2': 0,
 'HAVE_PLOCK': 0,
 'HAVE_POLL': 0,
 'HAVE_POLL_H': 0,
 'HAVE_POSIX_FADVISE': 0,
 'HAVE_POSIX_FALLOCATE': 0,
 'HAVE_POSIX_SPAWN': 0,
 'HAVE_POSIX_SPAWNP': 0,
 'HAVE_PREAD': 0,
 'HAVE_PREADV': 0,
 'HAVE_PREADV2': 0,
 'HAVE_PRLIMIT': 0,
 'HAVE_PROCESS_H': 1,
 'HAVE_PROTOTYPES': 1,
 'HAVE_PTHREAD_CONDATTR_SETCLOCK': 0,
 'HAVE_PTHREAD_DESTRUCTOR': 0,
 'HAVE_PTHREAD_GETCPUCLOCKID': 0,
 'HAVE_PTHREAD_H': 0,
 'HAVE_PTHREAD_INIT': 0,
 'HAVE_PTHREAD_KILL': 0,
 'HAVE_PTHREAD_SIGMASK': 0,
 'HAVE_PTHREAD_STUBS': 0,
 'HAVE_PTY_H': 0,
 'HAVE_PWRITE': 0,
 'HAVE_PWRITEV': 0,
 'HAVE_PWRITEV2': 0,
 'HAVE_READLINK': 0,
 'HAVE_READLINKAT': 0,
 'HAVE_READV': 0,
 'HAVE_REALPATH': 0,
 'HAVE_RECVFROM': 1,
 'HAVE_RENAMEAT': 0,
 'HAVE_RL_APPEND_HISTORY': 1,
 'HAVE_RL_CATCH_SIGNAL': 1,
 'HAVE_RL_COMPLETION_APPEND_CHARACTER': 1,
 'HAVE_RL_COMPLETION_DISPLAY_MATCHES_HOOK': 1,
 'HAVE_RL_COMPLETION_MATCHES': 1,
 'HAVE_RL_COMPLETION_SUPPRESS_APPEND': 1,
 'HAVE_RL_PRE_INPUT_HOOK': 1,
 'HAVE_RL_RESIZE_TERMINAL': 1,
 'HAVE_RPC_RPC_H': 0,
 'HAVE_RTPSPAWN': 0,
 'HAVE_SCHED_GET_PRIORITY_MAX': 0,
 'HAVE_SCHED_H': 0,
 'HAVE_SCHED_RR_GET_INTERVAL': 0,
 'HAVE_SCHED_SETAFFINITY': 0,
 'HAVE_SCHED_SETPARAM': 0,
 'HAVE_SCHED_SETSCHEDULER': 0,
 'HAVE_SEM_CLOCKWAIT': 0,
 'HAVE_SEM_GETVALUE': 0,
 'HAVE_SEM_OPEN': 0,
 'HAVE_SEM_TIMEDWAIT': 0,
 'HAVE_SEM_UNLINK': 0,
 'HAVE_SENDFILE': 0,
 'HAVE_SENDTO': 1,
 'HAVE_SETEGID': 0,
 'HAVE_SETEUID': 0,
 'HAVE_SETGID': 0,
 'HAVE_SETGROUPS': 0,
 'HAVE_SETHOSTNAME': 0,
 'HAVE_SETITIMER': 0,
 'HAVE_SETJMP_H': 1,
 'HAVE_SETLOCALE': 1,
 'HAVE_SETPGID': 0,
 'HAVE_SETPGRP': 0,
 'HAVE_SETPRIORITY': 0,
 'HAVE_SETREGID': 0,
 'HAVE_SETRESGID': 0,
 'HAVE_SETRESUID': 0,
 'HAVE_SETREUID': 0,
 'HAVE_SETSID': 0,
 'HAVE_SETSOCKOPT': 1,
 'HAVE_SETUID': 0,
 'HAVE_SETVBUF': 1,
 'HAVE_SHADOW_H': 0,
 'HAVE_SHM_OPEN': 0,
 'HAVE_SHM_UNLINK': 0,
 'HAVE_SHUTDOWN': 1,
 'HAVE_SIGACTION': 0,
 'HAVE_SIGALTSTACK': 0,
 'HAVE_SIGFILLSET': 0,
 'HAVE_SIGINFO_T_SI_BAND': 0,
 'HAVE_SIGINTERRUPT': 0,
 'HAVE_SIGNAL_H': 1,
 'HAVE_SIGPENDING': 0,
 'HAVE_SIGRELSE': 0,
 'HAVE_SIGTIMEDWAIT': 0,
 'HAVE_SIGWAIT': 0,
 'HAVE_SIGWAITINFO': 0,
 'HAVE_SNPRINTF': 1,
 'HAVE_SOCKADDR_ALG': 0,
 'HAVE_SOCKADDR_SA_LEN': 0,
 'HAVE_SOCKADDR_STORAGE': 1,
 'HAVE_SOCKET': 1,
 'HAVE_SOCKETPAIR': 0,
 'HAVE_SPAWN_H': 0,
 'HAVE_SPLICE': 0,
 'HAVE_SSIZE_T': 1,
 'HAVE_STATVFS': 0,
 'HAVE_STAT_TV_NSEC': 0,
 'HAVE_STAT_TV_NSEC2': 0,
 'HAVE_STDARG_PROTOTYPES': 1,
 'HAVE_STDINT_H': 1,
 'HAVE_STDLIB_H': 1,
 'HAVE_STD_ATOMIC': 1,
 'HAVE_STRFTIME': 1,
 'HAVE_STRINGS_H': 1,
 'HAVE_STRING_H': 1,
 'HAVE_STRLCPY': 0,
 'HAVE_STROPTS_H': 0,
 'HAVE_STRSIGNAL': 0,
 'HAVE_STRUCT_PASSWD_PW_GECOS': 0,
 'HAVE_STRUCT_PASSWD_PW_PASSWD': 0,
 'HAVE_STRUCT_STAT_ST_BIRTHTIME': 0,
 'HAVE_STRUCT_STAT_ST_BLKSIZE': 0,
 'HAVE_STRUCT_STAT_ST_BLOCKS': 0,
 'HAVE_STRUCT_STAT_ST_FLAGS': 0,
 'HAVE_STRUCT_STAT_ST_GEN': 0,
 'HAVE_STRUCT_STAT_ST_RDEV': 1,
 'HAVE_STRUCT_TM_TM_ZONE': 0,
 'HAVE_SYMLINK': 0,
 'HAVE_SYMLINKAT': 0,
 'HAVE_SYNC': 0,
 'HAVE_SYSCONF': 0,
 'HAVE_SYSEXITS_H': 0,
 'HAVE_SYSLOG_H': 0,
 'HAVE_SYSTEM': 1,
 'HAVE_SYS_AUDIOIO_H': 0,
 'HAVE_SYS_AUXV_H': 0,
 'HAVE_SYS_BSDTTY_H': 0,
 'HAVE_SYS_DEVPOLL_H': 0,
 'HAVE_SYS_DIR_H': 0,
 'HAVE_SYS_ENDIAN_H': 0,
 'HAVE_SYS_EPOLL_H': 0,
 'HAVE_SYS_EVENTFD_H': 0,
 'HAVE_SYS_EVENT_H': 0,
 'HAVE_SYS_FILE_H': 1,
 'HAVE_SYS_IOCTL_H': 0,
 'HAVE_SYS_KERN_CONTROL_H': 0,
 'HAVE_SYS_LOADAVG_H': 0,
 'HAVE_SYS_LOCK_H': 0,
 'HAVE_SYS_MEMFD_H': 0,
 'HAVE_SYS_MKDEV_H': 0,
 'HAVE_SYS_MMAN_H': 0,
 'HAVE_SYS_MODEM_H': 0,
 'HAVE_SYS_NDIR_H': 0,
 'HAVE_SYS_PARAM_H': 1,
 'HAVE_SYS_POLL_H': 0,
 'HAVE_SYS_RANDOM_H': 0,
 'HAVE_SYS_RESOURCE_H': 0,
 'HAVE_SYS_SELECT_H': 0,
 'HAVE_SYS_SENDFILE_H': 0,
 'HAVE_SYS_SOCKET_H': 0,
 'HAVE_SYS_SOUNDCARD_H': 0,
 'HAVE_SYS_STATVFS_H': 0,
 'HAVE_SYS_STAT_H': 1,
 'HAVE_SYS_SYSCALL_H': 0,
 'HAVE_SYS_SYSMACROS_H': 0,
 'HAVE_SYS_SYS_DOMAIN_H': 0,
 'HAVE_SYS_TERMIO_H': 0,
 'HAVE_SYS_TIMES_H': 0,
 'HAVE_SYS_TIME_H': 1,
 'HAVE_SYS_TYPES_H': 1,
 'HAVE_SYS_UIO_H': 0,
 'HAVE_SYS_UN_H': 0,
 'HAVE_SYS_UTSNAME_H': 0,
 'HAVE_SYS_WAIT_H': 0,
 'HAVE_SYS_XATTR_H': 0,
 'HAVE_TCGETPGRP': 0,
 'HAVE_TCSETPGRP': 0,
 'HAVE_TEMPNAM': 1,
 'HAVE_TERMIOS_H': 0,
 'HAVE_TERM_H': 1,
 'HAVE_THREAD_H': 0,
 'HAVE_TIMEGM': 0,
 'HAVE_TIMES': 0,
 'HAVE_TMPFILE': 1,
 'HAVE_TMPNAM': 1,
 'HAVE_TMPNAM_R': 0,
 'HAVE_TM_ZONE': 0,
 'HAVE_TRUNCATE': 0,
 'HAVE_TTYNAME': 0,
 'HAVE_TZNAME': 1,
 'HAVE_UMASK': 1,
 'HAVE_UNAME': 0,
 'HAVE_UNISTD_H': 1,
 'HAVE_UNLINKAT': 0,
 'HAVE_USABLE_WCHAR_T': 1,
 'HAVE_UTIL_H': 0,
 'HAVE_UTIMENSAT': 0,
 'HAVE_UTIMES': 0,
 'HAVE_UTIME_H': 1,
 'HAVE_UTMP_H': 0,
 'HAVE_UUID_CREATE': 0,
 'HAVE_UUID_ENC_BE': 0,
 'HAVE_UUID_GENERATE_TIME_SAFE': 0,
 'HAVE_UUID_H': 0,
 'HAVE_UUID_UUID_H': 0,
 'HAVE_VFORK': 0,
 'HAVE_WAIT': 0,
 'HAVE_WAIT3': 0,
 'HAVE_WAIT4': 0,
 'HAVE_WAITID': 0,
 'HAVE_WAITPID': 0,
 'HAVE_WCHAR_H': 1,
 'HAVE_WCSCOLL': 1,
 'HAVE_WCSFTIME': 1,
 'HAVE_WCSXFRM': 1,
 'HAVE_WMEMCMP': 1,
 'HAVE_WORKING_TZSET': 0,
 'HAVE_WRITEV': 0,
 'HAVE_WS2TCPIP_H': 1,
 'HAVE_ZLIB_COPY': 1,
 'HAVE_ZLIB_H': 0,
 'HAVE__GETPTY': 0,
 'HOSTRUNNER': '',
 'HOST_GNU_TYPE': 'x86_64-w64-mingw32',
 'INCLDIRSTOMAKE': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                   'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                   'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/python3.11 '
                   'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/python3.11',
 'INCLUDEDIR': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include',
 'INCLUDEPY': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/python3.11',
 'INSTALL': '/usr/bin/install -c',
 'INSTALL_DATA': '/usr/bin/install -c -m 644',
 'INSTALL_PROGRAM': '/usr/bin/install -c',
 'INSTALL_SCRIPT': '/usr/bin/install -c',
 'INSTALL_SHARED': '/usr/bin/install -c -m 755',
 'INSTSONAME': 'libpython3.11.dll.a',
 'IO_H': 'Modules/_io/_iomodule.h',
 'IO_OBJS': '\\',
 'LDCXXSHARED': 'x86_64-w64-mingw32-c++ -shared -Wl,--enable-auto-image-base',
 'LDFLAGS': '-pipe -fno-ident '
            '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
            '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
            '-L/c/buildroot/prerequisites/x86_64-w64-mingw32-static/lib '
            '-LC:/buildroot/prerequisites/x86_64-zlib-static/lib '
            '-LC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib',
 'LDLIBRARY': 'libpython3.11.dll.a',
 'LDLIBRARYDIR': '',
 'LDSHARED': 'x86_64-w64-mingw32-gcc -shared -Wl,--enable-auto-image-base '
             '-pipe -fno-ident '
             '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
             '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
             '-L/c/buildroot/prerequisites/x86_64-w64-mingw32-static/lib '
             '-LC:/buildroot/prerequisites/x86_64-zlib-static/lib '
             '-LC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib',
 'LDVERSION': '3.11',
 'LIBC': '',
 'LIBDEST': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11',
 'LIBDIR': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib',
 'LIBEXPAT_A': 'Modules/expat/libexpat.a',
 'LIBEXPAT_CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -O2 -pipe -fno-ident '
                    '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                    '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                    '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                    '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                    '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                    '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                    '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC '
                    '-fno-semantic-interposition -std=c11 '
                    '-Werror=implicit-function-declaration -fvisibility=hidden '
                    '-D_WIN32_WINNT=0x0602 '
                    '-DPY3_DLLNAME=\'L"libpython3.11.dll"\' '
                    '-DMS_DLL_ID=\'"3.11"\' -fprofile-use -fprofile-correction '
                    '-I../../../src/Python-3.11.6/Include/internal -IObjects '
                    '-IInclude -IPython -I. '
                    '-I../../../src/Python-3.11.6/Include '
                    '-I../../../src/Python-3.11.6/PC  '
                    '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                    '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                    '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                    '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                    '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                    '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                    '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC -I.',
 'LIBEXPAT_HEADERS': '\\',
 'LIBEXPAT_OBJS': '\\',
 'LIBFFI_INCLUDEDIR': '/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include',
 'LIBM': '-lm',
 'LIBMPDEC_A': 'Modules/_decimal/libmpdec/libmpdec.a',
 'LIBMPDEC_CFLAGS': '-I../../../src/Python-3.11.6/Modules/_decimal/libmpdec '
                    '-DCONFIG_64=1 -DANSI=1 -DHAVE_UINT128_T=1 -DNDEBUG -g '
                    '-fwrapv -O3 -Wall -O2 -pipe -fno-ident '
                    '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                    '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                    '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                    '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                    '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                    '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                    '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC '
                    '-fno-semantic-interposition -std=c11 '
                    '-Werror=implicit-function-declaration -fvisibility=hidden '
                    '-D_WIN32_WINNT=0x0602 '
                    '-DPY3_DLLNAME=\'L"libpython3.11.dll"\' '
                    '-DMS_DLL_ID=\'"3.11"\' -fprofile-use -fprofile-correction '
                    '-I../../../src/Python-3.11.6/Include/internal -IObjects '
                    '-IInclude -IPython -I. '
                    '-I../../../src/Python-3.11.6/Include '
                    '-I../../../src/Python-3.11.6/PC  '
                    '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                    '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                    '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                    '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                    '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                    '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                    '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC -I.',
 'LIBMPDEC_HEADERS': '\\',
 'LIBMPDEC_OBJS': '\\',
 'LIBOBJDIR': 'Python/',
 'LIBOBJS': '',
 'LIBPC': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/pkgconfig',
 'LIBPL': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11/config-3.11',
 'LIBPYTHON': '-lpython3.11',
 'LIBRARY': 'libpython3.11.a',
 'LIBRARY_DEPS': 'libpython3.11.a libpython3.11.dll.a',
 'LIBRARY_OBJS': '\\',
 'LIBRARY_OBJS_OMIT_FROZEN': '\\',
 'LIBS': '-lffi -ltcl -ltk -lole32 -loleaut32 -luuid -lversion -lshlwapi '
         '-lpathcch -lbcrypt',
 'LIBSUBDIRS': 'asyncio \\',
 'LINKCC': 'x86_64-w64-mingw32-gcc',
 'LINKFORSHARED': '-Wl,--stack,2000000',
 'LINK_PYTHON_DEPS': 'libpython3.11.a libpython3.11.dll.a',
 'LINK_PYTHON_OBJS': '-L. -lpython3.11',
 'LIPO_32BIT_FLAGS': '',
 'LIPO_INTEL64_FLAGS': '',
 'LLVM_PROF_ERR': 'no',
 'LLVM_PROF_FILE': '',
 'LLVM_PROF_MERGER': 'true',
 'LN': 'ln',
 'LOCALMODLIBS': '-lws2_32',
 'MACHDEP': 'win32',
 'MACHDEP_OBJS': 'PC/dl_nt.o',
 'MACHDESTLIB': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11',
 'MACOSX_DEPLOYMENT_TARGET': '',
 'MAINCC': 'x86_64-w64-mingw32-gcc',
 'MAJOR_IN_MKDEV': 0,
 'MAJOR_IN_SYSMACROS': 0,
 'MAKESETUP': '../../../src/Python-3.11.6/Modules/makesetup',
 'MANDIR': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/share/man',
 'MKDIR_P': '/usr/bin/mkdir -p',
 'MODBUILT_NAMES': 'atexit  faulthandler  nt  _signal  _tracemalloc  _codecs  '
                   '_collections  errno  _io  itertools  _sre  _thread  time  '
                   '_weakref  _abc  _functools  _locale  _operator  _stat  '
                   '_symtable  winreg  msvcrt  _winapi  xxsubtype',
 'MODDISABLED_NAMES': '',
 'MODLIBS': '-lws2_32',
 'MODOBJS': 'Modules/atexitmodule.o  Modules/faulthandler.o  '
            'Modules/posixmodule.o  Modules/signalmodule.o  '
            'Modules/_tracemalloc.o  Modules/_codecsmodule.o  '
            'Modules/_collectionsmodule.o  Modules/errnomodule.o  '
            'Modules/_io/_iomodule.o Modules/_io/iobase.o Modules/_io/fileio.o '
            'Modules/_io/bytesio.o Modules/_io/bufferedio.o '
            'Modules/_io/textio.o Modules/_io/stringio.o '
            'Modules/_io/winconsoleio.o  Modules/itertoolsmodule.o  '
            'Modules/_sre/sre.o  Modules/_threadmodule.o  '
            'Modules/timemodule.o  Modules/_weakref.o  Modules/_abc.o  '
            'Modules/_functoolsmodule.o  Modules/_localemodule.o  '
            'Modules/_operator.o  Modules/_stat.o  Modules/symtablemodule.o  '
            'Modules/../PC/winreg.o  Modules/../PC/msvcrtmodule.o  '
            'Modules/_winapi.o  Modules/xxsubtype.o',
 'MODSHARED_NAMES': '',
 'MODULE_ARRAY_STATE': 'yes',
 'MODULE_ATEXIT_LDFLAGS': '',
 'MODULE_AUDIOOP_LDFLAGS': '-lm',
 'MODULE_AUDIOOP_STATE': 'yes',
 'MODULE_BINASCII_CFLAGS': '-DUSE_ZLIB_CRC32 '
                           '-I/c/buildroot/prerequisites/x86_64-zlib-static/include',
 'MODULE_BINASCII_LDFLAGS': '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
                            '-lz',
 'MODULE_BINASCII_STATE': 'yes',
 'MODULE_CMATH_DEPS': '../../../src/Python-3.11.6/Modules/_math.h',
 'MODULE_CMATH_LDFLAGS': '-lm',
 'MODULE_CMATH_STATE': 'yes',
 'MODULE_ERRNO_LDFLAGS': '',
 'MODULE_FAULTHANDLER_LDFLAGS': '',
 'MODULE_FCNTL_STATE': 'missing',
 'MODULE_GRP_STATE': 'missing',
 'MODULE_ITERTOOLS_LDFLAGS': '',
 'MODULE_MATH_DEPS': '../../../src/Python-3.11.6/Modules/_math.h',
 'MODULE_MATH_LDFLAGS': '-lm',
 'MODULE_MATH_STATE': 'yes',
 'MODULE_MMAP_STATE': 'yes',
 'MODULE_MSVCRT_STATE': 'yes',
 'MODULE_NIS_STATE': 'missing',
 'MODULE_NT_LDFLAGS': '',
 'MODULE_OBJS': '\\',
 'MODULE_OSSAUDIODEV_STATE': 'missing',
 'MODULE_PWD_STATE': 'missing',
 'MODULE_PYEXPAT_CFLAGS': '',
 'MODULE_PYEXPAT_DEPS': '',
 'MODULE_PYEXPAT_LDFLAGS': '-lexpat',
 'MODULE_PYEXPAT_STATE': 'yes',
 'MODULE_RESOURCE_STATE': 'missing',
 'MODULE_SELECT_STATE': 'yes',
 'MODULE_SPWD_STATE': 'missing',
 'MODULE_SYSLOG_STATE': 'missing',
 'MODULE_TERMIOS_STATE': 'missing',
 'MODULE_TIME_LDFLAGS': '',
 'MODULE_TIME_STATE': 'yes',
 'MODULE_UNICODEDATA_DEPS': '../../../src/Python-3.11.6/Modules/unicodedata_db.h '
                            '../../../src/Python-3.11.6/Modules/unicodename_db.h',
 'MODULE_UNICODEDATA_STATE': 'yes',
 'MODULE_WINREG_LDFLAGS': '',
 'MODULE_WINSOUND_LDFLAGS': '-lwinmm',
 'MODULE_WINSOUND_STATE': 'yes',
 'MODULE_XXLIMITED_35_STATE': 'yes',
 'MODULE_XXLIMITED_STATE': 'yes',
 'MODULE_XXSUBTYPE_LDFLAGS': '',
 'MODULE_ZLIB_CFLAGS': '-I/c/buildroot/prerequisites/x86_64-zlib-static/include',
 'MODULE_ZLIB_LDFLAGS': '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
                        '-lz',
 'MODULE_ZLIB_STATE': 'yes',
 'MODULE__ABC_LDFLAGS': '',
 'MODULE__ASYNCIO_STATE': 'yes',
 'MODULE__BISECT_STATE': 'yes',
 'MODULE__BLAKE2_CFLAGS': '',
 'MODULE__BLAKE2_DEPS': '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2-config.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2-impl.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2b-load-sse2.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2b-load-sse41.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2b-ref.c '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2b-round.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2b.c '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2s-load-sse2.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2s-load-sse41.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2s-load-xop.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2s-ref.c '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2s-round.h '
                        '../../../src/Python-3.11.6/Modules/_blake2/impl/blake2s.c '
                        '../../../src/Python-3.11.6/Modules/_blake2/blake2module.h '
                        '../../../src/Python-3.11.6/Modules/hashlib.h',
 'MODULE__BLAKE2_LDFLAGS': '',
 'MODULE__BLAKE2_STATE': 'yes',
 'MODULE__BZ2_CFLAGS': '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include',
 'MODULE__BZ2_LDFLAGS': '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
                        '-lbz2',
 'MODULE__BZ2_STATE': 'yes',
 'MODULE__CODECS_CN_STATE': 'yes',
 'MODULE__CODECS_HK_STATE': 'yes',
 'MODULE__CODECS_ISO2022_STATE': 'yes',
 'MODULE__CODECS_JP_STATE': 'yes',
 'MODULE__CODECS_KR_STATE': 'yes',
 'MODULE__CODECS_LDFLAGS': '',
 'MODULE__CODECS_TW_STATE': 'yes',
 'MODULE__COLLECTIONS_LDFLAGS': '',
 'MODULE__CONTEXTVARS_STATE': 'yes',
 'MODULE__CRYPT_STATE': 'missing',
 'MODULE__CSV_STATE': 'yes',
 'MODULE__CTYPES_DEPS': '../../../src/Python-3.11.6/Modules/_ctypes/ctypes.h',
 'MODULE__CTYPES_TEST_LDFLAGS': '-lm',
 'MODULE__CTYPES_TEST_STATE': 'yes',
 'MODULE__DATETIME_LDFLAGS': '-lm',
 'MODULE__DATETIME_STATE': 'yes',
 'MODULE__DECIMAL_CFLAGS': '-I../../../src/Python-3.11.6/Modules/_decimal/libmpdec '
                           '-DCONFIG_64=1 -DANSI=1 -DHAVE_UINT128_T=1',
 'MODULE__DECIMAL_DEPS': '../../../src/Python-3.11.6/Modules/_decimal/docstrings.h '
                         '\\ Modules/_decimal/libmpdec/libmpdec.a',
 'MODULE__DECIMAL_LDFLAGS': '-lm Modules/_decimal/libmpdec/libmpdec.a',
 'MODULE__DECIMAL_STATE': 'yes',
 'MODULE__ELEMENTTREE_CFLAGS': '',
 'MODULE__ELEMENTTREE_DEPS': '../../../src/Python-3.11.6/Modules/pyexpat.c',
 'MODULE__ELEMENTTREE_STATE': 'yes',
 'MODULE__FUNCTOOLS_LDFLAGS': '',
 'MODULE__GDBM_CFLAGS': '',
 'MODULE__GDBM_LDFLAGS': '-lgdbm',
 'MODULE__GDBM_STATE': 'yes',
 'MODULE__HASHLIB_CFLAGS': '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include',
 'MODULE__HASHLIB_DEPS': '../../../src/Python-3.11.6/Modules/hashlib.h',
 'MODULE__HASHLIB_LDFLAGS': '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib   '
                            '-lcrypto',
 'MODULE__HASHLIB_STATE': 'yes',
 'MODULE__HEAPQ_STATE': 'yes',
 'MODULE__IO_CFLAGS': '-I../../../src/Python-3.11.6/Modules/_io',
 'MODULE__IO_DEPS': '../../../src/Python-3.11.6/Modules/_io/_iomodule.h',
 'MODULE__IO_LDFLAGS': '',
 'MODULE__IO_STATE': 'yes',
 'MODULE__JSON_STATE': 'yes',
 'MODULE__LOCALE_LDFLAGS': '',
 'MODULE__LSPROF_STATE': 'yes',
 'MODULE__LZMA_CFLAGS': '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include',
 'MODULE__LZMA_LDFLAGS': '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
                         '-llzma',
 'MODULE__LZMA_STATE': 'yes',
 'MODULE__MD5_DEPS': '../../../src/Python-3.11.6/Modules/hashlib.h',
 'MODULE__MD5_STATE': 'yes',
 'MODULE__MSI_LDFLAGS': '-lmsi -lcabinet -lrpcrt4',
 'MODULE__MSI_STATE': 'yes',
 'MODULE__MULTIBYTECODEC_STATE': 'yes',
 'MODULE__MULTIPROCESSING_CFLAGS': '-I../../../src/Python-3.11.6/Modules/_multiprocessing',
 'MODULE__MULTIPROCESSING_STATE': 'yes',
 'MODULE__OPCODE_STATE': 'yes',
 'MODULE__OPERATOR_LDFLAGS': '',
 'MODULE__OVERLAPPED_LDFLAGS': '-lws2_32',
 'MODULE__OVERLAPPED_STATE': 'yes',
 'MODULE__PICKLE_STATE': 'yes',
 'MODULE__POSIXSHMEM_STATE': 'missing',
 'MODULE__POSIXSUBPROCESS_STATE': 'missing',
 'MODULE__QUEUE_STATE': 'yes',
 'MODULE__RANDOM_STATE': 'yes',
 'MODULE__SCPROXY_STATE': 'n/a',
 'MODULE__SHA1_DEPS': '../../../src/Python-3.11.6/Modules/hashlib.h',
 'MODULE__SHA1_STATE': 'yes',
 'MODULE__SHA256_DEPS': '../../../src/Python-3.11.6/Modules/hashlib.h',
 'MODULE__SHA256_STATE': 'yes',
 'MODULE__SHA3_DEPS': '../../../src/Python-3.11.6/Modules/_sha3/sha3.c '
                      '../../../src/Python-3.11.6/Modules/_sha3/sha3.h '
                      '../../../src/Python-3.11.6/Modules/hashlib.h',
 'MODULE__SHA3_STATE': 'yes',
 'MODULE__SHA512_DEPS': '../../../src/Python-3.11.6/Modules/hashlib.h',
 'MODULE__SHA512_STATE': 'yes',
 'MODULE__SOCKET_DEPS': '../../../src/Python-3.11.6/Modules/socketmodule.h '
                        '../../../src/Python-3.11.6/Modules/addrinfo.h '
                        '../../../src/Python-3.11.6/Modules/getaddrinfo.c '
                        '../../../src/Python-3.11.6/Modules/getnameinfo.c',
 'MODULE__SOCKET_LDFLAGS': '',
 'MODULE__SOCKET_STATE': 'yes',
 'MODULE__SQLITE3_CFLAGS': '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                           '-I../../../src/Python-3.11.6/Modules/_sqlite',
 'MODULE__SQLITE3_DEPS': '../../../src/Python-3.11.6/Modules/_sqlite/connection.h '
                         '../../../src/Python-3.11.6/Modules/_sqlite/cursor.h '
                         '../../../src/Python-3.11.6/Modules/_sqlite/microprotocols.h '
                         '../../../src/Python-3.11.6/Modules/_sqlite/module.h '
                         '../../../src/Python-3.11.6/Modules/_sqlite/prepare_protocol.h '
                         '../../../src/Python-3.11.6/Modules/_sqlite/row.h '
                         '../../../src/Python-3.11.6/Modules/_sqlite/util.h',
 'MODULE__SQLITE3_LDFLAGS': '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
                            '-lsqlite3',
 'MODULE__SQLITE3_STATE': 'yes',
 'MODULE__SRE_LDFLAGS': '',
 'MODULE__SSL_CFLAGS': '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include',
 'MODULE__SSL_DEPS': '../../../src/Python-3.11.6/Modules/_ssl.h '
                     '../../../src/Python-3.11.6/Modules/_ssl/cert.c '
                     '../../../src/Python-3.11.6/Modules/_ssl/debughelpers.c '
                     '../../../src/Python-3.11.6/Modules/_ssl/misc.c '
                     '../../../src/Python-3.11.6/Modules/_ssl_data.h '
                     '../../../src/Python-3.11.6/Modules/_ssl_data_111.h '
                     '../../../src/Python-3.11.6/Modules/_ssl_data_300.h '
                     '../../../src/Python-3.11.6/Modules/socketmodule.h',
 'MODULE__SSL_LDFLAGS': '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib  '
                        '-lssl -lcrypto -lws2_32',
 'MODULE__SSL_STATE': 'yes',
 'MODULE__STATISTICS_LDFLAGS': '-lm',
 'MODULE__STATISTICS_STATE': 'yes',
 'MODULE__STAT_LDFLAGS': '',
 'MODULE__STRUCT_STATE': 'yes',
 'MODULE__SYMTABLE_LDFLAGS': '',
 'MODULE__TESTBUFFER_STATE': 'yes',
 'MODULE__TESTCAPI_DEPS': '../../../src/Python-3.11.6/Modules/testcapi_long.h',
 'MODULE__TESTCAPI_STATE': 'yes',
 'MODULE__TESTCLINIC_STATE': 'yes',
 'MODULE__TESTIMPORTMULTIPLE_STATE': 'yes',
 'MODULE__TESTINTERNALCAPI_CFLAGS': '-DPY3_DLLNAME="libpython3.11.dll"',
 'MODULE__TESTINTERNALCAPI_STATE': 'yes',
 'MODULE__TESTMULTIPHASE_STATE': 'yes',
 'MODULE__THREAD_LDFLAGS': '',
 'MODULE__TKINTER_CFLAGS': '-Wno-strict-prototypes -DWITH_APPINIT=1',
 'MODULE__TKINTER_LDFLAGS': '',
 'MODULE__TKINTER_STATE': 'yes',
 'MODULE__TRACEMALLOC_LDFLAGS': '',
 'MODULE__TYPING_STATE': 'yes',
 'MODULE__UUID_STATE': 'missing',
 'MODULE__WEAKREF_LDFLAGS': '',
 'MODULE__WINAPI_LDFLAGS': '',
 'MODULE__WINAPI_STATE': 'yes',
 'MODULE__XXSUBINTERPRETERS_STATE': 'yes',
 'MODULE__XXTESTFUZZ_STATE': 'yes',
 'MODULE__ZONEINFO_STATE': 'yes',
 'MULTIARCH': '',
 'MULTIARCH_CPPFLAGS': '',
 'MVWDELCH_IS_EXPRESSION': 1,
 'NCURSESW_INCLUDEDIR': '/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw',
 'NO_AS_NEEDED': '-Wl,--no-as-needed',
 'NT_THREADS': 1,
 'OBJECT_OBJS': '\\',
 'OPENSSL_INCLUDES': '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include',
 'OPENSSL_LDFLAGS': '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib',
 'OPENSSL_LIBS': '-lssl -lcrypto',
 'OPENSSL_RPATH': '',
 'OPT': '-DNDEBUG -g -fwrapv -O3 -Wall',
 'OTHER_LIBTOOL_OPT': '',
 'PACKAGE_BUGREPORT': 0,
 'PACKAGE_NAME': 0,
 'PACKAGE_STRING': 0,
 'PACKAGE_TARNAME': 0,
 'PACKAGE_URL': 0,
 'PACKAGE_VERSION': 0,
 'PARSER_HEADERS': '\\',
 'PARSER_OBJS': '\\ \\ Parser/myreadline.o Parser/tokenizer.o',
 'PEGEN_HEADERS': '\\',
 'PEGEN_OBJS': '\\',
 'PGO_PROF_GEN_FLAG': '-fprofile-generate',
 'PGO_PROF_USE_FLAG': '-fprofile-use -fprofile-correction',
 'PLATLIBDIR': 'lib',
 'POBJS': '\\',
 'POSIX_SEMAPHORES_NOT_ENABLED': 1,
 'PROFILE_TASK': '-m test --pgo --timeout=1200',
 'PTHREAD_KEY_T_IS_COMPATIBLE_WITH_INT': 0,
 'PTHREAD_SYSTEM_SCHED_SUPPORTED': 0,
 'PURIFY': '',
 'PY3LIBRARY': '',
 'PYD_PLATFORM_TAG': 'mingw_x86_64_ucrt',
 'PYLONG_BITS_IN_DIGIT': 0,
 'PYTHON': 'python.exe',
 'PYTHONFRAMEWORK': '',
 'PYTHONFRAMEWORKDIR': 'no-framework',
 'PYTHONFRAMEWORKINSTALLDIR': '',
 'PYTHONFRAMEWORKPREFIX': '',
 'PYTHONPATH': '',
 'PYTHON_FOR_BUILD': './python.exe -E',
 'PYTHON_FOR_BUILD_DEPS': 'python.exe',
 'PYTHON_FOR_FREEZE': './_bootstrap_python',
 'PYTHON_FOR_REGEN': '',
 'PYTHON_HEADERS': '\\',
 'PYTHON_OBJS': '\\',
 'PY_BUILTIN_HASHLIB_HASHES': '"md5,sha1,sha256,sha512,sha3,blake2"',
 'PY_BUILTIN_MODULE_CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -O2 -pipe '
                             '-fno-ident '
                             '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                             '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                             '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                             '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                             '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                             '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                             '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC '
                             '-fno-semantic-interposition -std=c11 '
                             '-Werror=implicit-function-declaration '
                             '-fvisibility=hidden -D_WIN32_WINNT=0x0602 '
                             '-DPY3_DLLNAME=\'L"libpython3.11.dll"\' '
                             '-DMS_DLL_ID=\'"3.11"\' -fprofile-use '
                             '-fprofile-correction '
                             '-I../../../src/Python-3.11.6/Include/internal '
                             '-IObjects -IInclude -IPython -I. '
                             '-I../../../src/Python-3.11.6/Include '
                             '-I../../../src/Python-3.11.6/PC  '
                             '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                             '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                             '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                             '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                             '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                             '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                             '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC -I. '
                             '-DPy_BUILD_CORE_BUILTIN',
 'PY_CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -O2 -pipe -fno-ident '
              '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
              '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
              '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
              '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
              '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
              '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
              '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC',
 'PY_CFLAGS_NODIST': '-fno-semantic-interposition -std=c11 '
                     '-Werror=implicit-function-declaration '
                     '-fvisibility=hidden -D_WIN32_WINNT=0x0602 '
                     '-DPY3_DLLNAME=\'L"libpython3.11.dll"\' '
                     '-DMS_DLL_ID=\'"3.11"\' -fprofile-use '
                     '-fprofile-correction '
                     '-I../../../src/Python-3.11.6/Include/internal',
 'PY_COERCE_C_LOCALE': 0,
 'PY_CORE_CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -O2 -pipe -fno-ident '
                   '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                   '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                   '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                   '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                   '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                   '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                   '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC '
                   '-fno-semantic-interposition -std=c11 '
                   '-Werror=implicit-function-declaration -fvisibility=hidden '
                   '-D_WIN32_WINNT=0x0602 '
                   '-DPY3_DLLNAME=\'L"libpython3.11.dll"\' '
                   '-DMS_DLL_ID=\'"3.11"\' -fprofile-use -fprofile-correction '
                   '-I../../../src/Python-3.11.6/Include/internal -IObjects '
                   '-IInclude -IPython -I. '
                   '-I../../../src/Python-3.11.6/Include '
                   '-I../../../src/Python-3.11.6/PC  '
                   '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                   '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                   '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                   '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                   '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                   '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                   '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC -I. '
                   '-DPy_BUILD_CORE',
 'PY_CORE_LDFLAGS': '-pipe -fno-ident '
                    '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
                    '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
                    '-L/c/buildroot/prerequisites/x86_64-w64-mingw32-static/lib '
                    '-LC:/buildroot/prerequisites/x86_64-zlib-static/lib '
                    '-LC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
                    '-fno-semantic-interposition',
 'PY_CPPFLAGS': '-IObjects -IInclude -IPython -I. '
                '-I../../../src/Python-3.11.6/Include '
                '-I../../../src/Python-3.11.6/PC  '
                '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC -I.',
 'PY_ENABLE_SHARED': 1,
 'PY_FORMAT_SIZE_T': '"z"',
 'PY_LDFLAGS': '-pipe -fno-ident '
               '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
               '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
               '-L/c/buildroot/prerequisites/x86_64-w64-mingw32-static/lib '
               '-LC:/buildroot/prerequisites/x86_64-zlib-static/lib '
               '-LC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib',
 'PY_LDFLAGS_NODIST': '-fno-semantic-interposition',
 'PY_LDFLAGS_NOLTO': '-pipe -fno-ident '
                     '-L/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib '
                     '-L/c/buildroot/prerequisites/x86_64-zlib-static/lib '
                     '-L/c/buildroot/prerequisites/x86_64-w64-mingw32-static/lib '
                     '-LC:/buildroot/prerequisites/x86_64-zlib-static/lib '
                     '-LC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib',
 'PY_SQLITE_ENABLE_LOAD_EXTENSION': 1,
 'PY_SQLITE_HAVE_SERIALIZE': 0,
 'PY_SSL_DEFAULT_CIPHERS': 1,
 'PY_SSL_DEFAULT_CIPHER_STRING': 0,
 'PY_STDMODULE_CFLAGS': '-DNDEBUG -g -fwrapv -O3 -Wall -O2 -pipe -fno-ident '
                        '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                        '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                        '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                        '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                        '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                        '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                        '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC '
                        '-fno-semantic-interposition -std=c11 '
                        '-Werror=implicit-function-declaration '
                        '-fvisibility=hidden -D_WIN32_WINNT=0x0602 '
                        '-DPY3_DLLNAME=\'L"libpython3.11.dll"\' '
                        '-DMS_DLL_ID=\'"3.11"\' -fprofile-use '
                        '-fprofile-correction '
                        '-I../../../src/Python-3.11.6/Include/internal '
                        '-IObjects -IInclude -IPython -I. '
                        '-I../../../src/Python-3.11.6/Include '
                        '-I../../../src/Python-3.11.6/PC  '
                        '-I/c/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                        '-I/c/buildroot/prerequisites/x86_64-zlib-static/include '
                        '-I/c/buildroot/prerequisites/x86_64-w64-mingw32-static/include '
                        '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include '
                        '-IC:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/include/ncursesw '
                        '-IC:/buildroot/prerequisites/x86_64-zlib-static/include '
                        '-D__USE_MINGW_ANSI_STDIO=1 -DNCURSES_STATIC -I.',
 'PY_SUPPORT_TIER': 0,
 'Py_DEBUG': 0,
 'Py_ENABLE_SHARED': 1,
 'Py_HASH_ALGORITHM': 0,
 'Py_STATS': 0,
 'Py_TRACE_REFS': 0,
 'QUICKTESTOPTS': '-x test_subprocess test_io test_lib2to3 \\',
 'RCFLAGS': '-DFIELD3=6150 -O COFF --target=pe-x86-64',
 'READELF': 'readelf',
 'RESSRCDIR': 'Mac/Resources/framework',
 'RETSIGTYPE': 'void',
 'RUNSHARED': '',
 'SCRIPTDIR': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib',
 'SETPGRP_HAVE_ARG': 0,
 'SHELL': '/bin/sh',
 'SHLIBS': '-lffi -ltcl -ltk -lole32 -loleaut32 -luuid -lversion -lshlwapi '
           '-lpathcch -lbcrypt',
 'SHLIB_SUFFIX': '.pyd',
 'SIGNED_RIGHT_SHIFT_ZERO_FILLS': 0,
 'SITEPATH': '',
 'SIZEOF_DOUBLE': 8,
 'SIZEOF_FLOAT': 4,
 'SIZEOF_FPOS_T': 8,
 'SIZEOF_INT': 4,
 'SIZEOF_LONG': 4,
 'SIZEOF_LONG_DOUBLE': 16,
 'SIZEOF_LONG_LONG': 8,
 'SIZEOF_OFF_T': 8,
 'SIZEOF_PID_T': 8,
 'SIZEOF_PTHREAD_KEY_T': 0,
 'SIZEOF_PTHREAD_T': 0,
 'SIZEOF_SHORT': 2,
 'SIZEOF_SIZE_T': 8,
 'SIZEOF_TIME_T': 8,
 'SIZEOF_UINTPTR_T': 8,
 'SIZEOF_VOID_P': 8,
 'SIZEOF_WCHAR_T': 2,
 'SIZEOF__BOOL': 1,
 'SOABI': 'cpython-311',
 'SRCDIRS': 'Modules   Modules/_blake2   Modules/_ctypes   Modules/_decimal   '
            'Modules/_decimal/libmpdec   Modules/_io   '
            'Modules/_multiprocessing   Modules/_sha3   Modules/_sqlite   '
            'Modules/_sre   Modules/_xxtestfuzz   Modules/cjkcodecs   '
            'Modules/expat   Objects   Parser   Programs   Python   '
            'Python/frozen_modules   Python/deepfreeze PC',
 'SRC_GDB_HOOKS': '../../../src/Python-3.11.6/Tools/gdb/libpython.py',
 'STATIC_LIBPYTHON': 1,
 'STDC_HEADERS': 1,
 'STRICT_SYSV_CURSES': "/* Don't use ncurses extensions */",
 'STRIPFLAG': '-s',
 'SUBDIRS': '',
 'SUBDIRSTOO': 'Include Lib Misc',
 'SYSLIBS': '-lm',
 'SYS_SELECT_WITH_SYS_TIME': 1,
 'TESTOPTS': '',
 'TESTPATH': '',
 'TESTPYTHON': './python.exe -E',
 'TESTPYTHONOPTS': '',
 'TESTRUNNER': './python.exe -E '
               '../../../src/Python-3.11.6/Tools/scripts/run_tests.py',
 'TESTSUBDIRS': 'ctypes/test \\',
 'TESTTIMEOUT': 1200,
 'TEST_MODULES': 'yes',
 'THREAD_STACK_SIZE': 0,
 'TIMEMODULE_LIB': 0,
 'TIME_WITH_SYS_TIME': 1,
 'TM_IN_SYS_TIME': 0,
 'TZPATH': '/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zoneinfo:/etc/zoneinfo',
 'UNICODE_DEPS': '\\',
 'UNIVERSALSDK': '',
 'UPDATE_FILE': '../../../src/Python-3.11.6/Tools/scripts/update_file.py',
 'USE_COMPUTED_GOTOS': 0,
 'VENVLAUNCHERDIR': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11/venv/scripts/nt',
 'VERSION': '3.11',
 'VPATH': '../../../src/Python-3.11.6',
 'WASM_ASSETS_DIR': '.C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt',
 'WASM_STDLIB': '.C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/lib/python3.11/os.py',
 'WHEEL_PKG_DIR': '',
 'WINDOW_HAS_FLAGS': 1,
 'WINDRES': 'windres',
 'WITH_DECIMAL_CONTEXTVAR': 1,
 'WITH_DOC_STRINGS': 1,
 'WITH_DTRACE': 0,
 'WITH_DYLD': 0,
 'WITH_EDITLINE': 0,
 'WITH_FREELISTS': 1,
 'WITH_LIBINTL': 0,
 'WITH_NEXT_FRAMEWORK': 0,
 'WITH_PYMALLOC': 1,
 'WITH_VALGRIND': 0,
 'X87_DOUBLE_ROUNDING': 0,
 'XMLLIBSUBDIRS': 'xml xml/dom xml/etree xml/parsers xml/sax',
 'abs_builddir': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/build/Python-3.11.6',
 'abs_builddir_b2h': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/build/Python-3.11.6',
 'abs_srcdir': 'C:/buildroot/src/Python-3.11.6',
 'abs_srcdir_b2h': 'C:/buildroot/src/Python-3.11.6',
 'datarootdir': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt/share',
 'exec_prefix': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt',
 'prefix': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt',
 'prefix_b2h': 'C:/buildroot/x86_64-1320-win32-seh-ucrt-rt_v11-rev1/mingw64/opt',
 'srcdir': 'C:/buildroot/src/Python-3.11.6',
 'srcdir_b2h': 'C:/buildroot/src/Python-3.11.6'}


keys_to_replace = [
    'BINDIR', 'BINLIBDEST', 'CONFINCLUDEDIR',
    'CONFINCLUDEPY', 'DESTDIRS', 'DESTLIB', 'DESTSHARED',
    'INCLDIRSTOMAKE', 'INCLUDEDIR', 'INCLUDEPY',
    'LIBDEST', 'LIBDIR', 'LIBPC', 'LIBPL', 'MACHDESTLIB',
    'MANDIR', 'SCRIPTDIR', 'datarootdir', 'exec_prefix',
    'TZPATH',
]

prefix = build_time_vars['BINDIR'][:-4]

for key in keys_to_replace:
    value = build_time_vars[key]
    build_time_vars[key] = value.replace(prefix, sys.prefix)
