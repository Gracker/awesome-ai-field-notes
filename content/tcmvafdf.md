## The third era of AI software development

When we started building Cursor a few years ago, most code was written one keystroke at a time. Tab autocomplete changed that and opened the first era of AI-assisted coding.

当我们开始构建 Cursor 时，大多数代码是一次一个字符输入的。标签自动补全改变了这种状况，开启了人工智能辅助编程的第一个时代。

Then agents arrived, and developers shifted to directing agents through synchronous prompt-and-response loops. That was the second era. Now a third era is arriving. It is defined by agents that can tackle larger tasks independently, over longer timescales, with less human direction.

然后智能体出现了，开发者转向通过同步的提示和响应循环来指导智能体。这是第二个时代。现在第三个时代正在到来。它以能够独立处理更大任务、在更长时间尺度上工作、需要更少人工指导的智能体为特征。

As a result, Cursor is no longer primarily about writing code. It is about helping developers build the factory that creates their software. This factory is made up of fleets of agents that they interact with as teammates: providing initial direction, equipping them with the tools to work independently, and reviewing their work.

因此，Cursor 不再主要关于编写代码。它关于帮助开发者构建创造其软件的工厂。这个工厂由他们作为队友交互的智能体组成：提供初始方向、为它们配备独立工作的工具，并审查它们的工作。

Many of us at Cursor are already working this way. More than one-third of the PRs we merge are now created by agents that run on their own computers in the cloud. A year from now, we think the vast majority of development work will be done by these kinds of agents.

我们中的许多人在 Cursor 已经这样工作了。我们合并的三分之一以上的 PR 现在由在云端计算机上独立运行的智能体创建。一年后，我们认为绝大多数开发工作将由这些类型的智能体完成。

## From Tab to agents

Tab excelled at identifying where low-entropy, repetitive work could be automated. For nearly two years, it produced significant leverage.

标签自动补长在识别低熵、重复性工作可以自动化的地方方面表现出色。近两年来，它产生了显著的杠杆效应。

Then the models improved. Agents could hold more context, use more tools, and execute longer sequences of actions. Developer habits began to shift, slowly through the summer, then rapidly over the last few months.

然后模型得到了改进。智能体能够持有更多上下文、使用更多工具、执行更长的动作序列。开发者的习惯开始转变，夏季缓慢转变，然后在最近几个月快速转变。

The transformation has been so complete that today, many Cursor users never touch the tab key. In March 2025, we had roughly 2.5x as many Tab users as agent users. Now, that is flipped: we now have 2x as many agent users as Tab users and agent usage in Cursor has surged.

转变如此彻底，以至于今天许多 Cursor 用户从不使用 Tab 键。2025年3月，我们的 Tab 用户数量大约是 agent 用户的 2.5 倍。现在，情况相反：我们的 agent 用户数量现在是 Tab 用户的 2 倍，而 Cursor 中的 agent 使用量激增。

But already this shift is giving way to something bigger. The Tab era lasted nearly two years. The second era, in which most work is done with synchronous agents, may not last one.

但这个转变已经在让位于更大的变化。标签时代持续了近两年。大多数工作通过同步智能体完成的第二个时代可能不会持续一年。

## Cloud agents and artifacts

Compared to Tab, synchronous agents work further up the stack. They handle tasks that require context and judgment, but still keep the developer in the loop at every step.

与标签自动补全相比，同步智能体在栈上工作得更远。它们处理需要上下文和判断的任务，但仍然在每个步骤中保持开发者参与其中。

But this form of real-time interaction, combined with the fact that synchronous agents compete for resources on the local machine, means it is only practical to work with a few at a time.

但这种实时交互形式，加上同步智能体在本地机器上竞争资源的实际情况，意味着一次只与少数几个智能体一起工作是实际可行的。

Cloud agents remove both constraints. Each runs on its own virtual machine, allowing a developer to hand off a task and move on to something else. The agent works through it over hours, iterating and testing until it is confident in the output, and returns with something quickly reviewable: logs, video recordings, and live previews rather than diffs.

云端智能体消除了这两个约束。每个智能体都在自己的虚拟机上运行，允许开发者将任务移交给其他智能体并继续处理其他事情。智能体通过数小时处理任务，迭代和测试直到对输出有信心，并返回一些可以快速审查的内容：日志、视频录制和实时预览，而不是差异。

This makes running agents in parallel practical, because artifacts and previews give you enough context to evaluate output without reconstructing each session from scratch.

这使得并行运行智能体成为实际可行的选择，因为工件和预览提供了足够的上下文来评估输出，而不需要从头重建每个会话。

The human role shifts from guiding each line of code to defining the problem and setting review criteria.

人类的作用从指导每一行代码转变为定义问题和设置审查标准。

## The shift is underway inside Cursor

Thirty-five percent of the PRs we merge internally at Cursor are now created by agents operating autonomously in cloud VMs. We see the developers adopting this new way of working as characterized by three traits:

我们内部在 Cursor 合并的 PR 的 35% 现在由在云端虚拟机中自主运行的智能体创建。我们看到开发者采用这种新的工作方式，其特点是：

1. Agents write almost 100% of their code.
1. 智能体编写几乎 100% 的代码。

2. They spend their time breaking down problems, reviewing artifacts / code, and giving feedback.
2. 他们把时间花在分解问题、审查工件/代码和提供反馈上。

3. They spin up multiple agents simultaneously instead of handholding one to completion.
3. 他们同时启动多个智能体，而不是手把手地完成一个智能体。

There is a lot of work left before this approach becomes standard in software development. At industrial scale, a flaky test or broken environment that a single developer can work around turns into a failure that interrupts every agent run.

在这种方法成为软件开发标准之前，还有很多工作要做。在工业规模上，单个开发者可以解决的不可靠测试或损坏环境，会变成影响每个智能体运行的中断性故障。

More broadly, we still need to make sure agents can operate as effectively as possible, with full access to tools and context they need.

更广泛地说，我们仍然需要确保智能体能够尽可能有效地运行，拥有它们需要的工具和上下文完全访问权限。

We think yesterday's launch is an initial but important step in that direction.

我们认为昨天的发布是朝着这个方向迈出的初步但重要的一步。

