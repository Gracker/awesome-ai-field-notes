---
layout: home

hero:
  name: AI Field Notes
  text: AI 领域精选资源导航
  tagline: 有观点 · 有评分 · 每日自动更新 · 612 条 · 240 篇有全文
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
    details: 'Agent 框架 / MCP / A2A / 手机&桌面助手 · 104 条'
    link: /agents
  - title: '💻 AI编程'
    details: 'IDE / CLI / 代码审查 / 工作流 · 161 条'
    link: /coding
  - title: '⚡ 基础设施'
    details: '推理部署 / RAG / 微调 / 评测 / 多模态 · 60 条'
    link: /infra
  - title: '🌍 行业观察'
    details: 'AI 产品 / 大厂战略 / 融资 / 市场分析 · 55 条'
    link: /industry
  - title: '📖 学习资源'
    details: '教程 / 论文 / 提示工程 / 演讲 · 115 条'
    link: /learning
---

## 🆕 最新 10 篇

### [万字干货：理解 Harness Engineering，看这一篇就够了](/entry/72x6hfdeebbo) 📄
@咸鱼（TRAE 开发者用户） · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-12

Harness Engineering 是继 Prompt Engineering、Context Engineering 之后，由 Mitchell Hashimoto（HashiCorp 联合创始人）提出并因 OpenAI 报告而广为人知的第三类 AI 工程化方法。其核心隐喻是为 AI Agent 这匹野马套上缰绳，通过约束、引导与纠正确保其稳定运行。该框架以 R.E.S.T 四目标（可靠性、效率、安全性、可追溯性）为基石，通过上下文管理、Function Calling 降级策略、沙盒隔离与多层度量体系，将 Agent 从有趣的玩具变为可规模化的可靠生产力工具。

`harness-engineering` `agent-frameworks` `prompt-engineering` `context-engineering` `reliability`

---

### [破局Agent时代：ARIES RISCV+AI架构分析](/entry/jvblhpoud3ey) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-04-12

ISSCC 2026 展示的 ARIES 架构代表了 AI 芯片从算力怪兽向有脑子的行动派的进化路线。ARIES 通过 RISC-V CPU 集成（调度控制前额叶）+ 280MB 大容量 SRAM + CIM 存内计算，实现 PD/AF 融合方案（拒绝 NVIDIA/Groq 的物理分离路线），以 14nm 工艺在能效比上超越 4nm GPU。其三引擎 NPU Core（TCE/TME/VCE）+ 相似性感知 TCAM + LUT 非均匀量化，构成 Agent 时代芯片的差异化竞争力。

`risc-v` `ai-chip` `agent-era` `in-memory-computing` `cim`

---

### [万字干货：理解 Harness Engineering，看这一篇就够了](/entry/cc15hq4t) 📄
@咸鱼（TRAE 开发者用户） · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-11

Harness Engineering 是继 Prompt Engineering 和 Context Engineering 之后 2026 年 AI 领域的核心工程方法论，由 HashiCorp 联合创始人 Mitchell Hashimoto 提出。核心比喻是缰绳：AI Agent = SOTA 模型（野马）+ Harness（驾驭系统）= 千里马。文章系统性拆解了 Harness 的设计目标（R.E.S.T 模型：可靠性、效率、安全性、可观测性）、四层架构（控制平面+数据平面）、核心运行机制（REPL 容器抽象、Token 转化流水线、Function Calling 生命周期）、规划模式（Plan-and-Execute 为主）、沙盒执行框架（从进程级到 VM 级四档隔离）以及度量体系。适合 Agent 系统工程师建立完整的工程化框架认知。

`harness-engineering` `ai-agent` `prompt-engineering` `context-engineering` `llm`

---

### [破局Agent时代：ARIES RISCV+AI架构分析](/entry/n3m8itb5) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-04-11

本文深度分析 ISSCC 2026 展示的 ARIES 芯片架构，这是一款专为 AI Agent 时代设计的 RISC-V+AI 异构 SoC。核心创新三点：第一，将 RISC-V CPU 直接集成进 SoC 核心区作为调度单元，解决传统 NPU 控制流跳回 Host CPU 的 PCIe 时延问题；第二，采用统一 Tile + 独立时钟域替代 PD/AF 物理分离，同一硬件动态切换算力密集和访存密集模式；第三，堆 280MB 片内 SRAM + CIM 存内计算消灭访存瓶颈，通过 LUT-based 多精度量化在 14nm 工艺实现超越 4nm GPU 的能效比（YOLO 系列 10.12x FPS/W 提升）。ARIES 代表了 Agent 时代逻辑控制与极致算力耦合的实用主义芯片设计路线。

`risc-v` `ai-chip` `npu` `llm-inference` `agent`

---

### [GitHub - yetone/openai-translator: 基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用    -    Browser extension and cross-platform desktop application for translation based on ChatGPT API.](https://github.com/yetone/openai-translator) ⭐24,891
⭐⭐⭐3 🌐 · 2026-04-10

# GitHub - yetone/openai-translator: 基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用    -    Browser extension and cross-platform desktop application for translation based on ChatGPT API. 基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用    -    Browser extension and cross-platform desktop application for translation based on ...

`[]` `openai` `chatgpt`

---

### [GitHub - HW-whistleblower/True-Story-of-Pangu: 诺亚盘古大模型研发背后的真正的心酸与黑暗的故事。](https://github.com/HW-whistleblower/True-Story-of-Pangu) ⭐11,419
⭐⭐⭐3 🇨🇳 · 2026-04-10

# GitHub - HW-whistleblower/True-Story-of-Pangu: 诺亚盘古大模型研发背后的真正的心酸与黑暗的故事。 诺亚盘古大模型研发背后的真正的心酸与黑暗的故事。. Contribute to HW-whistleblower/True-Story-of-Pangu development by creating an account on GitHub. 盘古之殇：华为诺亚盘古大模型研发历程的心酸与黑暗 我是一名盘古大模型团队，华为诺亚方舟实验室的员工。 1. 现诺亚主任，前算法应用部部长，后改名为小模型实验室的主任王云鹤。前诺亚主任：姚骏（大家称姚老师）。...

`embedding` `[]` `大模型`

---

### [GitHub - steipete/CodexBar: Show usage stats for OpenAI Codex and Claude Code, without having to login.](https://github.com/steipete/CodexBar) ⭐10,549
⭐⭐⭐3 🌐 · 2026-04-10

# GitHub - steipete/CodexBar: Show usage stats for OpenAI Codex and Claude Code, without having to login. Show usage stats for OpenAI Codex and Claude Code, without having to login. - steipete/CodexBar CodexBar 🎚️ - May your tokens never run out. Tiny macOS 14+ menu bar app that keeps your Codex, Cl...

`mcp` `copilot` `[]` `cursor` `openai`

---

### [GitHub - rockbenben/ChatGPT-Shortcut: 让生产力加倍的 ChatGPT 快捷指令，按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复制。](https://github.com/rockbenben/ChatGPT-Shortcut) ⭐8,348
⭐⭐⭐3 🇨🇳 · 2026-04-10

# GitHub - rockbenben/ChatGPT-Shortcut: 让生产力加倍的 ChatGPT 快捷指令，按照领域和功能分区，可对提示词进行标签筛选、关键词搜索和一键复制。 ChatGPT Shortcut 是根据领域和功能划分的 ChatGPT 快捷指令表，可通过标签筛选、关键词搜索和一键复制来使用提示词，旨在简化你的工作流程并提高生产力。即使是初学者，你只需复制提示词，稍加修改后发送给 ChatGPT，就能获得指定输出，让你的生产力加倍！ 提示词（即 Prompt）通常是用户提供的问题或文本，以激活模型生成回复。简单来说，prompt 就是用户想要询问的内容，作为输入送到 ...

`[]` `openai` `prompt` `chatgpt`

---

### [GitHub - knemik97/Manifesto-against-the-Plagiarist-Yunhe-Wang: 讨贼王云鹤檄文](https://github.com/knemik97/Manifesto-against-the-Plagiarist-Yunhe-Wang?s=09) ⭐1,103
⭐⭐⭐3 🇨🇳 · 2026-04-10

# GitHub - knemik97/Manifesto-against-the-Plagiarist-Yunhe-Wang: 讨贼王云鹤檄文 讨贼王云鹤檄文. Contribute to knemik97/Manifesto-against-the-Plagiarist-Yunhe-Wang development by creating an account on GitHub. 文章license和Qwen一样，apache-2.0。 王云鹤，1991年生于黑龙江。2018年博士毕业进入华为，经历不到7年时间，于2025年2月中旬，从小模型实验室主任任上，正式顶替姚骏，被任命为诺亚方舟...

`deepseek` `[]` `大模型`

---

### [Google Gemma-4-31B 模型被彻底破解](/entry/zokld58k) 📄
@Lonely__MH · ⭐⭐⭐3 🇨🇳 · 2026-04-10

Google 最新 Gemma-4-31B 基础模型出现越狱版本 Gemma-4-31B-JANG_4M-CRACK，HarmBench 得分 93.7%（149/159）。采用 18GB 混合精度 MLX 量化，支持 Apple Silicon，原生支持视觉多模态。已在 Hugging Face 开放下载。

`gemma` `jailbreak` `open-source` `harmbench` `safety`

---
