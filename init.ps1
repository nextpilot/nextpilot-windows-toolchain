echo "******************************************************************"
echo "*      _   __             __   ____   _  __        __"
echo "*     / | / /___   _  __ / /_ / __ \ (_)/ /____   / /_"
echo "*    /  |/ // _ \ | |/_// __// /_/ // // // __ \ / __/"
echo "*   / /|  //  __/_>  < / /_ / ____// // // /_/ // /_"
echo "*  /_/ | _/ \___//_/| _| \__//_/    /_//_/ \____/ \__/"
echo "*"
echo "* Copyright All Reserved (C) 2015-$(Get-Date -Format 'yyyy') NextPilot Development Team"
echo "******************************************************************"

function  add_windows_terminate() {
    # npdt的配置
    $npdt = [PSCustomObject]@{
        commandline = "`"$env:windir\System32\cmd.exe`" /K `"$PSScriptRoot\init.bat`"";
        guid        = "{c06ccb37-4fca-4609-b969-30aa1b3d8549}";
        hidden      = $false;
        # icon              = "";
        name        = "Nextpilot Windows Toolchain";
        # source            = "Nextpilot.WindowsToolchain";
        # startingDirectory = "";
    }

    # C:\Users\zhanfuyu\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
    $wt_setting_file = "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"

    if (Test-Path "$wt_setting_file") { 
        # 读取wt的配置文件
        $wt_setting = (Get-Content "$wt_setting_file" -Raw)  | ConvertFrom-Json

        # 移除guid一样的配置，然后将npdt添加到末尾
        $wt_setting.profiles.list = $wt_setting.profiles.list.where({ $npdt.guid -ne $_.guid }) + $npdt 
        
        # 将npdt设置为默认终端
        $wt_setting.defaultProfile = $npdt.guid
        
        #  将wt配置写入到文件
        $wt_setting | ConvertTo-Json -Depth 10  | Set-Content -Path $wt_setting_file
    }
}

function add_context_menu() {

}


$need_install = $false

if (-not (Test-Path "$PSScriptRoot\install.lock")) {
    $need_install = $true
}

if ($need_install) {
    # 添加到windows terminate
    add_windows_terminate
    # 添加右键快捷菜单
    add_context_menu

    echo ""> "$PSScriptRoot\install.lock"
}

$custom_env_path = "$env:SystemRoot\system32"

# fatdisk
$custom_env_path += "; $PSScriptRoot\toolchain\fatdisk"

# git
$custom_env_path += "; $PSScriptRoot\toolchain\git\MinGit-2.42.0.2-64-bit\cmd"

# python
$custom_env_path += "; $PSScriptRoot\toolchain\python\python-3.10.11-embed-amd64"

# arm-gcc
$env:GCC_ARM_HOME = "$PSScriptRoot\toolchain\gcc\gcc-arm-none-eabi-10.3-2021.10"
$env:GCC_EXEC_PATH = "$env:GCC_ARM_HOME\bin"
$env:RTT_EXEC_PATH = "$env:GCC_EXEC_PATH"
$env:RTT_CC = "gcc"
$custom_env_path += "; $env:GCC_EXEC_PATH"

# qemu
$env:QEMU_HOME = "$PSScriptRoot\toolchain\qemu\qemu-w64-v8.2.0"
$custom_env_path += "; $env:QEMU_HOME"

# pkgs
$env:PKGS_ROOT = "$PSScriptRoot\rthread"
$env:PKGS_DIR = "$PSScriptRoot\rthread"

# update env:path
$env:PATH = "$custom_env_path; $env:PATH"

