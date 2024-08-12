@echo off

title NextPilot Windows Toolchain

rem Simple "ver" prints empty line before Windows version
rem Use this construction to print just a version info
@REM cmd /d /c ver | "%windir%\system32\find.exe" "Windows"

@REM chcp 65001 > nul

echo.
echo ******************************************************************
echo *      _   __             __   ____   _  __        __
echo *     / ^| / /___   _  __ / /_ / __ \ (_)/ /____   / /_
echo *    /  ^|/ // _ \ ^| ^|/_// __// /_/ // // // __ \ / __/
echo *   / /^|  //  __/_^>  ^< / /_ / ____// // // /_/ // /_
echo *  /_/ ^|_/ \___//_/^|_^| \__//_/    /_//_/ \____/ \__/
echo *
echo * Copyright All Reserved (C) 2015-2024 NextPilot Development Team
echo ******************************************************************


if /i not "%~dp0"=="C:\nextpilot-windows-toolchain\" (
  echo.
  echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  echo ERROR: Toolchain must be installed in "C:\nextpilot-windows-toolchain"
  echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
)

rem Do not repeat run
if not "%NdtInited%" == "" goto :eof


REM ============= Change Command Prompt ==================

:set_command_prompt

rem Run in ConEmu
if not "%ConEmuBaseDir%" == "" goto :add_toolchain_path

rem Now we form the command prompt
rem This will start prompt with `User@PC `
set PROMPT0=$E[m$E[32m$E]9;8;"USERNAME"$E\@$E]9;8;"COMPUTERNAME"$E\$S

rem Followed by colored `Path`
set PROMPT1=%PROMPT0%$E[92m$P$E[90m
if NOT "%PROCESSOR_ARCHITECTURE%" == "AMD64" (
  if "%PROCESSOR_ARCHITEW6432%" == "AMD64" if "%PROCESSOR_ARCHITECTURE%" == "x86" (
    rem Use another text color if cmd was run from SysWow64
    set PROMPT1=%PROMPT0%$E[93m$P$E[90m
  )
)

rem Carriage return and `$` or `>`
rem Spare `$E[90m` was specially added because of GitShowBranch.cmd
if "%ConEmuIsAdmin%" == "ADMIN" (
  set PROMPT2=$_$E[90m$$
) else (
  set PROMPT2=$_$E[90m$G
)

rem Finally reset color and add space
set PROMPT3=$E[m$S$E]9;12$E\
prompt %prompt1%%prompt2%%prompt3%


REM ============= Activate Python Venv ==================

:activate_python_venv

@REM set VENV_ROOT=%~dp0\.venv
@REM if not exist "%VENV_ROOT%" (
@REM   echo Create Python Venv
@REM   %~dp0\toolchain\python\python-3.11.9-amd64\python.exe -m pip uninstall pip -y
@REM   %~dp0\toolchain\python\python-3.11.9-amd64\python.exe -m ensurepip
@REM   %~dp0\toolchain\python\python-3.11.9-amd64\python.exe -m venv "%VENV_ROOT%"
@REM   echo Activate Python Venv in %VENV_ROOT%
@REM   %VENV_ROOT%\Scripts\activate.bat
@REM   echo Install Python Packages
@REM   pip install -r  %~dp0\toolchain\python\requirements.txt
@REM ) else (
@REM    echo Activate Python Venv in %VENV_ROOT%
@REM   %VENV_ROOT%\Scripts\activate.bat  
@REM )


REM ============= Add Toolchain Path ==================

:add_toolchain_path

@REM Setlocal ENABLEDELAYEDEXPANSION

@REM NDT_ROOT
set NDT_ROOT=%~dp0

set PATH=%SystemRoot%\system32;%PATH%

@REM python
set PYTHONHOME=%NDT_ROOT%\toolchain\python\python-3.11.9-amd64
set PYTHONPATH=%PYTHONHOME%
set PATH=%PYTHONHOME%;%PYTHONHOME%\Scripts;%PATH%

@REM arm-gcc
set GCC_ARM_HOME=%NDT_ROOT%\toolchain\gcc\gcc-arm-none-eabi-10.3-2021.10
set GCC_EXEC_PATH=%NDT_ROOT%\toolchain\gcc\gcc-arm-none-eabi-10.3-2021.10\bin
set RTT_EXEC_PATH=%GCC_EXEC_PATH%
set RTT_CC=gcc
set PATH=%RTT_EXEC_PATH%;%PATH%

@REM git
set PATH=%NDT_ROOT%\toolchain\git\MinGit-2.42.0.2-64-bit\cmd;%PATH%

@REM mconf
set PATH=%NDT_ROOT%\toolchain\mconf\kconfig-frontends-3.12.0-windows;%PATH%

@REM fatdisk
set PATH=%NDT_ROOT%\toolchain\fatdisk;%PATH%

@REM qemu
set QEMU_HOME=%NDT_ROOT%\toolchain\qemu\qemu-w64-v8.2.0
set PATH=%NDT_ROOT%\toolchain\qemu\qemu-w64-v8.2.0;%PATH%

@REM env和pkgs
set ENV_ROOT=%~dp0rtthread
set PKGS_ROOT=%ENV_ROOT%\packages
set PKGS_DIR=%ENV_ROOT%\packages
@REM set PATH=%ENV_ROOT%\bin;%PATH%


@REM set inited flag
@REM set NdtInited=1


REM ============= Inject Clink Tools ==================

:inject_clink

rem Run in ConEmu
if not "%ConEmuBaseDir%" == "" goto :eof

%~dp0\toolchain\conemu\ConEmuPack.230724\ConEmu\clink\clink.bat inject