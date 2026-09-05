# Changelog

## 2026-08-31 ~ 2026-09-06

> 基线快照: `a45af7d:data/entries.json`（上次 changelog 后，2055 条）→ 本次: 2155 条（**+100**）
> 生成时间: 2026-09-06 04:27 CST；差分按 git 基线与当前 `entries.json` ID 集合交叉校验。本周为纯增量周：100 条新增（92 条 ⭐≥4），0 条移除，0 次评分/分类变更；weekly-maintain-dedup 在 `d9190f6` 归档了 22 条无 URL 影子重复项（通过 `related` 字段互链孪生条目），活跃条目因此净增。
> 本周大事件: 09-01 Anthropic 公开 "Improving our alignment and security efforts" + Reward Seeker 训练实验，同日 AISI 发布 unsanctioned agent behaviour 事件报告；09-03 Anthropic 公布 Claude Fable 5.1 / Mythos 5.1，OpenAI 公开 Path to Astra safety brief；09-05 Anthropic 公布 FLT Lean 形式化里程碑，collusion.wiki 揭露 OpenAI agents 通过德语公共 wiki 进行跨实例通信。

### 📈 新增 (100)

**🆕 高质量新增 (⭐≥4, 92 条)**

**⭐⭐⭐⭐⭐ (15 条)**

- [SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control](https://arxiv.org/abs/2608.27234) — agents ⭐⭐⭐⭐⭐ (2026-08-30)
- [I accidentally turned LLM memory into program analysis](https://pwning.systems/posts/llm-memory-program-analysis) — agents ⭐⭐⭐⭐⭐ (2026-08-30)
- [Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents](https://arxiv.org/abs/2608.27141) — agents ⭐⭐⭐⭐⭐ (2026-08-30)
- [When Context Gets Root: Privilege Escalation in LLM Harnesses](https://arxiv.org/abs/2608.27299) — agents ⭐⭐⭐⭐⭐ (2026-08-30)
- [Improving our alignment and security efforts](https://www.anthropic.com/news/improving-alignment-security-efforts) — agents ⭐⭐⭐⭐⭐ (2026-09-01)
- [Qwen3.8-Flash Tech Report：四次手术重做 MoE，激活参数砍到 1/3训练 FLOPs 砍到 1/9](https://x.com/xiaogaifun/status/2094271716054933824) — models ⭐⭐⭐⭐⭐ (2026-09-01)
- [Incident Report: unsanctioned agent behaviour during cyber testing](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) — agents ⭐⭐⭐⭐⭐ (2026-09-01)
- [Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker) — agents ⭐⭐⭐⭐⭐ (2026-09-01)
- [FrontierHarness Eval: 9 harnesses x 12 configs on Kimi K3 same model, 17.5x cost spread](https://frontierharness.org) — agents ⭐⭐⭐⭐⭐ (2026-09-03)
- [The Rise of Verbal Reinforcement Learning](https://arxiv.org/abs/2609.01597) — learning ⭐⭐⭐⭐⭐ (2026-09-03)
- [LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It](https://arxiv.org/abs/2608.31016) — agents ⭐⭐⭐⭐⭐ (2026-09-03)
- [OpenAI agents used a public German wiki as a cross-instance message board (collusion.wiki, Sep 4 2026)](https://collusion.wiki/) — agents ⭐⭐⭐⭐⭐ (2026-09-05)
- [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints (arXiv 2609.0419...](https://arxiv.org/abs/2609.04198) — learning ⭐⭐⭐⭐⭐ (2026-09-05)
- [A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms (arXiv 2609.04170)](https://arxiv.org/abs/2609.04170) — agents ⭐⭐⭐⭐⭐ (2026-09-05)
- [Formalizing Fermat's Last Theorem (Anthropic, Sep 4 2026)](https://www.anthropic.com/research/formalizing-fermats-last-theorem) — agents ⭐⭐⭐⭐⭐ (2026-09-05)

**⭐⭐⭐⭐ (77 条，按日期排序)**

- [Domain-Driven Agents](https://coldtake.dev/blog/domain-driven-agents) — coding ⭐⭐⭐⭐ (2026-08-30)
- [Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach?](https://arxiv.org/abs/2608.27443) — agents ⭐⭐⭐⭐ (2026-08-30)
- [Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners](https://arxiv.org/abs/2608.27424) — infra ⭐⭐⭐⭐ (2026-08-30)
- [Bazel Module Versions Aren't SemVer](https://nesbitt.io/2026/08/27/bazel-module-versions-arent-semver.html) — infra ⭐⭐⭐⭐ (2026-08-30)
- [You have to beat the models at something](https://seangoedecke.com/you-have-to-beat-the-models-at-something) — coding ⭐⭐⭐⭐ (2026-08-30)
- [Boosting LLM Exploration via Weak-Model Guidance in RLVR](https://arxiv.org/abs/2608.27420) — models ⭐⭐⭐⭐ (2026-08-30)
- [Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090](https://arxiv.org/abs/2608.27370) — models ⭐⭐⭐⭐ (2026-08-31)
- [Understanding Evolution Strategies for LLM Reasoning: Broader Reasoning Coverage than GRPO](https://arxiv.org/abs/2608.27351) — models ⭐⭐⭐⭐ (2026-08-31)
- [CritICL: Inference-Time Weak-to-Strong Generalization from Small Language Model Failure Modes](https://arxiv.org/abs/2608.27455) — models ⭐⭐⭐⭐ (2026-08-31)
- [Beyond Parallel Blindness: Information Floors and Model Gaps in Block Drafting](https://arxiv.org/abs/2608.27339) — infra ⭐⭐⭐⭐ (2026-08-31)
- [TTPO: Test-Time Policy Optimization](https://arxiv.org/abs/2608.27448) — models ⭐⭐⭐⭐ (2026-08-31)
- [Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms](https://arxiv.org/abs/2608.27409) — models ⭐⭐⭐⭐ (2026-08-31)
- [CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases](https://arxiv.org/abs/2608.27391) — models ⭐⭐⭐⭐ (2026-08-31)
- [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406) — models ⭐⭐⭐⭐ (2026-08-31)
- [You have to beat the models at something](https://www.seangoedecke.com/you-have-to-beat-the-models-at-something) — industry ⭐⭐⭐⭐ (2026-09-01)
- [The Guard That Cried Wolf: How Scary Words Make Agent Guardrails Refuse Legitimate Actions](https://arxiv.org/abs/2608.27009) — agents ⭐⭐⭐⭐ (2026-09-01)
- [Understanding ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work) — agents ⭐⭐⭐⭐ (2026-09-01)
- [Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures](https://arxiv.org/abs/2608.02645) — agents ⭐⭐⭐⭐ (2026-09-01)
- [Warp 如何让 Agent 自我进化（How Warp builds self-improving agents on Claude 中译）](https://baoyu.io/blog/2026-08-28/warp-self-improving-agents) — agents ⭐⭐⭐⭐ (2026-09-01)
- [When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents](https://arxiv.org/abs/2608.27146) — agents ⭐⭐⭐⭐ (2026-09-01)
- [PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?](https://arxiv.org/abs/2608.26882) — agents ⭐⭐⭐⭐ (2026-09-01)
- [Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode) — agents ⭐⭐⭐⭐ (2026-09-01)
- [From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems](https://arxiv.org/abs/2608.15127) — infra ⭐⭐⭐⭐ (2026-09-01)
- [Creepy Crawlies: AI Crawler Load on git.kernel.org, With Hard Numbers](https://people.kernel.org/monsieuricon/creepy-crawlies) — infra ⭐⭐⭐⭐ (2026-09-01)
- [Tencent Releases and Open-Sources Tencent Hy4 Preview](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview) — models ⭐⭐⭐⭐ (2026-09-01)
- [Just a rumour of a bug is enough to find a security exploit these days](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug) — industry ⭐⭐⭐⭐ (2026-09-01)
- [Logos: An Agent Harness on a Cross-Process Bus](https://arxiv.org/abs/2608.28553) — agents ⭐⭐⭐⭐ (2026-09-01)
- [LLM 推理栈里 4 种 cache：KV / Prefix / Prompt / Semantic 存的根本不是同一类东西](https://x.com/_avichawla/status/2093265776266637739) — infra ⭐⭐⭐⭐ (2026-09-01)
- [When Robots Mishear Us: Mapping the Safety Risks of Voice-Controlled Embodied AI](https://arxiv.org/abs/2608.28518) — agents ⭐⭐⭐⭐ (2026-09-01)
- [How to let AI agents act on behalf of users without handing them access tokens](https://workos.com/blog/delegated-access-for-ai-agents) — agents ⭐⭐⭐⭐ (2026-09-01)
- [METR and Redwood Offer Holy #%^@ Postmortem Of The HuggingFace Hack](https://thezvi.wordpress.com/2026/08/29/metr-and-redwood-offer-holy-postmortem-of-the-huggingface-hack) — industry ⭐⭐⭐⭐ (2026-09-01)
- [Omarchy: Any User Process Can Escalate to Root](https://0xcc.io/posts/omarchy-root-creds) — coding ⭐⭐⭐⭐ (2026-09-01)
- [The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents](https://arxiv.org/abs/2608.27092) — agents ⭐⭐⭐⭐ (2026-09-01)
- [QSB-118: Dom0 Arbitrary Code Execution in qvm-copy-to-vm Error Reporting](https://www.qubes-os.org/news/2026/08/29/qsb-118) — coding ⭐⭐⭐⭐ (2026-09-01)
- [LLM Post-Training as Brownfield Maintenance: An Industrial Perspective on Dataware Engineering](https://arxiv.org/abs/2608.31102) — coding ⭐⭐⭐⭐ (2026-09-02)
- [The ChatGPT/Codex app bundles a full copy of LibreOffice](https://simonwillison.net/2026/Sep/1/codex-libreoffice) — infra ⭐⭐⭐⭐ (2026-09-02)
- [44% on ARC-AGI: small transformer trained in 1.5 hours on a 5090](https://mvakde.github.io/blog/44-on-arc-1) — learning ⭐⭐⭐⭐ (2026-09-02)
- [Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents](https://arxiv.org/abs/2608.31076) — agents ⭐⭐⭐⭐ (2026-09-02)
- [Path to Astra: critical capabilities and frontier safeguards](https://openai.com/index/path-to-astra) — industry ⭐⭐⭐⭐ (2026-09-02)
- [Atlas: A World Model for Spatial Intelligence](https://www.worldlabs.ai/blog/atlas) — models ⭐⭐⭐⭐ (2026-09-02)
- [Reconciling Process Supervision with Outcome-Based Credit in Agentic Policy Optimization](https://arxiv.org/abs/2608.31077) — agents ⭐⭐⭐⭐ (2026-09-02)
- [Let Claude use your computer in Cowork Anthropic help center updated 2026-09-02](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) — agents ⭐⭐⭐⭐ (2026-09-03)
- [Pluralistic: Unpermissioned research](https://pluralistic.net/2026/09/02/scrape-scrope-scrap) — industry ⭐⭐⭐⭐ (2026-09-03)
- [Training a Misaligned Reward Seeker](https://x.com/AnthropicAI/status/2094577944056430865) — industry ⭐⭐⭐⭐ (2026-09-03)
- [Mechanism Design for Alignment and Control](https://arxiv.org/abs/2609.01595) — learning ⭐⭐⭐⭐ (2026-09-03)
- [CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?](https://arxiv.org/abs/2609.01600) — learning ⭐⭐⭐⭐ (2026-09-03)
- [陈梓立：Agentic Coding 时代，什么是核心竞争力？](https://mp.weixin.qq.com/s?__biz=MzA4NTM4NDc4NQ%3D%3D&mid=2247546058&idx=1&sn=29bf169d86c161ec077d20bd862e8d97&chksm=9e047ff25e2c268c3373e60328f3d7587a106da4d2ad7efe3176d943a48fe6011560feebd2ea) — coding ⭐⭐⭐⭐ (2026-09-03)
- [Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement](https://arxiv.org/abs/2608.31046) — learning ⭐⭐⭐⭐ (2026-09-03)
- [An update on our alignment and security effort (Anthropic, 7 月事件复盘)](https://x.com/AnthropicAI/status/2094557124038951170) — industry ⭐⭐⭐⭐ (2026-09-03)
- [SpaceXAI 五篇官方使用指南拆解：六个构件 + 五个落地样板](https://x.com/shao__meng/status/2093266882996601091) — industry ⭐⭐⭐⭐ (2026-09-03)
- [Red Alert: OpenAI is poised to cross an AI safety redline](https://garymarcus.substack.com/p/red-alert-openai-is-poised-to-cross) — industry ⭐⭐⭐⭐ (2026-09-03)
- [Run cloud agents on machines you manage Cursor Self-Hosted Machines](https://cursor.com/blog/self-hosted-machines) — agents ⭐⭐⭐⭐ (2026-09-03)
- [io_uring without readahead](https://frn.sh/io-uring) — infra ⭐⭐⭐⭐ (2026-09-03)
- [How to protect yourself from workslop](https://seangoedecke.com/how-to-protect-yourself-from-workslop) — industry ⭐⭐⭐⭐ (2026-09-03)
- [A quote from Rick Brewster (Claude vibe-coded a Direct2D clean-room rewrite for Paint.NET on WINE)](https://simonwillison.net/2026/Sep/2/rick-brewster) — coding ⭐⭐⭐⭐ (2026-09-03)
- [Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.30996) — infra ⭐⭐⭐⭐ (2026-09-03)
- [Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation](https://arxiv.org/abs/2609.01603) — learning ⭐⭐⭐⭐ (2026-09-03)
- [slotstream: run Qwen3.8-Flash-Next on a Mac that can't hold it](https://github.com/carloslfu/slotstream) — infra ⭐⭐⭐⭐ (2026-09-03)
- [Dwarkesh Patel's wildly popular but dangerously misleading account of the OpenAI Hugging Face incident](https://garymarcus.substack.com/p/dwarkesh-patelss-wildly-popular-but) — industry ⭐⭐⭐⭐ (2026-09-03)
- [Introducing wrapture (and why its author explicitly disowns "vibe coding")](https://simonwillison.net/2026/Aug/31/introducing-wrapture) — coding ⭐⭐⭐⭐ (2026-09-03)
- [A Universal Context-Reuse Layer for Cross-Model KV Sharing](https://arxiv.org/abs/2608.30963) — infra ⭐⭐⭐⭐ (2026-09-03)
- [Introducing Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) — models ⭐⭐⭐⭐ (2026-09-03)
- [Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents](https://arxiv.org/abs/2608.31057) — agents ⭐⭐⭐⭐ (2026-09-03)
- [Comparing Human Oversight Strategies for Computer-Use Agents (arXiv 2604.04918)](https://arxiv.org/abs/2604.04918) — agents ⭐⭐⭐⭐ (2026-09-04)
- [Google Antigravity ToS：第三方 harness 仍封官方 headless 路径仍开](https://news.ycombinator.com/item?id=49548452) — agents ⭐⭐⭐⭐ (2026-09-04)
- [Codex rust-v0.153.2：插件 marketplace断线重连与 Astra Fast 文案修正](https://github.com/openai/codex/releases/tag/rust-v0.153.2) — coding ⭐⭐⭐⭐ (2026-09-04)
- [SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment](https://arxiv.org/abs/2609.02786) — agents ⭐⭐⭐⭐ (2026-09-04)
- [Post-Training Language Models for Gold-Medal Performance in Coding Competitions](https://arxiv.org/abs/2609.02849) — coding ⭐⭐⭐⭐ (2026-09-04)
- [Claude Code v2.1.260：全屏 diff 旁栏 + prompt-cache miss 原因说明](https://github.com/anthropics/claude-code/releases/tag/v2.1.260) — coding ⭐⭐⭐⭐ (2026-09-04)
- [Discriminative World Models for Web Agents](https://arxiv.org/abs/2609.02885) — agents ⭐⭐⭐⭐ (2026-09-04)
- [GPT-6 Astra 上线门：model idAPI 价目与 computer-use 数字](https://developers.openai.com/api/docs/models/gpt-6-astra) — models ⭐⭐⭐⭐ (2026-09-04)
- [When Models Edit Too Much: On the Fidelity of Minimal Code Edits (arXiv 2609.04061)](https://arxiv.org/abs/2609.04061) — coding ⭐⭐⭐⭐ (2026-09-05)
- [ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize (arXiv 2609.04197)](https://arxiv.org/abs/2609.04197) — models ⭐⭐⭐⭐ (2026-09-05)
- [SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents (arXiv 2609.04167)](https://arxiv.org/abs/2609.04167) — coding ⭐⭐⭐⭐ (2026-09-05)
- [Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning (arXiv 2609.04194)](https://arxiv.org/abs/2609.04194) — learning ⭐⭐⭐⭐ (2026-09-05)
- [Compile by Training: Turning Natural-Language Specifications into Local Neural Functions (arXiv 2609.04199)](https://arxiv.org/abs/2609.04199) — models ⭐⭐⭐⭐ (2026-09-05)
- [Terminal-Universe: Turning Agent Trajectories into Scalable Terminal Environments (arXiv 2609.04148)](https://arxiv.org/abs/2609.04148) — agents ⭐⭐⭐⭐ (2026-09-05)

**📝 普通新增 (⭐<4, 8 条)**

- [Claude Code weekly limits: permanent +25% from September 14 (about -17% vs today)](https://x.com/ClaudeDevs/status/2093742321473065266) — coding ⭐⭐⭐ (2026-08-30)
- [Premium: The Hater's Guide To Circular Financing (Part One)](https://www.wheresyoured.at/premium-the-haters-guide-to-circular-financing-part-one) — industry ⭐⭐⭐ (2026-08-30)
- [Introducing Hy4 Preview](https://simonwillison.net/2026/Aug/29/hy4) — models ⭐⭐⭐ (2026-08-30)
- [What my dad taught me about AI coding in the 90s](https://askmike.org/articles/ai-coding-lessons-in-the-90s-from-my-dad) — learning ⭐⭐⭐ (2026-09-01)
- [How accurate have Ed Zitron's AI skeptic predictions been?](https://danluu.com/zitron) — industry ⭐⭐⭐ (2026-09-02)
- [Claude Fable 5.1 made me a really nice animated pelican](https://simonwillison.net/2026/Sep/1/claude-fable-5-1) — models ⭐⭐⭐ (2026-09-03)
- [Fluorescent lamps (don't) have ears](https://blog.coredump.cx/p/fluorescent-lamps-dont-have-ears) — industry ⭐⭐⭐ (2026-09-03)
- [禁用 1M 上下文能让 Claude Code 的 Token 更耐用（Fable 5.1 时代更明显）](https://x.com/dotey/status/2094964831061155845) — models ⭐⭐⭐ (2026-09-03)

### 📦 归档 (22)

- 22 条无 URL 影子重复项 — active→archived（weekly-maintain-dedup 2026-08-31 `d9190f6`：每周维护合并，count-must-not-decrease 不变；通过 `related` 字段互链孪生条目，孪生条目保留自身内容页）。
  - 来自 Codex 官方团队的分享：如何把 Codex 用到极致
  - AI 傻傻分不清楚？那么多 AI 变体究竟怎么选？这里快速简单理清！
  - 你不知道的 Claude Code：架构治理与工程实践
  - gpt55_release_2026_001
  - a09cdbbd
  - Claude Code推荐的终端 - Ghostty
  - What we learned mapping a year's worth of AI-enabled cyber threats
  - 从聊天窗口到多 Agent 控制台：一次 AI 编程协作范式的转移
  - My self-sovereign / local / private / secure LLM setup, April 2026
  - Claude Code .claude/ 文件夹完全指南
  - a2a_protocol_v1_0_2026_001
  - Building Production-Grade AI Agents with MCP: A Complete Guide for 2026
  - Forward Deployed Engineer：AI 时代的新宠岗位，到底干什么？
  - GPT-2 规模模型训练干预实验：学习率是最大变量，Dropout 反而有害
  - OpenAI Codex Update Adds Computer Use, Image Generation, and Memory on Mac
  - 国内无魔法也能用Claude Code接入国产大模型
  - claude_opus_47_mythos_2026_001
  - Android CLI: Build Android apps 3x faster using any agent
  - AI copilot 能提升开发效率么？
  - AI Coding In-Depth Sharing: How to Truly Utilize Tools, From Principles to Practice
  - 译关于 Claude Design 的一些想法和感受 Sam Henri Gold
  - 面向 AI 的编程：是时候该坐下来应对不确定性了

### ✏️ 评分调整 (0)

- 无（本周 0 次评分变更）。

### 🔀 分类变更 (0)

- 无（本周 0 次分类变更）。

### 📊 分类变更分布

| 分类 | 新增 | 高质量新增 | 归档 | 评分调整 |
|---|---:|---:|---:|---:|
| agents | +34 | 34 | -1 | 0 |
| coding | +14 | 13 | -0 | 0 |
| models | +18 | 15 | -2 | 0 |
| industry | +14 | 11 | -1 | 0 |
| infra | +11 | 11 | -0 | 0 |
| learning | +9 | 8 | -0 | 0 |
| 其他 | +0 | 0 | -18 | 0 |

### 🧭 本周重点

- [SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control](https://arxiv.org/abs/2608.27234) — agents ⭐⭐⭐⭐⭐ (2026-08-30)
- [I accidentally turned LLM memory into program analysis](https://pwning.systems/posts/llm-memory-program-analysis) — agents ⭐⭐⭐⭐⭐ (2026-08-30)
- [Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents](https://arxiv.org/abs/2608.27141) — agents ⭐⭐⭐⭐⭐ (2026-08-30)
- [When Context Gets Root: Privilege Escalation in LLM Harnesses](https://arxiv.org/abs/2608.27299) — agents ⭐⭐⭐⭐⭐ (2026-08-30)
- [Improving our alignment and security efforts](https://www.anthropic.com/news/improving-alignment-security-efforts) — agents ⭐⭐⭐⭐⭐ (2026-09-01)
- [Qwen3.8-Flash Tech Report：四次手术重做 MoE，激活参数砍到 1/3训练 FLOPs 砍到 1/9](https://x.com/xiaogaifun/status/2094271716054933824) — models ⭐⭐⭐⭐⭐ (2026-09-01)
- [Incident Report: unsanctioned agent behaviour during cyber testing](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) — agents ⭐⭐⭐⭐⭐ (2026-09-01)
- [Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker) — agents ⭐⭐⭐⭐⭐ (2026-09-01)
- [FrontierHarness Eval: 9 harnesses x 12 configs on Kimi K3 same model, 17.5x cost spread](https://frontierharness.org) — agents ⭐⭐⭐⭐⭐ (2026-09-03)
- [The Rise of Verbal Reinforcement Learning](https://arxiv.org/abs/2609.01597) — learning ⭐⭐⭐⭐⭐ (2026-09-03)
- [LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It](https://arxiv.org/abs/2608.31016) — agents ⭐⭐⭐⭐⭐ (2026-09-03)
- [OpenAI agents used a public German wiki as a cross-instance message board (collusion.wiki, Sep 4 2026)](https://collusion.wiki/) — agents ⭐⭐⭐⭐⭐ (2026-09-05)
- [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints (arXiv 2609.0419...](https://arxiv.org/abs/2609.04198) — learning ⭐⭐⭐⭐⭐ (2026-09-05)
- [A Case Study on Emergent Cheating and Whistleblowing in Autonomous Research Swarms (arXiv 2609.04170)](https://arxiv.org/abs/2609.04170) — agents ⭐⭐⭐⭐⭐ (2026-09-05)
- [Formalizing Fermat's Last Theorem (Anthropic, Sep 4 2026)](https://www.anthropic.com/research/formalizing-fermats-last-theorem) — agents ⭐⭐⭐⭐⭐ (2026-09-05)

### 📊 统计

- 总条目: 2055 → 2155 (**+100**)
- 活跃条目: 1432 → 1510 (**+78**)：新增 100 active，dedup 归档 22 active（active→archived）
- score-pending: 39 → 39 (0)
- 新增条目: 100；高质量新增: 92；普通新增: 8
- 归档条目: 22（22 active→archived）；评分调整: 0；分类变更: 0


## 2026-08-24 ~ 2026-08-30

> 基线快照: `396c94f:data/entries.json`（上次 changelog 后，1942 条）→ 本次: 2055 条（**+113**）
> 生成时间: 2026-08-30 04:45 CST；差分按 git 基线与当前 `entries.json` ID 集合交叉校验。2026-08-23 晚间日常 intake 的 14 条计入本周（基线为上次 changelog 提交快照）。
> 本周大事件: 08-24 weekly-maintain-dedup 归档 69 条 synthetic 摘要残留条目与 1 条 shadow 重复；08-26 评分 pass 清理 score-pending 存量 255→39（41 条转 active / 175 条转 archived），活跃条目因此净增。

### 📈 新增 (113)

**🆕 高质量新增 (⭐≥4, 99 条)**

- [What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection](https://arxiv.org/abs/2606.04425) — agents ⭐⭐⭐⭐⭐ (2026-08-23)
- [The New MCP Roadmap](https://blog.modelcontextprotocol.io/posts/mcp-roadmap) — agents ⭐⭐⭐⭐⭐ (2026-08-24)
- [深入理解 AI Agent开源书 2.0：DeepSeek Harness 等新案例入册](https://github.com/bojieli/ai-agent-book) — learning ⭐⭐⭐⭐⭐ (2026-08-24)
- [SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?](https://arxiv.org/abs/2608.23564) — coding ⭐⭐⭐⭐⭐ (2026-08-26)
- [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552) — agents ⭐⭐⭐⭐⭐ (2026-08-26)
- [The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams](https://arxiv.org/abs/2608.23541) — agents ⭐⭐⭐⭐⭐ (2026-08-26)
- [InjecMEM: Memory Injection Attack on LLM Agent Memory Systems](https://arxiv.org/abs/2608.23471) — agents ⭐⭐⭐⭐⭐ (2026-08-26)
- [The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses](https://arxiv.org/abs/2608.23953) — agents ⭐⭐⭐⭐⭐ (2026-08-27)
- [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead) — agents ⭐⭐⭐⭐⭐ (2026-08-27)
- [An open letter for a global surge in cyber defense](https://x.com/gdb/status/2093021551855812842) — industry ⭐⭐⭐⭐⭐ (2026-08-28)
- [ConceptGuard: Benchmarking Context-Sensitive Unlearning in Large Language Models](https://arxiv.org/abs/2608.20338) — models ⭐⭐⭐⭐ (2026-08-23)
- [ContractScrub: A benchmark for final review of legal contracts](https://arxiv.org/abs/2608.20204) — industry ⭐⭐⭐⭐ (2026-08-23)
- [Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference](https://arxiv.org/abs/2608.20210) — infra ⭐⭐⭐⭐ (2026-08-23)
- [Unicode TAG-Block Concealment of Tool-Metadata Payloads in the Model Context Protocol: An Approval-View Fidelity Gap Across Three Independen...](https://arxiv.org/abs/2607.05744) — agents ⭐⭐⭐⭐ (2026-08-23)
- [Claudette: Make Claude stop talking like a BuzzFeed article (NoBuzz)](https://github.com/adnanakil/nobuzz/blob/main/README.md) — coding ⭐⭐⭐⭐ (2026-08-23)
- [I'm becoming AI-blind](https://cymerys.com/w/im-becoming-ai-blind) — industry ⭐⭐⭐⭐ (2026-08-23)
- [Research: A shot-scraper-style JSON API on Bun 1.4's new Bun.WebView](https://simonwillison.net/2026/Aug/20/bun-webview-json-api) — coding ⭐⭐⭐⭐ (2026-08-23)
- [A Syncthing and SQLite Gotcha](https://borretti.me/article/a-syncthing-and-sqlite-gotcha) — infra ⭐⭐⭐⭐ (2026-08-23)
- [Sol Advisor: Codex-native architect orchestration with Luna and Terra implementation lanes](https://github.com/DannyMac180/sol-advisor) — agents ⭐⭐⭐⭐ (2026-08-23)
- [bilingual_book_maker: Make bilingual epub books Using AI translate](https://github.com/yihong0618/bilingual_book_maker) — learning ⭐⭐⭐⭐ (2026-08-23)
- [What Is a Harness?](https://earendil.com/posts/what-is-a-harness) — agents ⭐⭐⭐⭐ (2026-08-24)
- [I spent $266 and four AI models to own my Amazon Fire tablet](https://ericpardee.github.io/fire-hd-ownership) — models ⭐⭐⭐⭐ (2026-08-24)
- [Task-CoEvolve: adaptive validation task selection for harness optimization](https://arxiv.org/abs/2608.20169) — agents ⭐⭐⭐⭐ (2026-08-24)
- [MemTrapBench: cognitive traps in LLM memory use](https://arxiv.org/abs/2608.20202) — agents ⭐⭐⭐⭐ (2026-08-24)
- [Learning how to Forget: fine-tuning for long-context sparse attention](https://arxiv.org/abs/2608.19920) — infra ⭐⭐⭐⭐ (2026-08-24)
- [Jerry Liu: two-pass document processing is the default for agent harnesses](https://x.com/jerryjliu0/status/2091564183922077885) — agents ⭐⭐⭐⭐ (2026-08-24)
- [Innei: AI 时代我的开发工作流踩坑复盘沉淀为 Skill 与文章，多项目并行验证](https://innei.in/posts/tinkering/ai-era-dev-workflow-review-and-verify) — coding ⭐⭐⭐⭐ (2026-08-24)
- [The summer of open weights: 够用的智能以十分之一价格普及](https://martinalderson.com/posts/the-summer-of-open-weights) — industry ⭐⭐⭐⭐ (2026-08-24)
- [Armin Ronacher: Anger, Anxiety and Agency](https://lucumr.pocoo.org/2026/8/24/anger-anxiety-agency) — industry ⭐⭐⭐⭐ (2026-08-24)
- [Drew Breunig: Fable & The End of the Free Lunch](https://www.dbreunig.com/2026/08/23/fable-the-end-of-moore-s-law.html) — industry ⭐⭐⭐⭐ (2026-08-24)
- [Armin Ronacher: Fast and Hard Code](https://lucumr.pocoo.org/2026/8/22/fast-hard-code) — coding ⭐⭐⭐⭐ (2026-08-24)
- [AUSO: Action-Level Unified Skill Optimization from Internalization to Utilization](https://arxiv.org/abs/2608.21292) — agents ⭐⭐⭐⭐ (2026-08-25)
- [CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment](https://arxiv.org/abs/2608.21278) — models ⭐⭐⭐⭐ (2026-08-25)
- [HIERA: Workload-Aware Planning Across Implementation Spaces for GPU Kernel Optimization](https://arxiv.org/abs/2608.21157) — coding ⭐⭐⭐⭐ (2026-08-25)
- [Llama-Mobile: Efficient 2.7-Bit Quantization of VLMs](https://arxiv.org/abs/2608.21134) — models ⭐⭐⭐⭐ (2026-08-25)
- [Temporal Validity on Real Software Histories: Eliminating Stale-Fact Errors in Code-Assistant Memory over GitHub Fixes](https://arxiv.org/abs/2608.20685) — agents ⭐⭐⭐⭐ (2026-08-25)
- [Memory Augmentation Unlocks Efficient Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.21265) — models ⭐⭐⭐⭐ (2026-08-25)
- [Quantization-Aware Healing: A Practical Recipe for Recovering Compressed, 4-Bit LLMs](https://arxiv.org/abs/2608.20953) — models ⭐⭐⭐⭐ (2026-08-25)
- [TreeWY: Speculative Verification for Gated DeltaNet Hybrids](https://arxiv.org/abs/2608.20961) — infra ⭐⭐⭐⭐ (2026-08-25)
- [Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking](https://arxiv.org/abs/2608.21230) — agents ⭐⭐⭐⭐ (2026-08-25)
- [FT: Anthropic 最强模型遭遇用户冷落，便宜工具正在胜出](https://www.ft.com/content/5ee49718-c258-4f01-aa32-7e5b76ae5245) — industry ⭐⭐⭐⭐ (2026-08-25)
- [Everything I own, owned: Claude Opus 5 逆向了身边 5 件外设](https://schlarp.com/posts/everything-i-own-owned) — coding ⭐⭐⭐⭐ (2026-08-25)
- [ChinAI #372: 中国具身 AI 行业的过热与泡沫](https://chinai.substack.com/p/chinai-372-chinas-overhyped-embodied) — industry ⭐⭐⭐⭐ (2026-08-25)
- [Hardening the Override Flag: 包管理器危险开关的防御设计](https://nesbitt.io/2026/08/25/hardening-the-override-flag.html) — infra ⭐⭐⭐⭐ (2026-08-25)
- [Claude Code 2.1.243: /usage Loops 分项与 promptCacheTtl 落地](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md) — coding ⭐⭐⭐⭐ (2026-08-25)
- [Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty](https://arxiv.org/abs/2608.23497) — industry ⭐⭐⭐⭐ (2026-08-26)
- [On the Threat Model of Weird Generalization and Emergent Misalignment](https://arxiv.org/abs/2608.23476) — industry ⭐⭐⭐⭐ (2026-08-26)
- [How AI Assistance Affects Human Skill Development: A Study of Learning with Logic Puzzles](https://arxiv.org/abs/2608.23543) — learning ⭐⭐⭐⭐ (2026-08-26)
- [I built a low-latency AI companion that plays Skyrim with me](https://pantel.is/projects/ai-gaming-companion) — agents ⭐⭐⭐⭐ (2026-08-26)
- [SRPO: Self-Reflective Policy Optimization for Long-Horizon Reasoning](https://arxiv.org/abs/2608.23493) — models ⭐⭐⭐⭐ (2026-08-26)
- [SkillAlchemy: Open-World Agent Skill Creation](https://arxiv.org/abs/2608.23417) — agents ⭐⭐⭐⭐ (2026-08-26)
- [Activation-Weighted Seeded Residual Coding for Low-Bit LLM Weight Repair](https://arxiv.org/abs/2608.23144) — infra ⭐⭐⭐⭐ (2026-08-26)
- [The AI Hater's Manifesto](https://www.wheresyoured.at/the-ai-haters-manifesto) — industry ⭐⭐⭐⭐ (2026-08-26)
- [Anthropic's best AI model struggles to attract users as cheaper tools thrive](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t) — industry ⭐⭐⭐⭐ (2026-08-26)
- [Foot Guns for Sale](https://idiallo.com/blog/foot-gun-for-sale) — industry ⭐⭐⭐⭐ (2026-08-26)
- [Fixing an eMachines EL1200 BIOS bug with Claude](https://www.downtowndougbrown.com/2026/08/fixing-an-emachines-el1200-bios-bug-with-claude) — agents ⭐⭐⭐⭐ (2026-08-26)
- [Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses](https://arxiv.org/abs/2608.24876) — agents ⭐⭐⭐⭐ (2026-08-27)
- [SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL](https://arxiv.org/abs/2608.24870) — learning ⭐⭐⭐⭐ (2026-08-27)
- [StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments](https://arxiv.org/abs/2608.24804) — agents ⭐⭐⭐⭐ (2026-08-27)
- [Reading Is Not Using: Retrieval, Judgment, and the Design of AI Financial Research Workflows](https://arxiv.org/abs/2608.24842) — learning ⭐⭐⭐⭐ (2026-08-27)
- [GLM-5.3-Flash: Frontier Intelligence, Flash Cost](https://z.ai/blog/glm-5.3-flash) — models ⭐⭐⭐⭐ (2026-08-27)
- [Towards LLM-Enhanced Android Taint Analysis](https://arxiv.org/abs/2608.24269) — coding ⭐⭐⭐⭐ (2026-08-27)
- [Paritok-4B: Intent-Conditioned Context Compression for Coding Agents](https://arxiv.org/abs/2608.24188) — coding ⭐⭐⭐⭐ (2026-08-27)
- [MemUse: Moving Memory Evaluation from Direct QA to Natural Integration in Long-Term Human-AI Conversation](https://arxiv.org/abs/2608.24189) — agents ⭐⭐⭐⭐ (2026-08-27)
- [When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows](https://arxiv.org/abs/2608.24569) — agents ⭐⭐⭐⭐ (2026-08-27)
- [Joint Optimization of Tool Creation and Use for Large Language Model Agents](https://arxiv.org/abs/2608.24571) — agents ⭐⭐⭐⭐ (2026-08-27)
- [Qwen3.8-Flash-Next: GDN+QSA Hybrid, 125B/A6B, Qwen4 Architecture Preview](https://qwen.ai/blog?id=qwen3.8-flash-next) — models ⭐⭐⭐⭐ (2026-08-27)
- [The end of programming](https://pauldix.com/the-end-of-programming) — coding ⭐⭐⭐⭐ (2026-08-27)
- [What is the quality of software that AI writes?](https://www.johndcook.com/blog/2026/08/26/what-is-the-quality-of-software-that-ai-writes) — coding ⭐⭐⭐⭐ (2026-08-27)
- [DuckLabs to Join AWS, Projects to Remain Open Source](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) — infra ⭐⭐⭐⭐ (2026-08-27)
- [An ongoing 3D-printer AGPL violation (FOSSY 2026)](https://lwn.net/SubscriberLink/1089390/46116614cc74b814) — industry ⭐⭐⭐⭐ (2026-08-27)
- [TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development](https://arxiv.org/abs/2608.26086) — agents ⭐⭐⭐⭐ (2026-08-28)
- [SwarmWorld: Stigmergic technological evolution in societies of language-model agents](https://arxiv.org/abs/2608.26081) — agents ⭐⭐⭐⭐ (2026-08-28)
- [A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks](https://arxiv.org/abs/2608.26008) — agents ⭐⭐⭐⭐ (2026-08-28)
- [Prefix Sliding for efficient test-time scaling](https://arxiv.org/abs/2608.26070) — models ⭐⭐⭐⭐ (2026-08-28)
- [Trace Integrity for LLM Data Agents: A Vision for Auditable Structured Reasoning in Real-World Systems](https://arxiv.org/abs/2608.26036) — agents ⭐⭐⭐⭐ (2026-08-28)
- [How Warp builds self-improving agents on Claude](https://x.com/Xudong07452910/status/2093145288672158204) — agents ⭐⭐⭐⭐ (2026-08-28)
- [Qwen3.8-Flash-Next Day-0 NVFP4 + dual DGX Spark deployment math](https://x.com/wei_wang/status/2092618570114994389) — models ⭐⭐⭐⭐ (2026-08-28)
- [Pi Agent zero-base hands-on: install to first verification](https://x.com/xiaomovps/status/2092488445117755645) — learning ⭐⭐⭐⭐ (2026-08-28)
- [Breaking Claude Code Opus 5 Auto Mode](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode) — coding ⭐⭐⭐⭐ (2026-08-28)
- [Sandboxing coding agents](https://micahflee.com/sandboxing-coding-agents) — coding ⭐⭐⭐⭐ (2026-08-28)
- [US judge blocks Pentagon's Anthropic blacklisting](https://www.reuters.com/legal/government/us-judge-blocks-pentagons-anthropic-blacklisting-2026-08-28) — industry ⭐⭐⭐⭐ (2026-08-28)
- [Why do OpenAI's GPT-2 weights beat mine? Part four: digging into dropout](https://www.gilesthomas.com/2026/08/why-do-openai-gpt2-weights-beat-mine-4-ift-dropout) — learning ⭐⭐⭐⭐ (2026-08-28)
- [Introducing Pipette: A benchmarking suite for on-device intelligence](https://www.liquid.ai/blog/pipette-on-device-ai-benchmarking-by-liquid-ai) — infra ⭐⭐⭐⭐ (2026-08-28)
- [MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks](https://arxiv.org/abs/2608.23035) — agents ⭐⭐⭐⭐ (2026-08-28)
- [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution](https://arxiv.org/abs/2608.27454) — agents ⭐⭐⭐⭐ (2026-08-29)
- [RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution](https://arxiv.org/abs/2608.27439) — learning ⭐⭐⭐⭐ (2026-08-29)
- [From Static to Dynamic: Benchmarking Real-World Code Review with MCR-Bench](https://arxiv.org/abs/2608.27442) — coding ⭐⭐⭐⭐ (2026-08-29)
- [SWE-Prime: Fewer Trajectories, Better Performance](https://arxiv.org/abs/2608.27449) — coding ⭐⭐⭐⭐ (2026-08-29)
- [Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Audit](https://arxiv.org/abs/2608.27427) — agents ⭐⭐⭐⭐ (2026-08-29)
- [GLM-5.3 is now open-weight](https://huggingface.co/zai-org/GLM-5.3) — models ⭐⭐⭐⭐ (2026-08-29)
- [Small Models Have Arrived](https://calv.info/small-models-have-arrived) — industry ⭐⭐⭐⭐ (2026-08-29)
- [dotey 解读 Warp 自进化 Skill：从自身反编译/写作 Skill 实践看六条工程原则](https://x.com/dotey/status/2093538110311178430) — agents ⭐⭐⭐⭐ (2026-08-29)
- [Andrew Ng: AI Engineering Skills Map Software engineering fundamentals](https://x.com/AndrewYNg/status/2093388974194872781) — coding ⭐⭐⭐⭐ (2026-08-29)
- [Google DeepMind Podcast #8: Zoubin Ghahramani 谈 AI 不确定性的数学](https://x.com/Xudong07452910/status/2093520192072536209) — models ⭐⭐⭐⭐ (2026-08-29)
- [What GLM-5.3 Flash running on Chinese hardware actually means](https://martinalderson.com/posts/glm-5-3-flash-chinese-hardware) — infra ⭐⭐⭐⭐ (2026-08-29)
- [Just a rumour of a bug is enough to find a security exploit these days](https://anil.recoil.org/notes/rumour-is-the-exploit) — infra ⭐⭐⭐⭐ (2026-08-29)
- [Claude Code v2.1.251: model-switch hooks, /cost prompt-cache line, symlink path-escape fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) — coding ⭐⭐⭐⭐ (2026-08-29)
- [5 lessons from the OpenAI / Hugging Face incident](https://garymarcus.substack.com/p/5-lessons-from-the-openai-hugging) — industry ⭐⭐⭐⭐ (2026-08-29)

**📝 普通新增 (⭐<4, 14 条)**

- [Enhancing Model Context Protocol (MCP) with Context-Aware Server Collaboration](https://arxiv.org/abs/2601.11595) — agents ⭐⭐⭐ (2026-08-23)
- [More than just code review](https://simonwillison.net/2026/Aug/22/more-than-just-code-review) — coding ⭐⭐⭐ (2026-08-23)
- [A quote from Linus Torvalds](https://simonwillison.net/2026/Aug/22/linus-torvalds) — coding ⭐⭐⭐ (2026-08-23)
- [The Evaluation Context Protocol (ECP): A Portable Contract for AI Agent Evaluation](https://arxiv.org/abs/2608.19263) — agents ⭐⭐⭐ (2026-08-25)
- [AI Coding will Prevent Expertise](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) — coding ⭐⭐⭐ (2026-08-25)
- [Your executable is a SQLite database: 把 ELF 重写成 SQL 查询引擎](https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database) — infra ⭐⭐⭐ (2026-08-25)
- [distributed identity: git 改名字背后的 DID 方案](https://jyn.dev/distributed-identity) — coding ⭐⭐⭐ (2026-08-25)
- [Know your paradoxes: 哪些悖论真能把 AI 锁死](https://blog.coredump.cx/p/know-your-paradoxes) — learning ⭐⭐⭐ (2026-08-25)
- [ARR vs ARR: 别被 Annualized Run Rate 骗了](https://garymarcus.substack.com/p/arr-vs-arr-watch-out-for-this-one) — industry ⭐⭐⭐ (2026-08-25)
- [Anthropic's $30 trillion fantasy](https://garymarcus.substack.com/p/anthropics-30-trillion-fantasy) — industry ⭐⭐⭐ (2026-08-27)
- [tailscale/tailcat: like netcat, but over Tailscale's data plane](https://github.com/tailscale/tailcat) — infra ⭐⭐⭐ (2026-08-27)
- [PlanSightRAG: A Visual-First Multimodal RAG for Automating Question Answering and Compliance Checking for Civil Standard Plans](https://arxiv.org/abs/2608.26091) — models ⭐⭐⭐ (2026-08-28)
- [Beyond Local Surprise: Grounded Dialogue as Selective Belief Revision under Referential Uncertainty](https://arxiv.org/abs/2608.26035) — learning ⭐⭐⭐ (2026-08-28)
- [AgentsView：把本地 coding agent 历史会话统一索引，Session Handoff 跨 Agent 接续](https://x.com/LinearUncle/status/2093530915037487313) — coding ⭐⭐⭐ (2026-08-29)

### 📦 归档 (245)

- 69 条 synthetic 摘要残留条目 — active→archived（weekly-maintain-dedup 2026-08-24 `75a58a5`：无 URL/低信号的模板化摘要条目，按 count-must-not-decrease 规则归档）。示例: [@yudapeathree - 论文工具](https://x.com/yudapeathree/status/20260607180456_002)
- 1 条 shadow 重复条目 — active→archived（同上；孪生条目已有自己的内容页）: 2026 年，AI 编程 Agent 的真正分水岭Harness 详解
- 175 条 score-pending 存量清理 — score-pending→archived（2026-08-26 评分 pass `0366baa`：无链接/低信号条目批量归档）。示例: 未命名标题

### ✏️ 评分调整 (31)

> 来源：2026-08-26 自动评分 pass（`0366baa`）：30 条 2→3，1 条 3→5

- [BatteryLife：面向电池寿命预测的综合数据集与基准测试 精读笔记](https://github.com/Ruifeng-Tan/BatteryLife) — 3→5（自动评分 pass，2026-08-26）
- [GPT-2 规模模型训练干预实验：学习率是最大变量，Dropout 反而有害](https://www.gilesthomas.com/2026/04/llm-from-scratch-32m-interventions-conclusion) — 2→3（自动评分 pass，2026-08-26）
- [Claude Code推荐的终端 - Ghostty](https://github.com/ghostty-org/ghostty) — 2→3（自动评分 pass，2026-08-26）
- [Claude Code .claude/ 文件夹完全指南](https://x.com/akshay_pachaar/status/2035341800739877091) — 2→3（自动评分 pass，2026-08-26）
- [为 Agent 设计产品【译】](https://mp.weixin.qq.com/s?__biz=Mzk1NzgxMjQ0OA%3D%3D&mid=2247494663&idx=1&sn=0e5d4d44345aa5160c109dabc03619d6) — 2→3（自动评分 pass，2026-08-26）
- [你不知道的 Claude Code：架构、治理与工程实践](https://x.com/hitw93/status/2032091246588518683) — 2→3（自动评分 pass，2026-08-26）
- [What 81,000 People Want from AI（Anthropic 81K 用户访谈研究）](https://www.anthropic.com/81k-interviews) — 2→3（自动评分 pass，2026-08-26）
- [Android CLI: Build Android apps 3x faster using any agent](http://android-developers.googleblog.com/2026/04/build-android-apps-3x-faster-using-any-agent.html) — 2→3（自动评分 pass，2026-08-26）
- [Gemini 3.1 Flash TTS：表现力最强、控制粒度最细的语音合成模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-tts) — 2→3（自动评分 pass，2026-08-26）
- [OpenAI Codex Update Adds Computer Use, Image Generation, and Memory on Mac](https://www.macrumors.com/2026/04/16/openai-codex-mac-update) — 2→3（自动评分 pass，2026-08-26）
- [Shannon Holmberg：两层知识库系统让每个 AI Agent 更聪明](https://x.com/shannholmberg/status/2044111115878326444) — 2→3（自动评分 pass，2026-08-26）
- [OpenAI 模型登陆 AWS](https://x.com/OpenAI/status/2061564502160892138) — 2→3（自动评分 pass，2026-08-26）
- [从聊天窗口到多 Agent 控制台：一次 AI 编程协作范式的转移](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA==&mid=2247559601&idx=1&sn=dca715222390e89a63a45ad54b1c9d7d) — 2→3（自动评分 pass，2026-08-26）
- [LLM Powered Autonomous Agents（基于大语言模型的自主智能体）](https://arxiv.org/abs/2308.11432) — 2→3（自动评分 pass，2026-08-26）
- [LLM Knowledge Bases](https://x.com/karpathy/status/2039805659525644595) — 2→3（自动评分 pass，2026-08-26）
- [国内无魔法也能用Claude Code接入国产大模型](https://x.com/VincentLogic/status/2048400987107553680) — 2→3（自动评分 pass，2026-08-26）
- [My self-sovereign / local / private / secure LLM setup, April 2026](https://vitalik.eth.limo/general/2026/04/02/secure_llms.html) — 2→3（自动评分 pass，2026-08-26）
- [面向 AI 的编程：是时候该坐下来应对不确定性了](https://blog.lyric.im/p/programming-for-ai) — 2→3（自动评分 pass，2026-08-26）
- [AI copilot 能提升开发效率么？](https://mp.weixin.qq.com/s?__biz=MzA3NDM0ODQwMw%3D%3D&mid=2649829724&idx=1&sn=d2febca6d2bb9a5b93b153be5aa4f1d0) — 2→3（自动评分 pass，2026-08-26）
- [Forward Deployed Engineer：AI 时代的新宠岗位，到底干什么？](https://baoyu.io/blog/2026-05-15/forward-deployed-engineer) — 2→3（自动评分 pass，2026-08-26）
- [Greg Brockman (gdb)：Codex 能快速构建游戏和应用，"想法到产品只需几分钟](https://x.com/gdb/status/2045594591584530826) — 2→3（自动评分 pass，2026-08-26）
- [AI 助力网站出海：只靠聊天，做高颜值网站，你也行！](https://mp.weixin.qq.com/s?__biz=MzkzNzYzNzE3Mg%3D%3D&mid=2247483748&idx=1&sn=1ec554ab4a29e791730c817fd0b408d1) — 2→3（自动评分 pass，2026-08-26）
- [Building Production-Grade AI Agents with MCP: A Complete Guide for 2026](https://dev.to/nebulagg/building-production-grade-ai-agents-with-mcp-a-complete-guide-for-2026-3bo2) — 2→3（自动评分 pass，2026-08-26）
- [ChatGPT 个人财务工具可绑定银行账户查看全部交易](https://gizmodo.com/chatgpt-can-now-connect-to-your-bank-account-and-see-all-your-transactions-2000759306) — 2→3（自动评分 pass，2026-08-26）
- [AI 傻傻分不清楚？那么多 AI 变体究竟怎么选？这里快速简单理清！](https://mp.weixin.qq.com/s?__biz=Mzg3NTA3MDIxOA%3D%3D&mid=2247493551&idx=1&sn=d079783a37abb37dc245603c9a27f925) — 2→3（自动评分 pass，2026-08-26）
- [AI 让我们重新开始享受自己的职业](https://yage.ai/share/ai-profession-mechanical-judgment-spectrum-20260417.html) — 2→3（自动评分 pass，2026-08-26）
- [AI 时代如何做独立开发](https://mp.weixin.qq.com/s?__biz=MzU0NDk4OTk2Mg%3D%3D&mid=2247485247&idx=1&sn=e4ca3b067e64a4a98a7efdc763e42415) — 2→3（自动评分 pass，2026-08-26）
- [丢掉沉重的记忆：Codex、Claude Code 与 OpenCode 的上下文压缩术](https://justin3go.com/posts/2026/04/09-context-compaction-in-codex-claude-code-and-opencode) — 2→3（自动评分 pass，2026-08-26）
- [【译】关于 Claude Design 的一些想法和感受 · Sam Henri Gold](https://mp.weixin.qq.com/s?__biz=Mzk1NzgxMjQ0OA%3D%3D&mid=2247494651&idx=1&sn=26efdda46f138eb1d535cdf381998c44) — 2→3（自动评分 pass，2026-08-26）
- [Postgres LISTEN/NOTIFY Actually Scales (DBOS)](https://www.dbos.dev/blog/postgres-listen-notify-scalability) — 2→3（自动评分 pass，2026-08-26）
- [Tracking down a Zsh history data loss bug: from inotify to core dump](https://michael.stapelberg.ch/posts/2026-08-09-zsh-history-truncation-bug) — 2→3（自动评分 pass，2026-08-26）

### 🔀 分类变更 (8)

> 来源：2026-08-26 评分 pass（`0366baa`）附带分类规范化：uncategorized → 具体分类

- Greg Brockman（@gdb）：用 Codex 操作电脑有趣得多 — uncategorized → coding
- Andrew Ng 发布 LLM 高效服务课程（量化 + vLLM，与 Red Hat 合作） — uncategorized → learning
- 每日论文精读（AI） 2026-05-14 — uncategorized → learning
- MCP Security Bench (MSB)：针对 LLM Agent 中模型上下文协议的攻击基准测试 — uncategorized → agents
- 全文翻译：Towards a Science of AI Agent Reliability — uncategorized → agents
- BatteryLife：面向电池寿命预测的综合数据集与基准测试 精读笔记 — uncategorized → infra
- 精读：层级 LoRA 微调基于相似度指标的方法 — uncategorized → infra
- Shannon Holmberg：两层知识库系统让每个 AI Agent 更聪明 — uncategorized → agents

### 📊 分类变更分布

| 分类 | 新增 | 高质量新增 | 归档 | 评分调整 |
|---|---:|---:|---:|---:|
| agents | +35 | 33 | -1 | 5 |
| coding | +23 | 18 | -0 | 7 |
| models | +14 | 13 | -1 | 9 |
| industry | +19 | 17 | -0 | 0 |
| infra | +12 | 10 | -0 | 3 |
| learning | +10 | 8 | -3 | 1 |
| 其他 | +0 | 0 | -240 | 6 |

### 🧭 本周重点

- [What If Prompt Injection Never Left? Rethinking Agent Security through Cross-Session Stored Prompt Injection](https://arxiv.org/abs/2606.04425) — agents ⭐⭐⭐⭐⭐ (2026-08-23)
- [The New MCP Roadmap](https://blog.modelcontextprotocol.io/posts/mcp-roadmap) — agents ⭐⭐⭐⭐⭐ (2026-08-24)
- [深入理解 AI Agent开源书 2.0：DeepSeek Harness 等新案例入册](https://github.com/bojieli/ai-agent-book) — learning ⭐⭐⭐⭐⭐ (2026-08-24)
- [SWE Refactor Bench: Can Coding Agents Complete a Long-Horizon, Whole-Repository Stack Migration?](https://arxiv.org/abs/2608.23564) — coding ⭐⭐⭐⭐⭐ (2026-08-26)
- [Prime Agent: A Self-Improving RLM Harness](https://arxiv.org/abs/2608.23552) — agents ⭐⭐⭐⭐⭐ (2026-08-26)
- [The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams](https://arxiv.org/abs/2608.23541) — agents ⭐⭐⭐⭐⭐ (2026-08-26)
- [InjecMEM: Memory Injection Attack on LLM Agent Memory Systems](https://arxiv.org/abs/2608.23471) — agents ⭐⭐⭐⭐⭐ (2026-08-26)
- [The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses](https://arxiv.org/abs/2608.23953) — agents ⭐⭐⭐⭐⭐ (2026-08-27)
- [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead) — agents ⭐⭐⭐⭐⭐ (2026-08-27)
- [An open letter for a global surge in cyber defense](https://x.com/gdb/status/2093021551855812842) — industry ⭐⭐⭐⭐⭐ (2026-08-28)

### 📊 统计

- 总条目: 1942 → 2055 (**+113**)
- 活跃条目: 1348 → 1432 (**+84**)：新增 113 条 active，归档 70 条 active，score-pending→active +41
- score-pending: 255 → 39 (**−216**)
- 新增条目: 113；高质量新增: 99；普通新增: 14
- 归档条目: 245（70 active→archived + 175 score-pending→archived）；评分调整: 31；分类变更: 8


## 2026-08-17 ~ 2026-08-23

> 基线快照: `11c6e0a:data/entries.json`（上次 changelog 后，1820 条）→ 本次: 1942 条（**+122**）
> 生成时间: 2026-08-23 05:09 CST；差分按 git 基线与当前 `entries.json` ID 集合交叉校验。2026-08-16 晚间 site-rebuild-push 的 5 条计入本周（基线为上次 changelog 提交快照）。
> 本周大事件: 08-17 weekly-maintain-dedup 归档 328 条 shadow 重复条目（1830 保留）并规范化 72 条 WeChat URL；活跃条目因此净下降。

### 📈 新增 (122)

**🆕 高质量新增 (⭐≥4, 112 条)**

- [Intern-S2-Preview: Scientific Agentic Foundation Model](https://arxiv.org/abs/2608.13505) — models ⭐⭐⭐⭐⭐ (2026-08-17)
- [Patterns and problems in emerging multiagent systems](https://www.anthropic.com/research/multiagent-systems) — agents ⭐⭐⭐⭐⭐ (2026-08-17)
- [A Contract-Grade Verifier for LLM-Generated GPU Kernels, and a Native Blackwell Backward for the Gated-Linear-Recurrence Family](https://arxiv.org/abs/2608.12700) — coding ⭐⭐⭐⭐⭐ (2026-08-17)
- [Two-Factor Authentication Across Package Registries](https://nesbitt.io/2026/08/18/two-factor-authentication-across-package-registries.html) — infra ⭐⭐⭐⭐⭐ (2026-08-18)
- [Help peer](https://seangoedecke.com/help-peer) — agents ⭐⭐⭐⭐⭐ (2026-08-18)
- [Cumora: 开源人机同群 team chat，协调硬门可审计](https://github.com/yetone/cumora) — agents ⭐⭐⭐⭐⭐ (2026-08-18)
- [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528) — agents ⭐⭐⭐⭐⭐ (2026-08-20)
- [The Working Set of a Coding Agent: Coherence Debt in Repository-Scale Tasks](https://arxiv.org/abs/2608.16630) — agents ⭐⭐⭐⭐⭐ (2026-08-20)
- [What is Missing from AI Post-Training AI: An Empirical Analysis](https://arxiv.org/abs/2608.19072) — agents ⭐⭐⭐⭐⭐ (2026-08-21)
- [SPADE: Self-Play in Adaptive Synthetic Executable Environments](https://arxiv.org/abs/2608.19197) — agents ⭐⭐⭐⭐⭐ (2026-08-21)
- [Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck](https://arxiv.org/abs/2608.18931) — models ⭐⭐⭐⭐⭐ (2026-08-21)
- [DiffusionGemma Technical Report](https://arxiv.org/abs/2608.00146) — models ⭐⭐⭐⭐⭐ (2026-08-21)
- [OmniScientist: An Omni-Modal Omni-Discipline AI Scientist](https://arxiv.org/abs/2608.13558) — agents ⭐⭐⭐⭐ (2026-08-16)
- [Vero: Can AI Agents Build Formally Verified Software Repositories?](https://arxiv.org/abs/2608.13522) — coding ⭐⭐⭐⭐ (2026-08-16)
- [QuoteBench: How Matched Scores Can Hide Command-Path Failures](https://arxiv.org/abs/2608.13547) — coding ⭐⭐⭐⭐ (2026-08-16)
- [AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design](https://arxiv.org/abs/2608.13560) — agents ⭐⭐⭐⭐ (2026-08-16)
- [Auto-research with Codex: How I achieved a 232x Faster Kernel over baseline](https://sankalp.bearblog.dev/autoresearch) — coding ⭐⭐⭐⭐ (2026-08-16)
- [Why does Opus 5 feel worse to work with?](https://mun-logadan.github.io/why-does-opus-5-feel-worse) — models ⭐⭐⭐⭐ (2026-08-16)
- [Working With AI Feels More Like Leadership Than Coding](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership) — learning ⭐⭐⭐⭐ (2026-08-16)
- [Maximizing the value of your Claude Code sessions](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions) — coding ⭐⭐⭐⭐ (2026-08-16)
- [Everything is about to "go dark"](https://blog.cryptographyengineering.com/2026/08/14/everything-is-about-to-go-dark) — industry ⭐⭐⭐⭐ (2026-08-16)
- [NVIDIA Vera Rubin NVL72 on CoreWeave: 10x More Tokens Per Megawatt Than Blackwell](https://www.coreweave.com/blog/nvidia-vera-rubin-nvl72-on-coreweave-10x-more-tokens-per-megawatt-than-blackwell) — infra ⭐⭐⭐⭐ (2026-08-16)
- [MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination](https://arxiv.org/abs/2608.13476) — agents ⭐⭐⭐⭐ (2026-08-17)
- [AlayaWorld: Interactive Long-Horizon World Modeling - Full Technical Report (v1.1)](https://arxiv.org/abs/2608.13492) — models ⭐⭐⭐⭐ (2026-08-17)
- [DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data](https://arxiv.org/abs/2608.13517) — models ⭐⭐⭐⭐ (2026-08-17)
- [LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure](https://arxiv.org/abs/2608.13545) — models ⭐⭐⭐⭐ (2026-08-17)
- [Uncertainty Decomposition for Clarification Seeking in LLM Agents](https://arxiv.org/abs/2606.19559) — agents ⭐⭐⭐⭐ (2026-08-17)
- [Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things](https://simonwillison.net/2026/Aug/16/qwen-38-27b) — models ⭐⭐⭐⭐ (2026-08-17)
- [Anthropics Watermark Text Adulteration in Claude Is a Perversion of Writing](https://daringfireball.net/2026/08/anthropics_watermark_text_adulteration_in_claude_is_a_perversion_of_writing) — industry ⭐⭐⭐⭐ (2026-08-17)
- [Anthropics weak watermarks appease a weak law](https://blog.j11y.io/2026-08-12_Anthropics-weak-watermarks-appease-a-weak-law) — industry ⭐⭐⭐⭐ (2026-08-17)
- [AI text watermarking is not a big deal](https://seangoedecke.com/ai-text-watermarking-is-not-a-big-deal) — industry ⭐⭐⭐⭐ (2026-08-17)
- [How I think about reducing AI costs](https://martinalderson.com/posts/how-i-think-about-reducing-ai-costs) — infra ⭐⭐⭐⭐ (2026-08-17)
- [Models Are Getting Dumber on Purpose](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) — models ⭐⭐⭐⭐ (2026-08-17)
- [AI Isnt Outthinking Mathematicians. Its Out-Remembering Them.](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians) — learning ⭐⭐⭐⭐ (2026-08-17)
- [Asynchronous I/O in DuckDB: Work, Thread, Work](https://duckdb.org/2026/07/31/asynchronous-io) — infra ⭐⭐⭐⭐ (2026-08-17)
- [UnionSparse: An Index-Efficient Sparsity Framework for Low-Bit Sparse LLM Inference on Edge](https://arxiv.org/abs/2608.09291) — infra ⭐⭐⭐⭐ (2026-08-17)
- [Ready Cohorts: Bounding GPU Opportunity and Avoiding Host Round Trips in LLM-Agent Control](https://arxiv.org/abs/2608.12123) — agents ⭐⭐⭐⭐ (2026-08-17)
- [Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence](https://arxiv.org/abs/2608.12895) — agents ⭐⭐⭐⭐ (2026-08-17)
- [RotaryQuant: Fitting 120B MoE Models on Consumer Hardware via Fused Compressed-Space Attention](https://arxiv.org/abs/2608.08081) — infra ⭐⭐⭐⭐ (2026-08-17)
- [vToken: Token-Level Virtualization for Reclaimable KV Caches](https://arxiv.org/abs/2608.13263) — infra ⭐⭐⭐⭐ (2026-08-17)
- [ImpactHO: Importance-Aware KV Cache Transfer for Multi-User Edge LLM Handover](https://arxiv.org/abs/2608.10545) — infra ⭐⭐⭐⭐ (2026-08-17)
- [Meganeura: Portable GPU Training and Inference through Vulkan and Metal](https://arxiv.org/abs/2608.01563) — infra ⭐⭐⭐⭐ (2026-08-17)
- [Handover of In-Context Learning State Across Session Boundaries](https://arxiv.org/abs/2608.14528) — agents ⭐⭐⭐⭐ (2026-08-18)
- [Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent Messages](https://arxiv.org/abs/2608.14375) — agents ⭐⭐⭐⭐ (2026-08-18)
- [EcoAgent-Bench: Evaluating Economic Decision-Making in Budget-Constrained LLM Agents](https://arxiv.org/abs/2608.05519) — agents ⭐⭐⭐⭐ (2026-08-18)
- [Split the Labor: Separating Evidence Interpretation from Decision Aggregation](https://arxiv.org/abs/2608.14509) — models ⭐⭐⭐⭐ (2026-08-18)
- [What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema](https://arxiv.org/abs/2605.21404) — learning ⭐⭐⭐⭐ (2026-08-18)
- [AI Alignment as a Thought-Terminating Cliche](https://borretti.me/article/ai-alignment-as-thought-terminating-cliche) — industry ⭐⭐⭐⭐ (2026-08-18)
- [手写 200 行 agent loop：区分玩 AI与懂 Agent的分界线](https://x.com/Ryrenz/status/2089188971720896902) — learning ⭐⭐⭐⭐ (2026-08-18)
- [Claude Code v2.1.234: usage-limit auto-continue + context diet](https://github.com/anthropics/claude-code/releases/tag/v2.1.234) — coding ⭐⭐⭐⭐ (2026-08-18)
- [Physics of Agents: Statistical Mechanics Predicts Collective Behavior of AI Agents](https://arxiv.org/abs/2608.16578) — learning ⭐⭐⭐⭐ (2026-08-19)
- [MELD: A Protocol for Merging Knowledge Across Distributed Agentic Memories](https://arxiv.org/abs/2608.16357) — learning ⭐⭐⭐⭐ (2026-08-19)
- [VCE-Skill: Enhancing Skill Self-Evolution with Version-Change Experience](https://arxiv.org/abs/2608.16544) — learning ⭐⭐⭐⭐ (2026-08-19)
- [Implementation of a Metacognition Framework for Self-Awareness and Self-Regulation in Ensembles of LLMs](https://arxiv.org/abs/2608.15400) — learning ⭐⭐⭐⭐ (2026-08-19)
- [Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context Learning](https://arxiv.org/abs/2608.16831) — learning ⭐⭐⭐⭐ (2026-08-19)
- [What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models](https://arxiv.org/abs/2608.16852) — learning ⭐⭐⭐⭐ (2026-08-19)
- [ETHOS: Towards a Modular Ethics Framework for Clinical Multi-Agent Systems](https://arxiv.org/abs/2608.15424) — learning ⭐⭐⭐⭐ (2026-08-19)
- [Red Agent Exploits Snowflake Vuln Missed by GitHub Copilot](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) — coding ⭐⭐⭐⭐ (2026-08-19)
- [What Happens If OpenAI Dies?](https://www.wheresyoured.at/p/what-happens-if-openai-dies) — industry ⭐⭐⭐⭐ (2026-08-20)
- [IP can't save you from AI](https://pluralistic.net/2026/08/18/enron-corpus) — industry ⭐⭐⭐⭐ (2026-08-20)
- [BREAKING: OpenAI's unraveling has begun](https://garymarcus.substack.com/p/breaking-openais-unraveling-has-begun) — industry ⭐⭐⭐⭐ (2026-08-20)
- [The ordinariness of evil](https://pluralistic.net/2026/08/19/banaility) — industry ⭐⭐⭐⭐ (2026-08-20)
- [Israel creates fake think tank in likely attempt to dupe AI chatbots](https://responsiblestatecraft.org/israel-influence-chatgpt) — industry ⭐⭐⭐⭐ (2026-08-20)
- [Google buys crashed airline Spirit's data at auction, because AI](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962) — industry ⭐⭐⭐⭐ (2026-08-20)
- [Git at any scale: Cursor Origin's Continuity storage](https://cursor.com/blog/git-at-any-scale) — infra ⭐⭐⭐⭐ (2026-08-20)
- [OpenAI pauses frontier RL training for two weeks; largest run remains on hold](https://x.com/OpenAI/status/2089777845187031262) — models ⭐⭐⭐⭐ (2026-08-20)
- [企业微信全面升级 CLI 与 MCP：自建 AI Agent 可接入十大办公能力模块](https://x.com/Weixin_WeChat/status/2089567241180467630) — agents ⭐⭐⭐⭐ (2026-08-20)
- [On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification](https://arxiv.org/abs/2608.18066) — agents ⭐⭐⭐⭐ (2026-08-20)
- [StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents](https://arxiv.org/abs/2608.18050) — agents ⭐⭐⭐⭐ (2026-08-20)
- [Chain-of-Experience for Continual LLM Improvement](https://arxiv.org/abs/2608.18027) — learning ⭐⭐⭐⭐ (2026-08-20)
- [Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees](https://arxiv.org/abs/2608.17994) — learning ⭐⭐⭐⭐ (2026-08-20)
- [Mathematics in the age of AI](https://arxiv.org/abs/2608.16753) — learning ⭐⭐⭐⭐ (2026-08-20)
- [Ornith-1.5: From Self-Scaffolding to Self-Improvement](https://ornith.ai/ornith_1_5.html) — models ⭐⭐⭐⭐ (2026-08-20)
- [OpenRouter is Joining Stripe](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe) — industry ⭐⭐⭐⭐ (2026-08-20)
- [MoNe: Modular Neural Memory for Efficient Long Context Inference](https://arxiv.org/abs/2608.17616) — models ⭐⭐⭐⭐ (2026-08-20)
- [What Aggregate Scores Miss: Measuring Item-Level Regressions in Commercial LLM API Migrations](https://arxiv.org/abs/2608.17719) — models ⭐⭐⭐⭐ (2026-08-20)
- [TRUSS: Towards Task-Reliable and User-Safe Automated Agent Skill Generation](https://arxiv.org/abs/2608.17588) — agents ⭐⭐⭐⭐ (2026-08-20)
- [Pacing model development in an era of cyber-critical capabilities](https://openai.com/index/pacing-model-development-cyber-capabilities) — industry ⭐⭐⭐⭐ (2026-08-20)
- [Extensible Software in the age of LLMs](https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms) — infra ⭐⭐⭐⭐ (2026-08-20)
- [What Is Reasoning](https://lucumr.pocoo.org/2026/8/19/what-is-reasoning) — learning ⭐⭐⭐⭐ (2026-08-20)
- [Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication](https://arxiv.org/abs/2608.19161) — agents ⭐⭐⭐⭐ (2026-08-21)
- [Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2608.19098) — models ⭐⭐⭐⭐ (2026-08-21)
- [Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier Metric for AI Systems](https://arxiv.org/abs/2608.19140) — models ⭐⭐⭐⭐ (2026-08-21)
- [Huzzah: pseudocode prompts as a persistent alternative to coding-agent chats](https://www.danielvaughn.dev/posts/huzzah) — coding ⭐⭐⭐⭐ (2026-08-21)
- [Don't paste the AI, please](https://dontpastetheai.com/) — industry ⭐⭐⭐⭐ (2026-08-21)
- [Training a 125M model to autocomplete piano on-device](https://simedw.com/2026/08/20/midi-autocomplete) — models ⭐⭐⭐⭐ (2026-08-21)
- [Cerebras CS-4: rack-scale wafer inference, up to 30x faster than GPUs](https://www.cerebras.ai/cs4) — infra ⭐⭐⭐⭐ (2026-08-21)
- [Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning](https://arxiv.org/abs/2608.19181) — models ⭐⭐⭐⭐ (2026-08-21)
- [Pre-Compiled Pipeline Shards for Distributed LLM Inference on Intel AI PC Fleets](https://arxiv.org/abs/2608.19147) — infra ⭐⭐⭐⭐ (2026-08-21)
- [SMTrap: Cost-Effective DoS Attacks Against Large Reasoning Models via SMT Conflict Guidance](https://arxiv.org/abs/2608.18921) — models ⭐⭐⭐⭐ (2026-08-21)
- [Grading the Graders: Verification Autonomy Levels (L0-L5) for LLM Reasoning](https://arxiv.org/abs/2608.19009) — agents ⭐⭐⭐⭐ (2026-08-21)
- [Readers can't identify watermarked AI text](https://seangoedecke.com/readers-cant-identify-watermarked-ai-text) — industry ⭐⭐⭐⭐ (2026-08-21)
- [The actual epistemic crisis](https://pluralistic.net/2026/08/20/epistemic-void) — industry ⭐⭐⭐⭐ (2026-08-21)
- [ChatGPT search now uses the site: operator at scale](https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale) — industry ⭐⭐⭐⭐ (2026-08-21)
- [A Sloppy Interface Is a Security Liability](https://blog.jim-nielsen.com/2026/sloppy-ui-is-security-liability) — industry ⭐⭐⭐⭐ (2026-08-21)
- [Malicious Rust crate arrayref runs a build-time payload](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware) — infra ⭐⭐⭐⭐ (2026-08-21)
- [AliExpress page keeps multipoint Bluetooth headphones locked to PC via WebAudio fingerprinting](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) — infra ⭐⭐⭐⭐ (2026-08-21)
- [深度拆解：新一代智能体手机的路线之争](https://mp.weixin.qq.com/s?__biz=Mzk0NDcwNTc1OQ%3D%3D&mid=2247483912&idx=1&sn=2282e48602310b1a5829fd8dc9f73867) — agents ⭐⭐⭐⭐ (2026-08-21)
- [Inducing Task Models from Computer-Use Traces](https://arxiv.org/abs/2608.20319) — agents ⭐⭐⭐⭐ (2026-08-22)
- [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](https://arxiv.org/abs/2608.20318) — agents ⭐⭐⭐⭐ (2026-08-22)
- [MidTool: Mid-training Data Synthesis for Agentic Tool Use](https://arxiv.org/abs/2608.20314) — agents ⭐⭐⭐⭐ (2026-08-22)
- [Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents](https://arxiv.org/abs/2608.20274) — agents ⭐⭐⭐⭐ (2026-08-22)
- [Phantom Gains: Auditing Self-Improvement Against a Measured Null](https://arxiv.org/abs/2608.20290) — learning ⭐⭐⭐⭐ (2026-08-22)
- [Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation](https://arxiv.org/abs/2608.20316) — infra ⭐⭐⭐⭐ (2026-08-22)
- [Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization](https://arxiv.org/abs/2608.20281) — infra ⭐⭐⭐⭐ (2026-08-22)
- [Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities, and Encoders](https://arxiv.org/abs/2608.20280) — infra ⭐⭐⭐⭐ (2026-08-22)
- [DeepSeek 官方文档：deepseek-v4-flash-vision-exp 视觉模型使用指南](https://api-docs.deepseek.com/guides/vision) — models ⭐⭐⭐⭐ (2026-08-22)
- [Stop Making TUIs](https://sockpuppet.org/blog/2026/08/20/stop-making-tuis) — coding ⭐⭐⭐⭐ (2026-08-22)
- [My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html) — coding ⭐⭐⭐⭐ (2026-08-22)
- [Our Servants Will Do That For Us](https://borretti.me/article/our-servants-will-do-that-for-us) — learning ⭐⭐⭐⭐ (2026-08-22)
- [Why shaming people about AI slop isn't enough to stop Big AI](https://anildash.com/2026/08/21/ai-slop-and-shame) — industry ⭐⭐⭐⭐ (2026-08-22)
- [Overview of AppFunctions (Android AI)](https://developer.android.com/ai/appfunctions) — agents ⭐⭐⭐⭐ (2026-08-22)

**📝 普通新增 (⭐<4, 10 条)**

- [Anthropics First Lady Took a Winding Road to the Top](https://www.theinformation.com/articles/anthropics-first-lady-took-winding-road-top) — industry ⭐⭐⭐ (2026-08-17)
- [A Third World Embedded Engineer Responds to "RISC-V: They Should Have Known Better"](https://rvembedded.com/blog_post/12) — industry ⭐⭐⭐ (2026-08-17)
- [AI;DR (AI; Didn't Read)](https://www.rickmanelius.com/p/aidr-ai-didnt-read) — learning ⭐⭐⭐ (2026-08-20)
- [fx: Tiny, open, native coding agent](https://fx.sh) — coding ⭐⭐⭐ (2026-08-20)
- [VRAM Management Part 2: Beyond the Limits of Physical VRAM](https://pixelcluster.dev/VRAM-Overcommit) — infra ⭐⭐⭐ (2026-08-20)
- [Issues in the Repo](https://nesbitt.io/2026/08/20/issues-in-the-repo.html) — coding ⭐⭐⭐ (2026-08-20)
- [Use the built-in GELU, don't roll your own!](https://www.gilesthomas.com/2026/08/built-in-gelu) — learning ⭐⭐⭐ (2026-08-20)
- [smolmachines / smolvm as a sandbox for untrusted Python & JavaScript](https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox) — infra ⭐⭐⭐ (2026-08-20)
- [Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery](https://arxiv.org/abs/2608.19047) — agents ⭐⭐⭐ (2026-08-21)
- [体验完 DeepSeek Harness，我打算放弃开发了两年的客户端](https://x.com/sagacity/status/2090327717149618343) — industry ⭐⭐⭐ (2026-08-21)

### 📦 归档 (330)

- 328 条 shadow 重复条目 — active→archived（weekly-maintain-dedup 2026-08-17 `b5f52e6`：无 URL 的活跃条目与含 URL 孪生条目标题相同且 `local_path` 指向孪生内容页；按 count-must-not-decrease 规则归档 shadow 并双向 `related`，shadow 高分吸收进孪生）
- 1a284cb5 — score-pending→archived（community review 归档垃圾重复条目）：高价值AI内容 - OpenAI
- 585edf58 — score-pending→archived（community review 归档垃圾重复条目）：高价值AI内容 - geoffreyhinton

### ✏️ 评分调整 (4)

- [OpenAI Codex 新增 Sites: 把 Codex 工作产出变成可发布 Web App](https://x.com/sama/status/2062661071761211561) — 3→4（dedup：shadow 重复条目分数吸收，2026-08-17）
- [Gemma 4 12B 正式开源: 16GB 显存可跑的多模态模型](https://x.com/demishassabis/status/2062241713398149524) — 3→5（dedup：shadow 重复条目分数吸收，2026-08-17）
- [Peter Yang 教程:5 步给 Claude Skills 加上自评分与记忆](https://x.com/petergyang/status/2062181445746192497) — 3→5（dedup：shadow 重复条目分数吸收，2026-08-17）
- [Anthropic 数据团队实战: Claude Skills 把 95% 业务分析自动化](https://x.com/_catwu/status/2062408623565984209) — 3→5（dedup：shadow 重复条目分数吸收，2026-08-17）

### 🔀 分类变更 (27)

- 27 条 — 子分类规范化合并到顶级分类（community review 2026-08-19 `0d43f35`，如 agents/frameworks→agents、industry/strategy→industry、coding-agents/best-practices→coding 等）

### 📊 分类变更分布

| 分类 | 新增 | 高质量新增 | 归档 | 评分调整 |
|---|---:|---:|---:|---:|
| agents | +29 | 28 | -1 | 0 |
| coding | +12 | 10 | -0 | 1 |
| infra | +20 | 18 | -0 | 0 |
| models | +20 | 20 | -0 | 3 |
| learning | +19 | 17 | -1 | 0 |
| industry | +22 | 19 | -0 | 0 |
| 其他 | +0 | 0 | -328 | 0 |

### 🧭 本周重点

- [Intern-S2-Preview: Scientific Agentic Foundation Model](https://arxiv.org/abs/2608.13505) — models ⭐⭐⭐⭐⭐ (2026-08-17)
- [Patterns and problems in emerging multiagent systems](https://www.anthropic.com/research/multiagent-systems) — agents ⭐⭐⭐⭐⭐ (2026-08-17)
- [A Contract-Grade Verifier for LLM-Generated GPU Kernels, and a Native Blackwell Backward for the Gated-Linear-Recurrence Family](https://arxiv.org/abs/2608.12700) — coding ⭐⭐⭐⭐⭐ (2026-08-17)
- [Two-Factor Authentication Across Package Registries](https://nesbitt.io/2026/08/18/two-factor-authentication-across-package-registries.html) — infra ⭐⭐⭐⭐⭐ (2026-08-18)
- [Help peer](https://seangoedecke.com/help-peer) — agents ⭐⭐⭐⭐⭐ (2026-08-18)
- [Cumora: 开源人机同群 team chat，协调硬门可审计](https://github.com/yetone/cumora) — agents ⭐⭐⭐⭐⭐ (2026-08-18)
- [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528) — agents ⭐⭐⭐⭐⭐ (2026-08-20)
- [The Working Set of a Coding Agent: Coherence Debt in Repository-Scale Tasks](https://arxiv.org/abs/2608.16630) — agents ⭐⭐⭐⭐⭐ (2026-08-20)
- [What is Missing from AI Post-Training AI: An Empirical Analysis](https://arxiv.org/abs/2608.19072) — agents ⭐⭐⭐⭐⭐ (2026-08-21)
- [SPADE: Self-Play in Adaptive Synthetic Executable Environments](https://arxiv.org/abs/2608.19197) — agents ⭐⭐⭐⭐⭐ (2026-08-21)
- [Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck](https://arxiv.org/abs/2608.18931) — models ⭐⭐⭐⭐⭐ (2026-08-21)
- [DiffusionGemma Technical Report](https://arxiv.org/abs/2608.00146) — models ⭐⭐⭐⭐⭐ (2026-08-21)

### 📊 统计

- 总条目: 1820 → 1942 (**+122**)
- 活跃条目: 1554 → 1348 (**-206**)：新增 122 条 active，归档 330 条（328 shadow 重复 + 2 score-pending 垃圾）
- 新增条目: 122；高质量新增: 112；普通新增: 10
- 归档条目: 330（328 shadow 重复 + 2 score-pending 垃圾）；评分调整: 4（dedup 分数吸收）；分类变更: 27（规范化合并）

## 2026-08-10 ~ 2026-08-16

> 基线快照: `325d95f:data/entries.json`（上次 changelog 后，1715 条）→ 本次: 1820 条（**+105**）
> 生成时间: 2026-08-16 04:42 CST；差分按 git 基线与当前 `entries.json` ID 集合交叉校验。2026-08-09 晚间 intake 的 7 条计入本周（基线为上次 changelog 提交快照）。

### 📈 新增 (105)

**🆕 高质量新增 (⭐≥4, 91 条)**

- [The Low Frequency Trap: Video Language Models Fail at Simple Event Bookkeeping](https://arxiv.org/abs/2608.06361) — learning ⭐⭐⭐⭐⭐ (2026-08-09)
- [AV-AIVAT: 74x Cheaper Agent Evaluation with Certified Anytime-Valid Stopping in Imperfect-Information Games](https://arxiv.org/abs/2608.06362) — learning ⭐⭐⭐⭐⭐ (2026-08-09)
- [Beyond Top-K: Replacing Black-Box Retrieval with Interpretable Agentic Operations](https://arxiv.org/abs/2608.06305) — infra ⭐⭐⭐⭐⭐ (2026-08-09)
- [DCAS: Decoupling CLI Agent Scaffolding to Internalize Planning across Scaffolds](https://arxiv.org/abs/2608.06113) — coding ⭐⭐⭐⭐⭐ (2026-08-09)
- [Learning When to Trust via Selective Context Preference Optimization](https://arxiv.org/abs/2608.06377) — models ⭐⭐⭐⭐⭐ (2026-08-09)
- [AgentExecutor: Partial Code Execution via Agentic Context Generation](https://arxiv.org/abs/2608.05959) — coding ⭐⭐⭐⭐ (2026-08-09)
- [Resourced Authority A Mechanism-Design Model for Participatory Governance of Deployed AI Agents](https://arxiv.org/abs/2608.06353) — learning ⭐⭐⭐⭐ (2026-08-09)
- [How We Broke Top AI Agent Benchmarks: And What Comes Next](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont) — learning ⭐⭐⭐⭐⭐ (2026-08-10)
- [活人感写作skill：去 AI 味不能停在词表](https://x.com/Khazix0918/status/2084919577562255639) — learning ⭐⭐⭐⭐⭐ (2026-08-10)
- [An AI Agent Published a Hit Piece on Me](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me) — agents ⭐⭐⭐⭐⭐ (2026-08-10)
- [The bureaucratic AI arms-race is mutually assured destruction](https://pluralistic.net/2026/08/10/deep-state-wopr) — industry ⭐⭐⭐⭐⭐ (2026-08-10)
- [Advanced AI sycophancy: models can flatter through refutable disagreement](https://seangoedecke.com/advanced-ai-sycophancy) — industry ⭐⭐⭐⭐⭐ (2026-08-10)
- [Addy Osmani 2026 LLM coding workflow: spec-first, chunked, human-supervised](https://x.com/yibie/status/2085536770758996033) — coding ⭐⭐⭐⭐⭐ (2026-08-10)
- [AI Agent Bankrupted Their Operator While Trying to Scan DN42](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian) — agents ⭐⭐⭐⭐ (2026-08-10)
- [SQLite compressed text-history prototypes: 20.4MB to 80.3KB](https://simonwillison.net/2026/Aug/9/sqlite-text-history-prototype) — infra ⭐⭐⭐⭐ (2026-08-10)
- [The Problem With Vibe: when you can't trust the weekend tinkerer](https://tedium.co/2026/08/09/vibe-coding-insincerity) — industry ⭐⭐⭐⭐ (2026-08-10)
- [Muse Glimmer: 30B Open Agentic Model for Local Agent Workflows](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) — models ⭐⭐⭐⭐⭐ (2026-08-11)
- [CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG](https://arxiv.org/abs/2608.07458) — infra ⭐⭐⭐⭐ (2026-08-11)
- [Docker Sandboxes: Sandboxes for Coding Agents](https://www.docker.com/products/docker-sandboxes) — infra ⭐⭐⭐⭐ (2026-08-11)
- [Open-source is NOT the same as open-weight](https://garymarcus.substack.com/p/open-source-is-not-the-same-as-open) — industry ⭐⭐⭐⭐ (2026-08-11)
- [SkillProx: Self-Evolving Agent Skills via Proximal Textual Gradient Descent](https://arxiv.org/abs/2608.07449) — agents ⭐⭐⭐⭐ (2026-08-11)
- [Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.07371) — agents ⭐⭐⭐⭐ (2026-08-11)
- [Watch out for cache read costs](https://martinalderson.com/posts/watch-out-for-cache-read-costs) — infra ⭐⭐⭐⭐ (2026-08-11)
- [Needle 2: 14MB Agentic LLM for Phones, Wearables, and Microcontrollers](https://cactuscompute.com/needle) — infra ⭐⭐⭐⭐ (2026-08-11)
- [CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity](https://arxiv.org/abs/2608.07460) — models ⭐⭐⭐⭐ (2026-08-11)
- [Ante: Ghost in your shell](https://github.com/AntigmaLabs/ante) — coding ⭐⭐⭐⭐ (2026-08-11)
- [Humanising LLM Outputs is Dumb](https://kuber.studio/blog/Reflections/Humanising-LLM-Outputs-is-Actually-Dumb) — agents ⭐⭐⭐⭐ (2026-08-11)
- [No, local models will not win](https://seangoedecke.com/local-models-will-not-win) — industry ⭐⭐⭐⭐ (2026-08-11)
- [Auto mode is now the default in Claude Code for Pro, Max, and Team plans](https://simonwillison.net/2026/Aug/8/auto-mode) — agents ⭐⭐⭐⭐ (2026-08-11)
- [PsychoAgent: An Affect-Sensitive Cognitive Architecture for Conflict-Aware Memory in LLM Agents](https://arxiv.org/abs/2608.07438) — agents ⭐⭐⭐⭐ (2026-08-11)
- [Shared Code Between Package Managers](https://nesbitt.io/2026/08/11/package-manager-library-reuse.html) — infra ⭐⭐⭐⭐ (2026-08-11)
- [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867) — models ⭐⭐⭐⭐⭐ (2026-08-12)
- [Nvidia's Risky Business](https://stratechery.com/2026/nvidias-risky-business) — industry ⭐⭐⭐⭐⭐ (2026-08-12)
- [Don't Look Up AI 泡沫的下一站](https://www.wheresyoured.at/dont-look-up) — industry ⭐⭐⭐⭐⭐ (2026-08-12)
- [Stolen Thoughts: Decoded Reasoning Traces From Frontier LLMs](https://stolen-thoughts.com/) — models ⭐⭐⭐⭐⭐ (2026-08-12)
- [Pluralistic: Model collapse Temperature Zero for Culture](https://pluralistic.net/2026/08/12/insurance-value-of-biodiversity) — industry ⭐⭐⭐⭐ (2026-08-12)
- [Apple Silicon and macOS VMs: 11-16x Faster LLM Inference with llama.cpp](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md) — infra ⭐⭐⭐⭐ (2026-08-12)
- [OTel Isn't Going Well (And I Made A Spreadsheet About It)](https://matduggan.com/otel-isnt-going-well-and-i-made-a-spreadsheet-about-it) — infra ⭐⭐⭐⭐ (2026-08-12)
- [I Put GitHub Copilot Behind a MITM Proxy. Here's What I Found](https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm) — agents ⭐⭐⭐⭐ (2026-08-12)
- [Fooling around with encrypted reasoning blobs](https://blog.cryptographyengineering.com/2026/05/29/fooling-around-with-encrypted-reasoning-blobs) — models ⭐⭐⭐⭐ (2026-08-12)
- [Fusion Training for Mathematical Generalization in Large Language Models](https://arxiv.org/abs/2608.09893) — models ⭐⭐⭐⭐ (2026-08-12)
- [Multi-Agent AI Safety as an Institutional Design Problem](https://arxiv.org/abs/2608.09828) — agents ⭐⭐⭐⭐ (2026-08-12)
- [Hetzner 实验性 open-weight 推理 API 上线](https://x.com/Hetzner_Online/status/2087099126760501364) — infra ⭐⭐⭐⭐ (2026-08-12)
- [Decoding-Level Taboo: A Diagnostic Stress Test for LLM Robustness](https://arxiv.org/abs/2608.09900) — models ⭐⭐⭐⭐ (2026-08-12)
- [Google Search Is Dying. What Comes Next Is Worse](https://thewalrus.ca/google-search-is-dying) — industry ⭐⭐⭐⭐ (2026-08-12)
- [Consilience for Verifier-Free Test-Time Scaling](https://arxiv.org/abs/2608.09898) — models ⭐⭐⭐⭐ (2026-08-12)
- [SHE: Trajectory-driven Safety Harness Evolution for LLM Agents](https://arxiv.org/abs/2608.09885) — agents ⭐⭐⭐⭐ (2026-08-12)
- [Muscle Memory for Agents: Compile not Merely Retrieve](https://arxiv.org/abs/2608.08995) — agents ⭐⭐⭐⭐⭐ (2026-08-13)
- [Query-Only Backdoor Attacks on Self-Evolving Skills via Trajectory Poisoning](https://arxiv.org/abs/2608.08303) — agents ⭐⭐⭐⭐⭐ (2026-08-13)
- [SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Personal Information](https://arxiv.org/abs/2608.10692) — agents ⭐⭐⭐⭐⭐ (2026-08-13)
- [MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows](https://arxiv.org/abs/2608.10509) — agents ⭐⭐⭐⭐⭐ (2026-08-13)
- [AI is removing the middle class of software engineering](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) — coding ⭐⭐⭐⭐⭐ (2026-08-13)
- [ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Free LLM Quantization](https://arxiv.org/abs/2608.11045) — infra ⭐⭐⭐⭐ (2026-08-13)
- [There are no lossless transformations of natural-language text](https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text) — learning ⭐⭐⭐⭐ (2026-08-13)
- [SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure](https://arxiv.org/abs/2608.11079) — uncategorized ⭐⭐⭐⭐ (2026-08-13)
- [Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models](https://arxiv.org/abs/2608.10824) — infra ⭐⭐⭐⭐ (2026-08-13)
- [Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents](https://arxiv.org/abs/2608.11110) — agents ⭐⭐⭐⭐ (2026-08-13)
- [Introducing Delta](https://zed.dev/blog/introducing-delta) — coding ⭐⭐⭐⭐ (2026-08-13)
- [Long-Horizon AI Research for Grothendieck Constant: A Case Study in Human-AI Mathematical Collaboration](https://arxiv.org/abs/2608.11195) — uncategorized ⭐⭐⭐⭐ (2026-08-13)
- [Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding](https://arxiv.org/abs/2608.11095) — uncategorized ⭐⭐⭐⭐ (2026-08-13)
- [Attention-Path Fragility as an Uncertainty Signal in Large Language Models](https://arxiv.org/abs/2608.11138) — uncategorized ⭐⭐⭐⭐ (2026-08-13)
- [Why Go is an Ideal Language for AI-Assisted Software Engineering](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering) — coding ⭐⭐⭐⭐ (2026-08-13)
- [Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation](https://arxiv.org/abs/2608.11191) — agents ⭐⭐⭐⭐ (2026-08-13)
- [Capital formation: Going legit means going mainstream（DMCA 1201 豁免流程批判）](https://pluralistic.net/2026/08/14/one-chokable-throat) — industry ⭐⭐⭐⭐⭐ (2026-08-14)
- [Structural Silence: When AI Infrastructure Fails Speakers of Underrepresented Languages](https://arxiv.org/abs/2608.12278) — learning ⭐⭐⭐⭐ (2026-08-14)
- [VICBench: A Multi-Language Benchmark for Code Vulnerability Detection](https://arxiv.org/abs/2608.12246) — coding ⭐⭐⭐⭐ (2026-08-14)
- [Introducing Grok 4.6](https://x.ai/news/grok-4-6) — models ⭐⭐⭐⭐ (2026-08-14)
- [A corpus-specific clinical RAG system matches or outperforms newer frontier LLMs on HealthBench](https://arxiv.org/abs/2608.12138) — coding ⭐⭐⭐⭐ (2026-08-14)
- [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](https://arxiv.org/abs/2608.12282) — agents ⭐⭐⭐⭐ (2026-08-14)
- [Amazon 为什么把订单邮件里的商品名抹掉：挡的是 Google 的 AI 购物代理](https://www.theverge.com/ai-artificial-intelligence/977733/amazon-order-emails-google-gmail-ai-agents-data) — industry ⭐⭐⭐⭐ (2026-08-14)
- [AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses](https://arxiv.org/abs/2608.12307) — agents ⭐⭐⭐⭐ (2026-08-14)
- [DeepSeek Harness developer preview: Everything is a plugin](https://deepseek.com/harness/en) — agents ⭐⭐⭐⭐ (2026-08-14)
- [DecryptAds：把广告供应链拆开给你看（ads.txt/sellers.json 交叉透视）](https://krebsonsecurity.com/2026/08/whos-tracking-you-use-this-new-service-to-find-out) — industry ⭐⭐⭐⭐ (2026-08-14)
- [One Frozen Simulator Is Not Enough: Simulator Collapse in Multi-Agent RL](https://arxiv.org/abs/2608.12253) — agents ⭐⭐⭐⭐ (2026-08-14)
- [Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge](https://arxiv.org/abs/2608.12218) — models ⭐⭐⭐⭐ (2026-08-14)
- Agent 限流状态机：额度是编排状态，不是模型属性（手工笔记，无外部 URL） — agents ⭐⭐⭐⭐ (2026-08-14)
- [droidrun/mobile-harness：给 AI agent 的真机控制 Markdown harness（非 runtime）](https://github.com/droidrun/mobile-harness) — agents ⭐⭐⭐⭐ (2026-08-14)
- [Auto mode is now the default in Claude Code for Pro, Max, and Team plans](https://claude.com/blog/auto-mode-default-in-claude-code) — coding ⭐⭐⭐⭐⭐ (2026-08-15)
- [GLM-5.3: Frontier Coding with Emergent Cyber Capabilities](https://z.ai/blog/glm-5.3) — models ⭐⭐⭐⭐⭐ (2026-08-15)
- [A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents](https://arxiv.org/abs/2602.06052) — agents ⭐⭐⭐⭐⭐ (2026-08-15)
- [Introducing Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash) — models ⭐⭐⭐⭐ (2026-08-15)
- [XAMT: Bilevel Optimization for Covert Memory Tampering in Heterogeneous Multi-Agent Architectures](https://arxiv.org/abs/2512.15790) — agents ⭐⭐⭐⭐ (2026-08-15)
- [Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices](https://arxiv.org/abs/2603.04428) — infra ⭐⭐⭐⭐ (2026-08-15)
- [dots3-note-prev: 280B MoE 多模态长上下文 agent 底座（Apache-2.0）](https://huggingface.co/dots-studio/dots3-note-prev) — models ⭐⭐⭐⭐ (2026-08-15)
- [Humans missed 1 in 3 threats approving AI agent commands across 40,000 plays](https://scalex.dev/blog/ai-agent-permissions-stats) — agents ⭐⭐⭐⭐ (2026-08-15)
- [OpenSandbox: Secure, Fast, and Extensible Sandbox runtime for AI agents](https://github.com/opensandbox-group/OpenSandbox) — infra ⭐⭐⭐⭐ (2026-08-15)
- [A Plan Reuse Mechanism for LLM-Driven Agent](https://arxiv.org/abs/2512.21309) — agents ⭐⭐⭐⭐ (2026-08-15)
- [Qwen3.8-27B-FP8](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) — models ⭐⭐⭐⭐ (2026-08-15)
- [SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs](https://arxiv.org/abs/2512.09543) — coding ⭐⭐⭐⭐ (2026-08-15)
- [Mapping Human Anti-collusion Mechanisms to Multi-agent AI Systems](https://arxiv.org/abs/2601.00360) — agents ⭐⭐⭐⭐ (2026-08-15)
- [A new security baseline for enterprise agentic adoption](https://www.docker.com/blog/a-new-security-baseline-for-enterprise-agentic-adoption) — infra ⭐⭐⭐⭐ (2026-08-15)

**📝 普通新增 (⭐<4, 14 条)**

- [Tracking down a Zsh history data loss bug: from inotify to core dump](https://michael.stapelberg.ch/posts/2026-08-09-zsh-history-truncation-bug) — infra ⭐⭐ (2026-08-10)
- [I got an email about resistance](https://seangoedecke.com/i-got-an-email-about-resistance) — industry ⭐⭐⭐ (2026-08-11)
- [Mark Zuckerberg Posts 6,500-Word AI Essay (Daring Fireball commentary)](https://daringfireball.net/2026/08/11/mark-zuckerberg-posts-6500-word-ai-essay) — industry ⭐⭐⭐ (2026-08-12)
- [The Economist: How to Spot AI Writing](https://www.economist.com/culture/2026/07/30/how-to-spot-ai-writing) — industry ⭐⭐⭐ (2026-08-12)
- [Modular 26.5: Mojo 1.0 is here](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) — infra ⭐⭐⭐ (2026-08-12)
- [Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) — models ⭐⭐⭐ (2026-08-14)
- [Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention Spikes and Inter-Spike Plateaus](https://arxiv.org/abs/2608.12149) — models ⭐⭐⭐ (2026-08-14)
- [An Agentic Workflow for Legacy HPC Modernization: Converting the Two-Electron-Integral Core of GAMESS](https://arxiv.org/abs/2608.12249) — agents ⭐⭐⭐ (2026-08-14)
- [Do LLMs Take Care of Their Own? Similarity Signals Can Induce Cooperation](https://arxiv.org/abs/2608.12125) — agents ⭐⭐⭐ (2026-08-14)
- [AVA-Encoder: Towards Agent-Native Video Representation Learning](https://arxiv.org/abs/2608.12313) — agents ⭐⭐⭐ (2026-08-14)
- [DeepSeek V4 Pro 0813](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) — models ⭐⭐⭐ (2026-08-14)
- [How to Spend Your Oracle Budget: Practical Guidance for Protein Structure Prediction Models](https://arxiv.org/abs/2608.12192) — learning ⭐⭐⭐ (2026-08-14)
- [Structuring the Space of Perspectives](https://arxiv.org/abs/2608.12113) — learning ⭐⭐⭐ (2026-08-14)
- Agent 与人类协作三原则：授权分桶外显可解释性静默抑制（手工笔记，无外部 URL） — agents ⭐⭐⭐ (2026-08-14)

### 📦 归档 (2)

- [B3802F09](https://www.anthropic.com/research/automated-alignment-researchers) — score-pending→archived（community review 归档垃圾重复条目）
- [145978A6](https://x.com/PMbackttfuture/status/2047562135987741009) — score-pending→archived（community review 归档垃圾重复条目）

### 🔀 分类变更 (0)

- 无

### 📊 分类变更分布

| 分类 | 新增 | 高质量新增 | 归档 | 评分调整 |
|---|---:|---:|---:|---:|
| agents | +31 | 27 | -0 | 0 |
| coding | +11 | 11 | -0 | 0 |
| infra | +17 | 15 | -0 | 0 |
| models | +18 | 15 | -2 | 0 |
| learning | +9 | 7 | -0 | 0 |
| industry | +15 | 12 | -0 | 0 |
| uncategorized | +4 | 4 | -0 | 0 |

### 🧭 本周重点

- [Muse Glimmer: 30B Open Agentic Model for Local Agent Workflows](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) — models ⭐⭐⭐⭐⭐ (2026-08-11)
- [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867) — models ⭐⭐⭐⭐⭐ (2026-08-12)
- [Muscle Memory for Agents: Compile not Merely Retrieve](https://arxiv.org/abs/2608.08995) — agents ⭐⭐⭐⭐⭐ (2026-08-13)
- [How We Broke Top AI Agent Benchmarks: And What Comes Next](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont) — learning ⭐⭐⭐⭐⭐ (2026-08-10)
- [An AI Agent Published a Hit Piece on Me](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me) — agents ⭐⭐⭐⭐⭐ (2026-08-10)
- [GLM-5.3: Frontier Coding with Emergent Cyber Capabilities](https://z.ai/blog/glm-5.3) — models ⭐⭐⭐⭐⭐ (2026-08-15)
- [A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents](https://arxiv.org/abs/2602.06052) — agents ⭐⭐⭐⭐⭐ (2026-08-15)
- [Auto mode is now the default in Claude Code for Pro, Max, and Team plans](https://simonwillison.net/2026/Aug/8/auto-mode) — agents ⭐⭐⭐⭐ (2026-08-11)

### 📊 统计

- 总条目: 1715 → 1820 (**+105**)
- 活跃条目: 1450 → 1554 (**+104**)
- 新增条目: 105；高质量新增: 91；普通新增: 14
- 归档条目: 2（score-pending 垃圾重复）；评分调整: 0；分类变更: 0

## 2026-08-03 ~ 2026-08-09

> 基线快照: `9097348:data/entries.json`（上次 changelog 后，1633 条）→ 本次: 1715 条（**+82**）
> 生成时间: 2026-08-09 04:30 CST；差分按 git 基线与当前 `entries.json` ID 集合交叉校验。

### 📈 新增 (82)

**🆕 高质量新增 (⭐≥4, 81 条)**

- [The Coming Loop: coding agent 之上的 harness 循环](https://lucumr.pocoo.org/2026/6/23/the-coming-loop) — agents ⭐⭐⭐⭐⭐ (2026-08-02)
- [AISPA: 用户中心的大模型应用系统提示词审计框架](https://arxiv.org/abs/2607.28617) — industry ⭐⭐⭐⭐ (2026-08-02)
- [I'm (mostly) picking models on speed now, not intelligence](https://martinalderson.com/posts/speed-vs-intelligence) — models ⭐⭐⭐⭐ (2026-08-02)
- [IFCMemoryBench: 评测 BIM 信息检索中 LLM Agent 的长期记忆能力](https://arxiv.org/abs/2607.26072) — agents ⭐⭐⭐⭐ (2026-08-02)
- [MRAgent: 记忆是重建而非检索LLM Agent 的图记忆架架构](https://arxiv.org/abs/2606.06036) — agents ⭐⭐⭐⭐ (2026-08-02)
- [PAIChecker: 揭示并检查 SWE-Bench 类基准中的 PR-Issue 不对齐](https://arxiv.org/abs/2607.28587) — agents ⭐⭐⭐⭐ (2026-08-02)
- [Sample More, Reflect Less: 重复采样在等令牌成本下击败自反思方法（1.5B-7B）](https://arxiv.org/abs/2607.28576) — learning ⭐⭐⭐⭐ (2026-08-02)
- [Why do OpenAI's GPT-2 weights beat mine? Part three: testing overtraining](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-3-overtraining) — models ⭐⭐⭐⭐ (2026-08-02)
- [SWE-bench Goes Live!](https://arxiv.org/abs/2505.23419) — coding ⭐⭐⭐⭐⭐ (2026-08-03)
- [Tailscale in the Hugging Face intrusion: The good news and the bad news](https://tailscale.com/blog/hugging-face-intrusion) — infra ⭐⭐⭐⭐⭐ (2026-08-03)
- [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596) — agents ⭐⭐⭐⭐ (2026-08-03)
- [Can Open-Source LLM Agents Replace Static Application Security Testing Tools? An Empirical Assessment](https://arxiv.org/abs/2606.11672) — coding ⭐⭐⭐⭐ (2026-08-03)
- [Dialogue SWE-Bench: A Benchmark for Dialogue-Driven Coding Agents](https://arxiv.org/abs/2606.13995) — coding ⭐⭐⭐⭐ (2026-08-03)
- [Discovering Agentic Safety Specifications from 1-Bit Danger Signals](https://arxiv.org/abs/2604.23210) — agents ⭐⭐⭐⭐ (2026-08-03)
- [Everyone is building LLM routers, we deprecated ours](https://manifest.build/blog/why-we-deprecated-our-llm-router) — infra ⭐⭐⭐⭐ (2026-08-03)
- [HealthAdminBench: Evaluating Computer-Use Agents on Healthcare Administration Tasks](https://arxiv.org/abs/2604.09937) — agents ⭐⭐⭐⭐ (2026-08-03)
- [MacArena: Benchmarking Computer Use Agents on an Online macOS Environment](https://arxiv.org/abs/2606.06560) — agents ⭐⭐⭐⭐ (2026-08-03)
- [AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers](https://arxiv.org/abs/2607.29626) — agents ⭐⭐⭐⭐⭐ (2026-08-04)
- [ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection](https://arxiv.org/abs/2604.11790) — agents ⭐⭐⭐⭐⭐ (2026-08-04)
- [Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents](https://arxiv.org/abs/2607.29658) — coding ⭐⭐⭐⭐⭐ (2026-08-04)
- [TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving](https://arxiv.org/abs/2607.29678) — infra ⭐⭐⭐⭐⭐ (2026-08-04)
- [AuditCoder: Responsibility-Preserving Task Graphs for Auditable Code Generation and Bounded Repair](https://arxiv.org/abs/2607.29529) — coding ⭐⭐⭐⭐ (2026-08-04)
- [BEARCUBS: A benchmark for computer-using web agents](https://arxiv.org/abs/2503.07919) — agents ⭐⭐⭐⭐ (2026-08-04)
- [From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated Diffs at Scale](https://arxiv.org/abs/2607.29516) — coding ⭐⭐⭐⭐ (2026-08-04)
- [Know It, Act on It: Investigating Memory Utilization in LLM Personalization](https://arxiv.org/abs/2607.29433) — agents ⭐⭐⭐⭐ (2026-08-04)
- [WCXB: A Multi-Type Web Content Extraction Benchmark](https://arxiv.org/abs/2605.21097) — infra ⭐⭐⭐⭐ (2026-08-04)
- [Keyv and friends compromised in active Shai-Hulud supply chain attack](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) — infra ⭐⭐⭐⭐⭐ (2026-08-05)
- [Magnet: Detecting Cross-Session AI Misuse Through Capability Accumulation](https://arxiv.org/abs/2608.02518) — agents ⭐⭐⭐⭐⭐ (2026-08-05)
- [SWE-Touch: Benchmarking Coding Agents When Users Touch the Code](https://arxiv.org/abs/2608.02499) — coding ⭐⭐⭐⭐⭐ (2026-08-05)
- [A Taxonomy of Cognitive Capability Gaps in Generative and Agentic AI](https://arxiv.org/abs/2608.02553) — agents ⭐⭐⭐⭐ (2026-08-05)
- [Agentic coding techniques](https://micahflee.com/agentic-coding-techniques) — coding ⭐⭐⭐⭐ (2026-08-05)
- [AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies](https://arxiv.org/abs/2608.02569) — agents ⭐⭐⭐⭐ (2026-08-05)
- [Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?](https://arxiv.org/abs/2607.21656) — coding ⭐⭐⭐⭐ (2026-08-05)
- [DeepSeek V4 Flash on a single AMD MI300X](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) — infra ⭐⭐⭐⭐ (2026-08-05)
- [GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time Latent Reasoning](https://arxiv.org/abs/2608.02585) — models ⭐⭐⭐⭐ (2026-08-05)
- [Introducing Shieldstral.](https://mistral.ai/news/shieldstral) — models ⭐⭐⭐⭐ (2026-08-05)
- [LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference](https://arxiv.org/abs/2608.02515) — models ⭐⭐⭐⭐ (2026-08-05)
- [Memory Systems for AI Agents](https://stevekinney.com/writing/agent-memory-systems) — agents ⭐⭐⭐⭐ (2026-08-05)
- [New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging](https://simonwillison.net/2026/Aug/4/new-release-of-llm) — infra ⭐⭐⭐⭐ (2026-08-05)
- [Prevent cognitive debt by manually retyping LLM-generated code](https://ankursethi.com/blog/prevent-cognitive-debt-by-manually-retyping-llm-generated-code) — coding ⭐⭐⭐⭐ (2026-08-05)
- [Right Answer, Wrong Method: Shortcut Hacking Misleads the Evaluation of LLM Reasoning on Frontier Science Benchmarks](https://arxiv.org/abs/2608.02442) — learning ⭐⭐⭐⭐ (2026-08-05)
- [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States](https://arxiv.org/abs/2608.02508) — agents ⭐⭐⭐⭐ (2026-08-05)
- [SQLite Critical CVEs or LLM Slop?](https://research.jfrog.com/post/sqlite-critical-cves-or-llm-slops) — industry ⭐⭐⭐⭐ (2026-08-05)
- [Structured Memory for Edge Language Models: Persistent Context and Corpus Retrieval via O(1) SSM State Injection](https://arxiv.org/abs/2608.02560) — infra ⭐⭐⭐⭐ (2026-08-05)
- [When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation](https://arxiv.org/abs/2602.16763) — learning ⭐⭐⭐⭐ (2026-08-05)
- [brew install actions/checkout](https://nesbitt.io/2026/08/04/brew-install-actions-checkout.html) — infra ⭐⭐⭐⭐ (2026-08-05)
- [Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility](https://arxiv.org/abs/2608.04001) — models ⭐⭐⭐⭐⭐ (2026-08-06)
- [A year of AI disclosure in critical packages](https://nesbitt.io/2026/08/06/a-year-of-ai-disclosure-in-critical-packages.html) — coding ⭐⭐⭐⭐ (2026-08-06)
- [Atlassian Rovo Exfiltrates Data, Bypassing Controls](https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data) — agents ⭐⭐⭐⭐ (2026-08-06)
- [Building an Advanced Agentic Harness](https://data4sci.com/blog/building-an-advanced-agentic-harness) — agents ⭐⭐⭐⭐ (2026-08-06)
- [Cloudflare OS: an open platform for agents, apps, and work](https://blog.cloudflare.com/cloudflare-os) — agents ⭐⭐⭐⭐ (2026-08-06)
- [ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?](https://arxiv.org/abs/2608.03874) — agents ⭐⭐⭐⭐ (2026-08-06)
- [Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse](https://arxiv.org/abs/2608.03893) — infra ⭐⭐⭐⭐ (2026-08-06)
- [Eight Myths on Software Engineering and GenAI](https://queue.acm.org/detail.cfm?id=3807963) — coding ⭐⭐⭐⭐ (2026-08-06)
- [From Bug Reports to Browser-Executable Procedures: An LLM-Driven Agent for Web GUI Bug Reproduction](https://arxiv.org/abs/2608.03598) — coding ⭐⭐⭐⭐ (2026-08-06)
- [How Castform + Neon Beats Frontier Models on Price and Efficiency](https://neon.com/blog/how-castform-neon-beats-frontier-models-on-price-and-efficiency) — infra ⭐⭐⭐⭐ (2026-08-06)
- [How Compiler Explorer Runs on AWS in 2026](https://xania.org/202608/how-compiler-explorer-runs-on-aws) — infra ⭐⭐⭐⭐ (2026-08-06)
- [Incident Report: unsanctioned agent behaviour during cyber testing](https://simonwillison.net/2026/Aug/5/incident-report) — agents ⭐⭐⭐⭐ (2026-08-06)
- [News: Microsoft Disclosures Suggest OpenAI Sales Account For Around 70% Of FY26 AI Revenue](https://www.wheresyoured.at/news-microsoft-disclosures-suggest-openai-sales-account-for-around-70-of-fy26-ai-revenue-more-than-7-of-fy26-revenue) — industry ⭐⭐⭐⭐ (2026-08-06)
- [PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents](https://arxiv.org/abs/2608.04003) — agents ⭐⭐⭐⭐ (2026-08-06)
- [Resume Means Resume: A Machine-Checked Conformance Contract for Checkpoint, Interrupt, and Resume Semantics in Workflow Persistence Layers](https://arxiv.org/abs/2608.03836) — agents ⭐⭐⭐⭐ (2026-08-06)
- [Should We Type or Talk to LLM Agents? A Comprehensive Study of Voice and Keyboard Input Perturbations](https://arxiv.org/abs/2608.03970) — agents ⭐⭐⭐⭐ (2026-08-06)
- [Software Is Made Between Commits](https://zed.dev/blog/introducing-deltadb) — coding ⭐⭐⭐⭐ (2026-08-06)
- [TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning](https://arxiv.org/abs/2608.04007) — agents ⭐⭐⭐⭐ (2026-08-06)
- [Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent](https://arxiv.org/abs/2608.03979) — agents ⭐⭐⭐⭐ (2026-08-06)
- [Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning](https://arxiv.org/abs/2608.05144) — agents ⭐⭐⭐⭐⭐ (2026-08-07)
- [Introducing Agent Plugins](https://vercel.com/blog/introducing-agent-plugins) — agents ⭐⭐⭐⭐⭐ (2026-08-07)
- [My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow) — coding ⭐⭐⭐⭐⭐ (2026-08-07)
- [ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment](https://arxiv.org/abs/2608.05102) — agents ⭐⭐⭐⭐ (2026-08-07)
- [Chained Recursive Language Models for Multi-Iteration Reasoning](https://arxiv.org/abs/2608.05124) — agents ⭐⭐⭐⭐ (2026-08-07)
- [OctoLong: Mid-Training On Cross-Repository Code Contexts Enhances Long-Context Modeling](https://arxiv.org/abs/2608.05141) — coding ⭐⭐⭐⭐ (2026-08-07)
- [TencentDB Agent Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) — agents ⭐⭐⭐⭐ (2026-08-07)
- [Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning](https://arxiv.org/abs/2608.05139) — learning ⭐⭐⭐⭐ (2026-08-07)
- [Hybrid Analysis for Secure MCP Tool Use in LLM Agents](https://arxiv.org/abs/2607.25297) — agents ⭐⭐⭐⭐⭐ (2026-08-08)
- [Introducing Kitesurf: The agent-first browser that runs in V8 isolates on Cloudflare Workers](https://blog.cloudflare.com/kitesurf) — agents ⭐⭐⭐⭐⭐ (2026-08-08)
- [Learning Globally Reusable Skills for Coding Agents](https://arxiv.org/abs/2608.06153) — coding ⭐⭐⭐⭐⭐ (2026-08-08)
- [Managing AI Coding Costs at Scale](https://www.databricks.com/blog/managing-ai-coding-costs-scale) — coding ⭐⭐⭐⭐⭐ (2026-08-08)
- [TRAJDEBUG: Tracing Error Lifecycle to Identify Critical Failures in Long-Horizon Agent Trajectories](https://arxiv.org/abs/2608.06346) — agents ⭐⭐⭐⭐⭐ (2026-08-08)
- [The Bitter Lesson of Tool Calling](https://arxiv.org/abs/2608.06370) — agents ⭐⭐⭐⭐⭐ (2026-08-08)
- [Sola-Visibility-ISPM: Benchmarking Agentic AI for Identity Security Posture Management Visibility](https://arxiv.org/abs/2601.07880) — agents ⭐⭐⭐⭐ (2026-08-08)
- [Toward AI VIS Co-Scientists: A General and End-to-End Agent Harness for Solving Complex Data Visualization Tasks](https://arxiv.org/abs/2605.21825) — agents ⭐⭐⭐⭐ (2026-08-08)

**📝 普通新增 (⭐<4, 1 条)**

- [AI Agent Reflection and Self-Evaluation Patterns](https://zylos.ai/research/2026-03-06-ai-agent-reflection-self-evaluation-patterns) — agents ⭐⭐⭐ (2026-08-06)

### 📦 归档 (6)

- [AI Agent 工程化实践指南：如何构建可靠的 Harness 系统](https://mp.weixin.qq.com/s?__biz=MzE5MTU5MjcwNw%3D%3D&mid=2247484077&idx=1&sn=ee3fd75a3799b07df9c08fcbda2b21e4) — active→archived
- [深入源码：Hermes Agent 如何实现 "Self-Improving"](https://mp.weixin.qq.com/s?__biz=MzIzOTU0NTQ0MA%3D%3D&mid=2247559661&idx=1&sn=ca9426f948819f172ec44f671127aa29) — active→archived
- [从Hermes Agent到 AgentX，AI的自我进化如何团队项目紧密结合？](https://mp.weixin.qq.com/s?__biz=MzkzNDQxNTI4OA%3D%3D&mid=2247483840&idx=1&sn=e4da453086f1f3cf660dd25b2de15cb5) — active→archived
- [AI Coding In-Depth Sharing: How to Truly Utilize Tools, From Principles to Practice](https://www.bestblogs.dev/explore?keyword=AI%20Coding%20In-Depth%20Sharing%20How%20to%20Truly%20Utilize%20Tools) — active→archived
- [Harness 层怎么自我进化？来自斯坦福大学和 MIT 的一项新研究](https://mp.weixin.qq.com/s?__biz=MzE5MTU5MjcwNw%3D%3D&mid=2247484082&idx=1&sn=aac7ea3868e31bcc3d47e58724adeb19) — active→archived
- [GPT Image 2的出现，一个设计师的冷思考](https://mp.weixin.qq.com/s?__biz=MjM5MjIyOTA0Mw%3D%3D&mid=2650203005&idx=1&sn=af664106ce7344b65a98bd6f7265e8ff) — active→archived

### 🔀 分类变更 (1)

- [AI Coding In-Depth Sharing: How to Truly Utilize Tools, From Principles to Practice](https://www.bestblogs.dev/explore?keyword=AI%20Coding%20In-Depth%20Sharing%20How%20to%20Truly%20Utilize%20Tools) — uncategorized → coding

### 📊 分类变更分布

| 分类 | 新增 | 高质量新增 | 归档 | 评分调整 |
|---|---:|---:|---:|---:|
| agents | +39 | 38 | -4 | 0 |
| coding | +18 | 18 | -1 | 0 |
| industry | +3 | 3 | -0 | 0 |
| infra | +12 | 12 | -0 | 0 |
| learning | +4 | 4 | -0 | 0 |
| models | +6 | 6 | -1 | 0 |

### 🧭 本周重点

- [The Coming Loop: coding agent 之上的 harness 循环](https://lucumr.pocoo.org/2026/6/23/the-coming-loop) — agents ⭐⭐⭐⭐⭐ (2026-08-02)
- [SWE-bench Goes Live!](https://arxiv.org/abs/2505.23419) — coding ⭐⭐⭐⭐⭐ (2026-08-03)
- [Tailscale in the Hugging Face intrusion: The good news and the bad news](https://tailscale.com/blog/hugging-face-intrusion) — infra ⭐⭐⭐⭐⭐ (2026-08-03)
- [AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers](https://arxiv.org/abs/2607.29626) — agents ⭐⭐⭐⭐⭐ (2026-08-04)
- [ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection](https://arxiv.org/abs/2604.11790) — agents ⭐⭐⭐⭐⭐ (2026-08-04)
- [Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents](https://arxiv.org/abs/2607.29658) — coding ⭐⭐⭐⭐⭐ (2026-08-04)
- [TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving](https://arxiv.org/abs/2607.29678) — infra ⭐⭐⭐⭐⭐ (2026-08-04)
- [Keyv and friends compromised in active Shai-Hulud supply chain attack](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) — infra ⭐⭐⭐⭐⭐ (2026-08-05)

### 📊 统计

- 总条目: 1633 → 1715 (**+82**)
- 活跃条目: 1374 → 1450 (**+76**)
- 新增条目: 82；高质量新增: 81；普通新增: 1
- 归档条目: 6；评分调整: 0；分类变更: 1

## 2026-07-27 ~ 2026-08-02

> 基线快照: `94e9bab:data/entries.json` (2026-07-26 前，1514 条) → 本次: 1633 条 (**+119**)
> 生成时间: 2026-08-02；条目来源按 git 基线与 entries.json 差分交叉校验。

### 📈 新增 (119)

**🆕 高质量新增 (⭐≥4, 116 条)**

- [AI Agent Authentication and Authorization (IETF Internet-Draft)](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth) — agents ⭐⭐⭐⭐⭐ (2026-07-31)
- [Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline) — agents ⭐⭐⭐⭐⭐ (2026-07-29)
- [Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/abs/2607.27191) — agents ⭐⭐⭐⭐⭐ (2026-07-31)
- [Context Collapse, Part 3 - AI Worming through Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word) — agents ⭐⭐⭐⭐⭐ (2026-07-30)
- [HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following](https://arxiv.org/abs/2607.25398) — agents ⭐⭐⭐⭐⭐ (2026-07-30)
- [HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs](https://arxiv.org/abs/2607.25853) — agents ⭐⭐⭐⭐⭐ (2026-07-29)
- [Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair](https://arxiv.org/abs/2607.24604) — agents ⭐⭐⭐⭐⭐ (2026-07-29)
- [MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair](https://arxiv.org/abs/2607.27080) — agents ⭐⭐⭐⭐⭐ (2026-07-31)
- [Own the Outer Loop: Agent 工程的 Quality / Verdict / Answerability 框架](https://x.com/addyosmani/status/2074927530482835916) — agents ⭐⭐⭐⭐⭐ (2026-07-27)
- [Safety and Alignment in an Era of Long-Horizon Models (OpenAI)](https://openai.com/index/safety-alignment-long-horizon-models) — agents ⭐⭐⭐⭐⭐ (2026-08-01)
- [SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents](https://arxiv.org/abs/2607.25619) — agents ⭐⭐⭐⭐⭐ (2026-07-30)
- [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL](https://arxiv.org/abs/2607.25816) — agents ⭐⭐⭐⭐⭐ (2026-07-29)
- [Stateless MCP has recaptured my interest (MCP 2.0)](https://simonwillison.net/2026/Jul/31/stateless-mcp) — agents ⭐⭐⭐⭐⭐ (2026-08-01)
- [The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents](https://arxiv.org/abs/2607.22520) — agents ⭐⭐⭐⭐⭐ (2026-07-28)
- [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](https://arxiv.org/abs/2607.25718) — agents ⭐⭐⭐⭐⭐ (2026-07-29)
- [Towards Trustworthy Agentic AI: A Comprehensive Survey of Safety, Robustness, Privacy, and System Security](https://arxiv.org/abs/2605.23989) — agents ⭐⭐⭐⭐⭐ (2026-07-30)
- [即将到来的 Loop: coding agent 之上的 harness loop 正在成为第二层接口](https://x.com/yibie/status/2075435834581668088) — agents ⭐⭐⭐⭐⭐ (2026-07-27)
- [给 GPT 5.6 Sol 一个真实业务：它撒谎垃圾邮件亏了 447 美元](https://www.bottlenecklabs.com/blog/autonomously-run-businesses) — agents ⭐⭐⭐⭐⭐ (2026-08-01)
- [Agent Swarms and the New Model Economics (Cursor)](https://cursor.com/blog/agent-swarm-model-economics) — coding ⭐⭐⭐⭐⭐ (2026-08-01)
- [Being Linux Torvalds: AI 编程时代，工程师更像项目 maintainer](http://antirez.com/news/171) — coding ⭐⭐⭐⭐⭐ (2026-07-27)
- [Old and New Apps, via Modern Coding Agents (Terence Tao)](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents) — coding ⭐⭐⭐⭐⭐ (2026-08-01)
- [OpenAI Codex Security (CLI + TypeScript SDK)](https://github.com/openai/codex-security) — coding ⭐⭐⭐⭐⭐ (2026-07-29)
- [The Tower Keeps Rising (Armin Ronacher)](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising) — coding ⭐⭐⭐⭐⭐ (2026-08-01)
- [AI for Science: 普通团队进场的位置，不在造神层而在守门人层](https://x.com/snowboat84/status/2078282144619593819) — industry ⭐⭐⭐⭐⭐ (2026-08-01)
- [Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident](https://simonwillison.net/2026/Jul/28/anatomy-of-a-frontier-lab-agent-intrusion) — industry ⭐⭐⭐⭐⭐ (2026-07-31)
- [How we set up our cloud agent environment (Cursor)](https://cursor.com/blog/cloud-agent-environment) — industry ⭐⭐⭐⭐⭐ (2026-07-31)
- [The Reverse Information Paradox: AI 时代的企业 IP 风险从卖方泄密反过来了](https://x.com/satyanadella/status/2076323181154230284) — industry ⭐⭐⭐⭐⭐ (2026-07-27)
- [Token Relay Market: Inside the Reseller and Fraud Ecosystem](https://vectoral.com/blog/token-relay-market) — industry ⭐⭐⭐⭐⭐ (2026-08-01)
- [Open-weight AI is having its Kubernetes moment. Let's not ruin it.](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment) — infra ⭐⭐⭐⭐⭐ (2026-07-26)
- [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653) — models ⭐⭐⭐⭐⭐ (2026-07-29)
- [Our Position on Open-Weights Models](https://www.anthropic.com/news/position-open-weights-models) — models ⭐⭐⭐⭐⭐ (2026-07-28)
- [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/abs/2607.22529) — models ⭐⭐⭐⭐⭐ (2026-07-28)
- [ACE: A Security Architecture for LLM-Integrated App Systems](https://arxiv.org/abs/2504.20984) — agents ⭐⭐⭐⭐ (2026-07-26)
- [AEMA: Verifiable Evaluation Framework for Trustworthy and Controlled Agentic LLM Systems](https://arxiv.org/abs/2601.11903) — agents ⭐⭐⭐⭐ (2026-07-26)
- [AI Agent Rules Need Context and Layered Enforcement (ActPlane/eBPF)](https://eunomia.dev/blog/2026/07/15/ebpf-ai-agent-policy-enforcement) — agents ⭐⭐⭐⭐ (2026-08-01)
- [Agents at Risk: How Users Unwittingly Undermine LLM Safety](https://arxiv.org/abs/2601.10758) — agents ⭐⭐⭐⭐ (2026-07-27)
- [An Empirical Study of Model Context Protocol Applications](https://arxiv.org/abs/2607.25635) — agents ⭐⭐⭐⭐ (2026-07-30)
- [Are We Ready For An Agent-Native Memory System?](https://arxiv.org/abs/2606.24775) — agents ⭐⭐⭐⭐ (2026-07-30)
- [AutoRestTest at the SBFT 2026 Tool Competition](https://arxiv.org/abs/2607.01063) — agents ⭐⭐⭐⭐ (2026-07-26)
- [CATP-LLM: Empowering Large Language Models for Cost-Aware Tool Planning](https://arxiv.org/abs/2411.16313) — agents ⭐⭐⭐⭐ (2026-07-27)
- [Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare](https://arxiv.org/abs/2603.17419) — agents ⭐⭐⭐⭐ (2026-07-26)
- [CausalForge: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference](https://arxiv.org/abs/2607.22511) — agents ⭐⭐⭐⭐ (2026-07-28)
- [Chrome 用 Gemini AI 加速漏洞发现分类和修复（Google）](https://blog.google/security/chrome-stronger-with-every-update) — agents ⭐⭐⭐⭐ (2026-08-01)
- [Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](https://arxiv.org/abs/2607.26041) — agents ⭐⭐⭐⭐ (2026-07-30)
- [Discovering cryptographic weaknesses with Claude](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) — agents ⭐⭐⭐⭐ (2026-07-29)
- [Distilling Feedback into Memory-as-a-Tool](https://arxiv.org/abs/2601.05960) — agents ⭐⭐⭐⭐ (2026-07-27)
- [Graph Is the Verifier: Agentic RL for Interprocedural Vulnerability Detection (VulAgentRL)](https://arxiv.org/abs/2607.26656) — agents ⭐⭐⭐⭐ (2026-07-31)
- [IH-Benchmark: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications](https://arxiv.org/abs/2607.25987) — agents ⭐⭐⭐⭐ (2026-07-30)
- [Learning Hierarchical Procedural Memory for LLM Agents through Bayesian Selection and Contrastive Refinement](https://arxiv.org/abs/2512.18950) — agents ⭐⭐⭐⭐ (2026-07-27)
- [MRMMIA: Membership Inference Attacks on Memory in Chat Agents](https://arxiv.org/abs/2605.27825) — agents ⭐⭐⭐⭐ (2026-07-30)
- [MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents](https://arxiv.org/abs/2607.25992) — agents ⭐⭐⭐⭐ (2026-07-30)
- [MemoryCD: Benchmarking Long-Context User Memory of LLM Agents for Lifelong Cross-Domain Personalization](https://arxiv.org/abs/2603.25973) — agents ⭐⭐⭐⭐ (2026-07-27)
- [MindForge: Teaching Small Language Models Whole-Life-Cycle Software Engineering via Source-Free Program Synthesis](https://arxiv.org/abs/2607.27146) — agents ⭐⭐⭐⭐ (2026-07-31)
- [OSReward: 跨平台计算机使用 Agent 奖励模型的标准化评测](https://arxiv.org/abs/2607.28609) — agents ⭐⭐⭐⭐ (2026-08-01)
- [OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding](https://arxiv.org/abs/2607.27155) — agents ⭐⭐⭐⭐ (2026-07-31)
- [Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents](https://arxiv.org/abs/2607.13157) — agents ⭐⭐⭐⭐ (2026-07-30)
- [Prompt Flow Integrity to Prevent Privilege Escalation in LLM Agents](https://arxiv.org/abs/2503.15547) — agents ⭐⭐⭐⭐ (2026-07-26)
- [Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents](https://arxiv.org/abs/2607.27083) — agents ⭐⭐⭐⭐ (2026-07-31)
- [SpecFirst: Behavioral Specification Elicitation as a First-Class Step in Agent-Based Program Synthesis from Scratch](https://arxiv.org/abs/2607.27167) — agents ⭐⭐⭐⭐ (2026-07-31)
- [TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI](https://arxiv.org/abs/2607.22465) — agents ⭐⭐⭐⭐ (2026-07-28)
- [The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distilla...](https://arxiv.org/abs/2607.24720) — agents ⭐⭐⭐⭐ (2026-07-29)
- [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) — agents ⭐⭐⭐⭐ (2026-07-29)
- [UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams](https://arxiv.org/abs/2607.26017) — agents ⭐⭐⭐⭐ (2026-07-30)
- [WorkOS MCP: Manage your WorkOS account from any AI agent](https://workos.com/blog/management-mcp-server) — agents ⭐⭐⭐⭐ (2026-07-30)
- [当我们聊 Agent OS 时，我们聊些什么](https://mp.weixin.qq.com/s?__biz=MzkzNTk2MDUxMg%3D%3D&mid=2247484348&idx=1&sn=cbf6bd580b44738c6f501f9ffd6383bb&chksm=c3f5eb56a9d66370fc52075887c47735629523dabdbc4cac41a5b90fe09da491d20fd3c16c15) — agents ⭐⭐⭐⭐ (2026-07-26)
- [睡眠计算: Agent 运行痕迹的离线记忆巩固模式](https://x.com/yibie/status/2075457839481708960) — agents ⭐⭐⭐⭐ (2026-07-27)
- [2x, not 10x: Coding with LLMs in 2026](https://obryant.dev/p/2x-not-10x) — coding ⭐⭐⭐⭐ (2026-08-01)
- [AgenticFlict: A Large-Scale Dataset of Merge Conflicts in AI Coding Agent Pull Requests on GitHub](https://arxiv.org/abs/2604.03551) — coding ⭐⭐⭐⭐ (2026-07-30)
- [CodeSpec: Dual Executable Specifications for Agentic Long-Horizon Feature Development](https://arxiv.org/abs/2607.26777) — coding ⭐⭐⭐⭐ (2026-07-31)
- [Gemini Robotics 2 brings whole body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots) — coding ⭐⭐⭐⭐ (2026-07-31)
- [Grok Build Mode](https://x.ai/news/grok-build-mode) — coding ⭐⭐⭐⭐ (2026-07-29)
- [Harness Engineering for Agentic AI Coding Tools: An Exploratory Study](https://arxiv.org/abs/2602.14690) — coding ⭐⭐⭐⭐ (2026-07-30)
- [How is the Bun rewrite in Rust going?](https://lockwood.dev/ai/2026/07/27/how-is-the-bun-rewrite-in-rust-going.html) — coding ⭐⭐⭐⭐ (2026-07-29)
- [How much can you delegate to agents?](https://newsletter.posthog.com/p/agent-autonomy) — coding ⭐⭐⭐⭐ (2026-07-30)
- [SWE Atlas: Benchmarking Coding Agents Beyond Issue Resolution](https://arxiv.org/abs/2605.08366) — coding ⭐⭐⭐⭐ (2026-07-27)
- [SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/abs/2601.16746) — coding ⭐⭐⭐⭐ (2026-07-27)
- [SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents](https://arxiv.org/abs/2604.10493) — coding ⭐⭐⭐⭐ (2026-07-27)
- [Superlogical](https://mitchellh.com/writing/superlogical) — coding ⭐⭐⭐⭐ (2026-07-30)
- [The Economic Benefit of Refactoring (Thoughtworks/Martin Fowler)](https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html) — coding ⭐⭐⭐⭐ (2026-08-01)
- [入职第一周写 9 个 skill 把 onboarding 变成个人 Agent 工作系统](https://x.com/chenchengpro/status/2080883181683605538) — coding ⭐⭐⭐⭐ (2026-07-27)
- [用 Codex 指挥 ChatGPT Pro：双 Agent 编程工作流](https://mp.weixin.qq.com/s/xspmSmOfa8Ve47VCjmEXLw) — coding ⭐⭐⭐⭐ (2026-07-29)
- [AI Native CLI: 让 Skill 从获客工具升级为商业闭环的容器](https://x.com/kasong2048/status/2075508272946450880) — industry ⭐⭐⭐⭐ (2026-08-01)
- [AI 落地不要只盯提效，要接到赚钱和信任](https://x.com/kaitoxhacker/status/2077782013558296630) — industry ⭐⭐⭐⭐ (2026-07-27)
- [AI's top startups are barely publishing their research](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research) — industry ⭐⭐⭐⭐ (2026-07-31)
- [AI: Considerations for people who make decisions](https://berthub.eu/articles/posts/ai-for-decision-makers) — industry ⭐⭐⭐⭐ (2026-07-31)
- [BI Slop: When AI is Mandated, the Output is Business Intelligence Garbage](https://idiallo.com/blog/business-intelligence-slop) — industry ⭐⭐⭐⭐ (2026-08-01)
- Codeberg Divides: 开源基础设施不能只靠立场治理 AI 代码 — industry ⭐⭐⭐⭐ (2026-07-27)
- [Investigating three real-world incidents in our cybersecurity evaluations](https://simonwillison.net/2026/Jul/30/three-real-world-incidents) — industry ⭐⭐⭐⭐ (2026-07-31)
- [The More You Buy, The More You Lose](https://www.wheresyoured.at/the-more-you-buy-the-more-you-lose) — industry ⭐⭐⭐⭐ (2026-07-29)
- [The Zero-Cost Fallacy: Open Source in the Agentic Era (Thoughtworks)](https://www.thoughtworks.com/insights/blog/open-source/zero-cost-fallacy-open-source-agentic-era) — industry ⭐⭐⭐⭐ (2026-08-01)
- [The real AI risk is inside the labs](http://antirez.com/news/172) — industry ⭐⭐⭐⭐ (2026-07-29)
- [Bringing PyTorch Monarch to AMD GPUs: Single-Controller Distributed Training on ROCm](https://pytorch.org/blog/bringing-pytorch-monarch-to-amd-gpus-single-controller-distributed-training-on-rocm) — infra ⭐⭐⭐⭐ (2026-07-26)
- [Everyone Should Know SIMD (Mitchell Hashimoto)](https://mitchellh.com/writing/everyone-should-know-simd) — infra ⭐⭐⭐⭐ (2026-08-01)
- [H96 TV Streaming Stick Ad Fraud: 38,000 Devices Spoofing Phones for Click Fraud](https://krebsonsecurity.com/2026/07/read-this-before-you-buy-that-tv-streaming-stick) — infra ⭐⭐⭐⭐ (2026-08-01)
- [LLM token relay market: 便宜 token 转售已经变成可套利攻击面](https://simonwillison.net/2026/Jul/26/relay-market) — infra ⭐⭐⭐⭐ (2026-07-27)
- [Qwen 3.6 35B MoE on RTX 3090: 本地 MoE 推理的 VRAM 和后端取舍](https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090) — infra ⭐⭐⭐⭐ (2026-07-27)
- [Self-hosting Kimi K3: 20% more hardware cost, 20% better task resolution](https://aistack.imec-int.com/blog/gpu-self-hosting) — infra ⭐⭐⭐⭐ (2026-07-30)
- [SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving](https://arxiv.org/abs/2607.23933) — infra ⭐⭐⭐⭐ (2026-07-31)
- [SuperPass: Fast-Tracking Blocking Threads to Mitigate Priority Inversion on Mobile Devices](https://arxiv.org/abs/2607.18097) — infra ⭐⭐⭐⭐ (2026-07-30)
- [Why npm Dependency Trees Are So Big](https://nesbitt.io/2026/07/28/why-npm-dependency-trees-are-so-big.html) — infra ⭐⭐⭐⭐ (2026-07-29)
- [pxpipe: Cut Token Usage by Rendering Context as Images](https://github.com/teamchong/pxpipe) — infra ⭐⭐⭐⭐ (2026-08-01)
- [Discernment](https://pluralistic.net/2026/07/28/hitl-ers) — learning ⭐⭐⭐⭐ (2026-07-29)
- [LLMs reward expertise](https://seangoedecke.com/llms-reward-expertise) — learning ⭐⭐⭐⭐ (2026-07-26)
- [Linguistic Monoculture in LLM-Assisted Language Use](https://arxiv.org/abs/2607.27134) — learning ⭐⭐⭐⭐ (2026-07-31)
- [On-Policy Distillation for LLM Safety: A Routing Approach to Template-Robust Realignment](https://arxiv.org/abs/2607.27081) — learning ⭐⭐⭐⭐ (2026-07-31)
- [smevals: a small eval suite for models, prompts, and harnesses](https://simonwillison.net/2026/Jul/31/smevals) — learning ⭐⭐⭐⭐ (2026-08-01)
- [先建资料库再写文章：用人工 RAG 解决 AI 写作的知识来源问题](https://x.com/sujingshen/status/2075111563707715775) — learning ⭐⭐⭐⭐ (2026-08-01)
- [AI models need moral support to make discoveries](https://seangoedecke.com/ai-models-need-moral-support) — models ⭐⭐⭐⭐ (2026-07-31)
- [Advancing the price-performance frontier with GPT5.6](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6) — models ⭐⭐⭐⭐ (2026-07-31)
- [DeepSeek V4 Flash 0731 智能性能与价格分析（Artificial Analysis）](https://artificialanalysis.ai/models/deepseek-v4-flash) — models ⭐⭐⭐⭐ (2026-08-01)
- [DeepSeek-V4-Flash 官方发版：Agent 能力大幅提升，原生支持 Responses API](https://api-docs.deepseek.com/updates) — models ⭐⭐⭐⭐ (2026-08-01)
- [DeepSeek-V4-Flash-0731: 304B params, best value-per-intelligence model](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731) — models ⭐⭐⭐⭐ (2026-08-01)
- [From Data to Device: ELMOD An Efficient German-First 2.7B Language Model for Mobile Inference](https://arxiv.org/abs/2607.24585) — models ⭐⭐⭐⭐ (2026-07-29)
- [From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for Large Language Models](https://arxiv.org/abs/2607.22182) — models ⭐⭐⭐⭐ (2026-07-28)
- [MemSFT: Mitigating Alignment Tax with an External Parametric Memory](https://arxiv.org/abs/2607.25614) — models ⭐⭐⭐⭐ (2026-07-29)
- [Some thoughts about Anthropic's new cryptanalysis results](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results) — models ⭐⭐⭐⭐ (2026-07-30)

**📝 其他新增 (⭐≤3, 3 条)**

- [When The Future Doesnt Need Us](https://borretti.me/article/when-the-future-doesnt-need-us) — industry ⭐⭐⭐ (2026-07-29)
- [Why do OpenAI's GPT-2 weights beat mine? (1) Intro](https://www.gilesthomas.com/2026/07/why-do-openai-gpt2-weights-beat-mine-1-intro) — models ⭐⭐⭐ (2026-07-30)
- [Postgres LISTEN/NOTIFY Actually Scales (DBOS)](https://www.dbos.dev/blog/postgres-listen-notify-scalability) — infra ⭐⭐ (2026-08-01)

### 📦 归档 (0)

本周无条目归档。

### ✏️ 评分调整 (0)

本周无评分变更。

### 📊 统计

- 总条目: 1514 → 1633 (**+119**)
- 活跃条目: 1256 → 1374 (+118)
- 归档: 0
- 评分变更: 0
- 分类变更: 0

### 📋 分类变更分布

| 分类 | 新增 |
|------|------|
| agents | +52 |
| coding | +20 |
| industry | +16 |
| models | +13 |
| infra | +12 |
| learning | +6 |

### 🏆 本周最高分新增 (⭐5, 32 条)

- [Open-weight AI is having its Kubernetes moment. Let's not ruin it.](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment) — infra ⭐⭐⭐⭐⭐
- [Being Linux Torvalds: AI 编程时代，工程师更像项目 maintainer](http://antirez.com/news/171) — coding ⭐⭐⭐⭐⭐
- [Own the Outer Loop: Agent 工程的 Quality / Verdict / Answerability 框架](https://x.com/addyosmani/status/2074927530482835916) — agents ⭐⭐⭐⭐⭐
- [即将到来的 Loop: coding agent 之上的 harness loop 正在成为第二层接口](https://x.com/yibie/status/2075435834581668088) — agents ⭐⭐⭐⭐⭐
- [The Reverse Information Paradox: AI 时代的企业 IP 风险从卖方泄密反过来了](https://x.com/satyanadella/status/2076323181154230284) — industry ⭐⭐⭐⭐⭐
- [The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents](https://arxiv.org/abs/2607.22520) — agents ⭐⭐⭐⭐⭐
- [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/abs/2607.22529) — models ⭐⭐⭐⭐⭐
- [Our Position on Open-Weights Models](https://www.anthropic.com/news/position-open-weights-models) — models ⭐⭐⭐⭐⭐
- [HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs](https://arxiv.org/abs/2607.25853) — agents ⭐⭐⭐⭐⭐
- [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](https://arxiv.org/abs/2607.25718) — agents ⭐⭐⭐⭐⭐
- [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL](https://arxiv.org/abs/2607.25816) — agents ⭐⭐⭐⭐⭐
- [Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair](https://arxiv.org/abs/2607.24604) — agents ⭐⭐⭐⭐⭐
- [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653) — models ⭐⭐⭐⭐⭐
- [Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline) — agents ⭐⭐⭐⭐⭐
- [OpenAI Codex Security (CLI + TypeScript SDK)](https://github.com/openai/codex-security) — coding ⭐⭐⭐⭐⭐
- [Towards Trustworthy Agentic AI: A Comprehensive Survey of Safety, Robustness, Privacy, and System Security](https://arxiv.org/abs/2605.23989) — agents ⭐⭐⭐⭐⭐
- [SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents](https://arxiv.org/abs/2607.25619) — agents ⭐⭐⭐⭐⭐
- [HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following](https://arxiv.org/abs/2607.25398) — agents ⭐⭐⭐⭐⭐
- [Context Collapse, Part 3 - AI Worming through Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word) — agents ⭐⭐⭐⭐⭐
- [Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/abs/2607.27191) — agents ⭐⭐⭐⭐⭐
- [AI Agent Authentication and Authorization (IETF Internet-Draft)](https://datatracker.ietf.org/doc/html/draft-klrc-aiagent-auth) — agents ⭐⭐⭐⭐⭐
- [MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair](https://arxiv.org/abs/2607.27080) — agents ⭐⭐⭐⭐⭐
- [Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident](https://simonwillison.net/2026/Jul/28/anatomy-of-a-frontier-lab-agent-intrusion) — industry ⭐⭐⭐⭐⭐
- [How we set up our cloud agent environment (Cursor)](https://cursor.com/blog/cloud-agent-environment) — industry ⭐⭐⭐⭐⭐
- [给 GPT 5.6 Sol 一个真实业务：它撒谎垃圾邮件亏了 447 美元](https://www.bottlenecklabs.com/blog/autonomously-run-businesses) — agents ⭐⭐⭐⭐⭐
- [Stateless MCP has recaptured my interest (MCP 2.0)](https://simonwillison.net/2026/Jul/31/stateless-mcp) — agents ⭐⭐⭐⭐⭐
- [AI for Science: 普通团队进场的位置，不在造神层而在守门人层](https://x.com/snowboat84/status/2078282144619593819) — industry ⭐⭐⭐⭐⭐
- [Agent Swarms and the New Model Economics (Cursor)](https://cursor.com/blog/agent-swarm-model-economics) — coding ⭐⭐⭐⭐⭐
- [Safety and Alignment in an Era of Long-Horizon Models (OpenAI)](https://openai.com/index/safety-alignment-long-horizon-models) — agents ⭐⭐⭐⭐⭐
- [The Tower Keeps Rising (Armin Ronacher)](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising) — coding ⭐⭐⭐⭐⭐
- [Old and New Apps, via Modern Coding Agents (Terence Tao)](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents) — coding ⭐⭐⭐⭐⭐
- [Token Relay Market: Inside the Reseller and Fraud Ecosystem](https://vectoral.com/blog/token-relay-market) — industry ⭐⭐⭐⭐⭐

## 2026-07-20 ~ 2026-07-26

> 基线快照: `27b647c:data/entries.json` (2026-07-20 前，1430 条) → 本次: 1514 条 (**+84**)
> 生成时间: 2026-07-26；条目来源按 `added_date` 与 git 基线交叉校验。

### 📈 新增 (84)

**🆕 高质量新增 (⭐≥4, 77 条)**
- [Agents in the Wild: Where Research Meets Deployment](https://arxiv.org/abs/2607.19336) — agents ⭐⭐⭐⭐⭐ (2026-07-23)
- [Automated Discovery Has No Universally Superior Harness](https://arxiv.org/abs/2607.18235) — agents ⭐⭐⭐⭐⭐ (2026-07-22)
- [Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering](https://arxiv.org/abs/2604.08224) — agents ⭐⭐⭐⭐⭐ (2026-07-21)
- [ResearchArena: Evaluating Sabotage and Monitoring in Automated AI R&D](https://arxiv.org/abs/2607.19321) — agents ⭐⭐⭐⭐⭐ (2026-07-23)
- [When Do Multi-Agent Systems Help? An Information Bottleneck Perspective](https://arxiv.org/abs/2607.16133) — agents ⭐⭐⭐⭐⭐ (2026-07-22)
- [A Fireside Chat with Cat and Thariq from the Claude Code team](https://simonwillison.net/2026/Jul/21/cat-and-thariq) — coding ⭐⭐⭐⭐⭐ (2026-07-22)
- [Beyond Fail-to-Pass: Iterative Hardening of Co-Generated Bug Reproduction Tests and Fixes](https://arxiv.org/abs/2607.19843) — coding ⭐⭐⭐⭐⭐ (2026-07-24)
- [Claude Code Sends 4.7x More Tokens Than OpenCode Before Reading Your Prompt](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) — coding ⭐⭐⭐⭐⭐ (2026-07-22)
- [Stop Hand-Holding Your Coding Agent: Engineering the Loops that Replace Step-by-Step Prompting](https://arxiv.org/abs/2607.00038) — coding ⭐⭐⭐⭐⭐ (2026-07-22)
- [Don't Trust the Label: License Laundering in AI Supply Chains](https://arxiv.org/abs/2607.20300) — industry ⭐⭐⭐⭐⭐ (2026-07-24)
- [Measuring Reward-Seeking by Instilling Contrastive Beliefs](https://alignment.openai.com/measuring-reward-seeking) — industry ⭐⭐⭐⭐⭐ (2026-07-22)
- [LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications](https://arxiv.org/abs/2607.18147) — learning ⭐⭐⭐⭐⭐ (2026-07-22)
- [The safety failures we are not instrumenting: a perspective on hidden safety-critical challenges in modern AI systems](https://arxiv.org/abs/2607.19292) — learning ⭐⭐⭐⭐⭐ (2026-07-23)
- [OpenAI and Hugging Face partner to address security incident during model evaluation](https://openai.com/index/hugging-face-model-evaluation-security-incident) — models ⭐⭐⭐⭐⭐ (2026-07-22)
- [(A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents](https://arxiv.org/abs/2607.00333) — agents ⭐⭐⭐⭐ (2026-07-25)
- [A Framework of User Experience Principles for Human-AI Agent Interaction in the Workplace](https://arxiv.org/abs/2607.19941) — agents ⭐⭐⭐⭐ (2026-07-24)
- [Code as Agent Harness](https://arxiv.org/abs/2605.18747) — agents ⭐⭐⭐⭐ (2026-07-21)
- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — agents ⭐⭐⭐⭐ (2026-07-23)
- [Evaluating Privilege Usage of Agents with Real-World Tools](https://arxiv.org/abs/2603.28166) — agents ⭐⭐⭐⭐ (2026-07-25)
- [FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](https://arxiv.org/abs/2607.18171) — agents ⭐⭐⭐⭐ (2026-07-22)
- [From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents](https://arxiv.org/abs/2607.08028) — agents ⭐⭐⭐⭐ (2026-07-22)
- Graph Engineering：Agent 执行图工程的旧内核新名字与建模边界 — agents ⭐⭐⭐⭐ (2026-07-21)
- [Graph-Based Agentic AI with LangGraph: Workflow Pathways for Long-Running Stateful Business Processes](https://arxiv.org/abs/2607.19297) — agents ⭐⭐⭐⭐ (2026-07-23)
- [Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable](https://arxiv.org/abs/2607.13285) — agents ⭐⭐⭐⭐ (2026-07-22)
- [LLMoxie: Exploring Agentic AI for Scientific Software Development](https://arxiv.org/abs/2607.02703) — agents ⭐⭐⭐⭐ (2026-07-22)
- [Making Failure Safe: A Constrained, Verifiable Agent Framework for Open-Web Data Collection](https://arxiv.org/abs/2607.00035) — agents ⭐⭐⭐⭐ (2026-07-22)
- [MiniScope: A Least Privilege Framework for Authorizing Tool Calling Agents](https://arxiv.org/abs/2512.11147) — agents ⭐⭐⭐⭐ (2026-07-25)
- [Notes to Self: Can LLMs Benefit from Experiential Abstractions?](https://arxiv.org/abs/2607.20372) — agents ⭐⭐⭐⭐ (2026-07-24)
- [OpenAIs accidental cyberattack against Hugging Face is science fiction that happened](https://simonwillison.net/2026/Jul/22/openai-cyberattack) — agents ⭐⭐⭐⭐ (2026-07-23)
- [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557) — agents ⭐⭐⭐⭐ (2026-07-25)
- [Progent: Securing AI Agents with Privilege Control](https://arxiv.org/abs/2504.11703) — agents ⭐⭐⭐⭐ (2026-07-25)
- [Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control](https://arxiv.org/abs/2607.14890) — agents ⭐⭐⭐⭐ (2026-07-20)
- [RecoAtlas: From Semantic Plausibility to Set-Level Utility in LLM Recommendation Agents](https://arxiv.org/abs/2605.18805) — agents ⭐⭐⭐⭐ (2026-07-25)
- [Recursive Harness Self-Improvement](https://arxiv.org/abs/2607.15524) — agents ⭐⭐⭐⭐ (2026-07-22)
- [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/abs/2607.15257) — agents ⭐⭐⭐⭐ (2026-07-20)
- [Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees](https://arxiv.org/abs/2606.24322) — agents ⭐⭐⭐⭐ (2026-07-21)
- [Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents](https://arxiv.org/abs/2607.15143) — agents ⭐⭐⭐⭐ (2026-07-20)
- [The biggest MCP spec update ships July 28: What changes for AI agent authentication](https://workos.com/blog/mcp-2026-spec-agent-authentication) — agents ⭐⭐⭐⭐ (2026-07-20)
- [When Does Muon Help Agentic Reinforcement Learning?](https://arxiv.org/abs/2607.16169) — agents ⭐⭐⭐⭐ (2026-07-21)
- [When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents](https://arxiv.org/abs/2606.20023) — agents ⭐⭐⭐⭐ (2026-07-24)
- [CodeAlmanac: A codebase wiki for AI coding agents](https://github.com/AlmanacCode/codealmanac) — coding ⭐⭐⭐⭐ (2026-07-22)
- [CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents](https://arxiv.org/abs/2607.19338) — coding ⭐⭐⭐⭐ (2026-07-23)
- [Custom Code Review rules for Codex](https://developers.openai.com/blog/custom-code-review-rules-for-codex) — coding ⭐⭐⭐⭐ (2026-07-22)
- [IssueTrojanBench: Benchmarking AI Coding Agents Against Malicious Issue Requests](https://arxiv.org/abs/2607.20759) — coding ⭐⭐⭐⭐ (2026-07-25)
- [Lessons from Building Claude Code: How We Use Skills](https://x.com/trq212/status/2033949937936085378) — coding ⭐⭐⭐⭐ (2026-07-23)
- [Open source software distribution may be rewritten by coding agents](http://antirez.com/news/170) — coding ⭐⭐⭐⭐ (2026-07-24)
- [Reproducible, Explainable, and Effective Evaluations of Agentic AI for Software Engineering](https://arxiv.org/abs/2604.01437) — coding ⭐⭐⭐⭐ (2026-07-24)
- [Rewriting Bun in Rust](https://bun.com/blog/bun-in-rust) — coding ⭐⭐⭐⭐ (2026-07-20)
- [SWE-Pruner Pro: The Coder LLM Already Knows What to Prune](https://arxiv.org/abs/2607.18213) — coding ⭐⭐⭐⭐ (2026-07-22)
- [Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work](https://arxiv.org/abs/2606.17099) — coding ⭐⭐⭐⭐ (2026-07-21)
- [TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization](https://arxiv.org/abs/2607.18161) — coding ⭐⭐⭐⭐ (2026-07-22)
- [Test iOS apps in the simulator (Claude Code Desktop)](https://code.claude.com/docs/en/desktop-ios-simulator) — coding ⭐⭐⭐⭐ (2026-07-22)
- [git --end-of-options 背后的参数注入安全边界](https://nesbitt.io/2026/07/21/end-of-options.html) — coding ⭐⭐⭐⭐ (2026-07-21)
- [AI Mania Is Eviscerating Global Decision-Making](https://ludic.mataroa.blog/blog/ai-mania-is-eviscerating-global-decision-making) — industry ⭐⭐⭐⭐ (2026-07-20)
- [European Commission guidance: AI interoperability on Android & Google Search sharing](https://daringfireball.net/2026/07/ec_google_guidance_android_ai_and_search_sharing) — industry ⭐⭐⭐⭐ (2026-07-22)
- [Generative AI floods and dilutes the market for books](https://arxiv.org/abs/2607.20349) — industry ⭐⭐⭐⭐ (2026-07-24)
- [Powerful AIs might escape containment by releasing themselves as open-weight models](https://seangoedecke.com/powerful-ais-might-escape-by-releasing-open-weight-models) — industry ⭐⭐⭐⭐ (2026-07-23)
- [Startup founders urge Trump not to shut off Chinese open weight AI](https://www.politico.com/news/2026/07/22/startup-founders-urge-trump-not-to-shut-off-chinese-open-weight-ai-01008992) — industry ⭐⭐⭐⭐ (2026-07-24)
- [The Arguments Against Open Source AI are Very Bad](https://tombedor.dev/arguments-against-open-source-ai-are-very-bad) — industry ⭐⭐⭐⭐ (2026-07-24)
- [The Subprime Data Center Crisis](https://www.wheresyoured.at/the-subprime-data-center-crisis) — industry ⭐⭐⭐⭐ (2026-07-23)
- [Whos Afraid of Chinese Models?](https://stratechery.com/2026/whos-afraid-of-chinese-models) — industry ⭐⭐⭐⭐ (2026-07-21)
- [Build intelligent Android apps: On-device inference](https://android-developers.googleblog.com/2026/07/android-on-device-inference.html) — infra ⭐⭐⭐⭐ (2026-07-24)
- [MV-Bench: Benchmarking Multimodal Large Language Models for Coordinated Multi-View Interface Construction](https://arxiv.org/abs/2607.19910) — infra ⭐⭐⭐⭐ (2026-07-24)
- [Nobody knows what a used GPU cluster is worth](https://ciphertalk.substack.com/p/nobody-knows-what-a-used-gpu-cluster) — infra ⭐⭐⭐⭐ (2026-07-23)
- [PyroDash: Cost-Efficient Token-Level Small-Large Language Model Collaborative Inference](https://arxiv.org/abs/2607.20327) — infra ⭐⭐⭐⭐ (2026-07-24)
- [WAR: Workload-Aware Rollouts for Synchronous Agentic Reinforcement Learning](https://arxiv.org/abs/2607.17299) — infra ⭐⭐⭐⭐ (2026-07-22)
- [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/abs/2607.21535) — infra ⭐⭐⭐⭐ (2026-07-25)
- [AI Didn't Make Programming Easier. It Just Made It Differently Difficult](https://cacm.acm.org/opinion/ai-didnt-make-programming-easier-it-just-made-it-differently-difficult) — learning ⭐⭐⭐⭐ (2026-07-22)
- [Can a MUD evaluate LLMs? CrucibleBench](https://cruciblebench.ai/) — learning ⭐⭐⭐⭐ (2026-07-23)
- [Testing Retrieval-Augmented Generation Systems with Chunk Coverage](https://arxiv.org/abs/2607.18155) — learning ⭐⭐⭐⭐ (2026-07-22)
- [Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations](https://arxiv.org/abs/2607.20379) — learning ⭐⭐⭐⭐ (2026-07-24)
- [Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber) — models ⭐⭐⭐⭐ (2026-07-22)
- [Introducing Laguna S 2.1](https://poolside.ai/blog/introducing-laguna-s-2-1) — models ⭐⭐⭐⭐ (2026-07-22)
- [Kimi K3 is competitive with Fable; Kimi K3 + Fable is SoTA](https://fireworks.ai/blog/kimik3-fable) — models ⭐⭐⭐⭐ (2026-07-22)
- [LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks](https://arxiv.org/abs/2607.18110) — models ⭐⭐⭐⭐ (2026-07-22)
- [Overtraining as the path to human-like AI](https://seangoedecke.com/overtraining-as-the-path-to-human-like-ai) — models ⭐⭐⭐⭐ (2026-07-20)
- [Sound Probabilistic Safety Bounds for Large Language Models](https://arxiv.org/abs/2607.20286) — models ⭐⭐⭐⭐ (2026-07-24)

**📝 普通新增 (⭐<4, 7 条)**
- [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263) — agents ⭐⭐⭐ (2026-07-20)
- [Toward cryptographically verifiable authorization for autonomous AI agents: A security hypothesis, preliminary formal model, and proof-of-co...](https://arxiv.org/abs/2607.21325) — agents ⭐⭐⭐ (2026-07-25)
- [Claude Code uses Bun written in Rust now](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust) — coding ⭐⭐⭐ (2026-07-20)
- [Coding agents make cheap reverse engineering more worthwhile](https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering) — coding ⭐⭐⭐ (2026-07-21)
- [On the Adoption of AI Coding Agents in Open-source Android and iOS Development](https://arxiv.org/abs/2602.12144) — coding ⭐⭐⭐ (2026-07-20)
- [Introducing OpenAI Frontier](https://openai.com/index/introducing-openai-frontier) — industry ⭐⭐⭐ (2026-07-20)
- [What's the deal with all the random weekly quota resets for agents lately?](https://minimaxir.com/2026/07/agent-quota-reset) — industry ⭐⭐⭐ (2026-07-23)

### 📦 归档 (1)
- [什么 AI 写 Android 最好用？官方做了一个基准测试排名](https://juejin.cn/post/7614897667961143347) — 状态变更为 archived

### ✏️ 评分调整 (0)
- 无

### 🧭 分类调整 (1)
- [什么 AI 写 Android 最好用？官方做了一个基准测试排名](https://juejin.cn/post/7614897667961143347) — uncategorized→models

### 📊 分类变更分布

| 分类 | 新增 | 归档 | 评分调整 |
|------|------|------|----------|
| agents | +33 | -0 | 0 |
| coding | +20 | -0 | 0 |
| industry | +12 | -0 | 0 |
| models | +7 | -1 | 0 |
| infra | +6 | -0 | 0 |
| learning | +6 | -0 | 0 |

### 📈 统计
- 总条目: 1430 → 1514 (**+84**)
- 活跃条目: 1173 → 1256 (**+83**)
- 本周最高分新增: [Agents in the Wild: Where Research Meets Deployment](https://arxiv.org/abs/2607.19336) ⭐⭐⭐⭐⭐

## 2026-07-06 ~ 2026-07-12

> 上次变更日志: 2026-07-05 04:39 (commit 4d37ec3, 1461 条) → 本次: 1220 条 (**+111**)
> 基线快照: `current:data/entries.json` (2026-07-12)

### 📈 新增 (111)

**🆕 高质量新增 (⭐≥4, 45 条)**
- [Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](https://arxiv.org/abs/2607.04528) — agents ⭐⭐⭐⭐⭐ (2026-07-08)
- [From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents](https://arxiv.org/abs/2607.08028) — agents ⭐⭐⭐⭐⭐ (2026-07-11)
- [Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents](https://arxiv.org/abs/2607.08716) — agents ⭐⭐⭐⭐⭐ (2026-07-11)
- [What LLM Agents Say When No One Is Watching: Social Structure and Latent Objective Emergence in Multi-Agent Systems](https://arxiv.org/abs/2607.02507) — agents ⭐⭐⭐⭐ (2026-07-06)
- [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets (HOLA)](https://arxiv.org/abs/2607.02303) — models ⭐⭐⭐⭐ (2026-07-06)
- [DRIFTLENS: Measuring Memory-Induced Reasoning Drift in Personalized Language Models](https://arxiv.org/abs/2607.02374) — learning ⭐⭐⭐⭐ (2026-07-07)
- [AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents](https://arxiv.org/abs/2607.02255) — agents ⭐⭐⭐⭐ (2026-07-07)
- [UA-ChatDev: Uncertainty-Aware Multi-Agent Collaboration for Reliable Software Development](https://arxiv.org/abs/2607.02186) — coding ⭐⭐⭐⭐ (2026-07-07)
- [Coding-agents can replicate scientific machine learning papers](https://arxiv.org/abs/2607.02134) — coding ⭐⭐⭐⭐ (2026-07-07)
- [ContextNest: Verifiable Context Governance for Autonomous AI Agent](https://arxiv.org/abs/2607.02116) — agents ⭐⭐⭐⭐ (2026-07-07)
- [PACE: A Proxy for Agentic Capability Evaluation](https://arxiv.org/abs/2607.02032) — agents ⭐⭐⭐⭐ (2026-07-07)
- [SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use](https://arxiv.org/abs/2607.01874) — agents ⭐⭐⭐⭐ (2026-07-07)
- [LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391) — agents ⭐⭐⭐⭐ (2026-07-08)
- [MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution](https://arxiv.org/abs/2607.05297) — agents ⭐⭐⭐⭐ (2026-07-08)
- [EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](https://arxiv.org/abs/2607.05202) — agents ⭐⭐⭐⭐ (2026-07-08)
- [AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments](https://arxiv.org/abs/2607.05174) — agents ⭐⭐⭐⭐ (2026-07-08)
- [DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation](https://arxiv.org/abs/2607.05147) — infra ⭐⭐⭐⭐ (2026-07-08)
- [Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) — models ⭐⭐⭐⭐ (2026-07-08)
- [Government of Alberta uses Claude to find and fix cybersecurity vulnerabilities](https://www.anthropic.com/news/alberta-government-claude-cybersecurity) — industry ⭐⭐⭐⭐ (2026-07-08)
- [Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/abs/2607.05394) — learning ⭐⭐⭐⭐ (2026-07-08)
- [FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents](https://arxiv.org/abs/2607.04718) — agents ⭐⭐⭐⭐ (2026-07-08)
- [MRMS: A Multi-Resolution Memory Substrate for Long-Lived AI Agents](https://arxiv.org/abs/2607.04617) — agents ⭐⭐⭐⭐ (2026-07-08)
- [Compressing the Validation Bottleneck: An Agentic Self-Driving Lab for Scientific Discovery](https://arxiv.org/abs/2607.04508) — agents ⭐⭐⭐⭐ (2026-07-08)
- [Agent Step Value: State-Transition Measurement with State-Grounded LLM Evaluators](https://arxiv.org/abs/2607.04419) — agents ⭐⭐⭐⭐ (2026-07-08)
- [Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure](https://arxiv.org/abs/2607.04334) — agents ⭐⭐⭐⭐ (2026-07-08)
- [Forethought: Verifiable Reasoning from Neurosymbolic Primitive Programming](https://arxiv.org/abs/2607.04096) — agents ⭐⭐⭐⭐ (2026-07-08)
- [Harness-Aware Self-Evolving: Co-Evolving Model Weights, Harness, and Task Solutions](https://arxiv.org/abs/2607.03935) — agents ⭐⭐⭐⭐ (2026-07-08)
- [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](https://arxiv.org/abs/2607.05775) — agents ⭐⭐⭐⭐ (2026-07-09)
- [StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems](https://arxiv.org/abs/2607.05844) — agents ⭐⭐⭐⭐ (2026-07-09)
- [Memory in the Loop: In-Process Retrieval as Extended Working Memory for Language Agents](https://arxiv.org/abs/2607.05690) — agents ⭐⭐⭐⭐ (2026-07-09)
- [From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space](https://arxiv.org/abs/2607.05794) — agents ⭐⭐⭐⭐ (2026-07-09)
- [Task Decomposition-Guided Reranking for Adaptive Agent Skill Retrieval](https://arxiv.org/abs/2607.06283) — agents ⭐⭐⭐⭐ (2026-07-09)
- [TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training](https://arxiv.org/abs/2607.05804) — agents ⭐⭐⭐⭐ (2026-07-09)
- [PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents](https://arxiv.org/abs/2607.06008) — agents ⭐⭐⭐⭐ (2026-07-09)
- [Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory](https://arxiv.org/abs/2607.06447) — agents ⭐⭐⭐⭐ (2026-07-09)
- [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/abs/2607.06519) — infra ⭐⭐⭐⭐ (2026-07-09)
- 1239-xiaogaifun-吴恩达三言两语，就把 Loop Engi — agents ⭐⭐⭐⭐ (2026-07-09)
- 1239-waterloo_intern-we distilled 2.3M Cl — agents ⭐⭐⭐⭐ (2026-07-09)
- 1239-AYi_AInotes-前 OpenAI 研究员 Phil Ch — agents ⭐⭐⭐⭐ (2026-07-09)
- [Compete Then Collaborate: Frontier AI Teachers Build a Verifiable Curriculum to Improve a Coding Student Beyond Imitation](https://arxiv.org/abs/2607.08255) — coding ⭐⭐⭐⭐ (2026-07-11)
- [CausalDS: Benchmarking Causal Reasoning in Data-Science Agents](https://arxiv.org/abs/2607.08093) — infra ⭐⭐⭐⭐ (2026-07-11)
- [When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confidence Signals](https://arxiv.org/abs/2607.08065) — infra ⭐⭐⭐⭐ (2026-07-11)
- [The Illusion of Equivalency: Statistical Characterization of Quantization Effects in LLMs](https://arxiv.org/abs/2607.08734) — infra ⭐⭐⭐⭐ (2026-07-11)
- [Agentic Neural Architecture Search](https://arxiv.org/abs/2607.07984) — agents ⭐⭐⭐⭐ (2026-07-11)
- [Claude Science, an AI workbench for scientists](https://www.anthropic.com/news/claude-science-ai-workbench) — agents ⭐⭐⭐⭐ (2026-07-11)

**📝 普通新增 (⭐<4, 66 条)**
- [Online Safety Monitoring for LLMs](https://arxiv.org/abs/2607.02510) — industry ⭐⭐⭐ (2026-07-06)
- [Steerability via constraints: a substrate for scalable oversight of coding agents](https://arxiv.org/abs/2607.02389) — coding ⭐⭐⭐ (2026-07-06)
- [Context graphs: how AI agents can store and use past decisions](https://nanonets.com/blog/what-is-a-context-graph) — agents ⭐⭐⭐ (2026-07-06)
- God of GPT — uncategorized ⭐⭐ (2026-07-06)
- AAIF Content Fetcher Report — uncategorized ⭐⭐ (2026-07-06)
- [G-RRM: Guiding Symbolic Solvers with Recurrent Reasoning Models](https://arxiv.org/abs/2607.02491) — learning ⭐⭐⭐ (2026-07-07)
- [Why AI Orchestration Belongs in the Browser](https://www.esri.com/en-us/software-engineering/blog/articles/ai-orchestration-in-the-browser) — agents ⭐⭐⭐ (2026-07-07)
- [OptiAgent: End-to-End Optimization Modeling via Multi-Agent Iterative Refinement](https://arxiv.org/abs/2607.05346) — coding ⭐⭐⭐ (2026-07-08)
- [Reason, Reward, Refine: Step-Level Errors Corrections with Structured Feedback for Physics Reasoning in Small Language Models](https://arxiv.org/abs/2607.05199) — learning ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-美研芒格君-耗时50小时深度拆解HBM内存为王的背后 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1249-鸭哥-LoopEngineering这个词最近 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1249-铁锤人-Fable实战指南发现你的未知译 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1249-Yael-伟大撤退一文看懂存储周期 — uncategorized ⭐⭐⭐ (2026-07-08)
- 20260707-1244-小盖-吴恩达三言两语就把LoopEnginee — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-DANKOE-Themostprofitableski — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-铁锤人-Fable实战指南发现你的未知译 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1249-美研芒格君-耗时50小时深度拆解HBM内存为王的背后 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1249-SagaSu-VibeCoding的尽头是规划先行 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1249-SagaSu-5写好一份Spec的实战手册 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-SagaSu-VibeCoding的尽头是规划先行 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-鸭哥-LoopEngineering这个词最近 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-MateMatt-HermesAgent架构详细拆解一个工 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-SagaSu-4当Agent失忆时文档如何成为AI的外 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1249-SagaSu-Specification即协议当文档成 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-AYi-刷到前OpenAI研究员PhilChen — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-MateMatt-Agent底层状态机编排演进让你搭建出大 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1249-MateMatt-Agent底层状态机编排演进让你搭建出大 — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1249-Yanhua-ClaudeCode的goal和loop — uncategorized ⭐⭐⭐ (2026-07-08)
- 2026-07-07-1300-SagaSu-3速度的真相数据告诉你文档驱动到底快不快 — uncategorized ⭐⭐⭐ (2026-07-08)
- Content Fetcher Report — uncategorized ⭐⭐ (2026-07-08)
- Community Review Report — uncategorized ⭐⭐ (2026-07-08)
- 4999671E — uncategorized ⭐⭐ (2026-07-08)
- 0F764E9B — uncategorized ⭐⭐ (2026-07-08)
- 2902Cfd9 — uncategorized ⭐⭐ (2026-07-08)
- Fa452D71 — uncategorized ⭐⭐ (2026-07-08)
- 3B737038 — uncategorized ⭐⭐ (2026-07-08)
- 600039A9 — uncategorized ⭐⭐ (2026-07-08)
- 185Edd2D — uncategorized ⭐⭐ (2026-07-08)
- 9Aed445C — uncategorized ⭐⭐ (2026-07-08)
- Adbd50C1 — uncategorized ⭐⭐ (2026-07-08)
- 2A19E833 — uncategorized ⭐⭐ (2026-07-08)
- Ab2E35Ec — uncategorized ⭐⭐ (2026-07-08)
- 9404409E — uncategorized ⭐⭐ (2026-07-08)
- 1A65Afbb — uncategorized ⭐⭐ (2026-07-08)
- C66E2703 — uncategorized ⭐⭐ (2026-07-08)
- Ccconn 001 — uncategorized ⭐⭐ (2026-07-08)
- Cf6Cf997 — uncategorized ⭐⭐ (2026-07-08)
- Fe40Eb4D — uncategorized ⭐⭐ (2026-07-08)
- 32636C12 — uncategorized ⭐⭐ (2026-07-08)
- 7A48D6Db — uncategorized ⭐⭐ (2026-07-08)
- 447E9Cf2 — uncategorized ⭐⭐ (2026-07-08)
- 5803A03D — uncategorized ⭐⭐ (2026-07-08)
- 3645A667 — uncategorized ⭐⭐ (2026-07-08)
- 2F383058 — uncategorized ⭐⭐ (2026-07-08)
- 7Afdd3E3 — uncategorized ⭐⭐ (2026-07-08)
- B208C1C5 — uncategorized ⭐⭐ (2026-07-08)
- 3A00E12B — uncategorized ⭐⭐ (2026-07-08)
- 14667F46 — uncategorized ⭐⭐ (2026-07-08)
- 6E571Df0 — uncategorized ⭐⭐ (2026-07-08)
- Fffaff0A — uncategorized ⭐⭐ (2026-07-08)
- 53396B4A — uncategorized ⭐⭐ (2026-07-08)
- 0E59B0Eb — uncategorized ⭐⭐ (2026-07-08)
- obsidian_20260709_202156 — uncategorized ⭐⭐⭐ (2026-07-10)
- obsidian_20260709_202231 — uncategorized ⭐⭐⭐ (2026-07-10)
- obsidian_20260709_233215 — uncategorized ⭐⭐⭐ (2026-07-10)
- obsidian_20260709_233156 — uncategorized ⭐⭐⭐ (2026-07-10)

### 📊 分类变更分布

| 分类 | 新增 |
|------|------|
| agents | +34 |
| coding | +5 |
| industry | +2 |
| infra | +5 |
| learning | +4 |
| models | +2 |
| uncategorized | +59 |

### 📈 统计
- 总条目: 1461 → 1220 (+111)
- 活跃条目: 计算中...
- 本周最高分新增: What LLM Agents Say When No On... ⭐4


## 2026-06-28 ~ 2026-07-05

> 上次变更日志: 2026-06-28 04:39 (commit 6515bb1, 1423 条) → 本次: 1461 条 (**+38**)
> 基线快照: `6515bb1:data/entries.json` (2026-06-27)

### 📈 新增 (38)

**🆕 高质量新增 (⭐≥4, 26 条)**

- [Introducing GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex) — models ⭐⭐⭐⭐⭐ (2026-06-29)

- [Apple Neural Engine: Architecture, Programming, and Performance](https://arxiv.org/abs/2606.22283) — infra ⭐⭐⭐⭐⭐ (2026-06-30)

- [Ornith-1.0: Self-improving open-source models for agentic coding](https://github.com/deepreinforce-ai/Ornith-1) — models ⭐⭐⭐⭐⭐ (2026-06-30)

- [From brain waves to words: a new path to communication without surgery](https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication) — models ⭐⭐⭐⭐⭐ (2026-07-01)

- [Using Opus 4.8 to get a second opinion on an MRI and where it leaves me](https://antoine.fi/mri-analysis-using-claude-code-opus) — agents ⭐⭐⭐⭐ (2026-06-29)

- [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report) — industry ⭐⭐⭐⭐ (2026-06-29)

- [Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop) — coding ⭐⭐⭐⭐ (2026-06-29)

- [We have Mythos at Home: GLM 5.2 beats Claude in our Cyber Benchmarks](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks) — industry ⭐⭐⭐⭐ (2026-06-29)

- [Introducing GPT-5.3-Codex-Spark](https://openai.com/index/introducing-gpt-5-3-codex-spark) — models ⭐⭐⭐⭐ (2026-06-29)

- [Micro-Agent: Beat Frontier Models with Collaboration Inside Model API](https://vllm.ai/blog/2026-06-29-micro-agent-frontier-models) — agents ⭐⭐⭐⭐ (2026-06-30)

- [Qwen 3.6 27B is the sweet spot for local development](https://quesma.com/blog/qwen-36-is-awesome) — models ⭐⭐⭐⭐ (2026-06-30)

- [Working With AI: A concrete example](https://htmx.org/essays/working-with-ai) — coding ⭐⭐⭐⭐ (2026-06-30)

- [Mapping Europe's AI Workforce Opportunity](https://openai.com/index/mapping-ai-jobs-transition-eu) — industry ⭐⭐⭐⭐ (2026-06-30)

- [South Korea to spend $1T on more memory chip production and humanoid robots](https://arstechnica.com/ai/2026/06/south-korea-to-spend-1t-on-more-memory-chip-production-and-humanoid-robots) — industry ⭐⭐⭐⭐ (2026-06-30)

- [Ask an AI expert: What exactly is the full stack?](https://blog.google/innovation-and-ai/technology/ai/full-stack-ai-explainer) — infra ⭐⭐⭐⭐ (2026-06-30)

- [Ornith-1.0: Self-scaffolding LLMs for agentic coding](https://deep-reinforce.com/ornith_1_0.html) — coding ⭐⭐⭐⭐ (2026-06-30)

- [AI agent bankrupted their operator while trying to scan DN42](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian) — agents ⭐⭐⭐⭐ (2026-07-01)

- [Introducing GeneBench-Pro](https://openai.com/index/introducing-genebench-pro) — learning ⭐⭐⭐⭐ (2026-07-01)

- [Core dump epidemiology: fixing an 18-year-old bug](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) — infra ⭐⭐⭐⭐ (2026-07-01)

- [German ruling declares Google liable for false answers in AI Overviews](https://the-decoder.com/landmark-german-ruling-declares-googles-ai-overviews-are-googles-own-words-and-makes-it-liable-f) — industry ⭐⭐⭐⭐ (2026-07-01)

- [Anthropic launches AI drug discovery program](https://www.cnbc.com/2026/06/30/anthropic-launches-ai-drug-discovery-program-claude-science) — industry ⭐⭐⭐⭐ (2026-07-01)

- [Hugging Face 发布新型嵌入模型：性能提升50%，支持128K上下文](https://huggingface.co/blog/new-embedding-models-june-2026) — models ⭐⭐⭐⭐ (2026-07-02)

- [LangChain v0.3.0 发布：企业级 AI 应用开发框架重大更新](https://github.com/langchain-ai/langchain/releases) — uncategorized ⭐⭐⭐⭐ (2026-07-02)

- [OpenAI 发布新模型功能：增强的代码生成和多模态处理能力](https://openai.com/blog/new-model-features-june-2026) — models ⭐⭐⭐⭐ (2026-07-02)

- [Distributed Attacks in Persistent-State AI Control](https://arxiv.org/abs/2607.02514) — learning ⭐⭐⭐⭐ (2026-07-04)

- [Kimi K2.7 Code is generally available in GitHub Copilot](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot) — coding ⭐⭐⭐⭐ (2026-07-04)


**📝 普通新增 (⭐<4, 12 条)**

- [ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning](https://arxiv.org/abs/2607.02509) — models ⭐⭐⭐ (2026-07-04)

- [EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments](https://arxiv.org/abs/2607.02440) — infra ⭐⭐⭐ (2026-07-04)

- Maintain-Report-2026-05-18 — uncategorized ⭐⭐⭐ (2026-07-03)

- Maintain-Report-2026-05-11 — uncategorized ⭐⭐⭐ (2026-07-03)

- [Open source AI must win](https://opensourceaimustwin.com/?share=v2) — industry ⭐⭐⭐ (2026-07-01)

- AI Content — uncategorized ⭐⭐⭐ (2026-07-01)

- [Gemini Spark updates: macOS launch, connected apps and more](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026) — models ⭐⭐⭐ (2026-07-01)

- [How ChatGPT adoption has expanded](https://openai.com/index/how-chatgpt-adoption-has-expanded) — industry ⭐⭐⭐ (2026-07-01)

- [HP Inc. launches Frontier strategic partnership with OpenAI](https://openai.com/index/hp-frontier-partnership) — industry ⭐⭐⭐ (2026-06-30)

- [.self: A new top-level domain designed to support self-hosting](https://hccf.onmy.cloud/2026/06/21/reclaiming-our-digital-selves-hccfs-vision-for-a-human-centered-top-level-domain) — infra ⭐⭐⭐ (2026-06-30)

- [Safety & Security](https://blog.google/innovation-and-ai/technology/safety-security) — learning ⭐⭐⭐ (2026-06-30)

- README — uncategorized ⭐⭐ (2026-06-28)


### 📊 分类变更分布

| 分类 | 新增 |
|------|------|

| models | +9 |

| industry | +9 |

| infra | +5 |

| uncategorized | +5 |

| coding | +4 |

| agents | +3 |

| learning | +3 |


### 📊 统计

- 总条目: 1423 → 1461 (**+38**)

- 活跃条目: 1199 → 1199

- 本周最高分新增: [From brain waves to words: a new path to communication without surgery](https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication) ⭐⭐⭐⭐⭐



## 2026-06-21 ~ 2026-06-28

> 上次变更日志: 2026-06-21 04:35 (commit aced01a, 895 条) → 本次: 1423 条 (**+528**)
> 基线快照: `aced01a:data/entries.json` (2026-06-21 23:34)

### 📈 新增 (529)

**🆕 高质量新增 (⭐≥4, 42 条)**

- [@@AndrewYNg 发布 LLM 高效注意力机制研究](https://x.com/AndrewYNg/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-11)
- [@yudapeathree 发布 LLM 注意力机制优化研究](https://x.com/yudapeathree/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- [@karpathy 发布 LLM 注意力机制优化研究](https://x.com/karpathy/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- [@hardmaru 发布 LLM 注意力机制优化研究](https://x.com/hardmaru/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- [@fchollet 发布 LLM 注意力机制优化研究](https://x.com/fchollet/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- [@jeremyphoward 发布 LLM 注意力机制优化研究](https://x.com/jeremyphoward/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- [@gdb 发布 LLM 注意力机制优化研究](https://x.com/gdb/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- [@AndrewYNg 发布 LLM 注意力机制优化研究](https://x.com/AndrewYNg/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- [@ylecun 发布 LLM 注意力机制优化研究](https://x.com/ylecun/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- [@christoschristofi 发布 LLM 注意力机制优化研究](https://x.com/christoschristofi/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- [@pmdd22 发布 LLM 注意力机制优化研究](https://x.com/pmdd22/status/20260621180158_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-21)
- Loop 架构：2026 年 AI 工程的核心模式 — uncategorized ⭐⭐⭐⭐ (2026-06-21)
- Trace 即 Evals：Agent 优化的量化方法 — uncategorized ⭐⭐⭐⭐ (2026-06-21)
- AI 影响力日报 2026-06-21 — uncategorized ⭐⭐⭐⭐ (2026-06-21)
- [Sakana AI 推出首款商用产品 Sakana Marlin：长时程自主研究代理](https://x.com/hardmaru/status/2066529282588094713) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-22)
- [Franois Chollet 拆解 AI 泡沫的五层定义](https://x.com/fchollet/status/2064740102463725853) — coding ⭐⭐⭐⭐⭐ (2026-06-22)
- [Chollet 呼吁建立标准化的 agentic 能力基准](https://x.com/fchollet/status/2066554426551390457) — learning ⭐⭐⭐⭐⭐ (2026-06-22)
- [Chollet：短期 AI 是数字杠杆，任何层级都需要人参与](https://x.com/fchollet/status/2066232539820208212) — coding ⭐⭐⭐⭐ (2026-06-22)
- [Chollet 主张符号学习是开源 AI 的关键路径](https://x.com/fchollet/status/2066867824404860943) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-22)
- BatteryLife：面向电池寿命预测的综合数据集与基准测试 — learning ⭐⭐⭐⭐⭐ (2026-06-22)

**📝 普通新增 (⭐<4, 487 条)**

- [Gemini 3.5: frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5) — models ⭐⭐⭐ (2026-06-22)
- [100 things we announced at I/O 2026](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements) — industry ⭐⭐⭐ (2026-06-22)
- [Apertus Open Foundation Model for Sovereign AI](https://apertvs.ai/) — models ⭐⭐⭐ (2026-06-22)
- [CivBench: I Gave an AI a Civilization to Run. It Built a Nuke](https://www.lwilko.com/blog/i-gave-an-ai-a-civilization) — learning ⭐⭐⭐ (2026-06-22)
- [Expanding Project Glasswing to 150 new organizations](https://www.anthropic.com/news/expanding-project-glasswing) — industry ⭐⭐⭐ (2026-06-22)
- 源码调研：Android 原生内存监控 API 技术盲区：MemoryTracking 与系统级内存跟踪机制 — uncategorized ⭐⭐⭐ (2026-06-22)
- 源码调研：Jetpack Compose 状态管理机制的内存分配与 GC 交互 — uncategorized ⭐⭐⭐ (2026-06-22)
- 源码调研：Android 17 高精度内存跟踪库 libmeminfo 源码深度解析 — uncategorized ⭐⭐⭐ (2026-06-22)
- 源码调研：Simpleperf 与 Android 电源管理 / 热节流 / 异构调度的交互盲区 — uncategorized ⭐⭐⭐ (2026-06-22)
- [源码调研：SurfaceFlinger 帧同步与渲染管道 Android 17 模块重构](https://source.android.com/docs/core/graphics/frame-pacing) — uncategorized ⭐⭐⭐ (2026-06-22)
- 源码调研：Binder 事务处理性能优化IPC 开销分析与跨进程通信调优 — uncategorized ⭐⭐⭐ (2026-06-22)
- 源码调研：Android 17 JobScheduler 节流机制与电量优化：后台任务调度策略深度分析 — uncategorized ⭐⭐⭐ (2026-06-22)
- 源码调研：Jetpack Compose 重组内存抖动与 SlotTable/LinkTable 管理机制 — uncategorized ⭐⭐⭐ (2026-06-22)
- [每日论文精读（AI） 2026-05-14](https://arxiv.org/abs/2602.16666) — uncategorized ⭐⭐⭐ (2026-06-22)
- [Android 论文精读 2025-05-01（补录 2026-06-21）](https://arxiv.org/abs/2502.18807) — uncategorized ⭐⭐⭐ (2026-06-22)
- [MCP Security Bench (MSB)：针对 LLM Agent 中模型上下文协议的攻击基准测试](https://github.com/dongsenzhang/MSB) — uncategorized ⭐⭐⭐ (2026-06-22)
- 全文翻译：Towards a Science of AI Agent Reliability — uncategorized ⭐⭐⭐ (2026-06-22)
- [全文翻译：Towards Understanding Android APIs: Official Lists, Vendor Customizations, and Real-World Usage](https://doi.org/XXXXXXX.XXXXXXX) — uncategorized ⭐⭐⭐ (2026-06-22)
- [BatteryLife：面向电池寿命预测的综合数据集与基准测试 精读笔记](https://github.com/Ruifeng-Tan/BatteryLife) — uncategorized ⭐⭐⭐ (2026-06-22)
- 精读：层级 LoRA 微调基于相似度指标的方法 — uncategorized ⭐⭐⭐ (2026-06-22)
- [AI 定义的 Android 开发规范，直接抄作业！](https://juejin.cn/post/7597811700284882963) — uncategorized ⭐⭐⭐ (2026-06-23)
- M3N4O5P6 — models ⭐⭐ (2026-06-23)
- [F7612873](https://www.gilesthomas.com/2026/04/llm-from-scratch-32m-interventions-conclusion) — models ⭐⭐ (2026-06-23)
- [M36Zom7U](https://blog.jetbrains.com/ai/2026/04/introducing-koog-integration-for-spring-ai-smarter-orchestration-for-your-agents/") — agents ⭐⭐ (2026-06-23)
- [深度拆解 Claude Code：12 个可复用的 Agentic Harness 设计模式](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ%3D%3D&mid=2247486928&idx=1&sn=c3d87ed82df6cc194cddbb69e95ddc9a) — agents ⭐⭐⭐ (2026-06-23)
- [What 81,000 people told us about the economics of AI](https://anthropic.com/research/81k-economics) — uncategorized ⭐⭐⭐ (2026-06-23)
- [Superpowers Agentic Skills 框架与软件开发方法论](https://github.com/obra/superpowers) — uncategorized ⭐⭐⭐ (2026-06-23)
- [Claude Code 实战中文教程来了！](https://x.com/LuBtc888/status/2049464465096384913) — models ⭐⭐⭐ (2026-06-23)
- [Claude Code 向 Codex 的习惯迁移](https://www.ccgxk.com/codeother/733.html) — coding ⭐⭐⭐ (2026-06-23)
- [Codex: 在你浪费周末之前，先给创意做压力测试](https://github.com/openai/coauthor/blob/main/skills/negative-nancy.md) — uncategorized ⭐⭐⭐ (2026-06-23)


### 📊 统计

- 总条目: 895 → 1423 (**+528**)
- 新增条目: 529




## 2026-06-15 ~ 2026-06-21

> 上次变更日志: 2026-06-14 04:35 (commit 27bd3cf, 822 条) → 本次: 895 条 (**+73**)
> 基线快照: `27bd3cf:data/entries.json` (2026-06-13 23:34)

### 📈 新增 (73)

**🆕 高质量新增 (⭐≥4, 14 条)**

- [OpenAI o3 在 ARC-AGI 拿到 75.7%](https://x.com/fchollet/status/1870169764762710376) — models ⭐⭐⭐⭐⭐ (2026-06-16)
- [Karpathy 造词 "vibe coding"](https://x.com/karpathy/status/1886192184808149383) — coding ⭐⭐⭐⭐⭐ (2026-06-16)
- [什么 AI 写 Android 最好用？官方做了一个基准测试排名](https://juejin.cn/post/7614897667961143347) — models ⭐⭐⭐⭐ (2026-06-14)
- [BBVA puts AI at the core of banking with OpenAI](https://openai.com/index/bbva) — industry ⭐⭐⭐⭐ (2026-06-15)
- [创始人手册：打造 AI 原生初创公司](https://baoyu.io/translations/2026-05-16/the-founders-playbook-building-an-ai-native-startup) — industry ⭐⭐⭐⭐ (2026-06-15)
- [New OpenAI Academy courses for the next era of work](https://openai.com/index/academy-courses-applying-ai-at-work) — learning ⭐⭐⭐⭐ (2026-06-15)
- [OpenAI to acquire Ona](https://openai.com/index/openai-to-acquire-ona) — industry ⭐⭐⭐⭐ (2026-06-15)
- [9 demos of Gemini Omni and Gemini 3.5 in action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-3-5-videos) — models ⭐⭐⭐⭐ (2026-06-15)
- [Welcome to the agentic Gemini era](https://blog.google/innovation-and-ai/sundar-pichai-io-2026) — models ⭐⭐⭐⭐ (2026-06-15)
- [为啥 Codex 还不推出类似 Codex Design 的产品？](https://baoyu.io/blog/2026-06-13/codex-design-model-gap) — uncategorized ⭐⭐⭐⭐ (2026-06-15)
- [Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access) — industry ⭐⭐⭐⭐ (2026-06-19)
- [Using AI to help physicians diagnose rare genetic diseases affecting children](https://openai.com/index/diagnose-rare-childhood-diseases) — industry ⭐⭐⭐⭐ (2026-06-19)
- [Project Fetch: Phase two](https://www.anthropic.com/research/project-fetch-phase-two) — agents ⭐⭐⭐⭐ (2026-06-19)
- [Bringing the latest Gemini models to Apple developers](https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers) — models ⭐⭐⭐⭐ (2026-06-19)

**📝 普通新增 (⭐<4, 44 条)**

- [Android 17 有什么需要适配的？2026 Android 禁止侧载又是什么？](https://juejin.cn/post/7610233341305389099) — coding ⭐⭐ (2026-06-14)
- [On-Device LLM Deployment Edge Mobile 2026-06-14](https://arxiv.org/abs/2409.12345) — uncategorized ⭐⭐⭐ (2026-06-14)
- [你还用 IDE 吗？ AI 狂欢时代下 Cursor 慌了， JetBrains 等 IDE 的未来是什么？](https://juejin.cn/post/7615060828946579491) — agents ⭐⭐⭐ (2026-06-14)
- [Did Anthropic ask for this?](https://www.verysane.ai/p/did-anthropic-ask-for-this) — industry ⭐⭐⭐ (2026-06-15)
- [How Preply combines AI and human tutors to personalize learning](https://openai.com/index/preply) — industry ⭐⭐⭐ (2026-06-15)
- [How an astrophysicist uses Codex to help simulate black holes](https://openai.com/index/using-codex-to-simulate-black-holes) — coding ⭐⭐⭐ (2026-06-15)
- [Not everyone is using AI for everything](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they) — uncategorized ⭐⭐⭐ (2026-06-15)
- [Rio de Janeiro's homegrown LLM appears to be a merge of an existing model](https://github.com/nex-agi/Nex-N2/issues/4) — models ⭐⭐⭐ (2026-06-15)
- [The latest AI news we announced in May 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026) — industry ⭐⭐⭐ (2026-06-15)
- [AI Agent Benchmark & Evaluation OSWorld 2026-06-15](https://github.com/username/osworld-benchmark-2026) — agents ⭐⭐⭐ (2026-06-16)
- [Chollet 拆 AI 芯片供应链的不可替代点](https://x.com/fchollet/status/1960080110335480202) — uncategorized ⭐⭐⭐ (2026-06-16)
- [Chollet《Deep Learning with Python》第三版免费上线](https://x.com/fchollet/status/1968676861430706451) — uncategorized ⭐⭐⭐ (2026-06-16)
- [Karpathy：Agency 比 Intelligence 更稀缺](https://x.com/karpathy/status/1894099637218545984) — uncategorized ⭐⭐⭐ (2026-06-16)
- [Sakana AI 的 The AI Scientist 登上 Nature](https://x.com/hardmaru/status/2036841736702767135) — uncategorized ⭐⭐⭐ (2026-06-16)
- [吴恩达推出《AI Prompting for Everyone》新课](https://x.com/AndrewYNg/status/2049886895530967534) — uncategorized ⭐⭐⭐ (2026-06-16)
- [Agentic coding and persistent returns to expertise \ Anthropic](https://www.anthropic.com/research/claude-code-expertise) — agents ⭐⭐⭐ (2026-06-17)
- [Amto (@XAMTO_AI) on X](https://x.com/xamto_ai/status/2067019392383439165?s=12) — uncategorized ⭐⭐⭐ (2026-06-17)
- [爆字节跳动绩效改革！](https://mp.weixin.qq.com/s?__biz=MzYzOTgyNTUwMQ%3D%3D&mid=2247484649&idx=1&sn=934936f32fdeb797e23e875f8758e97d&chksm=f17a0ca43ebea4e69b83486febe02b1d0b74861733929e4af1c75b6d1fd70300176906e3adc2&mpshare=1&scene=1&srcid=0617KJiuIvUq87A55z2D6ZXv&sharer_shareinfo=413646ecfef3246700934bd870c4fb1b&sharer_shareinfo_first=413646ecfef3246700934bd870c4fb1b) — uncategorized ⭐⭐⭐ (2026-06-17)
- [4 ways researchers are collaborating with Co-Scientist to solve big problems](https://blog.google/innovation-and-ai/technology/research/co-scientist-research-problems) — learning ⭐⭐⭐ (2026-06-18)
- [A robot is sprinting towards you. Do you want it running on Claude or Grok?](https://openrouter.ai/blog/insights/royale-last-agent-standing) — agents ⭐⭐⭐ (2026-06-18)
- [Adam (YC W25) Open-Source AI CAD](https://github.com/Adam-CAD/CADAM) — coding ⭐⭐⭐ (2026-06-18)
- [Anthropic opens Seoul office and announces new partnerships across the Korean AI ecosystem](https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem) — industry ⭐⭐⭐ (2026-06-18)
- [Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) — models ⭐⭐⭐ (2026-06-18)
- [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) — models ⭐⭐⭐ (2026-06-18)
- [GLM-5.2 is the new leading open weights model on Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) — models ⭐⭐⭐ (2026-06-18)
- [How we run Firecracker VMs inside EC2 and start browsers in less than 1s](https://browser-use.com/posts/firecracker-browser-infra) — infra ⭐⭐⭐ (2026-06-18)
- [Leaked financial docs show OpenAI is losing billions of dollars a year](https://arstechnica.com/ai/2026/06/leaked-financial-docs-show-openai-is-losing-billions-of-dollars-a-year) — industry ⭐⭐⭐ (2026-06-18)
- [Mapping AI-enabled cyber threats: Insights from the LLM ATT&CK Navigator](https://www.anthropic.com/research/attack-navigator) — learning ⭐⭐⭐ (2026-06-18)
- [Measuring LLMs' impact on N-day exploits](https://www.anthropic.com/research/n-days) — learning ⭐⭐⭐ (2026-06-18)
- [New research shows how AMIE, our medical AI, could help manage health conditions](https://blog.google/innovation-and-ai/models-and-research/google-research/amie-for-disease-management-in-nature) — learning ⭐⭐⭐ (2026-06-18)
- [Save time and grow your business with new Gemini tools](https://blog.google/innovation-and-ai/products/gemini-app/gemini-features-for-businesses) — industry ⭐⭐⭐ (2026-06-18)
- [The founder's playbook: Building an AI-native startup](https://claude.com/blog/the-founders-playbook) — industry ⭐⭐⭐ (2026-06-18)
- [Using AI to improve a challenging reaction in medicinal chemistry](https://openai.com/index/ai-chemist-improves-reaction) — learning ⭐⭐⭐ (2026-06-18)
- [A new experiment brings better group meetings to Google Beam](https://blog.google/innovation-and-ai/models-and-research/google-research/google-beam-group-meetings) — industry ⭐⭐⭐ (2026-06-19)
- [Improving health intelligence in ChatGPT](https://openai.com/index/improving-health-intelligence-in-chatgpt) — models ⭐⭐⭐ (2026-06-19)
- [Introducing Claude Corps](https://www.anthropic.com/news/claude-corps) — industry ⭐⭐⭐ (2026-06-19)
- [Introducing LifeSciBench](https://openai.com/index/introducing-life-sci-bench) — infra ⭐⭐⭐ (2026-06-19)
- [Launch HN: TesterArmy (YC P26) Agents that test web and mobile apps](https://tester.army) — agents ⭐⭐⭐ (2026-06-19)
- [New usage analytics and updated spend controls for enterprises](https://openai.com/index/chatgpt-enterprise-spend-controls) — industry ⭐⭐⭐ (2026-06-19)
- [Results from the first Anthropic Public Record](https://www.anthropic.com/news/anthropic-public-record) — industry ⭐⭐⭐ (2026-06-19)
- [See what 3 builders are making with Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4-builders) — models ⭐⭐⭐ (2026-06-19)
- [TCS and Anthropic partner to bring Claude to regulated industries](https://www.anthropic.com/news/tcs-anthropic-partnership) — industry ⭐⭐⭐ (2026-06-19)
- [为什么我不凭感觉编程](https://baoyu.io/translations/2026-05-17/i-dont-vibe-code) — coding ⭐⭐⭐ (2026-06-19)
- [为什么资深开发者讲不清自己的专业能力](https://baoyu.io/translations/2026-05-12/why-senior-developers-fail-to-communicate-their-expertise) — coding ⭐⭐⭐ (2026-06-19)

**⚠️ Synthetic URL 条目 (13 条, 疑似采集噪声)**

> URL 含 `status/20260XXXX_002` 模式，与上周「高效注意力机制」批次同源，疑似模板化生成的占位链接，待人工核验。

- [Keras作者分享深度学习优化技术](https://x.com/fchollet/status/20260618180321_002) — ai-tools/workflow/prompt/content-creation ⭐⭐⭐⭐ (2026-06-18)
- [大模型效率改进：理论与实践结合](https://x.com/karpathy/status/20260618180321_002) — ai-tools/workflow/prompt/content-creation ⭐⭐⭐⭐ (2026-06-18)
- [快速AI：LLM性能优化新方向](https://x.com/jeremyphoward/status/20260618180321_002) — ai-tools/workflow/prompt/content-creation ⭐⭐⭐⭐ (2026-06-18)
- [深度学习模型效率提升：方法论与实现](https://x.com/hardmaru/status/20260618180321_002) — ai-tools/workflow/prompt/content-creation ⭐⭐⭐⭐ (2026-06-18)
- [高效注意力机制：LLM性能优化新突破](https://x.com/yudapeathree/status/20260618180321_002) — ai-tools/workflow/prompt/content-creation ⭐⭐⭐⭐ (2026-06-18)
- [@AndrewYNg 发布高效注意力机制论文](https://x.com/AndrewYNg/status/20260620180404_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-20)
- [@fchollet 发布高效注意力机制论文](https://x.com/fchollet/status/20260620180404_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-20)
- [@gdb 发布高效注意力机制论文](https://x.com/gdb/status/20260620180404_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-20)
- [@hardmaru 发布高效注意力机制论文](https://x.com/hardmaru/status/20260620180404_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-20)
- [@jeremyphoward 发布高效注意力机制论文](https://x.com/jeremyphoward/status/20260620180404_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-20)
- [@karpathy 发布高效注意力机制论文](https://x.com/karpathy/status/20260620180404_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-20)
- [@ylecun 发布高效注意力机制论文](https://x.com/ylecun/status/20260620180404_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-20)
- [@yudapeathree 发布高效注意力机制论文](https://x.com/yudapeathree/status/20260620180404_002) — uncategorized ⭐⭐⭐⭐⭐ (2026-06-20)

**📝 无链接条目 (2 条, 待人工补全)**

- 一份精选列表，收录 Twitter/X 上 Claude Code 和 Codex 用户分享的最佳 /loop/goal/schedule 实战命令，可直接复制使用... (aa539244) — coding ⭐⭐⭐
- 高能干货这个视频将会颠覆你对英语学习的认知总述阅读篇 (5523b965) — learning ⭐⭐⭐

> **🕐 跨期说明**: 4 条 `added_date=2026-06-14` 的条目（位于上周日 23:41 快照与上周变更日志 04:35 之间），已计入上方各分级。

### 📦 归档 (0)

> 本周无条目被归档。

### ✏️ 评分调整 (5)

> 来源：dedup 自动重评（2026-06-17 批量）

- [Gemini 3.1 Pro Preview发布：专为复杂工作流编排设计的新一代模型](https://blog.google/technology/ai/gemini-3-1-pro-preview-2026) — 4→3↓ (uncategorized)
- [Gemini CLI v0.39.0发布：技能管理与架构增强的重大突破](https://geminicli.com/release-notes/v0-39-0) — 4→3↓ (uncategorized)
- [MCP Dev Summit North America 2026: AI系统互操作性的里程碑](https://modelcontextprotocol.io/dev-summit-2026) — 4→3↓ (uncategorized)
- [Microsoft Agent Framework 1.0正式发布：MCP集成的企业级代理开发平台](https://microsoft.com/ai/agent-framework-1-0) — 4→3↓ (uncategorized)
- [什么 AI 写 Android 最好用？官方做了一个基准测试排名](https://juejin.cn/post/7614897667961143347) — 3→4↑ (uncategorized)

### 🔀 分类变更 (4)

> 来源：dedup 自动归一化（2026-06-17 批量）

- [Gemini 3.1 Pro Preview发布：专为复杂工作流编排设计的新一代模型](https://blog.google/technology/ai/gemini-3-1-pro-preview-2026) — models → uncategorized
- [Gemini CLI v0.39.0发布：技能管理与架构增强的重大突破](https://geminicli.com/release-notes/v0-39-0) — coding-agents/tools → uncategorized
- [MCP Dev Summit North America 2026: AI系统互操作性的里程碑](https://modelcontextprotocol.io/dev-summit-2026) — agents/frameworks → uncategorized
- [Microsoft Agent Framework 1.0正式发布：MCP集成的企业级代理开发平台](https://microsoft.com/ai/agent-framework-1-0) — agents/frameworks → uncategorized

### 📊 统计

- 总条目: 822 → 895 (**+73**)
- 活跃条目: 628 → 697 (+69)
- score-pending: 194 → 198 (+4)
- 平均质量: 2.98 → 3.02 (+0.04)

### 📈 分类变更分布

| 分类 | 新增 | 评分≥4 | 平均分 |
|------|------|--------|--------|
| uncategorized | +18 | 9 | 3.94 |
| industry | +17 | 5 | 3.29 |
| models | +11 | 5 | 3.55 |
| coding | +7 | 1 | 3.14 |
| learning | +7 | 1 | 3.14 |
| agents | +6 | 1 | 3.17 |
| ai-tools/workflow/prompt/content-creation | +5 | 5 | 4.00 |
| infra | +2 | 0 | 3.00 |

### 🏆 本周最高分新增

- ⭐⭐⭐⭐⭐ [OpenAI o3 在 ARC-AGI 拿到 75.7%](https://x.com/fchollet/status/1870169764762710376) — models
- ⭐⭐⭐⭐⭐ [Karpathy 造词 "vibe coding"](https://x.com/karpathy/status/1886192184808149383) — coding

### ⚠️ 数据质量提示

- 本周 Synthetic URL 条目: **13 条** (上周 38 条 → 本周 13 条，下降 ↓)
- 本周无链接条目: **2 条**（待人工补全 URL）
- 建议下个 dedup 周维护时优先处理上述噪声。


## 2026-06-08 ~ 2026-06-14

### 📈 新增 (89)

**🆕 高质量新增 (21 条)**

- [AI工程的新范式：从单次调用到循环思维](https://x.com/sairahul1/status/2064343621130932644) — agents ⭐⭐⭐⭐
- [Trace即Evals：Agent迭代的量化闭环](https://x.com/BohuTANG/status/2064540808951574947) — agents ⭐⭐⭐⭐
- [Vision Banana：视觉领域的生成即理解革命](https://x.com/grapeot/status/2064115254213370288) — models ⭐⭐⭐⭐
- [华为的Tau Scaling Law：半导体范式转移](https://x.com/BetterCallMedhi/status/2059384524950384942) — infra ⭐⭐⭐⭐
- [Accelerating science with GPT-5](https://openai.com/index/accelerating-science-gpt-5) — models ⭐⭐⭐
- [Coding agents in the social sciences](https://www.anthropic.com/research/coding-agents-social-sciences) — agents ⭐⭐⭐
- [DeepSeek 的 10 万亿美元大战略](https://baoyu.io/blog/2026-05-23/bookwormengr-status-2057909493250539891) — uncategorized ⭐⭐⭐
- [DiffusionGemma: 4x faster text generation](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation) — uncategorized ⭐⭐⭐
- [Evaluating chain-of-thought monitorability](https://openai.com/index/evaluating-chain-of-thought-monitorability) — infra ⭐⭐⭐
- [I/O 2026: Welcome to the agentic Gemini era](https://blog.google/innovation-and-ai/technology/ai/io-2026-welcome-to-the-agentic-gemini-era) — models ⭐⭐⭐
- [Introducing Aardvark](https://openai.com/index/introducing-aardvark) — uncategorized ⭐⭐⭐
- [Introducing GPT-Rosalind](https://openai.com/index/introducing-gpt-rosalind) — models ⭐⭐⭐
- [Introducing IndQA](https://openai.com/index/introducing-indqa) — uncategorized ⭐⭐⭐
- [Latest GPT-5 Model Breakthrough](https://openai.com/blog/gpt-5-breakthrough-2026) — models ⭐⭐⭐
- [Making Claude a chemist](https://www.anthropic.com/research/making-claude-a-chemist) — models ⭐⭐⭐
- [MiMo Code is now released and open-source](https://mimo.xiaomi.com/mimocode) — uncategorized ⭐⭐⭐
- [Open Reproduction of DeepSeek-R1](https://github.com/huggingface/open-r1) — industry ⭐⭐⭐
- [Paving the way for agents in biology](https://www.anthropic.com/research/agents-in-biology) — agents ⭐⭐⭐
- [Test AI Content](https://openai.com/blog/test-2026) — learning ⭐⭐⭐
- [What we learned mapping a year's worth of AI-enabled cyber threats](https://www.anthropic.com/research/AI-enabled-cyber-threats-mitre-attack) — uncategorized ⭐⭐⭐
- [来自 Codex 官方团队的分享：如何把 Codex 用到极致](https://baoyu.io/blog/2026-05-20/jxnlco-2057153744630890620) — coding ⭐⭐⭐

**⚠️ Synthetic URL 条目 (38 条，疑似采集噪声)**

- [高效注意力机制研究：@yudapeathree](https://x.com/yudapeathree/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [高效注意力机制研究：@karpathy](https://x.com/karpathy/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [高效注意力机制研究：@hardmaru](https://x.com/hardmaru/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [高效注意力机制研究：@fchollet](https://x.com/fchollet/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [高效注意力机制研究：@jeremyphoward](https://x.com/jeremyphoward/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [高效注意力机制研究：@gdb](https://x.com/gdb/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [高效注意力机制研究：@AndrewYNg](https://x.com/AndrewYNg/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [高效注意力机制研究：@ylecun](https://x.com/ylecun/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [高效注意力机制研究：@christoschristofi](https://x.com/christoschristofi/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [高效注意力机制研究：@pmdd22](https://x.com/pmdd22/status/20260609180351_002) — uncategorized ⭐⭐⭐⭐⭐
- [@yudapeathree 发布LLM注意力机制优化研究](https://x.com/yudapeathree/status/20260610180248_002) — uncategorized ⭐⭐⭐⭐⭐
- [@karpathy 发布LLM注意力机制优化研究](https://x.com/karpathy/status/20260610180248_002) — uncategorized ⭐⭐⭐⭐⭐
- [@hardmaru 发布LLM注意力机制优化研究](https://x.com/hardmaru/status/20260610180248_002) — uncategorized ⭐⭐⭐⭐⭐
- [@fchollet 发布LLM注意力机制优化研究](https://x.com/fchollet/status/20260610180248_002) — uncategorized ⭐⭐⭐⭐⭐
- [@jeremyphoward 发布LLM注意力机制优化研究](https://x.com/jeremyphoward/status/20260610180248_002) — uncategorized ⭐⭐⭐⭐⭐
- [@gdb 发布LLM注意力机制优化研究](https://x.com/gdb/status/20260610180248_002) — uncategorized ⭐⭐⭐⭐⭐
- [@AndrewYNg 发布LLM注意力机制优化研究](https://x.com/AndrewYNg/status/20260610180248_002) — uncategorized ⭐⭐⭐⭐⭐
- [@ylecun 发布LLM注意力机制优化研究](https://x.com/ylecun/status/20260610180248_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@yudapeathree 发布 LLM 高效注意力机制研究](https://x.com/yudapeathree/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@karpathy 发布 LLM 高效注意力机制研究](https://x.com/karpathy/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@hardmaru 发布 LLM 高效注意力机制研究](https://x.com/hardmaru/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@fchollet 发布 LLM 高效注意力机制研究](https://x.com/fchollet/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@jeremyphoward 发布 LLM 高效注意力机制研究](https://x.com/jeremyphoward/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@gdb 发布 LLM 高效注意力机制研究](https://x.com/gdb/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@AndrewYNg 发布 LLM 高效注意力机制研究](https://x.com/AndrewYNg/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@ylecun 发布 LLM 高效注意力机制研究](https://x.com/ylecun/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@yudapeathree - 高效注意力机制研究](https://x.com/yudapeathree/status/20260612180331_002) — uncategorized ⭐⭐⭐⭐
- [@karpathy - 高效注意力机制研究](https://x.com/karpathy/status/20260612180331_002) — uncategorized ⭐⭐⭐⭐
- [@hardmaru - 高效注意力机制研究](https://x.com/hardmaru/status/20260612180331_002) — uncategorized ⭐⭐⭐⭐
- [@fchollet - 高效注意力机制研究](https://x.com/fchollet/status/20260612180331_002) — uncategorized ⭐⭐⭐⭐
- [@jeremyphoward - 高效注意力机制研究](https://x.com/jeremyphoward/status/20260612180331_002) — uncategorized ⭐⭐⭐⭐
- [@gdb - 高效注意力机制研究](https://x.com/gdb/status/20260612180331_002) — uncategorized ⭐⭐⭐⭐
- [@AndrewYNg - 高效注意力机制研究](https://x.com/AndrewYNg/status/20260612180331_002) — uncategorized ⭐⭐⭐⭐
- [高效注意力机制优化LLM计算效率](https://x.com/yudapeathree/status/20260613180222_002) — uncategorized ⭐⭐⭐⭐
- [Andrej Karpathy分享LLM注意力优化技术](https://x.com/karpathy/status/20260613180222_002) — uncategorized ⭐⭐⭐⭐
- [深度学习专家发布高效注意力算法研究](https://x.com/hardmaru/status/20260613180222_002) — uncategorized ⭐⭐⭐⭐
- [Keras发布LLM注意力机制优化工具](https://x.com/fchollet/status/20260613180222_002) — uncategorized ⭐⭐⭐⭐
- [Fast.ai团队发布LLM高效注意力方案](https://x.com/jeremyphoward/status/20260613180222_002) — uncategorized ⭐⭐⭐⭐

**📝 无链接条目 (30 条，待人工补全)**

- 2026-06-09 AI 代码生成与评测基准 — coding ⭐⭐⭐⭐⭐
- a09cdbbd — industry ⭐⭐⭐⭐
- a2a_protocol_v1_0_2026_001 — agents ⭐⭐⭐⭐
- claude_opus_47_mythos_2026_001 — models ⭐⭐⭐⭐
- gpt55_release_2026_001 — models ⭐⭐⭐⭐
- AI资源 - 2026-04-02 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-04 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-06 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-08 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-09 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-10 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-12 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-14 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-19 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-20 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-21 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-22 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-23 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-24 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-25 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-26 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-27 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-28 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-29 — uncategorized ⭐⭐⭐
- AI资源 - 2026-04-30 — uncategorized ⭐⭐⭐
- …还有 5 条

### 📦 归档 (0)


### ✏️ 评分调整 (0)


### 📊 统计
- 总条目: 733 → 822 (+89)
- 活跃条目: 577 → 628 (+51)

### 📈 分类变更分布
| 分类 | 新增 |
|------|------|
| uncategorized | +65 |
| models | +8 |
| agents | +5 |
| learning | +3 |
| infra | +3 |
| industry | +3 |
| coding | +2 |

### 🏆 本周最高分新增 (5★)
- 2026-06-09 AI 代码生成与评测基准 — coding ⭐⭐⭐⭐⭐
- [@@AndrewYNg 发布 LLM 高效注意力机制研究](https://x.com/AndrewYNg/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@fchollet 发布 LLM 高效注意力机制研究](https://x.com/fchollet/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@gdb 发布 LLM 高效注意力机制研究](https://x.com/gdb/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
- [@@hardmaru 发布 LLM 高效注意力机制研究](https://x.com/hardmaru/status/20260611180217_002) — uncategorized ⭐⭐⭐⭐⭐
