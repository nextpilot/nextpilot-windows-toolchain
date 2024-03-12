@echo off

@REM Setlocal ENABLEDELAYEDEXPANSION

@REM ENV_ROOT
set ENV_ROOT=%~dp0

set PATH=%SystemRoot%\system32;%PATH%
set PATH=C:\WINDOWS\system32;%PATH%

@REM python
set PYTHONHOME=%ENV_ROOT%\toolchain\python\python-3.10.11-embed-amd64
set PYTHONPATH=%PYTHONHOME%
set PATH=%PYTHONHOME%;%PYTHONHOME%\Scripts;%PATH%

@REM arm-gcc
set RTT_EXEC_PATH=%ENV_ROOT%\toolchain\gcc\gcc-arm-none-eabi-10.3-2021.10\bin
set RTT_CC=gcc
set PATH=%RTT_EXEC_PATH%;%PATH%

@REM git
set PATH=%ENV_ROOT%\toolchain\git\MinGit-2.42.0.2-64-bit\cmd;%PATH%

@REM mconf
set PATH=%ENV_ROOT%\toolchain\mconf\kconfig-frontends-3.12.0-windows;%PATH%

@REM env和pkgs
set PKGS_ROOT=%ENV_ROOT%\rtthread\pkg
set PKGS_DIR=%ENV_ROOT%\rtthread\pkg
set PATH=%ENV_ROOT%\rtthread\bin;%PATH%