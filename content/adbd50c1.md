# Previewing GPT-5.6 Sol: a next-generation model

- **ID**: `adbd50c1`
- **Author**: OpenAI
- **Source URL**: https://openai.com/index/previewing-gpt-5-6-sol
- **Original Date**: 2026-07-03 (Wayback Machine snapshot)
- **Category**: models
- **Quality Score**: 5/5
- **Status**: active
- **Fetched**: 2026-07-08T12:19+08:00
- **Language**: en (with curated Chinese summary in entries.json)

> Source: <https://openai.com/index/previewing-gpt-5-6-sol>
> openai.com returned HTTP 403 on direct curl / Googlebot UA. Successfully retrieved
> via the Wayback Machine snapshot
> <http://web.archive.org/web/20260703233822/https://openai.com/index/previewing-gpt-5-6-sol/>
> (HTTP 200, 674,758 bytes, 2026-07-03 23:38:22 UTC).

---

## English

Sol is our strongest model yet. To give a preview of model performance, we share a set of evaluations highlighting improved agentic capabilities in coding, biology, and cybersecurity, with additional safety and preparedness evaluations available in our
system card
⁠
(opens in a new window)
. We will share an expanded suite of evaluation results when we make the model broadly available.
With GPT‑5.6, we’re introducing a new
max
reasoning effort to give Sol the most time to reason deeply. Additionally, we’re introducing a new
ultra
mode that goes beyond the capabilities of a single agent by leveraging subagents to accelerate complex work.
For coding workflows, GPT‑5.6 Sol sets a new state of the art on
Terminal‑Bench 2.1
, which tests command-line workflows requiring planning, iteration, and tool coordination.
GPT‑5.6 Sol also shows broad improvements in biology workflows. On
GeneBench v1
, which evaluates long-horizon genomics and quantitative-biology analyses, it achieves stronger results than GPT‑5.5 while using fewer tokens.
GPT‑5.6 Sol is our most capable model yet for cybersecurity. It shifts the performance-efficiency frontier for long-horizon security tasks including vulnerability research and exploitation. On
ExploitBench
², GPT‑5.6 Sol is competitive with Mythos Preview using only ~1/3 of the output tokens. On
ExploitGym
⁠
(opens in a new window)
3
, a benchmark created by UC Berkeley researchers in collaboration with OpenAI and other frontier labs, GPT‑5.6 Sol, Terra, and Luna models all demonstrate strong improvements in cyber capabilities as we increase reasoning.
Stronger cyber capabilities with stronger safeguards
We developed GPT‑5.6 Sol, Terra and Luna with our most robust safeguards to date, with configurations matched to each model’s capabilities. As the model becomes more capable, we design safeguards to increasingly hold up to real-world adversarial pressure while preserving access to legitimate work such as code review, vulnerability research, patch development, debugging, security education, and defensive testing. Our goal is to make prohibited offensive activity more difficult, uncertain, and detectable without unnecessarily limiting those beneficial uses. Based on our assessment of the model and safeguards, we expect substantial benefit for legitimate defensive work, while meaningfully constraining prohibited offensive use.
GPT‑5.6 Sol is better at helping people find and fix vulnerabilities than reliably carrying out end-to-end attacks. As these capabilities continue to advance, our priority is to make sure they reach and benefit defenders, who can use these tools to find weaknesses, develop patches, and strengthen systems more broadly.
GPT‑5.6 Sol does not cross the Cyber Critical threshold under our
Preparedness Framework
⁠
. In evaluations involving Chromium and Firefox, it identified bugs and exploitation primitives—the building blocks of an exploit—but did not autonomously produce a functional full-chain exploit under the conditions tested. Still, benchmark thresholds cannot capture every way a model may be used or combined with other tools. That uncertainty, along with the model’s broader step change in capabilities, is why we are pairing the model’s increased capabilities with stronger safeguards and a phased release. We share more details about our safeguards in the
GPT‑5.6 Preview system card
⁠
(opens in a new window)
.
A layered safeguard stack
No single safeguard is sufficient against determined or adaptive misuse. Across the GPT‑5.6 preview, we use layered safeguards, with exact configurations varying across models, and pressure-test them for real-world attacks. These include protections trained into the model, real-time checks during generation, account-level signals, differentiated access, monitoring, enforcement, and continued testing.
GPT‑5.6 is trained to refuse prohibited cyber assistance, including when users attempt to disguise their intent or jailbreak the model. These model-level safeguards establish the first boundary around what the model should and should not help with.
Real-time cyber and biology misuse classifiers provide another layer by evaluating output as it is generated. For higher risk cases, if they detect a potential violation, the generation may be paused while a larger reasoning model reviews the conversation and its context. If the output is assessed as disallowed, it is withheld before it reaches the user.
Flagged activity can also trigger account-level review across relevant conversations and risk signals, consistent with our terms and policies around content retention and review. Looking beyond a single conversation helps our systems distinguish persistent malicious behavior from legitimate dual-use security work, where similar technical concepts may appear in very different contexts.
Together, these layers make the overall approach more robust than any one safeguard on its own. Model behavior reduces the likelihood of harmful responses, real-time systems can intervene during generation, account-level review can identify broader patterns, and differentiated access preserves important defensive work without making the most sensitive capabilities broadly available by default.
Especially during the preview, users may encounter safeguards that block or refuse some requests. Other requests may take longer because generation is paused for additional review. Safeguards may occasionally intervene on legitimate work, particularly in dual-use areas where defensive and offensive activity can initially look similar.
That is part of what the preview is designed to test. We want to understand not only whether the safeguards constrain misuse, but whether legitimate users can still complete normal work reliably and efficiently. Feedback during the preview will help us reduce unnecessary blocks and delays, improve how the safeguards interpret context, and create a smoother experience before wider release.
We are also working with enterprise customers on longer-term approaches—including privacy-preserving detection, customer-operated safety controls, and access calibrated to the risk of a customer, user, or workload—to advance safety while supporting enterprise privacy requirements.
Improving robustness with automated red-teaming
Safeguards also need to remain effective when attackers adapt their tactics. A protection that works only on a fixed set of known attacks is not robust enough for a frontier model.
That’s why we are applying more intelligence and compute than ever before to safety, using our own models to find weaknesses and improve safeguards faster. We dedicated over 700,000 A100-equivalent GPU hours to automated red teaming aimed at finding universal jailbreaks: attacks that can work across many prompts or contexts, not just one narrow setting. Focusing on these harder, more general attacks let us test the safeguards beyond a fixed set of known failures. It also lets us explore far more attack patterns than human testing alone could cover, identify failure patterns earlier, and shorten the path from finding a weakness to addressing it.
In addition to automated red-teaming, we worked with third-party testers to conduct extensive human expert red teaming, which will continue in the preview period. Human red-teaming complements the automated work by testing safeguards against creative experts trying to misuse the model in ways our systems might not anticipate.
No evaluation can represent every product configuration, multi-step attack, or real-world workflow. We therefore maintain a rapid-response process to reproduce, assess, prioritize, and remediate newly discovered jailbreaks, then add them to our ongoing evaluations so we can test against similar failures in the future.
Availability and pricing
During the preview, GPT‑5.6 models will initially be available through the API and Codex to a select group of trusted partners and organizations. We plan to make them more broadly available to people using ChatGPT, Codex, and the API soon.
In this new naming system introduced with GPT‑5.6, the number identifies a model’s generation, while Sol, Terra, and Luna identify durable capability tiers that can advance on their own cadence. Together, the family gives people and developers clearer choices across intelligence, speed, and cost.
GPT‑5.6 is priced per 1M tokens across three model sizes: Sol is $5 input / $30 output; Terra is $2.50 input / $15 output; and Luna is $1 input / $6 output. GPT‑5.6 also introduces more predictable prompt caching, including support for explicit cache breakpoints and a 30-minute minimum cache life. For GPT‑5.6 and later models, cache writes are billed at 1.25x the model’s uncached input rate, while cache reads continue to receive the 90% cached-input discount.
We're also launching GPT‑5.6 Sol on Cerebras at up to 750 tokens per second in July, bringing frontier intelligence to customers at unprecedented speed. Access will initially be limited to select customers as we expand capacity.
We’re excited to continue learning from this preview period, and to bring GPT‑5.6 Sol, Terra and Luna to more people soon.
1. We estimate latency and API cost by looking at the production behavior of our models, and simulating offline. These estimates account for tool call details, sampled tokens, and input tokens. Real-world results may vary substantially, and depend on many factors not captured in our simulation. We simulate latency at fast API speeds, and cost at regular API pricing.
2. All models are evaluated using the ExploitBench API harness with 5 seeds and reasoning continuity.
3. We ran ExploitGym on our alpha API, which outputs responses faster than our public API, and then rescaled to match our public API. When rescaling latencies to the speeds expected for our public API, this causes some estimated latencies to exceed the 2h and 6h hour time limits, despite being correctly obeyed in the evaluation run. To get faster speeds for time-sensitive work, we offer priority processing⁠ in the API and fast mode⁠ in Codex.
4. Models without reported output tokens, latency or cost are plotted as horizontal dotted lines.
2026
Author
OpenAI
Keep reading
View all
New usage analytics and updated spend controls for enterprises
Product
Jun 18, 2026
Improving health intelligence in ChatGPT
Product
Jun 18, 2026
Introducing the OpenAI Partner Network
Product
Jun 14, 2026
Research
Research Index
Research Overview
Economic Research
Latest Advancements
GPT-5.5
GPT-5.4
GPT-5.3 Instant
Safety
Safety Approach
Deployment Safety
(opens in a new window)
Security & Privacy
Trust & Transparency
Products
ChatGPT
(opens in a new window)
ChatGPT Business
(opens in a new window)
ChatGPT Enterprise
(opens in a new window)
ChatGPT for Education
(opens in a new window)
Codex
Release Notes
API Platform
Overview
API Log In
(opens in a new window)
Docs
(opens in a new window)
Business
Overview
Solutions
Resources
Customer Stories
Partner Network
Contact Sales
Developers
Apps SDK
(opens in a new window)
Open Models
Docs
(opens in a new window)
Resources
(opens in a new window)
Developer Forum
(opens in a new window)
Company
About Us
Our Charter
Careers
News
Support
Help Center
(opens in a new window)
More
Stories
Academy
Livestreams
Podcast
RSS
Terms & Policies
Terms of Use
Privacy Policy
Other Policies
(opens in a new window)
(opens in a new window)
(opens in a new window)
(opens in a new window)
(opens in a new window)
(opens in a new window)
(opens in a new window)

### 中文摘要（来自 entries.json curated summary_zh）

> 

### One-liner（来自 entries.json curated one_liner）

> OpenAI 发布 GPT-5.6 Sol 预览版，主打编码科学与网络安全能力

---

## 中文（关键要点翻译）

OpenAI 发布 GPT-5.6 系列预览，包含三个能力层级：**Sol**（旗舰，最强）、**Terra**（中阶）、**Luna**（轻量）。新命名规则下，数字（5.6）标识模型代际，而 Sol / Terra / Luna 是可以独立演进的能力层级。

### 关键能力提升

- **编码**：GPT-5.6 Sol 在 **Terminal-Bench 2.1**（测试命令行工作流的规划、迭代与工具协调）上达到新的 SOTA。
- **生物学**：在 **GeneBench v1**（评估长程基因组学与定量生物学分析）上以更少 token 数超越 GPT-5.5。
- **网络安全**：在 **ExploitBench** 与 **ExploitGym**（UC Berkeley 与多家前沿实验室合作）上表现强劲，对长程安全任务（漏洞研究、利用）显著推进 performance-efficiency 前沿，仅用约 1/3 输出 token 即可与 Mythos Preview 竞争。

### 推理模式新增

- **max**（新）：给予 Sol 最长深度推理时间。
- **ultra**（新）：突破单 agent 能力上限，借助子 agent 并行加速复杂任务。

### 分层安全防护（Layered Safeguards）

GPT-5.6 是 OpenAI 迄今最强防护栈，按模型能力匹配配置：

1. **模型层防护**：训练阶段拒绝违规网络协助，包括伪装意图与 jailbreak。
2. **实时分类器**：评估生成中的网络与生物滥用输出；高风险请求由更大的推理模型复核后再返回。
3. **账户级审查**：跨对话风险信号识别持续恶意行为 vs 合法双用途安全工作。
4. **分级访问**：保留合法防御性工作访问权限，但限制最敏感能力默认开放。
5. **持续红队测试**：自动化 + 第三方人类专家红队，包括 70 万 A100 等效 GPU 小时自动化红队。

GPT-5.6 Sol 在 Preparedness Framework 下**未跨越 Cyber Critical 阈值**（在 Chromium / Firefox 评估中识别了 bug 与利用原语，但未在测试条件下自主产出完整的全链利用），但 OpenAI 仍采用分阶段发布以收集反馈。

### 可用性与定价

- 预览阶段：GPT-5.6 模型首先通过 **API** 和 **Codex** 向选定的可信赖合作伙伴开放。
- 命名规则：数字 = 代际，Sol / Terra / Luna = 能力层级（独立演进）。
- 价格（每 1M tokens）：Sol $5 输入 / $30 输出 · Terra $2.50 / $15 · Luna $1 / $6。
- 新增 **可预测的 prompt caching**：支持显式 cache breakpoints、最短 30 分钟缓存寿命；缓存写入按 1.25× 未缓存输入价计费，缓存读取仍享 90% 折扣。
- **GPT-5.6 Sol on Cerebras**：7 月起在 Cerebras 上以最高 750 tokens/秒运行。
