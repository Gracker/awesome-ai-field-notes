---
id: "7446883752334065748"
cubox_url: https://cubox.pro/web/card/7446883752334065748
url: https://mp.weixin.qq.com/s?__biz=MzkzNDQxNTI4OA==&mid=2247483840&idx=1&sn=e4da453086f1f3cf660dd25b2de15cb5&chksm=c394cb7b68fcde29ddcc61789a4e6a3ef94fa9ce1afb7270184354d7d29bfdb3421d728d8ce4&mpshare=1&scene=1&srcid=0423q3SKvW7vUuhiw3pRmVgH&sharer_shareinfo=b9cd866b181d5d2c0c62687d361c4bd8&sharer_shareinfo_first=ac0ba5471739e6da5738a8e927e4fff2
tags: []

---
# 从Hermes Agent到 AgentX，AI的自我进化如何团队项目紧密结合？

从Hermes Agent到 AgentX，AI的自我进化如何团队项目紧密结合？

[Read in Cubox](https://cubox.pro/web/card/7446883752334065748)  
[Read Original](https://mp.weixin.qq.com/s?__biz=MzkzNDQxNTI4OA==&mid=2247483840&idx=1&sn=e4da453086f1f3cf660dd25b2de15cb5&chksm=c394cb7b68fcde29ddcc61789a4e6a3ef94fa9ce1afb7270184354d7d29bfdb3421d728d8ce4&mpshare=1&scene=1&srcid=0423q3SKvW7vUuhiw3pRmVgH&sharer_shareinfo=b9cd866b181d5d2c0c62687d361c4bd8&sharer_shareinfo_first=ac0ba5471739e6da5738a8e927e4fff2)  

---

GitHub：https://github.com/lukelmouse-github/AgentX^\[7\]^

如果你已经在用 Claude Code，当前最简单的安装方式是：

    /plugin marketplace add lukelmouse-github/AgentX/plugin install ax@lukelmouse-github


这半年，AI Coding 工具的能力提升非常明显。  
Claude Code、Codex、OpenCode 这类 agent，已经不只是"代码补全器"，而是在逐步接管真实开发过程中的完整动作链：

•读代码•改文件•跑命令•查日志•排 bug•理解架构•补文档•生成 workflow

但我越来越明确地意识到一件事：

**今天大多数 AI Coding 只解决了"这次任务更快完成"，还没有真正解决"这个项目会不会因此变得越来越好做"。**

这是两个完全不同层级的问题。

前者是个人效率。  
后者是项目和团队是否开始拥有"持续积累知识、持续进化能力"的机制。

而我最近做的 **AgentX** ，核心就是后者。

*** ** * ** ***

## 一、Hermes Agent 给我的启发：真正重要的不是会做事，而是会积累


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FYNkojQPw39KpYt9HF99N1TUCXfeJiaLViaibom4uvJ2ZJ1ADGp51sK6mLZAAceLDqeDVxBkwYcbxCibBWmOvlXYx15xe82kW6Tibwe4VicHC1LbY0%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

我对这个问题的思考，很大程度上来自 Hermes Agent^\[1\]^。

Hermes Agent 最有价值的地方，不只是"它能做很多事"，而是它明确把**学习闭环** 放进了系统里：从经验中生成 skills、在使用中改进 skills、搜索历史会话、持续沉淀知识。

这个方向非常关键，因为它回答的是一个更本质的问题：

**AI agent 的长期价值，到底来自什么？**

不是来自某次回答有多惊艳，也不是来自某次 patch 改得有多快，而是来自：

**它能不能把这次经验，变成下一次可复用的能力。**

但 Hermes Agent 的自我进化，更多还是从"agent 本身"的角度出发。  
我想继续往前推进一步：

**如果把这种自我进化机制，从 agent 身上迁移到项目里，会发生什么？**

*** ** * ** ***

## 二、AI Coding 的下一阶段，不是更强的个人助手，而是更强的项目知识系统

真实开发中，最难的从来不是"写一段新代码"，而是反复遇到这些问题：

•这个项目的核心架构到底应该怎么理解？•这个模块的边界是什么？•某类 bug 过去是怎么定位出来的？•哪些日志是关键线索，哪些只是噪音？•哪个环境问题根本不是代码问题？•哪条 workflow 才是团队真正跑顺的路径？

这些知识每天都在产生，但大多数时候，它们只存在于对话里、临时笔记里、某个人的脑子里。

于是项目会反复支付同样的成本：

•同样的坑反复踩•同样的架构问题反复解释•同样的排障路径反复重建•同样的 prompt 反复写

所以我越来越确信：

**AI Coding 真正值得做的，不只是"把单次任务做得更快"，而是"把项目知识自动沉淀下来"。**

这就是 AgentX 的出发点。

*** ** * ** ***

## 三、AgentX 的核心目标：不是增强某个 agent 的私有记忆，而是增强项目的知识生产能力

AgentX^\[2\]^ 的核心思想很简单：

**把 Hermes Agent 风格的自我进化机制，从 agent 迁移到项目。**

它不想做"某个 AI 的私有 memory 增强器"，而是要做"项目级知识沉淀插件"。

它的目标不是记住"我上次说过什么"，而是自动把真实工作中的经验沉淀成项目资产，比如：

•核心架构说明•模块上下文•项目约定•排障结论•环境坑位•可复用工作流•最终可被 agent 自动发现和调用的 skills

一旦知识开始以项目资产的形式存在，它就天然拥有几个关键特性：

•可以被 Git 管理•可以被 review•可以被重构•可以跟随项目长期演化•可以被不同 coding agent 继续读取和复用

也就是说，知识不再属于某个 agent，而是属于项目本身。

*** ** * ** ***

## 四、为什么我强调"跨 agent 可读"


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2FYNkojQPw39IMHjaAQcvh9uzvZs1icl8pxLT3xoofjjElekofDZwuZlH4Hp4DBwyvbj4N4OCQImZMLS4tMXLicQPGSUQgwokhGqiaamOrw14VrQ%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

今天的 AI Coding 世界不可能只有一个工具。  
Claude Code、Codex、OpenCode，以及未来更多 agent，会长期并存。

所以如果知识沉淀最终只能服务某一个产品，那它的长期价值一定是受限的。

AgentX 从一开始就尽量避免这种绑定。  
它的方向是把知识沉淀成更开放、更通用、更接近标准化的形态，例如：

•项目级入口文档•可被 Git 管理的 Markdown•模块级上下文文档•SKILL.md 这类可迁移技能格式

这和 Agent Skills^\[3\]^ 的开放标准非常一致：  
skill 应该是简单的、文件化的、可共享的，而不是被某个工具锁在私有格式里。

所以 AgentX 想做的不是"给某个 agent 喂私有记忆"，而是：

**把知识沉淀成项目能长期持有、不同 agent 尽量都能消费的格式。**

*** ** * ** ***

## 五、AgentX 最关键的设计：先生成 Markdown，再让 Skill 从 Markdown 中演化出来


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FYNkojQPw39I2vLl7sAiaGibf9UwLl6Rtp2mwvxZ1qMcekQ3S2HdUicaX052WonHicS8dialea7c5PB7v5MO1ywoqD1uIC8emSaibwuGiaDicrhYCS0M%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

这一点是 AgentX 的核心。

很多人一看到"自动沉淀知识"，会自然想到"那就是自动生成 skill"。  
但我认为这一步绝对不能走快。

因为 skill 不是会话摘要，也不是任务备忘录。  
skill 是一种更高阶的能力抽象，它代表的是：

•稳定经验•可复用流程•明确触发条件•可被 agent 自动发现和调用的能力单元

所以在 AgentX 里，知识沉淀一定分两层：

### 第一层：Markdown

先把真实工作中形成的经验沉淀成 Markdown，例如：

•某个架构模块的解释•某类 bug 的排查路径•某个环境问题的结论•某条 workflow 的标准做法•某个模块的上下文说明

这些文档先成为项目的**知识基础层** 。

### 第二层：Skill

只有当这些 Markdown 已经足够稳定、足够重复、足够可复用时，AgentX 才进一步把它们抽象成 Skill。

所以 AgentX 的路径不是：

**对话 -\> Skill**

而是：

**对话 -\> Markdown -\> Skill**

这不是形式主义，而是一个关键的质量约束。

因为今天很多 AI 系统都容易犯同一个错误：

**把一次性的经验，误判成长期能力。**

而在 AgentX 里：

•Markdown 是证据层•Skill 是能力层

没有证据层，就不该直接进入能力层。

*** ** * ** ***

## 六、AgentX 生成的 Markdown，不是随手笔记，而是尽量对齐 Claude Code 官方最佳实践

我在做 AgentX 时，另一个非常在意的点是：

**它生成的 Markdown 不能只是把对话抄下来，而是要尽量符合 Claude Code 官方推荐的知识组织方式。**

我主要参考了三类官方文档：

•Claude Code Memory^\[4\]^•Claude Code Skills^\[5\]^•Skill Authoring Best Practices^\[6\]^

虽然这些文档主要讲的是 CLAUDE.md 和 SKILL.md，但其中很多原则同样适用于项目知识沉淀。

例如：

•文档要具体，不要模糊•结构要清晰，不要流水账•内容要简洁，不要超长•能分层就分层•能渐进式加载就不要一次性塞满•确定性操作优先交给脚本

我把这些原则映射到 AgentX 里，形成了下面这张约束表。

### AgentX 与 Claude Code 实践对照


原则

AgentX 做法

对齐

内容具体

写清路径、命令、模块、结论

✅

结构清晰

用标题、分段、列表组织信息

✅

聚焦主题

单篇 Markdown 只讲一类问题

✅

渐进披露

入口文档、专题文档、模块文档分层组织

✅

引用克制

优先浅层引用，避免多层跳转

✅

易于发现

统一沉淀到固定目录和命名

✅

确定性优先

Bash + Hook 处理流程与状态

✅

Skill 单一能力

Skill 从稳定 Markdown 中演化

✅

这张表的核心含义只有一句：

**AgentX 不是让模型"顺手写点文档"，而是在尽量用 Claude Code 官方推荐的方法，生产真正能被项目持续消费的知识。**

*** ** * ** ***

## 七、AgentX 里的 Markdown 不是平铺的，而是"分层 + 渐进式披露"的

AgentX 还借用了 Claude Code skill 设计里一个特别重要的思想：  
**progressive disclosure，也就是渐进式披露。**

这个思想放到项目知识沉淀里，价值非常大。

因为项目知识本来就不应该一次性全部塞进上下文。

如果每次都把所有架构、所有模块说明、所有历史 bug、所有 workflow 一起加载进来，agent 的上下文很快就会变成垃圾堆。

所以 AgentX 对 Markdown 的目标不是"越多越好"，而是：

**分层组织，按需读取。**

理想中的结构大致是：

•AGENTS.md：项目主入口•docs/ai-context/*.md：专题知识•{module}/AGENTS.md：模块局部上下文•.agents/skills/*/SKILL.md：已经稳定的能力单元

也就是说：

•上层文档更像导航和目录•下层文档承接专题和局部细节•Skill 则是从这些文档里进一步抽象出来的能力层

这就是 AgentX 所说的"**分层式的渐进式披露** "。

它不是把所有知识压成一份大文档，而是让项目逐步长出一棵知识树。

*** ** * ** ***

## 八、为什么 Skill 必须严格从 Markdown 演化出来

这个问题值得再强调一次，因为它是 AgentX 的"稳定性底线"。

一次对话最多只能证明：

**这次做成了。**

但 Skill 代表的是：

**以后还值得重复这么做。**

这两件事差别很大。

所以在 AgentX 里，Skill 的来源必须是：

•已经沉淀下来的 Markdown•被多次验证过的排障路径•已经稳定的项目工作流•触发条件明确、结构清晰的知识块

换句话说：

•bug 排查 Skill，必须先有 bug 文档•日志分析 Skill，必须先有日志排查文档•架构理解 Skill，必须先有架构文档•workflow Skill，必须先有流程类文档

所以 AgentX 的原则不是"能生成 Skill 就尽快生成"，而是：

**先让知识在项目中以 Markdown 的形式活下来，再让 Skill 从这些 Markdown 中严格演化出来。**

我觉得这件事会让系统慢一点，但会让它稳很多。  
而面向项目和团队的 AI 基础设施，稳定一定比炫技重要。

*** ** * ** ***

## 九、Harness Engineering：不是堆 prompt，而是先把工作框架搭稳


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2FYNkojQPw39JUGVEb0wJUXMNM7NA3ZSuJdFeQ1LNNCL4RoictSMkv4OGulGFbaQWy7W8NPRC6JBNsiamIEUvegfshddCIbSKUiamOLGHEbq21dE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D3)

AgentX 还有一条特别重要的设计哲学，就是尽量往 **harness engineering** 这个方向靠。

它的核心思想不是"提示词写得多复杂"，而是：

**先把流程、规则、环境、边界搭稳，再让模型发挥。**

Claude Code 官方对 hooks 的定义，本身就很有这个味道：  
hook 的意义就是在生命周期关键点执行 shell 命令，提供确定性控制，而不是期待模型自己记得去做每一件事。

所以在 AgentX 里，我尽量把职责拆成两类。

### Bash 负责的部分

•hook 接入•事件编排•硬指标快筛•文件系统操作•候选池管理•状态推进•日志记录•正式写入动作

### LLM 负责的部分

•语义价值判断•候选 Markdown 生成•内容压缩和抽象•从 Markdown 中提炼 Skill•判断某类知识是否具备升级价值

一句话概括：

**用 Bash 和 Hook 搭骨架，用模型做理解和表达。**

这也是 AgentX 为什么会尽量用确定性规则，而不是依赖模糊提示和松散约束。

*** ** * ** ***

## 十、AgentX 还在快速迭代，但已经跑通的 MVP 足够让我兴奋

这里也必须说一句实话。

AgentX 现在离我心里的"完整形态"还差得很远。  
整体架构还在持续迭代中，很多真正想做的能力，现在也只是刚把路径想清楚，或者只是有了第一版雏形。

但即便如此，我还是很想尽早把它拿出来聊一聊。

因为它已经跑通了一个让我非常兴奋的 MVP：

**Claude Code 的工作过程，已经可以开始被自动观察、自动判断，并自动沉淀成项目知识。**

这件事一旦能跑通，后面的想象空间就完全不一样了。

它意味着：

•AI Coding 不只是帮一个人更快写代码•它还可以开始帮助一个项目自动积累知识•进而帮助一个团队慢慢形成自己的知识系统•最后让不同 agent 在同一个项目里共享这些沉淀结果

这正是我最想验证的事情。

*** ** * ** ***

## 十一、我真正期待的，不是"今天更快"，而是"明天更顺"

如果把我对 AgentX 的期待压缩成一句话，那就是：

**我希望它让项目越用越舒服。**

也就是说，随着项目不断使用 AgentX，它应该逐步沉淀出：

•这个项目的核心架构应该怎么解释•这个模块的上下文是什么•哪类日志应该怎么查•哪些环境坑以前踩过•哪条 workflow 已经很成熟•哪些知识已经足够稳定，可以升级成 Skill

到那时，再进入同一个项目的 agent，不管是 Claude Code、Codex，还是 OpenCode，都会比第一次来时更容易获得正确上下文。

那时候，AI Coding 就不再只是"每次重新开一局"，而会更像：

**项目和团队真的在一起自我进化。**


