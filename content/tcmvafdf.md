---
title: "The third era of AI software development"
source: "field-notes"
entry_id: "tcmvafdf"
language: "bilingual"
---

## English

# The third era of AI software development

**By mntruell | Cursor**

When we started building Cursor a few years ago, most code was written one keystroke at a time. Tab autocomplete changed that and opened the first era of AI-assisted coding.

Then agents arrived, and developers shifted to directing agents through synchronous prompt-and-response loops. That was the second era. Now a third era is arriving. It is defined by agents that can tackle larger tasks independently, over longer timescales, with less human direction.

As a result, Cursor is no longer primarily about writing code. It is about helping developers build the factory that creates their software. This factory is made up of fleets of agents that they interact with as teammates: providing initial direction, equipping them with the tools to work independently, and reviewing their work.

Many of us at Cursor are already working this way. More than one-third of the PRs we merge are now created by agents that run on their own computers in the cloud. A year from now, we think the vast majority of development work will be done by these kinds of agents.

## From Tab to agents

Tab excelled at identifying where low-entropy, repetitive work could be automated. For nearly two years, it produced significant leverage.

Then the models improved. Agents could hold more context, use more tools, and execute longer sequences of actions. Developer habits began to shift, slowly through the summer, then rapidly over the last few months.

The transformation has been so complete that today, many Cursor users never touch the tab key. In March 2025, we had roughly 2.5x as many Tab users as agent users. Now, that is flipped: we now have 2x as many agent users as Tab users and agent usage in Cursor has surged.

But already this shift is giving way to something bigger. The Tab era lasted nearly two years. The second era, in which most work is done with synchronous agents, may not last one.

## Cloud agents and artifacts

Compared to Tab, synchronous agents work further up the stack. They handle tasks that require context and judgment, but still keep the developer in the loop at every step. But this form of real-time interaction, combined with the fact that synchronous agents compete for resources on the local machine, means it is only practical to work with a few at a time.

Cloud agents remove both constraints. Each runs on its own virtual machine, allowing a developer to hand off a task and move on to something else. The agent works through it over hours, iterating and testing until it is confident in the output, and returns with something quickly reviewable: logs, video recordings, and live previews rather than diffs.

This makes running agents in parallel practical, because artifacts and previews give you enough context to evaluate output without reconstructing each session from scratch. The human role shifts from guiding each line of code to defining the problem and setting review criteria.

## The shift is underway inside Cursor

Thirty-five percent of the PRs we merge internally at Cursor are now created by agents operating autonomously in cloud VMs. We see the developers adopting this new way of working as characterized by three traits:

1. Agents write almost 100% of their code.
2. They spend their time breaking down problems, reviewing artifacts / code, and giving feedback.
3. They spin up multiple agents simultaneously instead of handholding one to completion.

There is a lot of work left before this approach becomes standard in software development. At industrial scale, a flaky test or broken environment that a single developer can work around turns into a failure that interrupts every agent run. More broadly, we still need to make sure agents can operate as effectively as possible, with full access to tools and context they need.

We think yesterday's launch is an initial but important step in that direction.

---

## 中文

# AI 软件开发的第三个时代

**By mntruell | Cursor**

当我们几年前开始构建 Cursor 时，大多数代码是一个按键一个按键写出来的。Tab 自动补全改变了这一点，开启了 AI 辅助编码的第一个时代。

然后 Agent 出现了，开发者转向通过同步的提示-响应循环来指挥 Agent。这是第二个时代。现在第三个时代正在到来。它的特征是：Agent 能够独立处理更大的任务，在更长的时间范围内工作，而且需要的人类指导更少。

因此，Cursor 不再主要关乎写代码。它是关于帮助开发者构建制造软件的工厂。这个工厂由一群 Agent 组成，开发者像与队友一样与它们互动：提供初始方向，为它们配备独立工作的工具，并审查它们的工作。

Cursor 的许多员工已经在这样工作了。我们合并的 PR 中，超过三分之一现在是由在云端自己的计算机上运行的 Agent 创建的。一年后，我们认为绝大多数开发工作将由这类 Agent 完成。

## 从 Tab 到 Agent

Tab 擅长识别哪些低熵、重复性的工作可以自动化。在近两年的时间里，它产生了显著的杠杆效应。

然后模型改进了。Agent 可以容纳更多上下文、使用更多工具、执行更长的动作序列。开发者的习惯开始改变——整个夏天缓慢进行，然后在过去几个月里迅速加速。

这种转变如此彻底，以至于今天许多 Cursor 用户从不碰 Tab 键。2025 年 3 月，我们大约有 2.5 倍于 Agent 用户的 Tab 用户。现在，这个比例颠倒过来了：我们现在有 2 倍于 Tab 用户的 Agent 用户，Cursor 中 Agent 的使用量也大幅飙升。

但这种转变已经在让位于更大的变化。Tab 时代持续了近两年。第二时代——大多数工作通过同步 Agent 完成——可能持续不到一年。

## 云端 Agent 与产物

与 Tab 相比，同步 Agent 在更高层次上工作。它们处理需要上下文和判断的任务，但仍让开发者在每一步都保持参与。但这种实时交互形式，加上同步 Agent 在本地机器上争夺资源的事实，意味着每次只能实际处理少数几个。

云端 Agent 解除了这两个限制。每个 Agent 在自己的虚拟机上运行，允许开发者将任务交接出去后去做其他事情。Agent 通过数小时的时间处理它，迭代和测试直到对输出有信心，然后返回可以快速审查的东西：日志、视频录制和实时预览，而不是代码差异。

这使得并行运行 Agent 变得实用，因为产物和预览给了你足够的上下文来评估输出，而无需从零重建每个会话。人类的角色从指导每一行代码转变为定义问题和设置审查标准。

## 这种转变在 Cursor 内部正在进行

在我们内部合并的 PR 中，35% 现在是由在云虚拟机上自主运行的 Agent 创建的。我们看到采用这种新工作方式的开发者有三个特征：

1. Agent 几乎编写了 100% 的代码。
2. 开发者将时间花在分解问题、审查产物/代码和提供反馈上。
3. 他们同时启动多个 Agent，而不是手把手带一个到完成。

在这种方法成为标准开发实践之前，还有很多工作要做。在工业规模上，单个开发者可以解决的 flaky 测试或破坏性环境会变成中断每个 Agent 运行的问题。更广泛地说，我们仍然需要确保 Agent 能够尽可能有效地运作，并完全访问它们所需的工具和上下文。

我们认为昨天的发布是朝这个方向迈出的初始但重要的一步。
