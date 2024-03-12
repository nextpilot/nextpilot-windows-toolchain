# 如何安装Python

1 从Python官网下载所需版本的[Windows embeddable package (64bit)](https://www.python.org/downloads/windows/)，并解压到某个文件夹，比如`python-3.10.11-embed-amd64`

2 将`python-3.10.11-embed-amd64\python310._pth`**删除**，以便python能够根据规自动添加搜索路径

> 注意：根据[python导入module规则](https://docs.python.org/zh-cn/3/using/windows.html#finding-modules)，如果`pythonxxx._pth`（其中xxx是版本号，比如312）文件存在的情况下，Python并不会将工作目录或目标执行脚本添加到搜索路径中。

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
rem 安装依赖项
pip install -r ..\requirements.txt
```
