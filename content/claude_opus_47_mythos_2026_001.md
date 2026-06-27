# Claude Opus 4.7 与 Claude Mythos Preview 发布：Anthropic 迄今最强的模型

- **ID**: claude_opus_47_mythos_2026_001
- **原文链接**: https://www.anthropic.com/news/claude-opus-4-7
- **作者**: Anthropic
- **日期**: 2026-04-16
- **分类**: models
- **标签**: Claude, Opus 4.7, Mythos, xhigh, cybersecurity, 2026
- **质量评分**: 5/5
- **抓取时间**: 2026-06-27T20:40:00

---

## 中文翻译

### 概览

我们最新的模型 **Claude Opus 4.7** 现已正式发布。

Opus 4.7 在 Opus 4.6 的基础上，于高级软件工程领域有显著提升，尤其在最困难的任务上进步明显。用户反馈表示，他们现在能够放心地把以前需要密切监督的最棘手编码工作交给 Opus 4.7。Opus 4.7 能以严谨和一致的态度处理复杂的长期任务，精确遵循指令，并设计方法在汇报前自我验证输出。

该模型的视觉能力也有大幅提升：可以处理更高分辨率的图像。在完成专业任务时更具品味和创造性，能够输出更高质量的界面、幻灯片和文档。虽然它的能力范围不如我们最强的模型 **Claude Mythos Preview**，但在一系列基准测试中表现优于 Opus 4.6。

### 配套的安全考量

上周我们公布了 [Project Glasswing](https://www.anthropic.com/glasswing)，强调 AI 模型在网络安全领域的风险与收益。我们承诺对 Claude Mythos Preview 保持有限范围的发布，并先在能力较弱的模型上测试新的网络安全保障。Opus 4.7 是首个这样的模型：它的网络能力不如 Mythos Preview 先进（事实上，在训练过程中我们还试验性地尝试差异化地降低这些能力）。我们在 Opus 4.7 上部署了能够自动检测并拦截涉及被禁止或高风险网络安全用途请求的安全防护措施。真实部署中这些防护措施所积累的经验，将帮助我们最终实现广泛发布 Mythos 级别模型的长期目标。

从事合法网络安全工作的安全专家（如漏洞研究、渗透测试和红队演练）受邀加入我们新的 [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)。

### 售价与可用性

Opus 4.7 即日起在所有 Claude 产品和我们的 API、Amazon Bedrock、Google Cloud 的 Vertex AI 以及 Microsoft Foundry 上线。价格与 Opus 4.6 保持一致：每百万输入 token 5 美元，每百万输出 token 25 美元。开发者可通过 [Claude API](https://platform.claude.com/docs/en/about-claude/models/overview) 使用 `claude-opus-4-7` 模型。

### 早期测试者反馈

Claude Opus 4.7 收获了早期测试者的强烈好评：

- **金融科技平台**："我们看到 Claude Opus 4.7 对开发者具有重大飞跃的潜力。它在规划阶段就能捕捉到自己的逻辑错误，并加速执行，远超之前的 Claude 模型。作为一家为大量消费者和企业提供服务的金融科技平台，这种速度与精度的结合可能改变游戏规则。"

- **AI 编码平台**："Anthropic 已经为编码模型设立了标准，Claude Opus 4.7 在此基础上更进一步，是市场上最先进的模型。在我们的内部评估中，它不仅在原始能力上突出，更在处理真实异步工作流（自动化、CI/CD、长期任务）方面表现出色。它对问题思考得更深入，并带来更有主见的视角，而不只是简单地同意用户。"

- **Hex**："Claude Opus 4.7 是我们评估过的最强模型。它在数据缺失时正确地报告，而不是给出看似合理但不正确的答案，并能抵御 Opus 4.6 也会落入的'矛盾数据陷阱'。这是一个更智能、更高效的 Opus 4.6：低投入的 Opus 4.7 大致相当于中投入的 Opus 4.6。"

- **Cursor 团队**："在我们的 93 项编码基准测试中，Claude Opus 4.7 的解决率比 Opus 4.6 提高了 13%，包括 4 个 Opus 4.6 和 Sonnet 4.6 都没能解决的任务。"

- **Warp**："Claude Opus 4.7 对我们是一次有意义的升级。Opus 4.6 是开发者领域最好的模型之一，而 Opus 4.7 在此基础上可衡量的更彻底。它通过了之前 Claude 模型失败的 Terminal Bench 任务，并解决了一个 Opus 4.6 解决不了的棘手并发 bug。"

- **XBOW**："对于我们自主渗透测试中计算机使用相关的工作，新的 Claude Opus 4.7 是一个飞跃：我们的视觉敏锐度基准从 Opus 4.6 的 54.5% 提升到 98.5%。我们最大的 Opus 痛点基本消失了。"

### 测试中的亮点

下面是我们对 Opus 4.7 早期测试中的一些亮点与说明：

- **指令遵循**：Opus 4.7 在指令遵循方面有显著提升。有趣的是，这意味着为早期模型编写的提示词有时会产生意想不到的结果：以前模型会宽松地解读指令或跳过部分内容，Opus 4.7 则严格按照字面意思执行。用户应根据需要重新调整提示词与编排框架。

- **多模态支持增强**：Opus 4.7 拥有更好的高分辨率图像视觉：它可接受长边高达 2,576 像素的图像（约 3.75 兆像素），是之前 Claude 模型的三倍多。这为依赖精细视觉细节的多模态应用打开了大门：计算机使用代理读取密集截图、从复杂图表中提取数据，以及需要像素级精度的参考任务。

- **真实工作负载**：除了在 Finance Agent 评估中获得最先进分数（见上表）外，我们的内部测试显示 Opus 4.7 是比 Opus 4.6 更有效的金融分析师，能产出更严谨的分析与模型、更专业的演示文稿，以及跨任务更紧密的集成。Opus 4.7 在 [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa)（第三方对金融、法律等领域经济价值知识工作的评估）上也达到了最先进水平。

- **记忆**：Opus 4.7 更善于使用基于文件系统的记忆。它在长期、多会话工作中能记住重要笔记，并据此推进新任务，从而减少了对前置上下文的需求。

### 安全与对齐

总体而言，Opus 4.7 表现出与 Opus 4.6 相似的安全特征：我们的评估显示其在欺骗、谄媚和配合滥用等令人担忧的行为上发生率较低。在某些指标（如诚实性、抵御恶意"提示注入"攻击）上，Opus 4.7 较 Opus 4.6 有改进；在另一些指标（如对受控物质提供过于详尽的减害建议）上，Opus 4.7 略显弱化。我们的对齐评估结论是该模型"在很大程度上表现良好且值得信赖，但行为上仍不完美"。需要指出的是，根据我们的评估，Mythos Preview 仍然是我们训练过的对齐度最高的模型。完整的安全评估详见 [Claude Opus 4.7 System Card](https://anthropic.com/claude-opus-4-7-system-card)。

### 今日同步发布

除了 Claude Opus 4.7 本身，我们还发布以下更新：

- **更精细的 effort 控制**：Opus 4.7 引入新的 `xhigh`（"超高"）[effort 级别](https://platform.claude.com/docs/en/build-with-claude/effort)，位于 `high` 和 `max` 之间，让用户能在困难问题上的推理与延迟权衡上有更精细的控制。在 Claude Code 中，我们已将所有套餐的默认 effort 级别提升至 `xhigh`。在测试 Opus 4.7 编码与代理用例时，我们建议从 `high` 或 `xhigh` effort 起步。

- **Claude Platform (API) 上**：除了支持更高分辨率图像外，我们还在公测中推出 **task budgets**（任务预算），让开发者能引导 Claude 的 token 消耗，使其在长任务中能更好地安排工作优先级。

- **Claude Code 中**：新的 `/ultrareview` [斜杠命令](https://code.claude.com/docs/en/commands) 会启动专门的审查会话，逐一阅读变更并标记出认真审阅者会发现的 bug 与设计问题。我们为 Pro 和 Max 套餐的 Claude Code 用户提供三次免费的 ultrareview 试用。此外，我们已面向 Max 用户扩展了 [auto mode](https://claude.com/blog/auto-mode)。Auto mode 是一种新的权限选项，让 Claude 代表你做决策，意味着你可以用更少的中断运行更长时间的任务 —— 并且比直接跳过所有权限更安全。

### 从 Opus 4.6 迁移到 Opus 4.7

Opus 4.7 是 Opus 4.6 的直接升级，但有两点变化值得提前规划，因为它们会影响 token 使用量。第一，Opus 4.7 使用了更新后的分词器，改进了模型处理文本的方式。代价是相同的输入可能映射到更多 token —— 根据内容类型不同，约为 1.0–1.35 倍。第二，Opus 4.7 在更高 effort 级别下会进行更多思考，特别是在代理场景的较后回合。这提升了它在困难问题上的可靠性，但也意味着会生成更多输出 token。

用户可以通过多种方式控制 token 使用：使用 effort 参数、调整 task budgets，或者提示模型更简洁。在我们自己的测试中，综合效果是正面的 —— 在内部编码评估上所有 effort 级别的 token 使用都有改善 —— 但我们建议在真实流量上测量差异。我们已撰写 [迁移指南](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7)，提供从 Opus 4.6 升级到 Opus 4.7 的进一步建议。

### 脚注

- 这是一项[模型级变更](https://platform.claude.com/docs/en/build-with-claude/vision)而非 API 参数，因此发送给 Claude 的图像会自动以更高保真度处理。因为更高分辨率图像消耗更多 token，不需要额外细节的用户可以在发送给模型之前对图像下采样。
- 对于 GPT-5.4 和 Gemini 3.1 Pro，我们与 API 可用的最佳报告模型版本进行比较。
- MCP-Atlas：Opus 4.6 的分数已更新，以反映 Scale AI 修订后的评分方法。
- SWE-bench Verified、Pro 和 Multilingual：我们的记忆化筛查标记了这些 SWE-bench 评估中的一部分问题。排除有记忆化迹象的问题后，Opus 4.7 相对 Opus 4.6 的改进幅度保持不变。
- Terminal-Bench 2.0：我们使用 Terminus-2 框架并禁用 thinking。所有实验使用 1× 保证 / 3× 上限资源分配，每项任务平均 5 次。
- CyberGym：Opus 4.6 的分数已从最初报告的 66.6 更新为 73.8，因为我们更新了框架参数以更好激发网络能力。

**2026 年 5 月 4 日更新**：更新了 _Document reasoning_ 图表，以反映 Opus 4.7 更新的 OfficeQA Pro 分数。

*来源：Anthropic, 2026-04-16*

## English Original

# Introducing Claude Opus 4.7

*April 16, 2026 — Anthropic*

Our latest model, **Claude Opus 4.7**, is now generally available.

Opus 4.7 is a notable improvement on Opus 4.6 in advanced software engineering, with particular gains on the most difficult tasks. Users report being able to hand off their hardest coding work — the kind that previously needed close supervision — to Opus 4.7 with confidence. Opus 4.7 handles complex, long-running tasks with rigor and consistency, pays precise attention to instructions, and devises ways to verify its own outputs before reporting back.

The model also has substantially better vision: it can see images in greater resolution. It's more tasteful and creative when completing professional tasks, producing higher-quality interfaces, slides, and docs. And — although it is less broadly capable than our most powerful model, **Claude Mythos Preview** — it shows better results than Opus 4.6 across a range of benchmarks.

### Cybersecurity safeguards

Last week we announced Project Glasswing, highlighting the risks — and benefits — of AI models for cybersecurity. We stated that we would keep Claude Mythos Preview's release limited and test new cyber safeguards on less capable models first. Opus 4.7 is the first such model: its cyber capabilities are not as advanced as those of Mythos Preview (indeed, during its training we experimented with efforts to differentially reduce these capabilities). We are releasing Opus 4.7 with safeguards that automatically detect and block requests that indicate prohibited or high-risk cybersecurity uses.

Security professionals who wish to use Opus 4.7 for legitimate cybersecurity purposes (such as vulnerability research, penetration testing, and red-teaming) are invited to join our new [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude).

### Availability and pricing

Opus 4.7 is available today across all Claude products and our API, Amazon Bedrock, Google Cloud's Vertex AI, and Microsoft Foundry. Pricing remains the same as Opus 4.6: **$5 per million input tokens and $25 per million output tokens**. Developers can use `claude-opus-4-7` via the [Claude API](https://platform.claude.com/docs/en/about-claude/models/overview).

### Early access feedback highlights

- **Financial platform**: "In early testing, we're seeing the potential for a significant leap for our developers with Claude Opus 4.7. It catches its own logical faults during the planning phase and accelerates execution, far beyond previous Claude models."

- **AI coding platform**: "Anthropic has already set the standard for coding models, and Claude Opus 4.7 pushes that further in a meaningful way as the state-of-the-art model on the market."

- **Hex**: "Claude Opus 4.7 is the strongest model Hex has evaluated. It correctly reports when data is missing instead of providing plausible-but-incorrect fallbacks, and it resists dissonant-data traps that even Opus 4.6 falls for."

- **Cursor**: "On our 93-task coding benchmark, Claude Opus 4.7 lifted resolution by 13% over Opus 4.6, including four tasks neither Opus 4.6 nor Sonnet 4.6 could solve."

- **Devin**: "Claude Opus 4.7 takes long-horizon autonomy to a new level in Devin. It works coherently for hours, pushes through hard problems rather than giving up."

- **Rakuten / SWE-Bench**: "On Rakuten-SWE-Bench, Claude Opus 4.7 resolves 3x more production tasks than Opus 4.6, with double-digit gains in Code Quality and Test Quality."

- **XBOW (autonomous pentest)**: "For the computer-use work that sits at the heart of XBOW's autonomous penetration testing, the new Claude Opus 4.7 is a step change: 98.5% on our visual-acuity benchmark versus 54.5% for Opus 4.6."

### Testing highlights

- **Instruction following**. Opus 4.7 is substantially better at following instructions. Users should re-tune their prompts and harnesses accordingly.
- **Improved multimodal support**. Opus 4.7 can accept images up to 2,576 pixels on the long edge (~3.75 megapixels), more than three times as many as prior Claude models.
- **Real-world work**. State-of-the-art on Finance Agent and GDPval-AA evaluations.
- **Memory**. Opus 4.7 is better at using file system-based memory, remembering important notes across long, multi-session work.

### Safety and alignment

Opus 4.7 shows a similar safety profile to Opus 4.6: low rates of concerning behavior such as deception, sycophancy, and cooperation with misuse. On some measures (honesty, prompt-injection resistance) it is an improvement; on others (over-detailed harm-reduction advice on controlled substances) it is modestly weaker. Mythos Preview remains the best-aligned model we've trained.

### Also launching today

- **More effort control**: new `xhigh` ("extra high") effort level between `high` and `max`. Default in Claude Code is now `xhigh`.
- **On the Claude Platform (API)**: support for higher-resolution images, plus **task budgets** in public beta.
- **In Claude Code**: new `/ultrareview` slash command for dedicated review sessions, plus expanded **auto mode** for Max users.

### Migrating from Opus 4.6 to Opus 4.7

Two changes affect token usage: an updated tokenizer (1.0–1.35× more tokens for the same input depending on content type), and more "thinking" at higher effort levels (especially in later turns of agentic sessions). Use the [migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7) for tuning advice.

*Source: Anthropic, April 16, 2026 — Last updated May 4, 2026*
