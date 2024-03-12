
# 生成FAT32镜像文件

参考链接：<https://club.rt-thread.org/ask/article/a3332c09b89e295f.html>

## Windows生成fat32镜像文件

`fatdisk.exe`是用于**将指定文件夹打包成fat镜像文件**，在运行fatdisk.exe之前，需要先配置`fatdisk.xml`文件：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<fatdisk>
   <disk_size>5120</disk_size>
   <sector_size>4096</sector_size>
   <root_dir>rofs</root_dir>
   <output>rofs.bin</output>
   <strip>1</strip>
</fatdisk>
```

- `disk_size`：想要生成的目标root.bin大小 单位是Kbytes.
- `sector_size`：镜像文件的扇区大小，单位bytes，不同芯片的扇区不一样，一般SD卡是512
- `root_dir`：就是指定要打包的目录名称
- `output`：就是要生成镜像的名称
- `strip`：1表示生成镜像大小为root_dir文件夹里面文件的实际大小。0表示镜像大小为disk_size，不够的后面空白数据填0xff, 填充到想要的大小。

## Linux生成fat32镜像文件

linux环境下可以使用`mtools`生成`fat32`镜像

```shell
# 生成sd0_fat32镜像，bs是sector size，count是数量
dd if=/dev/zero of=sd0_fat32.img bs=1024 count=92160

# 格式化镜像文件
mkfs.fat sd0_fat32.img

# 将~/rootfs目录下的所有文件拷贝到sd0_fat32.img镜像中， 其中
# -/是递归拷贝
# -i是镜像名
# ::代表驱动器，也就是镜像内部
mcopy -/ -i sd0_fat32.img ~/rootfs/* ::/

# 验证拷贝是否成功，使用mdir显示镜像中的文件内容
mdir -i sd0_fat32.img
```
