# Nextpilot Develop Toolchain for Windows

nextpilot-windows-toolchain是nextpilot-flight-control在windows平台下的开发工具链，主要集成了以下开发工具：

|工具|版本|路径|
|---|---|---|
|python|python-3.11.9-amd64|toolchain/python/python-3.11.9-amd64|
|gcc-arm|gcc-arm-none-eabi-10.3-2021.10|toolchain/gcc/gcc-arm-none-eabi-10.3-2021.10|
|qemu|qemu-w64-v8.2.0|toolchain/qemu/qemu-w64-v8.2.0|
|git|MinGit-2.42.0.2-64-bit|toolchain/git/MinGit-2.42.0.2-64-bit|

## 目录结构

```
├─document
├─rtthread         # 保存rt-thread官方工具和代码
│  ├─bin           # menuconfig/pkgs/env等可执行文件，本质是rtt-env的exe封装
│  ├─env           # rtt-env的python代码
│  └─pkg           # rtt-pkg的kconfig文件
├─toolchain        # 第三方工具链，主要是python/arm-gcc等
│  ├─gcc           # arm-gcc，用于编译固件
│  ├─git           # git-for-windows，用于版本管理
│  ├─mconf         # kconfig-frontends，在windows下使用kconfig
│  ├─python        # python，已经添加了所需的模块
│  ├─qemu          # qemu，硬件模拟器，用于运行飞行仿真
│  └─vscode        # vscode，文本编辑器，已安装所需的插件
└─workspace        # 工作目录
```

## 如何使用

1 下载工具链到`c:\nextpilot-windows-toolchain`，**当前只支持该路径**，不支持其它自定义路径哈

> 安装pip软件包时，会将python绝对路径的写入exe文件中，如果将toolchain安装到其它路径，运行`scons.exe`等工具的时候会提示找不到python.exe，因此暂时只支持`c:\nextpilot-windows-toolchain`这个路径。

2 双击根目录下的`start.bat`脚本（为了方便下次使用，建议将start.bat添加桌面快捷方式），启动cmd终端

3 在cmd中切换到`nextpilot-flight-control`的bsp目录，然后执行配置、编译、仿真等

```bat
rem 切换到sitl虚拟飞行仿真目录
cd nextpilot-flight-control\bsps\sitl\qemu

# 配置编译模块，非必须
scons --menuconfig

# 编译固件
scons -j10

# 启动仿真
qemu.bat
```

## 常见问题

### 如何将添加到Windows Terminal

### 如何添加到右键菜单

### 如何安装其它pip模块

当前已集成pip工具以及开发所需pip包，如果还希望安装其他模块，直接通过`pip install`安装即可。如果是国内环境，建议切换pip源为：

```
# 使用清华大学pip源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 使用阿里云pip源
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

```

### 如何切换python版本

当前已集成了`python-3.11.9-amd64`，由于项目中部分依赖的软件包仅支持python3，因此nextpilot不支持python2。如果希望切换到其它python版本，请参考[toolchain/python/README.md](toolchain/python/README.md)安装python后，再修改[init.bat](init.bat)中python路径为新的python路径即可。

### 如何切换arm-gcc版本

当前已集成了`gcc-arm-none-eabi-10.3-2021.10`，安装其他版本gcc-arm请参考[toolchain/gcc/README.md](toolchain/gcc/README.md)，并将[init.bat](init.bat)中关于gcc-arm的路径修改为新版本gcc-arm路径。
