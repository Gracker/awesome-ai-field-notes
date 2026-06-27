# Previewing GPT-5.6 Sol: a next-generation model

- **ID**: adbd50c1
- **原文链接**: https://openai.com/index/previewing-gpt-5-6-sol
- **作者**: OpenAI
- **日期**: 2026-06-26
- **分类**: models
- **标签**: models, openai, gpt-5.6, sol, release, preview
- **质量评分**: 5/5
- **抓取时间**: 2026-06-27T12:25:00

---

## 中文翻译

OpenAI 于 2026 年 6 月 26 日宣布启动 GPT‑5.6 系列的限量预览，发布三款新模型：旗舰型号 **Sol**、面向日常工作的均衡型 **Terra**，以及高速低成本版 **Luna**。其中 Terra 性能可与 GPT‑5.5 抗衡但成本只有一半，Luna 则在保持强大能力的同时给出了 OpenAI 史上最低的价格。

GPT‑5.6 Sol 搭载了迄今最完善的安全防护栈，针对高风险活动、敏感网络请求以及重复性滥用行为进行了加固，并花费数周时间寻找薄弱环节、加固系统以应对真实世界的攻击。

OpenAI 强调对广泛可访问性的承诺，并计划在未来几周内向所有用户开放 GPT‑5.6 Sol、Terra 与 Luna。作为与美国政府持续合作的一部分，OpenAI 在发布前向政府展示了计划与模型能力。应政府要求，OpenAI 首先向一组经过筛选的可信合作伙伴开放限量预览——其参与情况已与政府共享，随后才会面向更广泛用户发布。OpenAI 表示，长期来看这种政府预审机制不应成为默认做法，但在当前阶段这是兼顾网络空间安全行政令框架落地与未来模型发布流程的最稳妥路径。

### 模型能力

GPT‑5.6 Sol 是迄今最强的模型。OpenAI 公布了在编程、生物学、网络安全等领域提升的智能体能力评测结果，并将在系统卡中提供更多细节。

GPT‑5.6 引入了新的 `max` 推理强度档位，让 Sol 能够获得最充分的思考时间。同时新增了 `ultra` 模式，通过调用子智能体（subagent）来突破单一 Agent 的能力上限，从而加速复杂工作流。

在编程工作流方面，GPT‑5.6 Sol 在 **Terminal‑Bench 2.1**（考验命令行规划、迭代与工具协作能力）上创下新的 SOTA。

GPT‑5.6 Sol 在生物学工作流上同样有大幅进步。在 **GeneBench v1**（长链路基因组学与定量生物学分析评测）中，Sol 用更少的 Token 取得了比 GPT‑5.5 更强的结果。

GPT‑5.6 Sol 是 OpenAI 迄今在网络安全方面最强的模型，重新定义了长链路安全任务（漏洞研究与漏洞利用）的性能-效率前沿。在 **ExploitBench** 上，Sol 仅用约 1/3 的输出 Token 即取得与 Mythos Preview 相媲美的成绩。在由 UC Berkeley 与 OpenAI 等前沿实验室合作提出的 **ExploitGym** 基准上，Sol、Terra、Luna 三款模型在提高推理强度时均表现出网络能力的明显提升。

### 更强的网络能力，更严密的安全护栏

OpenAI 在 GPT‑5.6 Sol/Terra/Luna 上部署了迄今最严密的护栏，并按模型能力匹配相应的防护配置。当模型能力变强，护栏被设计为既能扛住真实对抗压力，又能为合法的代码评审、漏洞研究、补丁开发、调试、安全教育和防御测试等保留使用通道。

GPT‑5.6 Sol 在"帮助人类发现和修复漏洞"方面明显优于"独立完成端到端攻击"。OpenAI 的目标是让这些能力优先到达防御者手中，他们能用它发现薄弱环节、开发补丁并增强整体系统。

GPT‑5.6 Sol 在 OpenAI 的 Preparedness Framework 下尚未跨越"网络关键（Cyber Critical）"门槛。在涉及 Chromium 与 Firefox 的评测中，模型能识别 Bug 与漏洞利用原语（exploitation primitive）——漏洞利用链的构成模块——但在被测条件下未能自主产出可运行的全链利用（full-chain exploit）。尽管如此，OpenAI 仍以"更强的能力 + 更严的护栏 + 分阶段发布"的组合来应对模型能力跃迁带来的不确定性。

### 分层防护体系

没有任何单一护栏能应对持续的对抗性滥用。GPT‑5.6 预览版采用了分层防护，包括模型内置的训练拒绝、生成期间的实时检查、账号层级信号、差异化访问、监测、执行与持续测试。

GPT‑5.6 在训练中被要求拒绝受禁止的网络安全协助请求，包括用户试图伪装意图或越狱的情况。模型层级护栏界定了"模型应不应帮"的第一道边界。

实时网络安全与生物滥用分类器在生成过程中评估输出，提供第二层防护。在高风险场景下，如果检测到潜在违规，生成会暂停，由更大的推理模型审查对话及其上下文；若被判定为不允许的内容，将在到达用户前被拦截。

被标记的活动还会触发账号层级复审，结合相关内容保留与复审策略，对跨对话的风险信号进行评估。这有助于区分持续恶意行为与合法的双重用途安全工作。

### 通过自动化红队提升稳健性

OpenAI 比以往任何时候都投入了更多的智能与算力来保障安全，使用自家模型更快发现薄弱环节并强化护栏。OpenAI 投入了超过 70 万 A100 等效 GPU 小时进行自动化红队测试，专注于寻找通用型越狱（universal jailbreak）——可在多种提示或上下文下生效的攻击，而不是单一狭窄场景下的攻击。

除自动化红队外，OpenAI 还与第三方测试人员合作开展广泛的人工专家红队测试，并在预览期间继续进行。

### 可用性与定价

在预览期间，GPT‑5.6 模型将首先通过 API 与 Codex 向选定可信合作伙伴和组织开放，并计划很快在 ChatGPT、Codex 与 API 中更广泛地开放。

在新命名体系下，数字标识模型的代际，Sol、Terra、Luna 标识持续演进的能力档位。三款模型组合为用户与开发者提供了在智能、速度与成本之间更清晰的选择。

GPT‑5.6 三档按每 100 万 Token 计价：Sol 输入 5 美元/输出 30 美元；Terra 输入 2.5 美元/输出 15 美元；Luna 输入 1 美元/输出 6 美元。GPT‑5.6 还引入了更可预测的提示词缓存，支持显式缓存断点与最短 30 分钟缓存寿命。对于 GPT‑5.6 及之后的模型，缓存写入按未缓存输入价的 1.25 倍计费，缓存读取仍享 90% 的折扣。

OpenAI 还将于 7 月在 Cerebras 上以最高每秒 750 Token 的速度推出 GPT‑5.6 Sol，为客户带来前所未有的速度的前沿智能。访问初期将面向选定客户开放，随后扩展容量。

*来源：OpenAI 官方公告 2026 年 6 月 26 日*

## English Original

We're beginning a limited preview of the GPT‑5.6 series: Sol, our flagship model; Terra, a balanced model for everyday work; and Luna, a fast and affordable model. Terra has competitive performance to GPT‑5.5 while being 2x cheaper and Luna brings strong capability at our lowest cost.

GPT‑5.6 Sol launches with our most robust safety stack to date. We strengthened protections for higher-risk activity, sensitive cyber requests, and repeated misuse, and spent multiple weeks finding weaknesses, pressure-testing our system, and hardening it against real-world attacks.

We believe in broad access, and we plan to make GPT‑5.6 Sol, Terra, and Luna generally available in the coming weeks. As part of our ongoing engagement with the U.S. government, we previewed our plans and the models' capabilities ahead of today's launch. At their request, we are starting with a limited preview for a small group of trusted partners whose participation has been shared with the government, before releasing more broadly.

GPT‑5.6 Sol is our strongest model yet. With GPT‑5.6, we're introducing a new `max` reasoning effort to give Sol the most time to reason deeply. Additionally, we're introducing a new `ultra` mode that goes beyond the capabilities of a single agent by leveraging subagents to accelerate complex work.

For coding workflows, GPT‑5.6 Sol sets a new state of the art on **Terminal‑Bench 2.1**, which tests command-line workflows requiring planning, iteration, and tool coordination.

GPT‑5.6 Sol also shows broad improvements in biology workflows. On **GeneBench v1**, it achieves stronger results than GPT‑5.5 while using fewer tokens.

GPT‑5.6 Sol is our most capable model yet for cybersecurity. On **ExploitBench**, GPT‑5.6 Sol is competitive with Mythos Preview using only ~1/3 of the output tokens. On **ExploitGym**, GPT‑5.6 Sol, Terra, and Luna all demonstrate strong improvements in cyber capabilities as we increase reasoning.

GPT‑5.6 is priced per 1M tokens: Sol $5 input / $30 output; Terra $2.50 / $15; Luna $1 / $6. We're also launching GPT‑5.6 Sol on Cerebras at up to 750 tokens per second in July.
