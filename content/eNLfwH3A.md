# 【问题分析】WMS无焦点窗口的ANR问题【Android 14】_waiting because no window has focus but activityre

> 原文链接: https://blog.csdn.net/ukynho/article/details/136669719

---

Monkey跑出的 Launcher ANR，场景为在Launcher的Recents界面下一个Activity启动又快速销毁导致的无焦点窗口问题。

## 1\. log分析

## 2\. 模拟 ANR

根据之前的log分析，我们已经可以写一个 Demo App来模拟该ANR的发生情况了，总结如下：

1、启动任意一个Activity，我这里写的Demo App为 MainActivity 。

2、接着输入 事件 KEYCODE\_RECENT\_APPS，回到Recents。

3、切回到Launcher后100ms，马上让MainActivity以NEW\_TASK的方式调起一个另外一个Activity，我这里用一个名为SingleTaskActivity的Activity去模拟。

4、SingleTaskActivity启动后，马上调用finish，我这里是在onCreate方法中调用的 —— KO，可以复现无焦点窗口的情况，如果此时再输入一个KeyEvent事件，即可发生ANR。

另外把Demo App安装在Pixel上发现没问题：

有可能是Pixel多了一些 patch ，所以修复了此问题？

## 3\. recents\_animation\_input\_consumer分析

多打些log：

看到及时是发生问题后，其实也是有继续调用InputMonitor.updateInputFocusRequest方法的，但是"recents\_animation\_input\_consumer"却没有获取焦点，继续看看代码是为什么：

这里的RecentsAnimationController是之前的逻辑了，现在点击切换到Recents，RecentsAnimationController也是为空的，那么我们主要看这个逻辑：

```java

```