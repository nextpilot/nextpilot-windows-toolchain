# 如何安装Python

1. 从Python官网下载所需版本的[Windows embeddable package (64bit)](https://www.python.org/downloads/windows/)，并解压在当前目录的某个文件夹，比如`python-3.12.0-embed-amd64`


2. 将`python-3.12.0-embed-amd64\python312._pth`中`#import site`的 `#` 号去掉，即：

```python
python312.zip
.

# Uncomment to run site.main() automatically
import site
```

3. 在cmd.exe中执行以下命令安装pip以及所需的依赖项

```bat
cd python-3.12.0-embed-amd64
rem 安装pip
python.exe ..\get-pip.py
rem 安装依赖项
python.exe pip3 install -r ..\requirements.txt
```