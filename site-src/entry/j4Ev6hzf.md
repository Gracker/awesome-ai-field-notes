---
title: '查看浏览器Browsers的内核版本, 可以用 navigator.userAgent - 掘金'
sidebar: false
---

::: info
[← 返回基础设施](/infra)
:::

# 查看浏览器Browsers的内核版本, 可以用 navigator.userAgent - 掘金

> Cubox 收藏 — 查看浏览器Browsers的内核版本, 可以用 navigator.userAgent - 掘金

🔗 [原文链接](https://juejin.cn/post/7147526675536969742) | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2024-03-05

---

# 查看浏览器Browsers的内核版本, 可以用 navigator.userAgent - 掘金

> 来源: https://juejin.cn/post/7147526675536969742

查看浏览器Browsers的内核版本, 可以用 navigator.userAgent查看浏览器Browsers的内核版 - 掘金 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

## 
查看浏览器Browsers的内核版本, 可以用 navigator.userAgent

kfepiza

2022-09-26

1,952

阅读7分钟

## 查看浏览器Browsers的内核版本, 可以用 navigator.userAgent

在浏览器控制台输入:`navigator.userAgent 

`navigator.userAgent

```

几乎所有主要浏览器都支持 `navigator.userAgent 属性

userAgent 属性是一个只读的字符串，声明了浏览器用于 HTTP 请求的用户代理头的值。
包含有关浏览器的信息。

User-Agent 的约定格式是：应用名，跟一个斜线，跟版本号，剩下的是自由的格式。

查看更详细的信息可以**在地址栏输入**:

- Chrome：`chrome://version 

`chrome://version

```

- Edge：`edge://version 

`edge://version

```

- Firefox：`about:support 

`about:support

```

以下内容参考转自[互联网的“套娃行为”有多凶残? 3 分钟解惑 (浏览器UA嵌套野史)](https://link.juejin.cn?target=https%3A%2F%2Fwww.runningcheese.com%2Fuseragent)

[互联网的“套娃行为”有多凶残? 3 分钟解惑 (浏览器UA嵌套野史,修改UA)](https://link.juejin.cn?target=https%3A%2F%2Fwww.runningcheese.com%2Fuseragent)
以下是原文: (留个备份)

几乎所有网民都不会忘记 2010 年的“3Q大战”。

在腾讯做出“非常艰难的决定”之后，360 不再能与 QQ 同时安装，使用 360 浏览器，也不再能访问 QQ 空间。

QQ 空间作为当时最受欢迎的社交网站，腾讯的这一操作，就等同于宣判了 360 浏览器的死刑。

在此次大战中，发挥着关键性作用的是：浏览器 UA。

今天我们就来聊聊这个话题。

## 一、浏览器 UA 的诞生

要讲清楚这个话题，我们要从 1990 年说起。

1990 年，英国计算机科学家`蒂姆·伯纳斯·李 巧妙地提出了 `HTTP 协议，然后又编写了世界上第一个浏览器 `World Wide Web ，**万维网就此诞生**。

1993 年，美国超级电脑应用中心（NCSA）推出了一款叫做 `Mosaic （马赛克） 的浏览器。

它第一次将图片与文字同时在一起展示，从此，浏览器就开始变得好玩起来。

为了发挥 Mosaic 浏览器的图片优势。

Mosaic 浏览器在访问网页时，会事先向网页服务器发送一段特定的字符串来标记自己。

这样使用 Mosaic 的用户，就能收到有图片的内容。

这个字符串 `Mosaic/2.0（Windows 3.1） 就是 `UserAgent ，简称 `UA ，中文叫作“用户代理”。

从此，浏览器 UA 作为一种“**根据用户软硬件环境，进而采用不同内容策略**”的技术，诞生了。

## 二、浏览器 UA 的伪装

## 2.1、Mozilla 浏览器

1994 年，**Mosaic** 项目的核心成员**马克·安德森**离职，然后发布了一款全新的浏览器 **Mozilla**。

Mozilla 除了是 Godzilla 的谐音外，它还是 Mosaic Killa 的缩写，意思是要做 Mosaic 的终结者。

然而在 Mosaic 的压力之下， Mozilla 还是改名为了 **Netscape** 浏览器。

不过在设置浏览器 **UA** 时，Netscape 还是使用了 Mozilla 的名字，也就是：**Mozilla/1.0 (Win3.1)**。

接着，Netscape 浏览器还率先支持了网页框架技术。

而其他它浏览器要么不支持，要么支持得不够好，Netscape 很快成为当时最流行的浏览器。

## 2.2、IE 浏览器

1995 年，微软宣布进军互联网，并发布了 IE 浏览器。

然而，尽管 IE 浏览器同样也支持框架技术，但总是收不到有框架的页面。

原因是网页服务器会先检测浏览器 UA 中是否包含 Mozilla 字符，如果有，就发送有框架的页面，没有就不发送。

微软等不及市场的反应，于是直接在 IE 浏览器的 UA 中加入了 Mozilla，也就是：

Mozilla/1.22 (compatible; MSIE 2.0; Windows 95)

于是，IE 浏览器就能正常接收到有框架的页面了。

从此，浏览器 UA 也成为了解决浏览器兼容性的一个重要手段。

## 三、浏览器 UA 的演变

## 3.1、Firefox 浏览器

没过多久，微软采用了将 IE 与 Windows 捆绑销售的策略，Netscape 浏览器被打败退出历史舞台。

不甘失败的 Netscape 团队，在 2004 年又推出了一款全新的浏览器 **Firefox**。

Firefox 使用的 **Gecko** 引擎非常优秀。

为了告诉大家，我使用了这个引擎，于是 Firefox 在浏览器 UA 里加入了：

`Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041108 Firefox/1.0 。

## 3.2、KHTML 浏览器

而由于 IE 止步不前，慢慢地，浏览器 UA 的探测规则发生了变化。

使用 Gecko 引擎的浏览器可以得到更好的网页代码，而其它的浏览器则没有这种待遇。

Linux 的追随者对此感觉难过，因为他们开发了好用的 **KHTML** 引擎，但却因为不是 Gecko 而得不到好的页面。

于是宣布 KHTML 兼容 Gecko（like Gecko），浏览器 UA 就变成了：

`Mozilla/5.0 (compatible; Konqueror/3.2; FreeBSD) (KHTML, like Gecko) 。

## 3.3、Opera 浏览器

一直使用自主 UA 的浏览器 **Opera**，也同样遇到了这样的问题。

但 Opera 不是简单地把自己也标记为 Gecko，而是主张让用户来决定变成什么样的浏览器。

于是 Opera 在菜单里增加了浏览器 UA 的选项，让用户来选择是变成 IE 还是 Firefox，又或者是它自己本体。

## 3.4、Safari 浏览器

2003 年，苹果公司从 **KHTML** 引擎中分支出来了 **Webkit**，然后开发了 Safari 浏览器。

为了兼容性的考虑，苹果将 KHTML 内核 UA 中 的 Mozilla、KHTML、Gecko 统统继承了下来，变成了：

`Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/85.7 (KHTML, like Gecko) Safari/85.5 

## 3.5、Chrome 浏览器

2008 年，谷歌使用了苹果的 **Webkit** 引擎开发出了 **Chrome** 浏览器。

Chrome 浏览器也想兼容那些专为 Safari 编写的页面，于是就继承了 Safari 的 UA，然后再加入自己的 UA：

`Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 。

## 3.6、Edge 浏览器

如果要问谁是“伪装之王”，那一定非 Edge 莫属了。

2020 年，微软转用谷歌的 Chromium 内核开发 Edge 浏览器，为了不再受兼容性的困扰，**Edge 浏览器几乎将所浏览器的 UA 都加入了进来**，于是就有了：

`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.70 Safari/537.36 Edg/90.0.818.38 

## 3.7、浏览器 UA 伪装

如果把浏览器 UA 伪装，比作是“俄罗斯套娃”的话，你会发现：

Edge 伪装成 Chrome，Chrome 伪装成 Safari，Safari 伪装成 KHTML，KHTML 伪装成 Gecko。

Gecko 和 IE 又伪装成 Mozilla。

最终，**所有浏览器的 `UA 都以 `Mozilla 开头**。

尽管，Mozilla 作为一个浏览器而言，早已从市场上消失。

## 四、浏览器 UA 的利用

浏览器 UA 的利用，通常与浏览器的功能性相关，但也会有其它因素。

比如当年的“3Q大战”，QQ 空间利用 360 浏览器 UA 中，含有的“360SE”字样来屏蔽 360 浏览器。

而 360 浏览器为了躲避封杀，将“360SE”的字样从浏览器 UA 中移了出去。

又比如一些视频网站，针对桌面浏览器和安卓浏览器，会推送视频广告，而对苹果的 Safari 浏览器则不推送。

还有比如百度网盘，用一般的浏览器下载会大幅限速，而用自家的“百度云管家”则小幅限速。

对于这样的区别对待，我们有必要夺回浏览器 UA 的控制权。

## 4.1、浏览器 UA 检查

首先，检查当前浏览器 UA 的方法，是在地址栏中输入 ：

- Chrome：`chrome://version 

`chrome://version

```

- Edge：`edge://version 

`edge://version

```

- Firefox：`about:support 

`about:support

```

## 4.2、User-Agent Switcher

然后，我们可以使用扩展 **User-Agent Switcher** 来自定义浏览器 **UA**。而且，扩展还支持“白名单模式”，我们可以对不同的网站使用不同的浏览器 UA。

## 4.3、Header Editor

又或者使用拓展 **Header Editor** 来修改浏览器 **UA**。

它的优点在于多功能合一，可以省去安装专门的浏览器 UA 扩展，支持 Chrome、Edge、Firefox 三款浏览器。

就是要注意，使用完后要记得关闭 UA 修改 。

## 结尾

说到底，浏览器 UA 其实是“浏览器之间争夺”的产物。

如果我们想要有一个畅通无阻的互联网，那就很有必要去了解它。

而且，随着 Python 和大数据的火热，「爬虫技术」和「反爬虫技术」的入门也都离不开浏览器 UA。

相信看完这篇文章，你已经半只脚踏入这个领域了。

至少在朋友面前炫耀一番，是没问题的了。

kfepiza

652
文章 
281k
阅读 
56
粉丝
