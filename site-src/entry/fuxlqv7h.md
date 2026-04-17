---
title: 'Anthropic全网追杀的人，可能是我……'
sidebar: false
---

::: info
[← 返回学习资源](/learning)
:::

# Anthropic全网追杀的人，可能是我……

> Anthropic 公司动态与分析收藏

🔗 [原文链接](https://mp.weixin.qq.com/s?__biz=MzI1MTUxNzgxMA==&mid=2247498537&idx=1&sn=23cafdfedc8297dfa05d46a5bce8db11&chksm=e83b872acc893f6ffb867f3fd3bd14634ae32630344f698f941bfa2f5b65d9f7755e82b8bd9c&mpshare=1&scene=1&srcid=0815evfjgbXaGDetZApIQOyX&sharer_shareinfo=fd637b036a75822befde463b74963297&sharer_shareinfo_first=fd637b036a75822befde463b74963297) | 🇨🇳 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2025-08-15

`Claude` `Anthropic`

---

# Anthropic全网追杀的人，可能是我……

> 公众号: 刘小排r
> 发布时间: 1970-01-01 08:33:45
> 原文链接: https://mp.weixin.qq.com/s?__biz=MzI1MTUxNzgxMA==&mid=2247498537&idx=1&sn=23cafdfedc8297dfa05d46a5bce8db11&chksm=e83b872acc893f6ffb867f3fd3bd14634ae32630344f698f941bfa2f5b65d9f7755e82b8bd9c&mpshare=1&scene=1&srcid=0815evfjgbXaGDetZApIQOyX&sharer_shareinfo=fd637b036a75822befde463b74963297&sharer_shareinfo_first=fd637b036a75822befde463b74963297

---
上个月，Anthropic官方发布了信息，有一个用户，只花了$200美元订阅套餐，却在一个月内消耗了数万美金的(tens of thousands)的token。从而决定对所有人进行限速……

全世界的程序员都在好奇，这位每个月花数万美金的老哥是谁？

刚刚发现，这位用户，好像，就是我本人。😂

没想到，吃瓜吃到自己头上了。



下面是正式的限速通知，从8月28日开始。



为什么说，这位用户，就是我本人？

我平时使用ccusage进行统计，日常消耗量大概是这样的



在国外用户维护的Claude Code 消耗量总榜上，如果按照Cost(消耗金额）排序，消耗第一的就是我。过去30天，消耗了5万美金……

榜单地址 https://www.claudecount.com/



事实上，这个统计数据比我真实使用的更少。

因为在我初始化统计脚本的时候，脚本提示我有大约一半的统计数据上传失败，可能是我数据太大了，遇到网络波动就失败了。

另外，从报错看，它只上传了我从7月15日以后的数据，这个也还不知道为啥。

回头我再研究一下看看能否把上传失败的部分重新上传……

如何加入Claude Code排行榜？

只需要在命令行执行


```css
npx claude-code-leaderboard
```


再通过Twitter账号授权。就可以了。

初次授权，系统会扫描本地Claude Code使用记录，一次性上传到榜单上。

不需要担心隐私问题，它只会上传数据(数字），不会上传你的对话记录、代码。

Claude Code排行榜，统计的方法和原理？

这个 CLI 工具的统计原理主要依赖于 Claude Code 的 hook 机制。

在每次你和Claude Code会话结束时，hook 脚本会自动运行，进行统计、并上传统计数据。

该脚本会扫描 Claude Code 项目的日志文件，提取本次会话的 token 使用数据，包括输入、输出、缓存等统计信息，再自动上传到服务器上。

了解Claude Code的hook机制

https://docs.anthropic.com/en/docs/claude-code/hooks-guide

统计脚本详细原理请参考

https://github.com/grp06/claude-code-leaderboard

为啥你使用的token不是最多的，钱却是最多呢？

Token和钱不是一一对应关系，涉及到模型选择、缓存比例。

如果你总是使用ultrathink、总是使用Opus模型， 消耗的金额就比较高。

如果你习惯于在不同的项目、不同的任务上并行使用Claude Code， 就会出现缓存比例较低的情况，对应的金额就更大。

相反，如果你喜欢在同一个任务上不断聊天，那你使用的cache就比较多（不断累加）。如下图所示，input和output都不多，但是cache一直在增长。 因为cache很便宜， 如果大量出现这种情况，你的消费金额就不会高。



你不睡觉吗？为什么我从早用到晚，也没你用得多？

我睡觉，是我的Claude Code不睡觉。

只要指挥得当，Claude Code是可以24小时干活的。

尤其是在Claude Code v1.0.71版本，增加了Background Commands功能后，让它24小时运行，更加容易。

感兴趣的同学可以去了解一下，别人在用Background Commands 干什么、有什么好玩的场景。



下图是一个我自己的示例，我正在让Claude Code进行一个它自己预估需要40分钟左右的任务。

也正是因为有这40分钟，我才有时间来写这篇公众号。

截图中标注的 bash running， 表示有后台任务在执行。



如果大家对Claude Code后台任务感兴趣，可以留言告诉我。如果人数足够多，我想办法脱敏后，单独写一篇，跟大家讲一讲。

你用Claude Code做了什么产品？

近期我三个主要产品是：

Raphael AI - https://raphael.app

AnyVoice - https://anyvoice.net

Fast3D - https://fast3d.io

其中，Fast3D完全是用Claude Code做的，页面打磨得比较精美，欢迎拍砖。另外两个产品有很多是Cursor的功劳。

你用了这么多Token只做了这么点东西，是不是因为你菜、你效率低？

是的，我菜，我效率低。你牛。

我是新手，有什么简单的方法，让我的消耗量增加？

如果是新手的话，我推荐一个简单的方法 —— 使用Claude Code Chat， 启用它默认推荐的所有MCP、总是勾选Opus模型、总是勾选Ultrathink。 就这么简单的几招，每天消耗1000美金以上，是比较容易的。

参考文章 [6小时消耗$6034美金！以每月$200美金的价格卖给我们Claude Code包月套餐，它真是亏大了](https://mp.weixin.qq.com/s?__biz=MzI1MTUxNzgxMA==&mid=2247498478&idx=1&sn=68829d593179d7d355b1270d43afaa8c&scene=21#wechat_redirect)

如果你是老手，建议你像我一样，认真研究如何让Claude Code 24小时不停机干活，这才是充分解放自己的双手、释放最大化的生产力。

* * *

最后提醒

马上8月28日Claude Code就要限速了！

只剩最后一两周！ 大家抓紧最后的疯狂，玩起来吧！😄

* * *
