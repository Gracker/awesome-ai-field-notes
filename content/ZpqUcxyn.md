# 如何配置Clion编写aosp的c++程序使用aidegen工具编译生成cmake文件，该方法适用于无法使用asfp I

> 发布时间: 2025-03-18T05:54:25.000Z
> 原文链接: https://juejin.cn/post/7482769108523171879

---

# 如何配置Clion编写aosp的c++程序

[二十四桥明月夜ya](/user/1209900381768872/posts)

2025-03-18 703 阅读2分钟

专栏：

Android

关注

`该方法适用于无法使用asfp IDE，windows挂载服务器磁盘并使用SSH编译AOSP，Linux直接编译AOSP等环境。`

`asfp IDE需要linux环境，需要直接打开ipr，修改.idea里的模块，比较麻烦，其实并不适用。`

`推荐使用下面的aidegen生成cmakeLists.txt来进行索引。`

`Android Studio编译frameworks或packages下都可以使用该方式，修改对应从IDE即可，这里仅对clion处理native程序或so库。`

## 1、编译aosp的aidegen

shell

 体验AI代码助手

 代码解读

复制代码

`source->lunch # 不用再说了 make aidegen # 编译aidegen工具`

## 2、使用aidegen来编译需要写的c++程序

首先需要了解aidegen的基础命令 [Android AIDEGen tools基本使用-CSDN博客](https://link.juejin.cn?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_44008788%2Farticle%2Fdetails%2F127947396 "https://blog.csdn.net/weixin_44008788/article/details/127947396")

无法贴出源码和图片，故只能文字说明。

这里只说clion的模块编译

shell

 体验AI代码助手

 代码解读

复制代码

`aidegen <moduleName> -n -s`

执行后，会进行ninja编译等，编译共享库，一般先执行make 会缩短时间。

等待一会，会输出日志

shell

 体验AI代码助手

 代码解读

复制代码

`Generate blueprint json successfully. 2025-03-18 11:42:09 common_util.py:89:DEBUG: aidegen.lib.module_info_util.generate_merged_module_info takes: 239.01s 2025-03-18 11:42:10 module_info.py:56:DEBUG: Loading /data1/aaa/workspace/android-14/out/soong/merged_module_info.json as module-info. 2025-03-18 11:42:12 project_info.py:587:INFO: Ready to build the jar or srcjar files. Files count = 0 2025-03-18 11:42:12 project_info.py:594:DEBUG: Build Time,  duration = 0.0001690387725830078 Warning: Native modules build skipped: moduleName. 2025-03-18 11:42:12 common_util.py:89:DEBUG: __main__.main_without_message takes: 552.79s INFO: To report an AIDEGen tool problem, please use this link: https://goto.google.com/aidegen-bug 2025-03-18 11:42:12 clearcut_client.py:130:DEBUG: Scheduling thread to run in 0.000000 seconds`

这时候会如果有网络环境应该会执行其他操作，但是我这边没有网络，故会卡住。直接ctrl+c退出即可

## 3、使用cmake文件

在目录`out/development/ide/clion/...`，"..."表示模块所在位置。

进入模块所在位置下，找到模块内部的cmakeLists文件，有**两个cmake**文件，对比就能看出，外部引用了内部的cmake文件。

然后将其拷贝到代码所在的位置即可，打开clion，clion会自动识别。

## 4、修改cmake文件

-   第三行的set（ANDROID\_ROOT ...)修改为自身对应的位置
-   第四行的c和第五行的cxx 编译器注释掉，使用clion自带的即可
-   注释掉下面所有的set，只要include和file的标签

点击右上角cmake的配置文件修改后出现的刷新图标即可，索引会自动设置成功。

## 5、修改clion的索引慢的配置设置

进入设置->高级设置->Clion->勾选使用ReSharper c++语言引擎

设置->高级设置->Clangd->勾选 使用Clangd的索引器、在clangd中保留过时的AST

重启clion即可。

在github上发现一个有趣的项目： [i-rtfsc/as-aosp: 此工程可以使用android studio快速的导入aosp framework(java、native部分并支持跳转)、 aosp 系统app、 国内某些厂商扩展的fwk代码。](https://link.juejin.cn?target=https%3A%2F%2Fgithub.com%2Fi-rtfsc%2Fas-aosp%3Ftab%3Dreadme-ov-file%23ext "https://github.com/i-rtfsc/as-aosp?tab=readme-ov-file#ext") 请大家放心使用。是否有对aosp更好的解决方案。