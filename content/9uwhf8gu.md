# Android11+ AIDL：专为提升应用性能而生！

> 公众号: Android系统攻城狮
> 发布时间: 1970-01-01 08:33:43
> 原文链接: https://mp.weixin.qq.com/s?__biz=MzU2NTI3NDI5MQ==&mid=2247485515&idx=1&sn=518a69ed57f50e2a6675a8bc0410df2d&chksm=fcbf7b97cbc8f2810e7cbb013767378563937226c743baca48d671b434fc55d195ea9948b28a

---
**点击下方👇关注** **Android系统攻城狮**

每日充电：OS+MultiMedia学习之旅

* * *

## 1.前言

**学习理念：一次理解一个知识点**

**难度：★★★********★******☆************

**源码环境：Android 12**

**硬件环境：SDM845**

**阅读时间：1.5分钟**

-   **接着上一篇****[Android HAL发展历程：探索HAL到HIDL四个阶段的演进过程](http://mp.weixin.qq.com/s?__biz=MzU2NTI3NDI5MQ==&mid=2247485390&idx=1&sn=f579ff513e9ba1c0dd55a5ef8591e527&chksm=fcbf7412cbc8fd04b056aaa60842bfd6ec192677cebf34b2fec0802c530016716ac336de0ea3&scene=21#wechat_redirect)****文章，我们已经介绍了HAL到HIDL发展的历程。**

-   **Android11版本开始，AIDL引入实现HAL同样的功能，可以调用HAL，也可以直接和内核驱动通信。**

-   **下面看一下HIDL和AIDL通信过程，AIDL比起传统通信方式有哪些优点？**

-   **接着****实现一个AIDL实现用例，读者可以和上一篇文章HIDL实现服务做一个对比，看看它们之间的差异在哪里？**

-   **1.先看一个HIDL模式通信路线图：**


![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eZ1UicZh3icjnZx8mEIXZicYN2HgeSeno6ibeDMcfnt18yGJ4VYJltBgNXsicBVPFnEywwQcByv1Wmg9Dahk19eKang/640?wx_fmt=jpeg&from=appmsg#imgIndex=0)

图一

-   **2.再看一个AIDL模式通信路线图：**


![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eZ1UicZh3icjnZx8mEIXZicYN2HgeSeno6ib9FS5CWx1KQq8PlkLelbCZL7oorUH4xicSWTFs0ic6HQFlUNicuUpVjSiag/640?wx_fmt=jpeg&from=appmsg#imgIndex=1)

图二

-   通过图一和图二比较，就能知道谷歌为什么要在Android 10以后逐渐去除HIDL通信模式。

-   AIDL优势很明显，它在应用端直接获取AIDL Service后，可以直接给AIDL的服务端发送IPC通信，在服务端直接调用**HAL的API**或者**直接通过open("/dev/xxx")与驱动通信**。

-   与传统的AIDL比起来，中间少了两三个通信环节，效率会显著提升。

-   **下面写一个AIDL使用Binder IPC通信的例子。**


## 2.AIDL客户端

**1.创建aidl接口**

`# mkdir -p hardware/interfaces/invcase/aidl/android/hardware/invcase # emacs IInvcase.aidl package android.hardware.invcase;   @VintfStability interface IInvcase {     String getChars();     void putChars(in String msg); } `

**2.创建Android.bp**

`# cd hardware/interfaces/invcase/aidl # emacs Android.bp aidl_interface {     name: "android.hardware.invcase",     vendor: true,     srcs: ["android/hardware/invcase/*.aidl"],     stability: "vintf",     owner: "vqtrong",     backend: {         cpp: {             enabled: false,         },         java: {             sdk_version: "module_current",         },     }, } `

****3.编译与配置****

```
1.执行以下命令：编译报错# mmm hardware/interfaces/invcase/aidl 2.执行以下操作后，再编译aidl# m android.hardware.invcase-update-api -j12 3.再编译aidl# mmm hardware/interfaces/invcase/aidl 4.将invacase模块配置编译到系统# emacs build/make/target/product/base_vendor.mkPRODUCT_PACKAGES += android.hardware.invcase
```

-   到此AIDL客户端创建完成，接下来创建AIDL Server端。


## 3.AIDL Server端

**1.AIDL对应Server端头文件实现**

`# emacs hardware/interfaces/invcase/aidl/default/Invcase.h #pragma once #include <aidl/android/hardware/invcase/BnInvcase.h> namespace aidl { namespace android { namespace hardware { namespace invcase {   class Invcase : public BnInvcase {     public:         //AIDL：String getChars();         ndk::ScopedAStatus getChars(std::string* _aidl_return);         //AIDL：void putChars(in String msg);         ndk::ScopedAStatus putChars(const std::string& in_msg); }; }  }   }  }`

**2.****AIDL对应Server端c++实现**

`# emacs hardware/interfaces/invcase/aidl/default/Invcase.cpp #define LOG_TAG "Invcase"   #include <utils/Log.h> #include <iostream> #include <fstream> #include "Invcase.h"   namespace aidl {     namespace android {         namespace hardware {             namespace invcase {                 //String getChars();                 ndk::ScopedAStatus Invcase::getChars(__unused std::string* _aidl_return) {                     std::string str = "I am from HAL layer";                     *_aidl_return = str;                     ALOGE("%s, %s(), line = %d, HAL: send_to_app: %s",__FILE__,__FUNCTION__,__LINE__,str.c_str());                     return ndk::ScopedAStatus::ok();                 }                 //void putChars(in String msg);                 ndk::ScopedAStatus Invcase::putChars(__unused const std::string& in_msg) {                     ALOGE("%s, %s(), line = %d, HAL: recive_from_app = %s",__FILE__,__FUNCTION__,__LINE__,in_msg.c_str());                     return ndk::ScopedAStatus::ok();                 }             }          }      }  }`

-   在Invcase::getChars和Invcase::putChars函数中添加对驱动程序的访问即可。在这里我只是写了打印语句。

-   到这里AIDL的Server端也实现完成，我们要将实现的内容注册成一个AIDL服务，可以通过Binder完成IPC通信。


## 4.创建AIDL IPC通信

**1.注册A****IDL服务**

`# emacs hardware/interfaces/invcase/aidl/default/service.cpp #define LOG_TAG "Invcase" #include <android-base/logging.h> #include <android/binder_manager.h> #include <android/binder_process.h> #include <binder/ProcessState.h> #include <binder/IServiceManager.h> #include "Invcase.h" using aidl::android::hardware::invcase::Invcase; using std::string_literals::operator""s;   int main() {     android::ProcessState::initWithDriver("/dev/vndbinder");      ABinderProcess_setThreadPoolMaxThreadCount(0);     ABinderProcess_startThreadPool();       std::shared_ptr<Invcase> invcase = ndk::SharedRefBase::make<Invcase>();     const std::string name = Invcase::descriptor + "/default"s;     ALOGE("%s, %s(), line = %d, descriptor = %s, name = %s,",__FILE__,__FUNCTION__,__LINE__,Invcase::descriptor,name.c_str());          if(AServiceManager_addService(invcase->asBinder().get(), name.c_str()) != STATUS_OK) {         ALOGE("Failed to register IInvcase service");         return -1;     }          ALOGE("IInvcase service starts to join service pool");     ABinderProcess_joinThreadPool();     return EXIT_FAILURE; } `

-   其中name就是AIDL服务名，它启动起来以后，我们通过service命令看到它。


****2.创建Android.bp****

`# emacs hardware/interfaces/invcase/aidl/default/Android.bp cc_binary {     name: "android.hardware.invcase-service",     vendor: true,     relative_install_path: "hw",     init_rc: ["android.hardware.invcase-service.rc"],     vintf_fragments: ["android.hardware.invcase-service.xml"],       srcs: [         "Invcase.cpp",         "service.cpp",     ],       cflags: [         "-Wall",         "-Werror",     ],       shared_libs: [         "libbase",         "liblog",         "libhardware",         "libbinder_ndk",         "libbinder",         "libutils",         "android.hardware.invcase-V1-ndk_platform",     ], }`

******3.编译、添加到系统设置******

`1.编译 # mmm hardware/interfaces/invcase/aidl/default # adb push out/target/product/xxx/vendor/lib64/android.hardware.invcase-V1-ndk_platform.so /vendor/lib64 # adb push out/target/product/xxx/vendor/bin/hw/android.hardware.invcase-service /vendor/bin/hw   2.将hal服务添加到系统编译 # emacs build/make/target/product/base_vendor.mk PRODUCT_PACKAGES += \     android.hardware.invcase \     android.hardware.invcase-service \     3.将hal服务增加到init.rc并启动 # emacs hardware/interfaces/invcase/aidl/default/android.hardware.invcase-service.rc service android.hardware.invcase-service /vendor/bin/hw/android.hardware.invcase-service         interface aidl android.hardware.invcase.IInvcase/default         class hal         user system         group system   .对外公开AIDL接口 # emacs hardware/interfaces/invcase/aidl/default/android.hardware.invcase-service.xml <manifest version="1.0" type="device">     <hal format="aidl">         <name>android.hardware.invcase</name>         <version>1</version>         <fqname>IInvcase/default</fqname>     </hal> </manifest>   5..将新的包增加到框架兼容性矩阵中 # emacs hardware/interfaces/compatibility_matrices/compatibility_matrix.6.xml # emacs hardware/interfaces/compatibility_matrices/compatibility_matrix.current.xml <hal format="aidl" optional="true">     <name>android.hardware.invcase</name>     <version>1</version>     <interface>         <name>IInvcase</name>         <instance>default</instance>     </interface> </hal> `

-   到这一步，基本设置已经完成，下面将它Run起来跑一下试试。


## 5.调试运行

`push编译出来依赖的so、.rc、xml、bin等 1.invcase启动服务 # adb push out/target/product/xxx/vendor/etc/init/android.hardware.invcase-service.rc /vendor/etc/init   2.invcase hal添加到系统 # adb push out/target/product/xxx/vendor/etc/vintf/manifest/android.hardware.invcase-service.xml /vendor/etc/vintf/manifest   3.hal调用aidl生成的api，实现服务 # adb push out/target/product/xxx/vendor/bin/hw/android.hardware.invcase-service /vendor/bin/hw   4.aidl生成cpp的api，提供给HAL服务使用 # adb push out/target/product/xxx/vendor/lib64/android.hardware.invcase-V1-ndk_platform.so /vendor/lib64     5.运行hal服务 # setenforce 0 # /vendor/bin/hw/android.hardware.invcase-service 6.运行hal服务 # start android.hardware.invcase-service 注意：使用start的方式启动失败，需要配置sepolicy，自行配置即可。 `

-   到这一步，我们的AIDL服务已经可以跑起来，毕竟Android默认开启了SeLinux策略，那么我们怎么添加SeLinux Policy？


## 6.增加Selinux Policy策略

`1.定义一个新类型 # emacs system/sepolicy/prebuilts/api/32.0/public/hwservice.te # emacs system/sepolicy/public/hwservice.te type hal_invcase_hwservice, hwservice_manager_type;   2.设置兼容性 忽略api为31，及以下的。 # emacs system/sepolicy/prebuilts/api/32.0/private/compat/31.0/31.0.ignore.cil # emacs system/sepolicy/private/compat/31.0/31.0.ignore.cil (type new_objects) (typeattribute new_objects) (typeattributeset new_objects     ( new_objects         hal_invcase_hwservice     ) )   3.添加服务路径 # emacs system/sepolicy/vendor/file_contexts /(vendor|system/vendor)/bin/hw/android\.hardware\.invcase-service u:object_r:hal_invcase_service_exec:s0   4.设置服务上下文接口 # emacs system/sepolicy/prebuilts/api/32.0/private/hwservice_contexts # emacs system/sepolicy/private/hwservice_contexts android.hardware.invcase::IInvcase     u:object_r:hal_invcase_hwservice:s0     5.声明属性 # emacs system/sepolicy/prebuilts/api/32.0/public/attributes # emacs system/sepolicy/public/attributes hal_attribute(invcase);   attribute hal_invcase; attribute hal_invcase_client; attribute hal_invcase_server;   6.定义默认域 # emacs system/sepolicy/vendor/hal_invcase_service.te type hal_invcase_service, domain; hal_server_domain(hal_invcase_service, hal_invcase) type hal_invcase_service_exec, exec_type, vendor_file_type, vendor_file_type, file_type; init_daemon_domain(hal_invcase_service)   7.设置binder策略 # emacs system/sepolicy/prebuilts/api/32.0/public/hal_invcase.te # emacs system/sepolicy/public/hal_invcase.te binder_call(hal_invcase_client, hal_invcase_server) binder_call(hal_invcase_server, hal_invcase_client) hal_attribute_hwservice(hal_invcase, hal_invcase_hwservice)   8.将system_server声明为HAL服务的客户端 # emacs system/sepolicy/prebuilts/api/32.0/private/system_server.te # emacs system/sepolicy/private/system_server.te hal_client_domain(system_server, hal_invcase)     9.将invcase hal服务添加系统编译中 # emacs build/target/product/base_vendor.mk + PRODUCT_PACKAGES += \ +     android.hardware.invcase-service \   注意：vendor ndk的so库被编译到system.img中。`

## 7.总结一下

-   AIDL本质是一个C/S架构通信模型，它可以自动生成后端服务代码，不止可以生成C++接口，还可以生成java、ndk、rust服务端目标代码。

-   AIDL支持服务端可以调用HAL接口，也可以直接和驱动通信，这个根据需求来定制自己的AIDL服务。总体来说，它的通信性能和稳定性上也有了很大的提升。


![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eZ1UicZh3icjlJVdGj557jTRJMjRiaOHiaiaCo20kF2JGdVmeRMWrtYOsaibMYJRziaNMn9RH6vnic66f1XjJdmTcxe2hg/640?wx_fmt=jpeg&from=appmsg#imgIndex=2)

**★★★★★★★★★★< END >****★****★★★★★★★★★**

* * *

**粉丝专属福利, 私信【****1024****】,****限时领取****多媒体系统****学习资料.**

**精彩文章合集**

  **专栏推荐**

☞【专栏一】[基础原理系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2NTI3NDI5MQ==&action=getalbum&album_id=2318389963295375364#wechat_redirect)

☞【专栏二】[Android音频系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2NTI3NDI5MQ==&action=getalbum&album_id=2789502080410648581#wechat_redirect)

☞【专栏三】[Android编解码系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2NTI3NDI5MQ==&action=getalbum&album_id=3055046478127366144#wechat_redirect)

☞【专栏四】[Android相机系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2NTI3NDI5MQ==&action=getalbum&album_id=3003914888358068225#wechat_redirect)

☞【专栏五】[](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzUxMjEyNDgyNw==&action=getalbum&album_id=1598710257097179137#wechat_redirect)[Android图形系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2NTI3NDI5MQ==&action=getalbum&album_id=3028698257297965057#wechat_redirect)

☞【专栏六】[](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzUxMjEyNDgyNw==&action=getalbum&album_id=1502410824114569216#wechat_redirect)[Android系统系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2NTI3NDI5MQ==&action=getalbum&album_id=2987704999789133826#wechat_redirect)

☞【专栏七】[](http://mp.weixin.qq.com/s?__biz=MzUxMjEyNDgyNw==&mid=2247496985&idx=1&sn=c3d5e8406ff328be92d3ef4814108cd0&chksm=f96b87edce1c0efb6f60a6a0088c714087e4a908db1938c44251cdd5175462160e26d50baf24&scene=21#wechat_redirect)[WSL进击AOSP系列](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzU2NTI3NDI5MQ==&action=getalbum&album_id=1400721183586484224#wechat_redirect)

********原创不易****, 谢谢****支持~~********