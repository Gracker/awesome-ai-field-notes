---
title: "On the coming era of highly bespoke software"
source: "field-notes"
entry_id: "rnjpbgtm"
language: "bilingual"
---

## English

# On the coming era of highly bespoke software

**By @karpathy**

Very interested in what the coming era of highly bespoke software might look like.

Example from this morning - I've become a bit loosy goosy with my cardio recently so I decided to do a more srs, regimented experiment to try to lower my Resting Heart Rate from 50 -> 45, over experiment duration of 8 weeks. The primary way to do this is to aspire to a certain sum total minute goals in Zone 2 cardio and 1 HIIT/week.

1 hour later I vibe coded this super custom dashboard for this very specific experiment that shows me how I'm tracking. Claude had to reverse engineer the Woodway treadmill cloud API to pull raw data, process, filter, debug it and create a web UI frontend to track the experiment. It wasn't a fully smooth experience and I had to notice and ask to fix bugs e.g. it screwed up metric vs. imperial system units and it screwed up on the calendar matching up days to dates etc.

But I still feel like the overall direction is clear:

1) There will never be (and shouldn't be) a specific app on the app store for this kind of thing. I shouldn't have to look for, download and use some kind of a "Cardio experiment tracker", when this thing is ~300 lines of code that an LLM agent will give you in seconds. The idea of an "app store" of a long tail of discrete set of apps you choose from feels somehow wrong and outdated when LLM agents can improvise the app on the spot and just for you.

2) Second, the industry has to reconfigure into a set of services of sensors and actuators with agent native ergonomics. My Woodway treadmill is a sensor - it turns physical state into digital knowledge. It shouldn't maintain some human-readable frontend and my LLM agent shouldn't have to reverse engineer it, it should be an API/CLI easily usable by my agent. I'm a little bit disappointed (and my timelines are correspondingly slower) with how slowly this progression is happening in the industry overall. 99% of products/services still don't have an AI-native CLI yet. 99% of products/services maintain .html/.css docs like I won't immediately look for how to copy paste the whole thing to my agent to get something done. They give you a list of instructions on a webpage to open this or that url and click here or there to do a thing. In 2026. What am I a computer? You do it. Or have my agent do it.

So anyway today I am impressed that this random thing took 1 hour (it would have been ~10 hours 2 years ago). But what excites me more is thinking through how this really should have been 1 minute tops. What has to be in place so that it would be 1 minute? So that I could simply say "Hi can you help me track my cardio over the next 8 weeks", and after a very brief Q&A the app would be up. The AI would already have a lot personal context, it would gather the extra needed data, it would reference and search related skill libraries, and maintain all my little apps/automations.

TLDR the "app store" of a set of discrete apps that you choose from is an increasingly outdated concept all by itself. The future are services of AI-native sensors & actuators orchestrated via LLM glue into highly custom, ephemeral apps. It's just not here yet.

---

## 中文

# 高度定制化软件的未来时代

**By @karpathy**

我非常感兴趣，想看看即将到来的高度定制化软件时代会是什么样子。

今天早上的一个例子——我最近对有氧训练有点松懈了，所以我决定做一个更认真的、有计划的实验，目标是 8 周内将静息心率从 50 降到 45。主要方法是有氧二区每周总分钟数达到一定目标，外加每周 1 次 HIIT。

1 小时后，我用 vibe coding 搞定了这个针对这个非常特定实验的超级定制仪表盘，用来追踪我的进展。Claude 必须逆向工程 Woodway 跑步机的云 API 来拉取原始数据、处理、过滤、调试，并创建一个 Web UI 前端来追踪实验。过程并不完全顺畅，我不得不注意到并要求修复 bug——比如它搞混了公制和英制单位，以及日期和星期几对不上等问题。

但我仍然觉得总体方向是明确的：

1）永远不会有（也不应该有）一个专门针对这类东西的 App Store 应用。我不应该去寻找、下载和使用某种"心肺实验追踪器"，因为这东西大约 300 行代码，一个 LLM Agent 几秒钟就能给你。当 LLM Agent 可以现场即兴创作应用、只为你一个人制作时，从一长串离散应用中选择安装的"应用商店"概念感觉有些不对劲，已经过时了。

2）第二，整个行业必须重新配置为一系列具有 Agent 原生人机工程学的传感器和执行器。我的 Woodway 跑步机是一个传感器——它将物理状态转化为数字知识。它不应该维护某种人类可读的界面，我的 LLM Agent 也不应该去逆向工程它，它应该是一个可以轻松被我的 Agent 使用的 API/CLI。我有点失望（相应地我的时间线也更慢了），整个行业进展得太慢了。99% 的产品/服务仍然没有 AI 原生的 CLI。99% 的产品/服务仍然维护着 .html/.css 文档，好像我不会立即把这些东西复制粘贴给 Agent 来完成任务一样。它们在网页上给你一系列说明，让你打开这个那个 URL，点击这里那里去做某件事。现在是 2026 年。我是什么，是计算机吗？你自己做。或者让我的 Agent 做。

所以总之，今天让我印象深刻的是，这个随机的事情花了 1 小时（两年前可能需要大约 10 小时）。但更让我兴奋的是思考这实际上应该最多只需要 1 分钟。需要什么条件才能达到 1 分钟？这样我就可以简单地说"能帮我追踪接下来 8 周的有氧训练吗"，在简短的问答之后应用就上线了。AI 已经有大量个人上下文，它会收集额外需要的数据，会参考和搜索相关技能库，并维护我所有的小应用/自动化。

总结：一组离散应用的"应用商店"概念本身正在日益过时。未来是一系列具有 AI 原生特性的传感器和执行器，通过 LLM 粘合剂编排成高度定制的、临时性的应用。只是这个未来还没有到来。
