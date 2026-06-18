# Claude Opus 4.7 and Claude Mythos Preview: Anthropic's Most Capable Models Yet

> **Source:** <https://www.anthropic.com/news/claude-opus-4-7>
> **Author:** Anthropic
> **Original Date:** 2026-04-16
> **Quality Score:** 5
> **Fetched:** 2026-06-18 12:18:00

---

## English

ProductAnnouncements

# Introducing Claude Opus 4.7

Apr 16, 2026

Our latest model, Claude Opus 4.7, is now generally available.

Opus 4.7 is a notable improvement on Opus 4.6 in advanced software engineering, with particular gains on the most difficult tasks. Users report being able to hand off their hardest coding work—the kind that previously needed close supervision—to Opus 4.7 with confidence. Opus 4.7 handles complex, long-running tasks with rigor and consistency, pays precise attention to instructions, and devises ways to verify its own outputs before reporting back.

The model also has substantially better vision: it can see images in greater resolution. It’s more tasteful and creative when completing professional tasks, producing higher-quality interfaces, slides, and docs. And—although it is less broadly capable than our most powerful model, Claude Mythos Preview—it shows better results than Opus 4.6 across a range of benchmarks:

Last week we announced [Project Glasswing](https://www.anthropic.com/glasswing), highlighting the risks—and benefits—of AI models for cybersecurity. We stated that we would keep Claude Mythos Preview’s release limited and test new cyber safeguards on less capable models first. Opus 4.7 is the first such model: its cyber capabilities are not as advanced as those of Mythos Preview (indeed, during its training we experimented with efforts to differentially reduce these capabilities). We are releasing Opus 4.7 with safeguards that automatically detect and block requests that indicate prohibited or high-risk cybersecurity uses. What we learn from the real-world deployment of these safeguards will help us work towards our eventual goal of a broad release of Mythos-class models.

Security professionals who wish to use Opus 4.7 for legitimate cybersecurity purposes (such as vulnerability research, penetration testing, and red-teaming) are invited to join our new [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude).

Opus 4.7 is available today across all Claude products and our API, Amazon Bedrock, Google Cloud’s Vertex AI, and Microsoft Foundry. Pricing remains the same as Opus 4.6: $5 per million input tokens and $25 per million output tokens. Developers can use `claude-opus-4-7` via the [Claude API](https://platform.claude.com/docs/en/about-claude/models/overview).

## Testing Claude Opus 4.7

Claude Opus 4.7 has garnered strong feedback from our early-access testers:

> In early testing, we’re seeing the potential for a significant leap for our developers with Claude Opus 4.7. It catches its own logical faults during the planning phase and accelerates execution, far beyond previous Claude models. As a financial technology platform serving millions of consumers and businesses at significant scale, this combination of speed and precision could be game-changing: accelerating development velocity for faster delivery of the trusted financial solutions our customers rely on every day.

> Anthropic has already set the standard for coding models, and Claude Opus 4.7 pushes that further in a meaningful way as the state-of-the-art model on the market. In our internal evals, it stands out not just for raw capability, but for how well it handles real-world async workflows—automations, CI/CD, and long-running tasks. It also thinks more deeply about problems and brings a more opinionated perspective, rather than simply agreeing with the user.

> Claude Opus 4.7 is the strongest model Hex has evaluated. It correctly reports when data is missing instead of providing plausible-but-incorrect fallbacks, and it resists dissonant-data traps that even Opus 4.6 falls for. It’s a more intelligent, more efficient Opus 4.6: low-effort Opus 4.7 is roughly equivalent to medium-effort Opus 4.6.

> On our 93-task coding benchmark, Claude Opus 4.7 lifted resolution by 13% over Opus 4.6, including four tasks neither Opus 4.6 nor Sonnet 4.6 could solve. Combined with faster median latency and strict instruction following, it’s particularly meaningful for complex, long-running coding workflows. It cuts the friction from those multi-step tasks so developers can stay in the flow and focus on building.

> Based on our internal research-agent benchmark, Claude Opus 4.7 has the strongest efficiency baseline we’ve seen for multi-step work. It tied for the top overall score across our six modules at 0.715 and delivered the most consistent long-context performance of any model we tested. On General Finance—our largest module—it improved meaningfully on Opus 4.6, scoring 0.813 versus 0.767, while also showing the best disclosure and data discipline in the group. And on deductive logic, an area where Opus 4.6 struggled, Opus 4.7 is solid.

> Claude Opus 4.7 extends the limit of what models can do to investigate and get tasks done. Anthropic has clearly optimized for sustained reasoning over long runs, and it shows with market-leading performance. As engineers shift from working 1:1 with agents to managing them in parallel, this is exactly the kind of frontier capability that unlocks new workflows.

> We’re seeing major improvements in Claude Opus 4.7’s multimodal understanding, from reading chemical structures to interpreting complex technical diagrams. The higher resolution support is helping Solve Intelligence build best-in-class tools for life sciences patent workflows, from drafting and prosecution to infringement detection and invalidity charting.

> Claude Opus 4.7 takes long-horizon autonomy to a new level in Devin. It works coherently for hours, pushes through hard problems rather than giving up, and unlocks a class of deep investigation work we couldn't reliably run before.

> For Replit, Claude Opus 4.7 was an easy upgrade decision. For the work our users do every day, we observed it achieving the same quality at lower cost—more efficient and precise at tasks like analyzing logs and traces, finding bugs, and proposing fixes. Personally, I love how it pushes back during technical discussions to help me make better decisions. It really feels like a better coworker.

> Claude Opus 4.7 demonstrates strong substantive accuracy on BigLaw Bench for Harvey, scoring 90.9% at high effort with better reasoning calibration on review tables and noticeably smarter handling of ambiguous document editing tasks. It correctly distinguishes assignment provisions from change-of-control provisions, a task that has historically challenged frontier models. Substance was consistently rated as a strength across our evaluations: correct, thorough, and well-cited.

> Claude Opus 4.7 is a very impressive coding model, particularly for its autonomy and more creative reasoning. On CursorBench, Opus 4.7 is a meaningful jump in capabilities, clearing 70% versus Opus 4.6 at 58%.

> For complex multi-step workflows, Claude Opus 4.7 is a clear step up: plus 14% over Opus 4.6 at fewer tokens and a third of the tool errors. It’s the first model to pass our implicit-need tests, and it keeps executing through tool failures that used to stop Opus cold. This is the reliability jump that makes Notion Agent feel like a true teammate.

> In our evals, we saw a double-digit jump in accuracy of tool calls and planning in our core orchestrator agents. As users leverage Hebbia to plan and execute on use cases like retrieval, slide creation, or document generation, Claude Opus 4.7 shows the potential to improve agent decision-making in these workflows.

> On Rakuten-SWE-Bench, Claude Opus 4.7 resolves 3x more production tasks than Opus 4.6, with double-digit gains in Code Quality and Test Quality. This is a meaningful lift and a clear upgrade for the engineering work our teams are shipping every day.

> For CodeRabbit’s code review workloads, Claude Opus 4.7 is the sharpest model we’ve tested. Recall improved by over 10%, surfacing some of the most difficult-to-detect bugs in our most complex PRs, while precision remained stable despite the increased coverage. It’s a bit faster than GPT-5.4 xhigh on our harness, and we’re lining it up for our heaviest review work at launch.

> For Genspark’s Super Agent, Claude Opus 4.7 nails the three production differentiators that matter most: loop resistance, consistency, and graceful error recovery. Loop resistance is the most critical. A model that loops indefinitely on 1 in 18 queries wastes compute and blocks users. Lower variance means fewer surprises in prod. And Opus 4.7 achieves the highest quality-per-tool-call ratio we’ve measured.

> Claude Opus 4.7 is a meaningful step up for Warp. Opus 4.6 is one of the best models out there for developers, and this model is measurably more thorough on top of that. It passed Terminal Bench tasks that prior Claude models had failed, and worked through a tricky concurrency bug Opus 4.6 couldn't crack. For us, that’s the signal.

> Claude Opus 4.7 is the best model in the world for building dashboards and data-rich interfaces. The design taste is genuinely surprising—it makes choices I’d actually ship. It’s my default daily driver now.

> Claude Opus 4.7 is the most capable model we've tested at Quantium. Evaluated against leading AI models through our proprietary benchmarking solution, the biggest gains showed up where they matter most: reasoning depth, structured problem-framing, and complex technical work. Fewer corrections, faster iterations, and stronger outputs to solve the hardest problems our clients bring us.

> Claude Opus 4.7 feels like a real step up in intelligence. Code quality is noticeably improved, it’s cutting out the meaningless wrapper functions and fallback scaffolding that used to pile up, and fixes its own code as it goes. It’s the cleanest jump we’ve seen since the move from Sonnet 3.7 to the Claude 4 series.

> For the computer-use work that sits at the heart of XBOW’s autonomous penetration testing, the new Claude Opus 4.7 is a step change: 98.5% on our visual-acuity benchmark versus 54.5% for Opus 4.6. Our single biggest Opus pain point effectively disappeared, and that unlocks its use for a whole class of work where we couldn’t use it before.

> Claude Opus 4.7 is a solid upgrade with no regressions for Vercel. It’s phenomenal on one-shot coding tasks, more correct and complete than Opus 4.6, and noticeably more honest about its own limits. It even does proofs on systems code before starting work, which is new behavior we haven’t seen from earlier Claude models.

> Claude Opus 4.7 is very strong and outperforms Opus 4.6 with a 10% to 15% lift in task success for Factory Droids, with fewer tool errors and more reliable follow-through on validation steps. It carries work all the way through instead of stopping halfway, which is exactly what enterprise engineering teams need.

> Claude Opus 4.7 autonomously built a complete Rust text-to-speech engine from scratch—neural model, SIMD kernels, browser demo—then fed its own output through a speech recognizer to verify it matched the Python reference. Months of senior engineering, delivered autonomously. The step up from Opus 4.6 is clear, and the codebase is public.

> Claude Opus 4.7 passed three TBench tasks that prior Claude models couldn’t, and it’s landing fixes our previous best model missed, including a race condition. It demonstrates strong precision in identifying real issues, and surfaces important findings that other models either gave up on or didn’t resolve. In Qodo’s real-world code review benchmark, we observed top-tier precision.

> On Databricks’ OfficeQA Pro, Claude Opus 4.7 shows meaningfully stronger document reasoning, with 21% fewer errors than Opus 4.6 when working with source information. Across our agentic reasoning over data benchmarks, it is the best-performing Claude model for enterprise document analysis.

> For Ramp, Claude Opus 4.7 stands out in agent-team workflows. We’re seeing stronger role fidelity, instruction-following, coordination, and complex reasoning, especially on engineering tasks that span tools, codebases, and debugging context. Compared with Opus 4.6, it needs much less step-by-step guidance, helping us scale the internal agent workflows our engineering teams run.

> Claude Opus 4.7 is measurably better than Opus 4.6 for Bolt’s longer-running app-building work, up to 10% better in the best cases, without the regressions we’ve come to expect from very agentic models. It pushes the ceiling on what our users can ship in a single session.

01 / 28

Below are some highlights and notes from our early testing of Opus 4.7:

-   _Instruction following_. Opus 4.7 is substantially better at following instructions. Interestingly, this means that prompts written for earlier models can sometimes now produce unexpected results: where previous models interpreted instructions loosely or skipped parts entirely, Opus 4.7 takes the instructions literally. Users should re-tune their prompts and harnesses accordingly.
-   _Improved multimodal support_. Opus 4.7 has better vision for high-resolution images: it can accept images up to 2,576 pixels on the long edge (~3.75 megapixels), more than three times as many as prior Claude models. This opens up a wealth of multimodal uses that depend on fine visual detail: computer-use agents reading dense screenshots, data extractions from complex diagrams, and work that needs pixel-perfect references.1
-   _Real-world work_. As well as its state-of-the-art score on the Finance Agent evaluation (see table above), our internal testing showed Opus 4.7 to be a more effective finance analyst than Opus 4.6, producing rigorous analyses and models, more professional presentations, and tighter integration across tasks. Opus 4.7 is also state-of-the-art on [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa), a third-party evaluation of economically valuable knowledge work across finance, legal, and other domains.
-   _Memory_. Opus 4.7 is better at using file system-based memory. It remembers important notes across long, multi-session work, and uses them to move on to new tasks that, as a result, need less up-front context.

The charts below display more evaluation results from our pre-release testing, across a range of different domains:

## Safety and alignment

Overall, Opus 4.7 shows a similar safety profile to Opus 4.6: our evaluations show low rates of concerning behavior such as deception, sycophancy, and cooperation with misuse. On some measures, such as honesty and resistance to malicious “prompt injection” attacks, Opus 4.7 is an improvement on Opus 4.6; in others (such as its tendency to give overly detailed harm-reduction advice on controlled substances), Opus 4.7 is modestly weaker. Our alignment assessment concluded that the model is “largely well-aligned and trustworthy, though not fully ideal in its behavior”. Note that Mythos Preview remains the best-aligned model we’ve trained according to our evaluations. Our safety evaluations are discussed in full in the [Claude Opus 4.7 System Card](https://anthropic.com/claude-opus-4-7-system-card).

Overall misaligned behavior score from our automated behavioral audit. On this evaluation, Opus 4.7 is a modest improvement on Opus 4.6 and Sonnet 4.6, but Mythos Preview still shows the lowest rates of misaligned behavior.

## Also launching today

In addition to Claude Opus 4.7 itself, we’re launching the following updates:

-   _More effort control_: Opus 4.7 introduces a new `xhigh` (“extra high”) [effort level](https://platform.claude.com/docs/en/build-with-claude/effort) between `high` and `max`, giving users finer control over the tradeoff between reasoning and latency on hard problems. In Claude Code, we’ve raised the default effort level to `xhigh` for all plans. When testing Opus 4.7 for coding and agentic use cases, we recommend starting with `high` or `xhigh` effort.
-   _On the Claude Platform (API)_: as well as support for higher-resolution images, we’re also launching task budgets in public beta, giving developers a way to guide Claude’s token spend so it can prioritize work across longer runs.
-   _In Claude Code_: The new `/ultrareview` [slash command](https://code.claude.com/docs/en/commands) produces a dedicated review session that reads through changes and flags bugs and design issues that a careful reviewer would catch. We’re giving Pro and Max Claude Code users three free ultrareviews to try it out. In addition, we’ve extended [auto mode](https://claude.com/blog/auto-mode) to Max users. Auto mode is a new permissions option where Claude makes decisions on your behalf, meaning that you can run longer tasks with fewer interruptions—and with less risk than if you had chosen to skip all permissions.

## Migrating from Opus 4.6 to Opus 4.7

Opus 4.7 is a direct upgrade to Opus 4.6, but two changes are worth planning for because they affect token usage. First, Opus 4.7 uses an updated tokenizer that improves how the model processes text. The tradeoff is that the same input can map to more tokens—roughly 1.0–1.35× depending on the content type. Second, Opus 4.7 thinks more at higher effort levels, particularly on later turns in agentic settings. This improves its reliability on hard problems, but it does mean it produces more output tokens.

Users can control token usage in various ways: by using the effort parameter, adjusting their task budgets, or prompting the model to be more concise. In our own testing, the net effect is favorable—token usage across all effort levels is improved on an internal coding evaluation, as shown below—but we recommend measuring the difference on real traffic. We’ve written a [migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7) that provides further advice on upgrading from Opus 4.6 to Opus 4.7.

Score on an internal agentic coding evaluation as a function of token usage at each effort level. In this evaluation, the model works autonomously from a single user prompt, and results may not be representative of token usage in interactive coding. See the [migration guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7) for more on tuning effort levels.

#### Footnotes

1 This is a [model-level change](https://platform.claude.com/docs/en/build-with-claude/vision) rather than an API parameter, so images users send to Claude will simply be processed at higher fidelity. Because higher-resolution images consume more tokens, users who don’t require the extra detail can downsample images before sending them to the model.

-   For GPT-5.4 and Gemini 3.1 Pro, we compared against the best reported model version available via API in the charts and table.
-   MCP-Atlas: The Opus 4.6 score has been updated to reflect revised grading methodology from Scale AI.
-   SWE-bench Verified, Pro, and Multilingual: Our memorization screens flag a subset of problems in these SWE-bench evals. Excluding any problems that show signs of memorization, Opus 4.7’s margin of improvement over Opus 4.6 holds.
-   Terminal-Bench 2.0: We used the Terminus-2 harness with thinking disabled. All experiments used 1× guaranteed/3× ceiling resource allocation averaged over five attempts per task.
-   CyberGym: Opus 4.6’s score has been updated from the originally reported 66.6 to 73.8, as we updated our harness parameters to better elicit cyber capability.
-   SWE-bench Multimodal: We used an internal implementation for both Opus 4.7 and Opus 4.6. Scores are not directly comparable to public leaderboard scores.

May 4, 2026: Updated _Document reasoning_ graph to reflect updated OfficeQA Pro scores for Opus 4.7.

[](https://twitter.com/intent/tweet?text=https://www.anthropic.com/news/claude-opus-4-7)[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/news/claude-opus-4-7)

---

## 中文

# 介绍 Claude Opus 4.7

2026 年 4 月 16 日

我们的最新模型 Claude Opus 4.7 现已正式发布。

Opus 4.7 是在 Opus 4.6 基础上的重大升级，尤其在高级软件工程能力上进步显著——在最困难的任务上提升尤为明显。早期用户反馈，他们已经可以放心地把以前需要人工密切监督的最棘手的编码工作交给 Opus 4.7。Opus 4.7 能够以严谨稳定的方式处理复杂、长周期的任务，精确遵循指令，并主动设计自我验证机制，在汇报前先核查自身输出。

模型在视觉能力上也有大幅提升：能识别更高分辨率的图像。在专业任务执行中，Opus 4.7 表现得更具品味与创意，能输出更高质量的界面、幻灯片与文档。尽管能力上仍不及我们最强大的 Claude Mythos Preview，但在多项基准测试中，Opus 4.7 已全面超越 Opus 4.6。

上周我们公布了 [Project Glasswing](https://www.anthropic.com/glasswing)，讨论了 AI 模型在网络安全领域的风险与收益。我们曾表示会限制 Claude Mythos Preview 的发布规模，并先在能力较弱的模型上测试新的网络安全防护措施。Opus 4.7 是首个承担此任务的模型：其网络安全能力不及 Mythos Preview（事实上在训练过程中我们尝试了差异化降低此类能力的方法）。我们为 Opus 4.7 部署了能自动检测并拦截高风险网络安全请求的安全护栏。这些真实部署中获得的经验，将帮助我们最终实现 Mythos 级模型的广泛发布。

希望将 Opus 4.7 用于合法网络安全用途（如漏洞研究、渗透测试、红队演练）的安全从业者，欢迎加入我们新推出的 [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)。

Opus 4.7 即日起在所有 Claude 产品及 API、Amazon Bedrock、Google Cloud Vertex AI、Microsoft Foundry 上线。定价与 Opus 4.6 保持一致：每百万输入 token 5 美元，每百万输出 token 25 美元。开发者可通过 `claude-opus-4-7` 调用 [Claude API](https://platform.claude.com/docs/en/about-claude/models/overview)。

## Claude Opus 4.7 测试反馈

Claude Opus 4.7 在早期测试者中获得了强烈反响。

> 在早期测试中，我们看到 Claude Opus 4.7 有潜力为我们的开发者带来一次显著跃迁。它能在规划阶段自我捕获逻辑错误，并大幅加速执行，远超此前的 Claude 模型。作为服务于数百万消费者与企业的金融科技平台，速度与精度的结合堪称变革性力量，能加速开发节奏，让我们更快交付客户日常依赖的可信金融方案。

> Anthropic 早已为编码模型设立了标杆，而 Claude Opus 4.7 在此基础上做出了有意义的推进，是当前市场上最前沿的模型。在我们内部评估中，Opus 4.7 不仅在原始能力上突出，更在真实异步工作流（自动化、CI/CD、长周期任务）的处理上表现卓越。它会深入思考问题，并提出更有主张的视角，而非简单地附和使用者。

> Claude Opus 4.7 是 Hex 评估过的最强模型。它能在数据缺失时正确报错，而不是提供看似合理实则错误的兜底结果，并能抵抗 Opus 4.6 都会落入的"反调数据陷阱"。它是更智能、更高效的 Opus 4.6：低强度 Opus 4.7 大致相当于中强度 Opus 4.6。

> 在我们 93 题的编码基准测试中，Opus 4.7 相对 Opus 4.6 提升了 13% 的解题率，其中包括 4 道 Opus 4.6 与 Sonnet 4.6 都未能解决的题目。配合更短的中位延迟与严格的指令遵循，它对复杂、长周期编码工作流的意义尤其重大——它让多步任务不再卡顿，让开发者保持心流专注于构建。

> 在我们内部的 Research-Agent 基准测试中，Opus 4.7 是多步工作中效率基线最高的模型。在六个模块的总体得分上以 0.715 并列第一，并在长上下文一致性上达到所有测试模型中的最佳。在 General Finance（我们最大的模块）上，它相对 Opus 4.6 有明显提升，得分 0.813 对比 0.767，并展示出组内最佳的信息披露与数据规范。在 Opus 4.6 表现不佳的演绎逻辑上，Opus 4.7 也站得很稳。

> Claude Opus 4.7 拓展了模型在调研与执行任务上的极限。Anthropic 明显针对长周期推理进行了优化——这从市场领先的性能上就能看出来。当工程师从 1:1 与 agent 协作，转向并行管理多个 agent 时，这正是能解锁新工作流的前沿能力。

> 我们在 Claude Opus 4.7 的多模态理解上看到重大改进，从读取化学结构到解析复杂技术图表。更高分辨率的支持正在帮助 Solve Intelligence 构建生命科学专利工作流（从撰写、申请到侵权检测、无效化图表）的一流工具。

> Claude Opus 4.7 把 Devin 的长周期自主能力推到了新层级。它能连贯工作数小时，能啃下难题而不是放弃，这解锁了一类我们此前无法可靠运行的深度调研工作。

> 对 Replit 来说，Opus 4.7 是个容易的升级决定。在用户的日常任务中，我们观察到它能以更低的成本达到同样的质量——在分析日志与调用链、定位 bug、提出修复方案等任务上更高效、精准。我个人很喜欢它在技术讨论中"唱反调"的做法，能帮我做出更好的决策。它真的就像个更好的同事。

> Claude Opus 4.7 在 Harvey 的 BigLaw Bench 上展现出强大的实质准确性——高强度下得分 90.9%，对评审表有更好的推理校准，对模糊文档编辑任务也明显更智能。它能正确区分转让条款与控制权变更条款——这一直是前沿模型的难题。实质内容在我们的评估中始终是强项：准确、详尽、引用充分。

> Claude Opus 4.7 是令人印象深刻的编码模型，特别是在自主性与更具创造性的推理上。在 CursorBench 上，Opus 4.7 是能力的一次跃升，从 Opus 4.6 的 58% 跨过了 70% 的门槛。

> 在复杂多步工作流上，Opus 4.7 是清晰的一阶跃升：相对 Opus 4.6 提升 14%，且 token 更少、工具错误减少到三分之一。它是首个通过我们"隐式需求测试"的模型，能在工具失败时继续执行——以前这会让 Opus 卡住。这是让 Notion Agent 感觉像真正队友的可靠性跃升。

> 在我们的评估中，Hebbia 核心编排 agent 的工具调用准确率与规划能力出现两位数提升。随着用户用 Hebbia 做检索、PPT 生成、文档生成等场景，Opus 4.7 展示了提升这些工作流中 agent 决策能力的潜力。

> 在 Rakuten-SWE-Bench 上，Opus 4.7 解决的产线任务是 Opus 4.6 的 3 倍，代码质量与测试质量也都有两位数提升。这是我们工程团队日常交付的明确升级。

> 对 CodeRabbit 的代码审查负载来说，Opus 4.7 是我们测试过的最锐利的模型。召回率提升超过 10%，能在最复杂的 PR 中发现最难捕捉的 bug，同时精度没有因为覆盖面增大而下滑。它在我们的测试平台上比 GPT-5.4 xhigh 略快，我们已准备好让它承担最重的审查任务。

> 对 Genspark 的 Super Agent，Opus 4.7 精准命中了产线上三个最重要的差异化指标：抗循环、稳定性、优雅的错误恢复。抗循环最关键——一个在 1/18 查询中无限循环的模型既浪费算力又阻塞用户。更低的方差意味着产线上更少的惊喜。Opus 4.7 实现了我们测过的"每次工具调用质量比"中的最高值。

> 对 Warp 来说，Opus 4.7 是有意义的升级。Opus 4.6 已经是开发者群体中最好的模型之一，而 Opus 4.7 在此基础上显著更彻底。它通过了之前 Claude 模型失败的 Terminal Bench 题目，并解决了 Opus 4.6 无法突破的一个棘手并发 bug。对我们来说，这就是信号。

> Claude Opus 4.7 是全球构建仪表盘与数据丰富接口的最佳模型。它的设计品味真的让人惊喜——会做出我愿意直接发布的取舍。它现在是我的默认日常 driver。

> Claude Opus 4.7 是 Quantium 测试过的最强模型。通过我们专有的基准测试与领先 AI 模型对比，最大的提升出现在最关键的地方：推理深度、结构化问题构建、复杂技术工作。更少的修正、更快的迭代、更强的输出来解决客户带来的最难题。

> Claude Opus 4.7 感觉是一次真实的智能跃升。代码质量明显提升——它削减了那些无意义的包装函数和兜底脚手架，并边写边自我修复。这是从 Sonnet 3.7 跨到 Claude 4 系列以来，我们看到的最干净的跃升。

> 对支撑 XBOW 自主渗透测试核心的计算机使用工作来说，新的 Claude Opus 4.7 是一次阶跃：我们的视觉锐度基准从 Opus 4.6 的 54.5% 跃升到 98.5%。我们 Opus 上最大的痛点基本消失，这解锁了一整类此前无法使用 Opus 的工作。

> 对 Vercel 来说，Opus 4.7 是个稳健的升级，无回归。它在一次性编码任务上极为出色，比 Opus 4.6 更正确、更完整，也更诚实地承认自己的局限。它甚至在开始工作前会对系统代码做证明——这是我们从前在 Claude 模型身上没见过的行为。

> Opus 4.7 非常强大，超越 Opus 4.6，Factory Droids 的任务成功率提升 10–15%，工具错误更少，验证步骤的执行更可靠。它能把工作一路做到底，不在中途停下来——这正是企业工程团队所需要的。

> Opus 4.7 从零开始自主构建了一整套 Rust 文本转语音引擎——神经网络模型、SIMD 内核、浏览器 demo——然后让它自己的输出走一遍语音识别器，验证与 Python 参考实现的一致性。相当于几个月的高级工程师工作，被自主交付。Opus 4.7 相对 Opus 4.6 的升级非常清晰，代码库是公开的。

> Opus 4.7 通过了三道此前的 Claude 模型都没过的 TBench 题目，并修好了我们之前的最佳模型漏掉的修复，包括一个 race condition。它在识别真实问题上表现出强精度，并挖掘出其他模型放弃或未解决的重要发现。在 Qodo 的真实代码审查基准中，我们观察到它的精度是顶级的。

> 在 Databricks 的 OfficeQA Pro 上，Opus 4.7 展现了明显更强的文档推理能力，相对 Opus 4.6 错误减少 21%。在我们针对数据的 agentic 推理基准中，它是企业文档分析最强的 Claude 模型。

> 对 Ramp 来说，Opus 4.7 在 agent 团队工作流中格外突出。我们看到更强的角色保真度、指令遵循、协调与复杂推理，特别是在跨工具、代码库、调试上下文的工程任务上。相对 Opus 4.6，它需要更少的逐步指导，这帮助我们扩展了工程团队内部的 agent 工作流。

> 对 Bolt 的长周期应用构建工作来说，Opus 4.7 比 Opus 4.6 可量化地更好，最佳场景下提升达 10%，且没有我们已经在非常 agent 化的模型身上习以为常的回归。它把单次会话能交付的内容天花板又抬高了。

以下是我们对 Opus 4.7 早期测试中的一些亮点与说明：

- **指令遵循**：Opus 4.7 在指令遵循上有大幅提升。有意思的是，这也意味着为旧模型写的 prompt 偶尔会产生意料之外的结果：旧模型倾向于宽松解释或跳过部分指令，而 Opus 4.7 是字面理解的。用户应相应地重新调优 prompt 与编排框架。
- **多模态支持提升**：Opus 4.7 在高分辨率图像的视觉上更强：能接受长边最大 2,576 像素（约 3.75 megapixel）的图像，是之前 Claude 模型的三倍多。这开启了一大批依赖精细视觉细节的多模态用例：computer-use agent 读取密集截图、从复杂图表中提取数据、需要像素级参考的工作。
- **真实场景工作**：除了在 Finance Agent 评估上达到 SOTA（见上表），我们的内部测试也显示 Opus 4.7 比 Opus 4.6 是更高效的金融分析师——更严谨的分析与建模、更专业的呈现，以及跨任务更紧密的整合。Opus 4.7 在 [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa) 上也达到了 SOTA，这是一项针对金融、法律及其他领域经济价值知识工作的第三方评估。
- **记忆**：Opus 4.7 在使用基于文件系统的记忆上更出色。它能在长周期、多会话工作中记住重要笔记，并据此展开新任务，因此下次任务需要的预置上下文更少。

下方图表展示了我们发布前在多个不同领域的更多评估结果。

## 安全与对齐

总体上，Opus 4.7 展现出与 Opus 4.6 类似的安全画像：我们的评估显示其在欺骗、谄媚、配合滥用等令人担忧的行为上发生率较低。在部分指标上（如诚实度、抵抗恶意 prompt injection 攻击），Opus 4.7 相对 Opus 4.6 有所改进；在另一些指标上（如在受控物质上给出过于详尽的减害建议），Opus 4.7 略微弱一些。我们的对齐评估结论是：该模型"在很大程度上对齐良好且可信赖，但行为尚未完全理想"。需要说明的是，根据我们的评估，Mythos Preview 仍是我们训练过的对齐程度最高的模型。完整的安全评估在 [Claude Opus 4.7 System Card](https://anthropic.com/claude-opus-4-7-system-card) 中讨论。

下方图表展示了我们自动化行为审计中的整体失对齐行为分数。在该评估中，Opus 4.7 相对 Opus 4.6 与 Sonnet 4.6 略有改进，但 Mythos Preview 仍展现出最低的失对齐行为发生率。

## 今日同步上线

除 Claude Opus 4.7 本身外，我们同步推出以下更新：

- **更强的努力程度控制**：Opus 4.7 引入了新的 `xhigh`（"超高"）[effort level](https://platform.claude.com/docs/en/build-with-claude/effort)，位于 `high` 与 `max` 之间，让用户在硬问题上的"推理 vs 延迟"权衡有更细粒度的控制。在 Claude Code 中，我们已将所有套餐的默认 effort level 提升到 `xhigh`。在测试 Opus 4.7 用于编码与 agent 化场景时，我们建议从 `high` 或 `xhigh` 起步。
- **Claude 平台（API）**：除了支持更高分辨率图像外，我们还推出了 task budgets 的公开 beta，让开发者可以引导 Claude 的 token 投入，使其在长周期运行中能优先处理更关键的工作。
- **Claude Code**：新的 `/ultrareview` [slash command](https://code.claude.com/docs/en/commands) 启动一个专门的审查会话，逐项阅读变更并标记出细致审阅者会发现的 bug 与设计问题。我们为 Pro 与 Max Claude Code 用户提供三次免费的 ultrareview 试用。此外，我们已将 [auto mode](https://claude.com/blog/auto-mode) 扩展到 Max 用户。Auto mode 是一种新的权限选项，让 Claude 代表你做决定，这意味着你能以更少的中断运行长任务——且风险低于直接"跳过所有权限"。

## 从 Opus 4.6 迁移到 Opus 4.7

Opus 4.7 是 Opus 4.6 的直接升级，但有两点变化值得提前规划，因为它们会影响 token 消耗。第一，Opus 4.7 使用了更新版的 tokenizer，改进了模型处理文本的方式；代价是同样的输入可能映射到更多 token——根据内容类型大致在 1.0–1.35× 之间。第二，Opus 4.7 在更高 effort 下会思考更多，特别是在 agent 化场景的后续轮次。这提升了对难题的可靠性，但也意味着会生成更多输出 token。

用户可以通过多种方式控制 token 消耗：使用 effort 参数、调整 task budget，或提示模型更简洁。在我们自己的测试中，净效果是正向的——在内部编码评估上，所有 effort 等级的 token 效率都有改善（见下图）——但我们建议在真实流量上做一次实测。我们写了一份 [迁移指南](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7)，提供从 Opus 4.6 升级到 Opus 4.7 的进一步建议。

下方图表展示了在内部 agent 化编码评估上，每个 effort 等级下得分与 token 消耗的关系。在此评估中，模型从单条用户 prompt 开始自主工作，结果不一定能代表交互式编码中的 token 消耗。请参阅 [迁移指南](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7) 了解如何调优 effort level。

---

> *Full benchmarks, footnotes and migration guide available at the source URL.*
