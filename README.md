# nextpilot-windows-toolchain

#### 介绍

nextpilot-windows-toolchain是nextpilot-flight-control在windows平台下的开发工具链，由于nextpilot-flight-control采用了[RT-Thread](https://gitee.com/rtthread/rt-thread.git)国产操作系统，因此工具链中集成了[RT-Thread ENV](https://gitee.com/RT-Thread-Mirror/env.git)和[Packages](https://gitee.com/RT-Thread-Mirror/packages.git)

#### 目录结构

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

#### 如何使用

1 下载工具链到任意**不包含中文**的路径，比如`c:\nextpilot-windows-toolchain`

2 然后双击运行根目录下的`start.bat`脚本（为了方便下次使用，建议将start.bat添加桌面快捷方式），启动cmd终端

3 在cmd中切换到nextpilot-flight-control的target目录，然后执行配置、编译、仿真等

```bat
rem 切换到sitl虚拟飞行仿真目录
cd nextpilot-flight-control\target\sitl\qemu-vexpress-a9

# 配置编译模块，非必须
menuconfig

# 编译固件
scons -j10

# 启动仿真
qemu.bat
```

#### 常见问题

1 如何将start.bat添加到Windows Terminal

2 如何通过pip安装其它模块

3 如何切换python版本

4 如何切换arm-gcc版本
