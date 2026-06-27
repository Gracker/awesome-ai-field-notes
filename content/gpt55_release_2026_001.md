# 重磅发布 GPT-5.5：OpenAI 迄今最智能的模型，专为实际工作打造

- **ID**: gpt55_release_2026_001
- **原文链接**: https://openai.com/index/introducing-gpt-5-5 （页面已自动重定向至 https://openai.com/zh-Hans-CN/index/introducing-gpt-5-5/ 中文版本）
- **作者**: OpenAI
- **日期**: 2026-04-23
- **分类**: models
- **标签**: GPT-5.5, OpenAI, coding, research, data-analysis, agentic, 2026
- **质量评分**: 5/5
- **抓取时间**: 2026-06-27T20:40:00

---

## 中文翻译

> 注：原页面在中文网络环境下会自动重定向到 OpenAI 的官方中文版本，因此下面的中文翻译与原文一致，整理为可读性更强的格式。

### 概览

我们正式发布 **GPT-5.5**。作为我们迄今最智能、交互体验最直观的模型，它标志着人类迈向全新计算机办公模式的关键一步。

GPT-5.5 能够更快速地洞察用户意向，并独立承担更多实质性工作。无论是编写与调试代码、开展在线调研、分析复杂数据，还是撰写文档、制作表格，乃至跨软件操作，它都能游刃有余地衔接各个工具，直至任务圆满完成。以往你需要步步为营地引导 AI，而现在，你只需将一个繁杂的多阶段任务交给 GPT-5.5。它具备极强的自主性，能够自行制定计划、调用工具、核查结果并在模糊的边界中寻找最优路径，始终保持高效推进。

在**智能体编程、计算机使用、知识型工作以及前沿科学研究**等领域，GPT-5.5 的提升尤为显著。这些领域往往要求模型具备跨语境推理及长周期的行动能力。令人惊叹的是，GPT-5.5 在实现智能跃迁的同时，并未牺牲响应速度。通常情况下，模型体量越大速度越慢，但 GPT-5.5 在真实应用环境中的单 Token 延迟与 GPT-5.4 持平，智能水平却大幅领先。此外，在处理相同的 Codex 任务时，其消耗的 Token 显著减少，真正实现了更高能、更经济。

伴随 GPT-5.5 一同发布的，还有我们迄今为止最完善的安全防护方案。这套体系旨在打击滥用行为，同时确保合法、有益的工作流程不受干扰。在正式发布前，我们不仅通过了全套安全与准备框架评估，还联合内外红队专家，针对高级网络安全和生物技术领域进行了专项测试。此外，我们还从近 200 家值得信赖的合作伙伴处收集了大量真实应用场景的反馈，确保模型在复杂实战中的安全性与可靠性。

即日起，GPT-5.5 将陆续面向 ChatGPT 及 Codex 的 Plus、Pro、Business 和 Enterprise 用户开放。同时，GPT-5.5 Pro 也将同步推送给 Pro、Business 和 Enterprise 的订阅用户。由于 API 部署涉及不同的防护策略，我们正与合作伙伴及客户紧密协作，确保在大规模服务下的安全性。GPT-5.5 与 GPT-5.5 Pro 的 API 服务将于近期正式上线。

### 核心基准对比

下表展示了 GPT-5.5 与竞品前沿模型在主要基准测试上的表现（粗体为最高分）：

| 评估 | GPT-5.5 | GPT-5.4 | GPT-5.5 Pro | GPT-5.4 Pro | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- | --- | --- |
| Terminal-Bench 2.0 | **82.7%** | 75.1% | – | – | 69.4% | 68.5% |
| Expert-SWE（内部） | **73.1%** | 68.5% | – | – | – | – |
| GDPval（胜出或平局） | **84.9%** | 83.0% | 82.3% | 82.0% | 80.3% | 67.3% |
| OSWorld-Verified | **78.7%** | 75.0% | – | – | 78.0% | – |
| Toolathlon | **55.6%** | 54.6% | – | – | – | 48.8% |
| BrowseComp | 84.4% | 82.7% | **90.1%** | 89.3% | 79.3% | 85.9% |
| FrontierMath Tier 1–3 | 51.7% | 47.6% | **52.4%** | 50.0% | 43.8% | 36.9% |
| FrontierMath Tier 4 | 35.4% | 27.1% | **39.6%** | 38.0% | 22.9% | 16.7% |
| CyberGym | **81.8%** | 79.0% | – | – | 73.1% | – |

### 模型能力

OpenAI 正在致力于打造全球性的智能体 AI 基础设施，旨在让全球用户与企业都能真正通过 AI 交付工作成果。在过去的一年里，我们见证了 AI 对软件工程效率的巨大拉动；而随着 GPT-5.5 接入 Codex 与 ChatGPT，这种变革正进一步延伸至科学研究及更广泛的计算机办公领域。

在这些领域中，GPT-5.5 的进化不仅体现在更深层次的智能，更在于其解决问题的高效性。它通常能以更少的 Token 消耗和更低的重试频率，交付更高质量的产出。在 Artificial Analysis 的 Coding Agent Index 中，GPT-5.5 以竞品前沿编程模型一半的成本，实现了行业领先的智能表现。

#### 智能体编程

GPT-5.5 是我们迄今最强大的智能体编程模型。在 **Terminal-Bench 2.0** 测试中，面对需要缜密规划、反复迭代及多工具协作的复杂命令行工作流，GPT-5.5 取得了 82.7% 的顶尖准确率。在衡量解决真实 GitHub 议题能力的 **SWE-Bench Pro** 评估中，其得分达到 58.6%，相比以往模型，它能在单次尝试中端到端地解决更多任务。而在针对长周期编程任务（人类中位完成时间约为 20 小时）的内部前沿评估 **Expert-SWE** 中，GPT-5.5 的表现同样超越了 GPT-5.4。

在上述三项评估中，GPT-5.5 不仅全面刷新了 GPT-5.4 的成绩，且 Token 使用量更少。

GPT-5.5 的编程能力优势在 Codex 中得到明显体现。从代码实现、重构到调试、测试及验证，它都能全方位接管工程任务。早期测试表明，GPT-5.5 更加契合真实工程环境下的行为模式：它能精准把握大型系统的上下文，在面对含义模糊的报错时进行深入推理，并主动通过工具验证假设，确保修改后的代码能适配整个库的既有逻辑。

> "这是我用过的第一个在概念理解上具有极高清晰度的编程模型。"  
> —— **Dan Shipper**，Every 创始人兼 CEO

> "它真的让我感觉是在与更高阶的智能协同工作，甚至产生了一种由衷的敬畏感。"  
> —— **Pietro Schirano**，MagicPath CEO

> "失去对 GPT-5.5 的访问权限，感觉就像被截肢了一样。"  
> —— **NVIDIA 工程师**（提前试用反馈）

> "相比 GPT-5.4，GPT-5.5 在智能程度和执行韧性上有显著提升，拥有更强大的编程表现以及更可靠的工具调用能力。它在处理任务时能保持更长时间的专注，而不会过早中断，这对于我们的用户交付给 Cursor 的那些复杂且长周期的工作任务至关重要。"  
> —— **Michael Truell**，Cursor 联合创始人兼 CEO

#### 知识型工作

这些让 GPT-5.5 在编程领域大放异彩的优势，同样使其成为日常办公的强大助力。由于模型能更敏锐地捕捉用户意向，它在处理知识型工作时显得更加自然流畅：从搜集资料、提炼核心价值，到调用工具、核查产出，并最终将零散的素材转化为实用成果，整个链路一气呵成。

在 Codex 环境下，GPT-5.5 制作文档、表格及演示文稿的能力较 GPT-5.4 有了显著提升。Alpha 测试者反馈，在运筹研究、电子表格建模以及将凌乱的业务需求转化为执行计划等任务中，它的表现远超以往模型。结合 Codex 的计算机使用（computer use）能力，GPT-5.5 带来了前所未有的"人机协作感"：它能实时理解屏幕内容，精准进行点击、录入和界面导航，并熟练地在不同工具间跨越操作。

目前，OpenAI 内部团队已率先将这些优势应用到真实的业务流中。如今，公司内超过 85% 的员工每周都会使用 Codex，涵盖软件工程、财务、传播、市场营销、数据科学和产品管理等多个职能领域。公关团队利用 Codex 中的 GPT-5.5 分析了过去六个月的演讲请求数据，建立了一套评分与风险预警框架，并以此验证了一款自动化 Slack 智能体。该智能体能够自动处理低风险请求，而将高风险项转交人工审核。财务团队借助 Codex 处理了 24,771 份 K-1 税务报表，共计 71,637 页。市场拓展团队的一名员工实现了周报生成的自动化，每周节省了 5 到 10 小时。

> "GPT-5.5 展现出了支撑重度执行类任务所需的持续性能。得益于在 NVIDIA GB200 NVL72 系统上的构建与部署，该模型让我们的团队仅凭自然语言提示词就能交付端到端的功能，将调试周期从几天缩短至数小时。"  
> —— **Justin Boitano**，NVIDIA 企业级 AI 副总裁

#### 科学研究

GPT-5.5 在科学和技术研究工作流中同样展现出显著优势。科研工作并非简单的问答，而是一个探索构思、搜集证据、验证假设、解读结果并决策下一步行动的完整循环。GPT-5.5 在这一循环中的表现比以往任何模型都更加稳健持久。

在 **GeneBench** 测试中，GPT-5.5 较 GPT-5.4 有了跨越式的提升。这是一项专注于遗传学和定量生物学多阶段科学数据分析的新型评估。在 BixBench 测试中，GPT-5.5 在所有已公布评分的模型中名列前茅。

在另一个案例中，一个搭载自定义框架的 GPT-5.5 内部版本协助发现了关于**拉姆齐数 (Ramsey numbers)** 的全新证明。拉姆齐数是组合数学的核心研究对象之一。GPT-5.5 发现了一个关于非对角拉姆齐数长期存在的渐近事实证明，随后该证明在 Lean 形式化证明语言中得到了验证。该成果是一个具体的范例，表明 GPT-5.5 不仅仅能提供代码或解释，更能为研究领域贡献出令人惊喜且极具价值的数学论证。

> "能在我们的系统框架中调用 OpenAI 全新的 GPT-5.5 模型，看到它在海量生化数据集上通过推理预测人体药物成效，并在我们最难的药物研发评估中实现准确率的显著飞跃，这真的非常振奋。如果 OpenAI 保持这种惊人的迭代速度，到今年年底，药物发现的基础格局将彻底改变。"  
> —— **Brandon White**，Axiom Bio 联合创始人兼 CEO

### 新一代推理效率

为了在维持 GPT-5.4 延迟水平的前提下提供 GPT-5.5 的强大性能，我们必须将推理视为一个完整的集成系统进行重新思考，而非单纯的局部优化。GPT-5.5 适配了 NVIDIA GB200 及 GB300 NVL72 系统，从联合设计、模型训练到在线服务均基于此。Codex 与 GPT-5.5 对实现性能目标起到了决定性作用。GPT-5.5 甚至亲自参与了系统底层栈的改进与实现。简而言之，模型亲自优化了运行它自身的底层基础设施。

其中一项关键改进体现在负载均衡与分区启发式算法。在 GPT-5.5 发布前，为了平衡计算核心的工作量并确保不同规模的请求能在同一 GPU 上运行，我们将加速器上的请求拆分为固定数量的区块。Codex 分析了数周的生产环境流量模式，并编写了定制的启发式算法，实现了任务的最优分区与平衡。这项工作产生了远超预期的影响，将 **Token 生成速度提升了 20% 以上**。

### 提升网络防御能力，守护全民安全

前沿模型在网络安全领域的实力正日益增强。在 GPT-5.5 中我们引入了更严苛的风险分类器。通过 **网络安全受信访问 (Trusted Access for Cyber)** 计划，我们正率先在 Codex 中提供"网络安全放行版"模型。这意味着在发布之初，符合特定信任信号的认证用户即可在更少限制的情况下，调用 GPT-5.5 强大的网络安全能力。

我们根据准备框架，将 GPT-5.5 的生物/化学及网络安全能力评定为"高"等级。尽管 GPT-5.5 尚未达到"极高"的网络安全能力水平，但评估显示，其防御实战能力较 GPT-5.4 已有显著跨越。

### 可用性与定价

即日起，GPT-5.5 将全面登陆 ChatGPT、Codex 及 API 平台，并同步面向 Microsoft Foundry 的开发者开放。

在 ChatGPT 中，Plus、Pro、Business 和 Enterprise 用户均可使用 GPT-5.5 Thinking。专为应对极端复杂问题、追求极高准确率而设计的 GPT-5.5 Pro，则面向 Pro、Business 及 Enterprise 用户开放。

在 Codex 中，GPT-5.5 已支持 Plus、Pro、Business、Enterprise、Edu 及 Go 套餐，并提供 400K 上下文窗口。此外，Codex 还推出了快速模式，能以 1.5 倍的生成速度响应请求（费用为标准模式的 2.5 倍）。

面向 API 开发者，gpt-5.5 即将接入 Responses 及 Chat Completions API。其定价为：
- **gpt-5.5**：每百万输入 Token 5 美元，每百万输出 Token 30 美元，支持高达 1M 的上下文窗口
- **gpt-5.5-pro**：每百万输入 Token 30 美元，每百万输出 Token 180 美元

尽管 GPT-5.5 的定价高于 GPT-5.4，但它在实现智能跃迁的同时，Token 利用效率也大幅提升。在 Codex 中，我们经过精心调优，确保 GPT-5.5 在大多数场景下能以更少的 Token 交付优于 GPT-5.4 的结果。

*来源：OpenAI, 2026-04-23*

## English Original

> Note: The page auto-redirected to OpenAI's official Simplified Chinese version during fetch; the content above is already in Chinese. The English summary from the official English version is preserved below for reference.

**GPT-5.5 is the smartest model we've ever shipped** — better at understanding user intent, more autonomous, and more efficient with tokens. It's now rolling out to ChatGPT and Codex Plus/Pro/Business/Enterprise users. GPT-5.5 Pro is available to Pro/Business/Enterprise. API access is coming soon.

Key benchmark highlights (vs GPT-5.4, Claude Opus 4.7, Gemini 3.1 Pro):

- **Terminal-Bench 2.0: 82.7%** (vs 75.1% GPT-5.4, 69.4% Opus 4.7)
- **SWE-Bench Pro: 58.6%** (long-horizon coding tasks)
- **GDPval: 84.9%** (knowledge work across 44 occupations)
- **OSWorld-Verified: 78.7%** (computer use)
- **CyberGym: 81.8%** (cybersecurity)
- **Tau2-bench Telecom: 98.0%** (no prompt tuning)

Three pillars of the release:

1. **Agentic coding** — best-ever on Terminal-Bench 2.0, SWE-Bench Pro, and Expert-SWE; matches Opus 4.7 on cursor/CursorBench.
2. **Knowledge work** — meaningful gains on OfficeQA Pro, FinanceAgent v1.1, internal IB modeling tasks.
3. **Scientific research** — strong gains on GeneBench (25.0% vs 19.0% GPT-5.4) and BixBench. Contributed a new asymptotic proof related to Ramsey numbers, verified in Lean.

Co-designed with **NVIDIA GB200/GB300 NVL72** systems, GPT-5.5 maintains the same per-token latency as GPT-5.4 while delivering significantly higher intelligence. Codex-assisted load-balancing heuristics improved token generation throughput by **>20%**.

Pricing: gpt-5.5 at **$5/$30 per million input/output tokens** (1M context); gpt-5.5-pro at **$30/$180 per million tokens**.

*Source: OpenAI, April 23, 2026*
