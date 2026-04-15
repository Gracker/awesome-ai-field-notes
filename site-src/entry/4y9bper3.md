---
title: '2026-03-02-0810-karpathy-AI-changed-programming-last-two-months-2026731645169185220'
sidebar: false
---

::: info
[← 返回AI编程](/coding)
:::

# 2026-03-02-0810-karpathy-AI-changed-programming-last-two-months-2026731645169185220

> AI 实践：2026-03-02-0810-karpathy-AI-changed-prog

🔗 [原文链接](https://x.com/karpathy/status/2026731645169185220) | @karpathy |  | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-03-02

`agent` `karpathy` `benchmark` `coding`

---

# 2026-03-02-0810-karpathy-AI-changed-programming-last-two-months

## English
It is hard to communicate how much programming has changed due to AI in the last 2 months: not gradually and over time in the "progress as usual" way, but specifically this last December. There are a number of asterisks but imo coding agents basically didn't work before December and basically work since - the models have significantly higher quality, long-term coherence and tenacity and they can power through large and long tasks, well past enough that it is extremely disruptive to the default programming workflow.

Just to give an example, over the weekend I was building a local video analysis dashboard for the cameras of my home so I wrote: "Here is the local IP and username/password of my DGX Spark. Log in, set up ssh keys, set up vLLM, download and bench Qwen3-VL, set up a server endpoint to inference videos, a basic web ui dashboard, test everything, set it up with systemd, record memory notes for yourself and write up a markdown report for me". The agent went off for ~30 minutes, ran into multiple issues, researched solutions online, resolved them one by one, wrote the code, tested it, debugged it, set up the services, and came back with the report and it was just done. I didn't touch anything. All of this could easily have been a weekend project just 3 months ago but today it's something you kick off and forget about for 30 minutes.

As a result, programming is becoming unrecognizable. You're not typing computer code into an editor like the way things were since computers were invented, that era is over. You're spinning up AI agents, giving them tasks *in English* and managing and reviewing their work in parallel. The biggest prize is in figuring out how you can keep ascending the layers of abstraction to set up long-running orchestrator Claws with all of the right tools, memory and instructions that productively manage multiple parallel Code instances for you. The leverage achievable via top tier "agentic engineering" feels very high right now.

It's not perfect, it needs high-level direction, judgement, taste, oversight, iteration and hints and ideas. It works a lot better in some scenarios than others (e.g. especially for tasks that are well-specified and where you can verify/test functionality). The key is to build intuition to decompose the task just right to hand off the parts that work and help out around the edges. But imo, this is nowhere near "business as usual" time in software.

## 中文
很难传达过去两个月里AI给编程带来了多大的变化：不是以"循序渐进"的方式随时间逐渐变化，而是特别在去年12月发生了根本性变化。虽然有一些需要注意的细节，但在我看来，编程代理在12月之前基本上无法工作，而从那之后基本上都能正常工作了——模型的质量、长期连贯性和毅力都显著提高，它们能够处理大型和长期任务，足以彻底改变默认的编程工作流程。

举个例子，上周末我正在为家里的摄像头构建一个本地视频分析仪表板，于是我写道："这是我DGX Spark的本地IP和用户名/密码。登录，设置ssh密钥，设置vLLM，下载并测试Qwen3-VL，设置一个用于视频推理的服务器端点，一个基本的web ui仪表板，测试所有内容，用systemd设置服务，为自己记录内存笔记，并为我写一份markdown报告"。这个代理大约运行了30分钟，遇到了多个问题，在网上研究解决方案，逐一解决，编写代码，测试它，调试它，设置服务，然后带回报告，一切就完成了。我什么都没碰。所有这些在3个月前可能是一个周末的项目，但今天你只需要启动它然后忘记30分钟。

因此，编程正在变得面目全非。你不再像计算机发明以来那样在编辑器中键入计算机代码，那个时代已经结束了。你正在启动AI代理，用*英语*给他们任务，并行管理和审查他们的工作。最大的奖励在于弄清楚如何不断抽象层次的攀升，建立长期运行的编排器Claw，配备所有正确的工具、内存和指令，为你有效地管理多个并行的Code实例。通过顶级的"代理工程"可实现的影响力感觉非常高。

它并不完美，需要高层次的指导、判断、品味、监督、迭代和想法。它在某些场景下比其他场景工作得好得多（例如，特别是对于那些可以验证/测试功能的明确定位的任务）。关键在于建立直觉来正确分解任务，交接工作的部分并在边缘提供帮助。但在我看来，这与软件领域的"一切如常"时间相去甚远。
