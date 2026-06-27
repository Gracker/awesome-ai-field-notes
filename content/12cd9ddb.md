# Project Fetch: Phase two

- **ID**: 12cd9ddb
- **原文链接**: https://www.anthropic.com/research/project-fetch-phase-two
- **作者**: Michael Ilie, C. Daniel Freeman, Kevin K. Troy (Anthropic Frontier Red Team)
- **日期**: 2026-06-18
- **分类**: agents
- **标签**: anthropic, claude, opus-4.7, robotics, agents, physical-ai, red-team
- **质量评分**: 4/5
- **抓取时间**: 2026-06-27T12:40:00

---

## 中文翻译

### 实验背景

2025 年 8 月，Anthropic 进行了 **Project Fetch** 实验，让非机器人学专业的 Anthropic 员工使用一台现成的四足机器人（robodog）完成复杂（且有趣）的任务。实验发现：获得当时最强模型 Claude Opus 4.1 协助的小组，明显胜过只能依赖互联网和自身智慧的小组。

在让同事拖着机器人去仓库做实验之前，研究人员先确认 Opus 4.1 是否能完全独立完成任务——显然不能，它跟没有 Claude 协助的小组一样卡在"如何连接机器人"的前期步骤上。

但 AI 模型发展得太快了——甚至比那只差点撞上人类小组的失控 robodog 还快。

于是 Anthropic 重启 Project Fetch，看更新的模型能否超越上一代。结果是：**Claude Opus 4.7 在无人协助的情况下，完所有参与者不到一年内完成的所有任务，速度约为最快人类小组的 20 倍。**

### 实验设计

原始 Project Fetch 让随机分配的小组（有或无 Claude 协助）完成以下步骤：用厂商控制器操作 robodog、连接视频与 lidar 传感器、编写程序手动控制 robodog、开发路径监控、检测沙滩球、最终整合实现自主取球。

Phase Two 中，研究人员无法让 Claude 使用物理控制器，也没评估研究人员使用 Claude 编写的控制器取球的时间（但确认其按预期工作）。在其余任务子集上，用 Opus 4.7 在 Claude Code 中以最高推理强度（adaptive thinking, effort=max）跑了三次试验。

研究人员的工作仅限于：把运行 Claude Code 的笔记本接入 robodog、输入初始提示词、批准命令、批准模型进入下一任务。

### Claude 的优势

简单来说：在所有至少一个人类小组完成的任务上，Opus 4.7 完成任务的速度**至少快 10 倍**。

考虑四个人类小组都完成的 4 个任务，Opus 4.7 平均比"无 Claude 组"快 37 倍以上，比"有 Claude 组"快 18 倍以上。

人类在选择 robodog 传感器接口的多种方案时犹豫不决，而 Opus 4.7 能迅速识别最优路径。它写的大部分代码一次就过（这在原始实验中两组人类都做不到）。从代码量看，Opus 4.7 几乎与两个小组同样成功，但代码量只有"有 Claude 组"的十分之一。

Opus 4.7 并不完美——比如它默认使用了过时的目标检测算法。但即便如此，它也能绕过这个问题找到有效方案。

在任务完成时间上，Opus 4.7 表现出很小的任务内方差。总体而言，在其实验能力范围内的任务上，Claude 已经相当可靠。

值得强调的是（如上篇博客所述），这种进步并不是因为 Anthropic 集中精力改进模型的机器人能力。这些改进与 LLM 发展史上的众多进步一样，来自更通用的规模化扩展。

### Claude 的不足

人类用双手练习后，能驾驶 robodog 轻推沙滩球回到出发点（仿真草皮）。这需要快速感知球是否偏离、错误与上一指令的关系、球当前位置、然后调整后续输入更精确地移动球——这是人类擅长的闭环反馈（即使需要犯错和学习）。

Phase Two 实验中，Claude 难以捕捉这种细腻度。跟到达"需要写程序自主取球"阶段的人类一样，Claude 能把机器人移到球后方并对准准备将球撞回起点，但控制很粗糙，（跟人类参与者一样）没有成功。

一位机器人学经验更丰富的研究人员成功完成了"编程自主取球"任务。Anthropic 认为，给当前代 Claude 更多时间与脚手架，它很可能也能完成。下一阶段要观察的是：模型能否以在其他元素上展示出的速度与可靠性，独立完成这最后一步。

### 启示

在 Phase One 的文章中，Anthropic 强调 LLM 能为非专家人类使用机器人提供助力。现在这一论断更加成立——模型能比此前"人类+模型结对编程"更快地独立完成工作，意味着人类可以更快过渡到"控制和使用机器人"的阶段。在某些任务上，循环中的人类用 D-pad 操作机器人的表现仍可能超过 AI 模型。

有趣且不同的是，我们似乎离"模型能相对轻松地使用现成物理工具"的世界更近了——至少在有限用途上。这与 AI 模型从软件编辑工具（如 string-replace）过渡到更智能体化的编码过程类似。我们很可能正在进入**物理智能体 AI 的早期时代**。

还需要更多研究来理解模型让这些物理工具更定制化的能力——无论是为特定任务编写控制策略，还是设计机器人系统。通向"物理能力强且适应性强的语言模型"的更宏大愿景，可能存在实质性障碍。但经验表明，看似很大的模型能力鸿沟，可能会被快速跨越。模型构建自己的软件工具在不久前还显得不可思议，但正在发生。对硬件沿同样轨迹演进的可能性，也不应轻易排除。

*注：6 月 18 日更新——修正了 Project Fetch 第一阶段的日期。*

*来源：Anthropic Frontier Red Team 2026-06-18*

## English Original

### Background

In August 2025, we ran an experiment to see how much Claude could help Anthropic employees—who were not robotics experts—perform sophisticated (and amusing) tasks with an off-the-shelf robotic quadruped (henceforth, a robodog). We called this Project Fetch. We found that access to our state-of-the-art model at the time (Claude Opus 4.1) helped one team substantially outperform the other, who had to rely only on the internet and their own ingenuity. The Claude-enabled team got more done, faster.

Before we dragged our colleagues to a warehouse for the experiment, we double checked whether Opus 4.1 could do the tasks entirely on its own. Unquestionably, it could not. Much like our team without Claude, it got hung up on the preliminary task of figuring out how to connect to the robot.

But AI models are moving fast—even faster than the runaway robodog that almost rammed into one of our human teams back in August.

We figured it was time to revisit Project Fetch to see if our newer models could outperform the previous generation. Not only did they do that, but **Claude Opus 4.7—operating without human assistance—was about 20 times faster than the fastest human team at all tasks completed by our participants less than a year ago**.

### What we did

The original Project Fetch had teams of Anthropic employees (randomly assigned to work with or without Claude) do the following steps: operate the robodog using the manufacturer-provided controller, connect to the robodog's video and lidar sensors, write and operate a program to manually control the robodog, develop a way to monitor the robodog's path through space, write a program to detect the beach ball, and finally put it all together to autonomously retrieve the ball.

For this autonomous update, we couldn't ask Claude to use a physical controller, nor did we evaluate the time it took a researcher to use the Claude-programmed controller to retrieve the ball (though we did confirm that it worked as intended). On the remaining subset of tasks, we ran three trials of Opus 4.7 using adaptive thinking with effort set to maximum in Claude Code.

### Where Claude excelled

Very simply: on every task that was completed by at least one human team in August, Opus 4.7 completed the same task at least ten times faster. If you consider the four tasks that were completed by both human teams, Opus 4.7 was, on average, more than 37 times faster than Team Claude-less and more than 18 times faster than Team Claude.

Whereas the humans struggled to choose between multiple different approaches to interface with the dog's sensors, Opus 4.7 was able to quickly identify the best path. Much of the code it wrote was effective on the first try. Indeed, we can see evidence of Opus 4.7's efficiency when we look at the volume of code it generated: it was as or more successful than both human teams while producing almost ten times less code than Team Claude.

We observed little within-task variance on completion times for steps the model finished. Overall, for the tasks in this experiment within its capability envelope, Claude is now quite reliable.

It is worth underscoring (as we did in our previous post) that this progress is not the result of a concerted effort to improve the robotics capabilities of our models. These improvements, like so many others in the history of LLM development, have emerged from much more general scaling.

### Where Claude struggled

When using their hands, and with some practice, our humans were able to pilot the robodogs to gently nudge a beach ball back to the home base. This required the ability to quickly perceive if the ball had gone off course, how that error related to the previous command, where the ball was now, and then how to adjust future inputs to more precisely move the ball. This is a kind of closed loop at which people excel.

In our Phase Two experiments, Claude struggled to capture this subtlety. Like the humans who reached the phase of needing to write a program for autonomous beach ball retrieval, Claude was able to move the robot behind the ball and position it to knock the ball back to the starting point. But the efforts to do so were poorly controlled and (again, like our human participants) not successful.

One of our researchers with more robotics experience than our Phase One volunteers successfully accomplished the task of programming autonomous fetching. With more time and additional scaffolding, we think it is very likely that current generations of Claude could do the same.

### What this means

Writing about Phase One, we emphasized how LLMs could provide uplift to non-expert humans needing to use robots. This is even more true now than before. Models now complete what was previously pair-programming work between humans and models much more quickly by themselves, which means that people can more quickly transition to controlling and using the robots.

What is interesting and different is that we now seem much closer to a world where models will be able to use off-the-shelf physical tools with relative ease—at least for limited purposes. This is similar to how AI models used existing software editing tools like string-replace when they made the transition to more agentic coding. We are plausibly entering the early era of _physical_ agentic AI.

More research is needed to understand models' ability to make these physical tools more bespoke, whether by writing control policies tailored to particular tasks or by designing robotic systems. But as we have seen, apparently large distances in model capability can be traversed quickly.

_Updated Jun 18: Corrected the date of the first phase of Project Fetch._
