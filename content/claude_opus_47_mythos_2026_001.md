# Introducing Claude Opus 4.7

- **来源**: Anthropic
- **原文链接**: https://www.anthropic.com/news/claude-opus-4-7
- **作者**: Anthropic
- **日期**: 2026-04-16
- **分类**: models
- **标签**: Claude, Opus 4.7, Mythos, xhigh, cybersecurity, 2026
- **抓取时间**: 2026-06-13 04:28

---

## English Original

Our latest model, Claude Opus 4.7, is now generally available.

Opus 4.7 is a notable improvement on Opus 4.6 in advanced software engineering, with particular gains on the most difficult tasks. Users report being able to hand off their hardest coding work—the kind that previously needed close supervision—to Opus 4.7 with confidence. Opus 4.7 handles complex, long-running tasks with rigor and consistency, pays precise attention to instructions, and devises ways to verify its own outputs before reporting back.

The model also has substantially better vision: it can see images in greater resolution. It's more tasteful and creative when completing professional tasks, producing higher-quality interfaces, slides, and docs. And—although it is less broadly capable than our most powerful model, Claude Mythos Preview—it shows better results than Opus 4.6 across a range of benchmarks.

Last week we announced Project Glasswing, highlighting the risks—and benefits—of AI models for cybersecurity. We stated that we would keep Claude Mythos Preview's release limited and test new cyber safeguards on less capable models first. Opus 4.7 is the first such model: its cyber capabilities are not as advanced as those of Mythos Preview (indeed, during its training we experimented with efforts to differentially reduce these capabilities). We are releasing Opus 4.7 with safeguards that automatically detect and block requests that indicate prohibited or high-risk cybersecurity uses. What we learn from the real-world deployment of these safeguards will help us work towards our eventual goal of a broad release of Mythos-class models.

Security professionals who wish to use Opus 4.7 for legitimate cybersecurity purposes (such as vulnerability research, penetration testing, and red-teaming) are invited to join our new Cyber Verification Program.

Opus 4.7 is available today across all Claude products and our API, Amazon Bedrock, Google Cloud's Vertex AI, and Microsoft Foundry. Pricing remains the same as Opus 4.6: $5 per million input tokens and $25 per million output tokens. Developers can use claude-opus-4-7 via the Claude API.

## Testing Claude Opus 4.7

Claude Opus 4.7 has garnered strong feedback from our early-access testers:

- **Cursor**: On CursorBench, Opus 4.7 is a meaningful jump in capabilities, clearing 70% versus Opus 4.6 at 58%.
- **Notion**: For complex multi-step workflows, plus 14% over Opus 4.6 at fewer tokens and a third of the tool errors. It's the first model to pass our implicit-need tests.
- **Rakuten-SWE-Bench**: Claude Opus 4.7 resolves 3x more production tasks than Opus 4.6, with double-digit gains in Code Quality and Test Quality.
- **CodeRabbit**: Recall improved by over 10%. It's a bit faster than GPT-5.4 xhigh on our harness.
- **Hex**: Claude Opus 4.7 is the strongest model Hex has evaluated. It correctly reports when data is missing instead of providing plausible-but-incorrect fallbacks.
- **Devin**: It takes long-horizon autonomy to a new level in Devin. It works coherently for hours.
- **Replit**: Claude Opus 4.7 was an easy upgrade decision—same quality at lower cost.
- **Harvey**: 90.9% accuracy at high effort on BigLaw Bench for substantive accuracy.
- **Bolt**: Up to 10% better in the best cases for longer-running app-building work.
- **XBOW**: 98.5% on visual-acuity benchmark versus 54.5% for Opus 4.6.
- **Vercel**: Solid upgrade with no regressions, including proofs on systems code before starting work.
- **Warp**: Passed Terminal Bench tasks that prior Claude models had failed.
- **Genspark**: Achieves the highest quality-per-tool-call ratio we've measured.
- **Quantium**: Most capable model tested on reasoning depth, structured problem-framing, and complex technical work.

## Highlights from pre-release testing

- **Instruction following**: Opus 4.7 is substantially better at following instructions. Interestingly, this means that prompts written for earlier models can sometimes now produce unexpected results: where previous models interpreted instructions loosely or skipped parts entirely, Opus 4.7 takes the instructions literally. Users should re-tune their prompts and harnesses accordingly.
- **Improved multimodal support**: Opus 4.7 has better vision for high-resolution images: it can accept images up to 2,576 pixels on the long edge (~3.75 megapixels), more than three times as many as prior Claude models. This opens up computer-use agents reading dense screenshots, data extractions from complex diagrams, and work that needs pixel-perfect references.
- **Real-world work**: As well as its state-of-the-art score on the Finance Agent evaluation, internal testing showed Opus 4.7 to be a more effective finance analyst than Opus 4.6. Opus 4.7 is also state-of-the-art on GDPval-AA, a third-party evaluation of economically valuable knowledge work across finance, legal, and other domains.
- **Memory**: Opus 4.7 is better at using file system-based memory. It remembers important notes across long, multi-session work, and uses them to move on to new tasks that, as a result, need less up-front context.

## Safety and alignment

Overall, Opus 4.7 shows a similar safety profile to Opus 4.6. On some measures, such as honesty and resistance to malicious prompt injection attacks, Opus 4.7 is an improvement; in others (such as its tendency to give overly detailed harm-reduction advice on controlled substances), Opus 4.7 is modestly weaker. Our alignment assessment concluded that the model is "largely well-aligned and trustworthy, though not fully ideal in its behavior". Note that Mythos Preview remains the best-aligned model we've trained according to our evaluations. Full details in the Claude Opus 4.7 System Card.

## Also launching today

- **More effort control**: Opus 4.7 introduces a new `xhigh` (extra high) effort level between `high` and `max`, giving users finer control over the tradeoff between reasoning and latency on hard problems. In Claude Code, the default effort level is raised to `xhigh` for all plans.
- **On the Claude Platform (API)**: As well as support for higher-resolution images, we're launching task budgets in public beta.
- **In Claude Code**: The new `/ultrareview` slash command produces a dedicated review session that reads through changes and flags bugs and design issues that a careful reviewer would catch. Pro and Max Claude Code users get three free ultrareviews to try it out. Auto mode extended to Max users.

## Migrating from Opus 4.6 to Opus 4.7

Opus 4.7 is a direct upgrade to Opus 4.6, but two changes are worth planning for because they affect token usage. First, Opus 4.7 uses an updated tokenizer that improves how the model processes text (roughly 1.0–1.35× more tokens depending on the content type). Second, Opus 4.7 thinks more at higher effort levels, particularly on later turns in agentic settings. This improves its reliability on hard problems, but it does mean it produces more output tokens. Token usage across all effort levels is improved on an internal coding evaluation.


---

## 中文翻译

Anthropic 于 2026 年 4 月 16 日正式发布最新模型 Claude Opus 4.7。

Opus 4.7 在高级软件工程方面相较 Opus 4.6 有显著提升，在最困难的任务上进步尤为明显。用户反馈表示，过去需要密切监督的最棘手编程工作，现在可以放心交给 Opus 4.7。Opus 4.7 能以严谨一致的方式处理复杂的长时间任务，精确遵循指令，并会在回报前自行设计验证机制来核实自身输出。

模型的多模态视觉能力也有实质性提升：可以处理更高分辨率的图像。在完成专业任务时表现更有品味和创造性，能产出更高质量的界面、幻灯片和文档。尽管在整体能力上不及我们最强的模型 Claude Mythos Preview，但 Opus 4.7 在一系列基准测试中都优于 Opus 4.6。

## Project Glasswing 与网络安全

上周我们公布了 Project Glasswing 项目，揭示了 AI 模型在网络安全方面的风险与收益。我们当时表示将限制 Claude Mythos Preview 的发布范围，并先在能力较弱的模型上测试新的网络安全防护。Opus 4.7 是第一个这样的模型：其网络能力不及 Mythos Preview（在训练中我们专门实验性地削弱了相关能力）。我们为 Opus 4.7 配备了自动检测并阻止高风险网络安全请求的防护机制。从实际部署中收集的反馈，将帮助我们最终实现 Mythos 级别模型的广泛发布。

希望将 Opus 4.7 用于合法网络安全用途（漏洞研究、渗透测试、红队演练）的安全专业人员，欢迎加入我们新推出的"网络安全验证计划"。

Opus 4.7 今日起在所有 Claude 产品、我们的 API、Amazon Bedrock、Google Cloud Vertex AI 和 Microsoft Foundry 上线。定价与 Opus 4.6 持平：输入 $5/百万 tokens，输出 $25/百万 tokens。开发者可通过 Claude API 使用模型 ID `claude-opus-4-7`。

## 测试反馈

Claude Opus 4.7 收到了早期测试者的高度评价：

- **Cursor**：在 CursorBench 上，Opus 4.7 能力大幅跃升，得分 70%，Opus 4.6 为 58%。
- **Notion**：在复杂多步工作流中，比 Opus 4.6 高 14%，但 token 消耗更少、工具错误仅三分之一。是首个通过我们"隐含需求测试"的模型。
- **Rakuten-SWE-Bench**：解决的真实生产任务是 Opus 4.6 的 3 倍，代码质量与测试质量均有两位数提升。
- **CodeRabbit**：召回率提升 10% 以上。在我们的测试环境中略快于 GPT-5.4 xhigh。
- **Hex**：是我们评估过的最强模型。能正确报告数据缺失，而非给出貌似合理但错误的答案。
- **Devin**：将长程自主能力提升到新高度，能持续数小时连贯工作。
- **Replit**：一次轻松的升级决策——同等质量，成本更低。
- **Harvey**：在 BigLaw Bench 高工作量下达到 90.9% 准确率。
- **Bolt**：在长时应用构建任务上最佳情况下提升达 10%。
- **XBOW**：在视觉敏锐度基准上达到 98.5%，Opus 4.6 为 54.5%。
- **Vercel**：稳定升级，无回归。会在开始工作前对系统代码进行证明验证。
- **Warp**：通过了之前 Claude 模型未能通过的 Terminal Bench 任务。
- **Genspark**：在我们所有测试中达到最高的"质量/工具调用比"。
- **Quantium**：在推理深度、结构化问题框架与复杂技术工作方面，是我们测试过的最强模型。

## 预发布测试要点

- **指令遵循**：Opus 4.7 在指令遵循方面显著提升。有趣的是，这也意味着为旧模型编写的提示词有时会产生意外结果——旧模型会宽松解释或跳过部分指令，而 Opus 4.7 会严格按字面执行。用户应相应重新调优提示词与 harness。
- **多模态能力提升**：Opus 4.7 的高分辨率视觉显著增强：图像长边可达 2,576 像素（约 3.75 兆像素），是此前 Claude 模型的三倍以上。这让依赖精细视觉细节的工作成为可能：计算机使用代理读取密集截图、从复杂图表中提取数据、需要像素级参考的工作。
- **实际业务表现**：在 Finance Agent 评估中获得最先进分数。内部测试显示，Opus 4.7 比 Opus 4.6 是更高效的金融分析师，能产出更严谨的分析、模型与更专业的演示文稿。在第三方评估 GDPval-AA（覆盖金融、法律等领域的经济价值知识工作评估）上也是最先进水平。
- **记忆能力**：Opus 4.7 更好地利用基于文件系统的记忆。能在跨多会话的长时工作中记住关键笔记，并用于启动新任务，从而减少所需的前置上下文。

## 安全与对齐

总体而言，Opus 4.7 与 Opus 4.6 具有相似的安全画像。在诚实性与抵抗恶意提示注入攻击等指标上，Opus 4.7 有改进；在某些指标（如对受控物质给出过于详细的减害建议）上略弱。我们的对齐评估结论是：模型"基本良好对齐且值得信赖，但行为尚未完全理想"。请注意，按评估结果 Mythos Preview 仍是我们训练过的对齐最佳模型。完整细节见 Claude Opus 4.7 系统卡。

## 今日同步发布

- **更精细的 effort 控制**：Opus 4.7 引入新的 `xhigh`（超高）effort 等级，介于 `high` 与 `max` 之间，让用户在困难问题的推理与延迟权衡中获得更精细的控制。在 Claude Code 中，所有套餐的默认 effort 等级已提升至 `xhigh`。
- **Claude 平台（API）**：除支持更高分辨率图像外，公共测试版新增"任务预算"（task budgets），让开发者引导 Claude 的 token 消耗，以在长时任务中合理分配工作量。
- **Claude Code**：新增 `/ultrareview` 斜杠命令，产生专门的代码审查会话，逐条阅读变更并标记细致审查者会发现的 bug 与设计问题。Pro 与 Max 套餐用户可获得三次免费试用。Auto 模式扩展至 Max 用户。

## 从 Opus 4.6 迁移到 Opus 4.7

Opus 4.7 是 Opus 4.6 的直接升级，但有两点会影响 token 使用需提前规划：第一，Opus 4.7 使用更新后的分词器，同样输入可能映射到 1.0–1.35 倍的 tokens（取决于内容类型）。第二，Opus 4.7 在高 effort 等级（尤其是代理场景的后续回合）会"想得更深"。这提升了硬问题的可靠性，但会产生更多输出 tokens。在内部编码评估上，所有 effort 等级下的净效果是 token 使用更优。

