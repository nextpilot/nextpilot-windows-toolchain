## arm-gcc

新版本下载：<https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads>

老版本下载：<https://developer.arm.com/downloads/-/gnu-rm>

## mingw64

下载地址：<https://github.com/niXman/mingw-builds-binaries/releases>

当前 mingw64 版本为`x86_64-13.2.0-release-win32-seh-ucrt-rt_v11-rev0`，

- 处理器架构：x86_64
- GCC 版本：13.2.0
- Threads接口：
  - Windows 选择 win32
  - Linux 和 Mac OS选择 posix
- 异常机制：
  - SJLJ：支持32/64位系统
  - DWARF：仅支持32位系统，性能优于SJLJ
  - SEH：仅支持64位系统，这是一种更高效的异常处理方式，尤其适用于 Windows 平台。
- C运行库：
  - MSVCRT：较早的C运行时库版本，它在所有版本的Windows中都默认可用。这个库由于向后兼容性问题，已经过时，不兼容C99标准，并且缺少一些功能。
  - UCRT：一个更新的C运行时库版本，它是为了更好地支持最新的Windows版本以及提供更好的标准一致性而编写的。从Windows 10开始，UCRT作为MSVCRT的替代品被引入，并且可以安装在早期版本的Windows上。
