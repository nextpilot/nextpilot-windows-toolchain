# 如何安装Python

python官方下载：<https://www.python.org/downloads/windows/>

python国内镜像：<https://registry.npmmirror.com/binary.html?path=python/>

## 普通版本

下载[python-3.12.3-amd64.exe](https://registry.npmmirror.com/-/binary/python/3.12.3/python-3.12.3-amd64.exe)到本地，然后从命令行安装

```bat
rem TargetDir是安装目录，AssociateFiles绑定扩展名，Shortcuts创建快捷方式，Include_doc安装帮助文档
python-3.12.3.exe /quiet TargetDir="python-3.12.3" AssociateFiles=0 Shortcuts=0 Include_doc=0
```

安装其它pip库

```bat
cd python-3.12.3

rem 切换国内源
python -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

rem 安装依赖项
python -m pip install -r ..\requirements.txt
```

## 便携版本

1 下载[python-3.10.11-embed-amd64.zip](https://registry.npmmirror.com/-/binary/python/3.10.11/python-3.10.11-embed-amd64.zip)，并解压到某个文件夹

2 将`python-3.10.11-embed-amd64\python310._pth`**删除**，以便python能够根据规自动添加搜索路径

> 注意：根据[python导入module规则](https://docs.python.org/zh-cn/3/using/windows.html#finding-modules)，如果`pythonxxx._pth`（其中xxx是版本号，比如312）文件存在的情况下，Python不会将工作目录或目标执行脚本添加到搜索路径中，因此我们这里需要将`python310._pth`删除了

`python310._pth`文件中内容一般如下：

```python
python310.zip
.

# Uncomment to run site.main() automatically

import site
```

3 在cmd.exe中执行以下命令安装pip以及所需的依赖项

```bat
cd python-3.10.11-embed-amd64

rem 安装pip
python.exe ..\get-pip.py

rem 切换国内源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

rem 安装依赖项
pip install -r ..\requirements.txt
```

4 安装tkinter，使用[UniExtract](https://github.com/Bioruebe/UniExtract2/releases)对下载`python-3.10.11-amd64.exe`解压，然后按照下面链接拷贝所需文件

<https://blog.csdn.net/nostmabole/article/details/132354099>
