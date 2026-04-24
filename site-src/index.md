---
layout: home

hero:
  name: AI Field Notes
  text: AI 领域精选资源导航
  tagline: 有观点 · 有评分 · 每日自动更新 · 682 条 · 2 篇有全文
  actions:
    - theme: brand
      text: 浏览全部
      link: /models
    - theme: alt
      text: GitHub
      link: https://github.com/Gracker/awesome-ai-field-notes

features:
  - title: '🧠 模型'
    details: 'GPT / Claude / Gemini / 开源模型 / 架构 · 94 条'
    link: /models
  - title: '🤖 智能体'
    details: 'Agent 框架 / MCP / A2A / 手机&桌面助手 · 105 条'
    link: /agents
  - title: '💻 AI编程'
    details: 'IDE / CLI / 代码审查 / 工作流 · 164 条'
    link: /coding
  - title: '⚡ 基础设施'
    details: '推理部署 / RAG / 微调 / 评测 / 多模态 · 60 条'
    link: /infra
  - title: '🌍 行业观察'
    details: 'AI 产品 / 大厂战略 / 融资 / 市场分析 · 53 条'
    link: /industry
  - title: '📖 学习资源'
    details: '教程 / 论文 / 提示工程 / 演讲 · 115 条'
    link: /learning
---

## 🆕 最新 10 篇

### [GPT Image 2的出现，一个设计师的冷思考](https://mp.weixin.qq.com/s?__biz=MjM5MjIyOTA0Mw==&mid=2650203005&idx=1&sn=af664106ce7344b65a98bd6f7265e8ff)
@梵猩智云 · ⭐⭐⭐3 🇨🇳 · 昨天

设计师视角反思GPT Image 2的影响，认为这是从工具升级到分水岭级别的跃迁，文字渲染准确、多语言海报、UI草图等信息图生成能力将设计执行门槛降至几乎为零。作者指出设计师的真正价值不是做图而是做对的选择，并提出三条出路：往上走（判断层）、往深走（垂直领域）、跟AI协作（超级设计师）。核心观点是工具变强不是设计师的灾难，不愿意接受身份重新定义才是。

`AI-image` `GPT-Image-2` `designer` `AI-impact` `product-thinking`

---

### [AI Agent 工程化实践指南：如何构建可靠的 Harness 系统](https://mp.weixin.qq.com/s?__biz=MzE5MTU5MjcwNw==&mid=2247484077&idx=1&sn=ee3fd75a3799b07df9c08fcbda2b21e4)
@Liz的AI冰美式 · ⭐⭐⭐⭐4 🇨🇳 · 昨天

文章系统阐述Harness Engineering的核心价值：AI时代技术重心正从单点能力转向对整体系统的组织、约束和协同。作者从Prompt工程化、Context工程化、Tools工程化、Workflow工程化四个维度展开，结合OpenAI、Anthropic、LangChain的实践经验，介绍Generator-Evaluator模式、多Agent协作框架（Anthropic 16个并行Claude协作编写C编译器案例）。强调Harness的核心不是塞信息而是设计信息结构，长任务靠外部状态管理而非更强Prompt。

`harness-engineering` `agent-frameworks` `prompt-engineering` `context-management` `workflow`

---

### [Building agents that reach production systems with MCP](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp)
@Anthropic · ⭐⭐⭐⭐4 🌐 · 昨天

Anthropic官方博客，系统阐述将Agent连接到外部生产系统的三条路径（Direct API、CLI、MCP）的适用场景及优劣。重点介绍构建生产级MCP服务器的最佳实践：远程服务器实现最大覆盖、按Intent而非端点分组工具、设计代码编排处理大表面、丰富语义（Elicitation/MCP Apps）、标准化认证（CIMD+Vaults）。提出MCP客户端的上下文效率优化（按需加载工具定义85%+节省、程序化工具调用37%节省）。

`MCP` `model-context-protocol` `agent-integration` `cloud-agent` `skills`

---

### [Harness 层怎么自我进化？来自斯坦福大学和 MIT 的一项新研究](https://mp.weixin.qq.com/s?__biz=MzE5MTU5MjcwNw==&mid=2247484082&idx=1&sn=aac7ea3868e31bcc3d47e58724adeb19)
@Liz的AI冰美式 · ⭐⭐⭐⭐4 🇨🇳 · 昨天

介绍斯坦福+MIT论文《Meta-Harness》，提出让Harness本身进入自动化演进。当前文本优化器在优化Harness时核心问题是反馈压缩——几千步轨迹被压缩成单分数，丢失诊断上下文。Meta-Harness通过将完整文件系统（Python源码、执行日志）开放给代码Agent，让它像人类工程师一样翻阅历史候选、推理失败原因、编写修复代码。实验中TerminalBench-2通过80行环境快照代码使Claude Haiku 4.5达37.6%通过率。

`harness-engineering` `self-improving` `Meta-Harness` `Stanford` `MIT`

---

### [深入源码：Hermes Agent 如何实现 Self-Improving](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247559661&idx=1&sn=ca9426f948819f172ec44f671127aa29)
@Unknown · ⭐⭐⭐⭐4 🇨🇳 · 昨天

深入分析Hermes Agent开源架构，阐述其Self-Improving闭环的三个子系统：Memory（2200字符容量限制，声明式事实，逼Agent压缩信息；冻结快照机制保护上下文缓存）、Skill（踩坑后自动创建/patch SKILL.md，Pitfalls节记录教训，按需渐进加载）、Nudge Engine（后台fork独立Agent实例审查会话，每10回合/10迭代触发，输出重定向/dev/null用户无感知）。与OpenClaw对比：Skill需手写，Agent不自主学习；Hermes让Agent越用越强。

`Hermes-Agent` `self-improving` `memory` `skill` `agent-architecture`

---

### [从Hermes Agent到 AgentX，AI的自我进化如何团队项目紧密结合？](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247559661&idx=1&sn=ca9426f948819f172ec44f671127aa29)
@Unknown · ⭐⭐⭐⭐4 🇨🇳 · 昨天

作者从Hermes Agent获得启发，开发AgentX插件将自我进化机制从Agent迁移到项目层面。核心设计：知识沉淀分两层（Markdown是证据层，Skill是能力层，必须从Markdown演化而来）；Markdown按Claude Code官方实践分层组织（AGENTS.md入口→专题文档→模块文档→SKILL.md能力层）；Harness Engineering哲学：用Bash/Hook搭骨架，用模型做理解和表达。目标是让Claude Code、Codex、OpenCode等不同agent进入同一项目时，都能共享项目积累的知识资产。

`AgentX` `project-knowledge` `coding-agent` `Hermes` `skill-evolution`

---

### [Greg Brockman：GPT-5.5是一种新的智能类别](https://x.com/gdb/status/2047381612372115812)
@@gdb · ⭐⭐⭐⭐4 🇨🇳 · 昨天

OpenAI联合创始人Greg Brockman定义GPT-5.5为一种新的智能类别：在极少人工干预下完成复杂任务，token效率极高，延迟低，可大规模运行。Brockman强调这是真正向让AI完成计算机工作迈进的里程碑。GPT-5.5现已在ChatGPT和Codex中可用，代表Agent时代的基础模型能力基准。

`x` `ai-tools` `gpt-5.5` `openai`

---

### [Peter Yang x Mercury VP：如何为Agent设计API和MCP实战复盘](https://x.com/petergyang/status/2047320679889162321)
@@petergyang · ⭐⭐⭐⭐4 🇨🇳 · 昨天

Peter Yang与Mercury VP @rywiggs合作推出关于Agent API和MCP设计的深度播客。核心观点：2020s的用户交互界面是API和MCP（Machine Communication Protocol），而非传统App。Mercury用Claude Code加500万字公司知识库构建第二大脑，每天自动生成日程/Linear/Slack简报。节目分享了：如何构建Agent友好的知识库结构、如何设计MCP工具接口、最佳API设计原则。这是第一份系统性Agent API/MCP设计实战复盘。

`x` `workflow` `api` `mcp` `agent`

---

### [Andrej Karpathy：Farzapedia用LLM把个人数据变成个人维基](https://x.com/karpathy/status/2040572272944324650)
@@karpathy · ⭐⭐⭐⭐4 🇨🇳 · 昨天

Andrej Karpathy推荐Farzapedia方案：用LLM将2500条日记、Apple Notes、iMessage对话转化为400篇结构化个人Wikipedia文章，涵盖朋友、创业项目、研究领域、喜爱的动漫及其影响。相比AI越用越懂你的隐性记忆，Farza的显式知识库方案更透明、可控、可复用。Karpathy高度评价这是Wiki LLM思路的最佳实践，为个人AI助手个性化提供了新范式。

`x` `ai-tools` `personal-knowledge` `llm`

---

### [Google DeepMind：Gemini 3.1 Flash TTS用自然语言控制语音风格](https://x.com/GoogleAI/status/2044447560384102592)
@@GoogleAI · ⭐⭐⭐⭐4 🇨🇳 · 昨天

Google DeepMind发布Gemini 3.1 Flash TTS，号称迄今最具表现力和可控性的TTS模型。核心创新是Audio Tags——用自然语言命令嵌入音频，可控制语速、语调、情感表达。这意味着TTS从选择固定音色升级为用Prompt控制声音，是AI语音交互的范式级进步。适用场景：语音助手、有声内容创作、无障碍工具。

`x` `ai-tools` `tts` `gemini` `google`

---
