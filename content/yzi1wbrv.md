# Claude Code 浏览器自动化方案，怎么选？

> 公众号: 刘小排r
> 发布时间: 1970-01-01 08:33:46
> 原文链接: https://mp.weixin.qq.com/s?__biz=MzI1MTUxNzgxMA==&mid=2247500962&idx=1&sn=84487e4cdd8d9d2e9a7023c633594a2c&chksm=e8296191c634db279b0c4194705f24282eaf2147717b9bda5f9b720afb60881edb150ee6c763

哈喽，大家好，我是刘小排。

昨天和几位创业的朋友吃饭，席间讨论了一个问题：“在Claude Code中，最好的浏览器自动化方案是什么？”

在刚有MCP的时候，我写过一些浏览器自动化文章，那时，最好用的Playwright MCP和一些第三方的浏览器自动化工具，还不算稳定。

（参考：[所有的RPA可以去死了！Claude Code可以只靠口喷完成一切！](https://mp.weixin.qq.com/s?__biz=MzI1MTUxNzgxMA==&mid=2247498197&idx=1&sn=51dd455d29ec1e790c56e018eade87b1&scene=21#wechat_redirect)）

大半年过去了，现在最流行、稳定、专门针对Agent的浏览器自动化方案已经有了三个明显的头部：Agent Browser 、Devtools MCP 、Playwright MCP，开发者分别是Vercel、Google、微软。

像下图这样的简单任务，这3个都做得很好。![图片](images/img_001.png)

那到底选哪个呢？哪个最好呢？

如果你想知道一个最简单直接的答案：请你选择Devtools MCP，它在大部分场景下是最全能的。

如果你有耐心想了解更多，可以往下看，因为它们的特性各有不同，需要根据不同的场景来选择。

声明：**表格是我和AI一起做的，所以用语可能稍微有点AI味儿，但我对内容质量和准确性负责。**

## 省流版

-   “看看”、“填表” : 用Agent Browser

-   性能、调试、网络请求： 用Devtools MCP

-   测试、跑全流程：用Playwright MCP

### 基本情况对比

维度

Agent Browser

Playwright MCP

Chrome DevTools MCP

开发者

Vercel Labs

Microsoft

Google

定位

专为 AI Agent 设计的轻量 CLI

通用浏览器自动化 + AI 扩展

Chrome 原生调试协议封装

推荐接入方式

Bash CLI 命令/Skill

MCP Server

MCP Server + Chrome 扩展

Token 消耗

减少93%

较高（完整可访问性树）

中等

核心机制

Snapshot + Refs（元素引用）

Accessibility Tree（可访问性树）

Chrome DevTools Protocol

浏览器支持

Chromium

Chrome/Firefox/WebKit

仅 Chrome

### Agent Browser — 适合日常浏览网页、快速操作

场景

示例

看看网页长什么样

"帮我打开竞品官网看看"

截图对比

"截个图看看改完的效果"

填表单测试

"把测试数据填进去"

信息采集

"看看这个页面的定价"

简单点击操作

"点一下那个按钮"

一句话：**轻量快速，省 token**

### Playwright MCP — 适合测试验证、复杂流程

场景

示例

功能测试

"测试一下登录流程"

用户旅程验证

"跑一遍下单流程"

回归测试

"确认修复没影响其他功能"

多步骤自动化

"注册→登录→发帖→退出"

稳定性要求高

"这个脚本要跑很久"

一句话：**专业、完整、稳定、慢**

### DevTools MCP — 适合调试排错、性能分析、抓取网络请求

场景

示例

看 Console 报错

"页面白屏了，帮我查查"

网络请求调试

"API 返回了什么"

性能分析

"页面加载太慢了"

CSS/DOM 检查

"样式为什么不对"

断点调试

"帮我看这个变量的值"

一句话：**调试代码、性能分析、抓网络请求**

### 特别强调：如果不是用于编程，Agent Browser是最好的。

为什么这么说？

这是因为Agent Browser太节省Token了，节省Token意味着速度快。

在我不写程序的时候，我也不一定使用Claude Code，而是使用Cowork、Craft Agents等图形化工具。

下面是我在Craft Agents里、使用Agent Browser来刷生财有术网站的过程。 这个过程，Agent Browser、Devtools MCP、Playwright MCP都能做到，**但是Agent Browser明显最快、体验最佳**。

刚开始，我们可以登录以后，保存Cookie，后面就不再需要登录了，甚至电脑上可以不出现浏览器界面。

```
用Agent Browser打开scys.com 让我登录，然后保存登录信息
```

![图片](images/img_002.png)

登录成功，右上角是我的头像。注意，此时Agent Browser启动的浏览器，左上角有一个小的TEST标，如下图所示

![图片](images/img_003.png)

我们让AI自动查看最近50条风向标

```
我已经登录好了，你找到“风向标”栏目，总结最近50个风向标，有什么亮点
```

![图片](images/img_004.png)

整体总结

![图片](images/img_005.png)

选择其中一条，详细查看。

```
我觉得你刚才说的 2 ，特别好，展开讲讲
```

![图片](images/img_006.png)

期待你的反馈