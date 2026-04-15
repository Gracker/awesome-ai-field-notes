---
title: 'Github Copilot 近期重要更新一览 (2025.4.9)Github Copilot 宣布推出 Pro+(3 - 掘金'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# Github Copilot 近期重要更新一览 (2025.4.9)Github Copilot 宣布推出 Pro+(3 - 掘金

> Cubox 收藏: Github Copilot 近期重要更新一览 (2025.4.9)Github Copilot 宣

🔗 [原文链接](https://juejin.cn/post/7490967893779431439) |  | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-04-10

`copilot` `[]` `cursor` `gpt-4` `claude`

---

## English
Github Copilot 近期重要更新一览 (2025.4.9)Github Copilot 宣布推出 Pro+(3 - 掘金

首页

                沸点

                课程

                数据标注

HOT

                AI Coding

更多

                    直播

                    活动

                    APP

插件

                直播

                活动

                APP

插件

搜索历史

                        清空

    创作者中心

写文章

发沸点

写笔记

写代码

草稿箱

创作灵感

            查看更多

                登录

                  注册

            Github Copilot 近期重要更新一览 (2025.4.9)

    coder_pig

                    2025-04-09

                    2,679

                    阅读3分钟

1. 引言

离上一篇
《Github Copilot 近期的一次重要更新 (2024.9.26)》
已经过去半年多了，今天比较闲，刷下 
Github Copilot 的

更新日志
 → 
Github Copilot ChangeLog
 看下都有哪些重要更新，这不刷不知道，一刷吓一跳 ❗️

2. 宣布推出 GitHub Copilot Pro+

😳 这是偷师啊腾的扣扣🐧吗？(VIP → SVIP → 大会员)，搞个 
Pro+
 ？

看下介绍：可以用最新的 
GPT-4.5
，然后每月 
1500
 个高级请求：

😳 哈？啥是 
高级请求
？调 
4o
 外的模型都算，还有个对应的 
倍率表
：

🤡 注意，是 
点数
，不是 
次数
，原本没限制次数的 
Pro
 改成 
每月300点
，能调几次 
Claude 3.7
 ？

300 / 1.25 = 240 次请求，除以30相当于 
每天8次。

😄 评论区一堆 "
准备拥抱 Cursor
"，不过 
涨价和限制次数
 也能理解，因为确实贵，从 
Cursor
 流量用完的慢速请求 和 
Trae国际版
 要排队就可见一斑：

😶 让AI算下直接调API要花多少钱：

🤣 Pro 收我 
10刀
，确实是亏钱了，而且实际使用过程中消耗的Token会更多，毕竟 
多轮对话
 (有会话上下文)。

🤷‍♀️ 然后，说是从【
5月5日
】开始限制，截至发稿前，
没限制次数
~

3. 其它

3.1. 直接切换模型重新生成输出

如题，会保留所有先前的对话上下文，还可以查看先前的响应并比较模型输出：

3.2. VSCode 添加 Agent 模式

😮 在此模式下可以：
自动在您的工作区中搜索相关上下文、编辑文件、检查错误，并运行终端命令
。

😅 哈？这怎么那么像 
Trae
 的 
Builder
 模式啊...

支持选择不同类型的 
上下文
，
工具
 (MCP Server)，取消了附加文件的数量限制：

还可以通过「
Custom instructions
」指导 
Copilot
 在为项目提供代码建议时 
遵循项目的结构、规范、回答风格等
。步骤：

在工作区创建 
.github/copilot-instructions.md
 文件描述具体要求。

VSCode 的 
设置
 中启用 
github.copilot.chat.codeGeneration.useInstructionFiles
。

具体指令参考
《Custom instructions for GitHub Copilot in VS Code》
，🐶 我选择让Copilot给我自动生成，然后输入prompts让它给我改~

设置效果：

😁 这部分还好些小细节，时间原因，就不慢慢过了，感兴趣读者可以自行尝试体验~

3.3. JetBrains IDE 支持 Copilot Edits

🐶 终于能 
切模型
 了，插件版本要更到最新的【
1.5.40
】才有这么多模型，然后插件有 
IDE版本限制
：

版本需要 
≥241
，比如我的AS是231的，就不不配，能用的最近插件版本只有 
1.5.33
，模型只有三：

🤷‍♀️ 还是比不上隔壁 
VSCode
 亲儿子啊，连类似于 
Builder
 的 
Agent
 模式安排上了，这还搁着复制粘贴代码...

3.4. GitHub Copilot chat 沉浸式更新

3.4.1. 4o 模型支持图片上传分析

😐 之前只在 
VS Code
 和 
Visual Studio
 上可用，现在 GitHub 上的 Copilot Chat 沉浸式模式也支持了：

3.4.2. 支持Copilot偏好设置

网页端也可以写约束提示词~

回答结果：

😀 再也不用为了避免这货说着说着就 
飙英文
，得在每次提问前加个 "
请用中文回答我
" 了~

4. 小结

😄 梳理下本文要点：

Github Copilot 宣布推出 
Pro+(39

🔪

/月)
 ，
5月5日
 开始限制 
高级模型
 (除4o外所有) 访问次数 ，原 
Pro
 每月 
300点
 (能问 
Claude 3.7x240次
 )。

VSCode插件
 新增类似于 
Trae Builder
 的 
Agent 模式
，可以自动在您的工作区中搜索相关上下文、编辑文件、检查错误，并运行终端命令。支持选择不同类型的 
上下文，工具
 (MCP Server)，取消了附加文件的数量限制。支持通过 
Custom instructions
 指导 Copilot 在为项目提供代码建议时 遵循项目的结构、规范、回答风格等。

JetBrains IDE
 支持 
Copilot Edits
，🐶 终于可以切模型，最新版插件才有【
全模型
】，IDE版本需 ≥241。

Eclipse
 (👴青回) & 
XCode
 支持 Copliot，GitHub Copilot chat 沉浸式 支持 
图片上传(4o)
 和 
偏好设置
。

💁‍♂️ 以上就是从上一篇文章截至目前的所有 
重要更新
 (🤡我认为的)，我们下次见🌸~

    coder_pig

        🏆掘金签约作者 | 摸鱼王 @来日未必方长

        236

文章

        1.3m

阅读

        13k

粉丝

目录

收起

      1. 引言

      2. 宣布推出 GitHub Copilot Pro+

      3. 其它

      3.1. 直接切换模型重新生成输出

      3.2. VSCode 添加 Agent 模式

      3.3. JetBrains IDE 支持 Copilot Edits

      3.4. GitHub Copilot chat 沉浸式更新

      3.4.1. 4o 模型支持图片上传分析

      3.4.2. 支持Copilot偏好设置

      4. 小结

## 中文
[翻译内容待添加]
