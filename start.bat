@echo off

set PATH=%SystemRoot%\system32;%PATH%
set PATH=C:\WINDOWS\system32;%PATH%

set ENV_ROOT=%~dp0
set PYTHONPATH=%ENV_ROOT%\python\python-3.10.11-embed-amd64
set PYTHONHOME=%ENV_ROOT%\python\python-3.10.11-embed-amd64
set RTT_EXEC_PATH=%ENV_ROOT%\gcc\gcc-arm-none-eabi-10.3-2021.10\bin
set RTT_CC=gcc
rem set PKGS_ROOT=%ENV_ROOT%\packages
rem set SCONS=%PYTHONPATH%\Scripts

rem set PATH=%ENV_ROOT%\tools\git-2.41.0-32-bit\cmd;%PATH%
rem set PATH=%ENV_ROOT%\tools\bin;%PATH%
set PATH=%RTT_EXEC_PATH%;%PATH%
set PATH=%PYTHONHOME%;%PATH%
set PATH=%PYTHONPATH%;%PYTHONHOME%\Scripts;%PATH%
rem set PATH=%SCONS%;%PATH%
set PATH=%ENV_ROOT%\env;%ENV_ROOT%\mconf\mconf-v4.6.0.0-idf-20190628-win32;%PATH%