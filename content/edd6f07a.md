# Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control

- source_url: https://arxiv.org/abs/2607.14890
- source_type: paper
- platform: arxiv
- author: Jek Huang, Jeffery Hsia, Jiayi Sun, Freddie Shi, Wei Huang, Ian H. White
- original_date: 2026-07-16
- added_date: 2026-07-20
- local_path: OpenClaw定时任务/论文流水线/2026-07-20-论文流水线.md
- quality_score: 4

## 摘要（中文）

论文讨论 coding agent 的生命周期控制：reviewedtestedDONEready-to-merge 不能只看 agent 自述，要绑定新鲜可追踪可机械验证的证据作者报告 unattended-loop engine 在 10 个场景中没有 false-DONE，本地 receipt bundle 能拒绝多类篡改；消融结果显示，证据门禁能显著降低 visible-pass/hidden-fail 放大

## Summary (English)

The paper proposes evidence-gated lifecycle control for coding agents, treating DONE and similar claims as assertions that must be backed by fresh, traceable, mechanically verifiable proof before state transitions.

## One-liner

Agent 不能自证完成，生命周期推进应由可验证证据触发

## 原文 / 元数据抓取

[
  {
    "id": "2607.14890",
    "title": "Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control",
    "authors": "Jek Huang, Jeffery Hsia, Jiayi Sun, Freddie Shi, Wei Huang, Ian H. White",
    "abstract": "Autonomous coding agents increasingly execute multi-step software work, but lifecycle states such as reviewed, tested, DONE, and ready-to-merge remain claims unless supported by current evidence. We present Proof-or-Stop Lifecycle Control, a method that permits lifecycle transitions only when fresh, tracked-source-state-bound, mechanically verifiable evidence satisfies the relevant gate. The method treats agent outputs as claims rather than lifecycle state, and uses proof operationally to mean gate-admissible evidence under a stated trust model, not semantic program correctness. We evaluate an open-source implementation through mechanism tests, a powered control-policy ablation, and operated self-application evidence. The unattended-loop engine passed 10 of 10 scenarios with zero false-DONE, and local-key receipt bundles rejected 18 tamper classes with zero false accepts. In a 9,240-cell ablation, the pre-registered A4 versus A2-prime comparison reduced visible-pass/hidden-fail amplification from 31 of 1,800 injected cells under a compute-budgeted naive loop to 2 of 1,800 under the gated loop, a 1.6 percentage-point improvement in not-amplified rate with a 95 percent confidence interval of [0.8, 2.5]. A near-compute A3 versus A4 comparison, 14 of 1,800 versus 2 of 1,800, indicates that the gain is associated with enforcing review as a lifecycle gate rather than merely adding a reviewer. The self-application corpus contains 565 stories and 1,007 review findings, with 94.8 percent resolved, plus a 68-row high/critical cross-vendor exhibit. These results support Proof-or-Stop as a model-agnostic, host-neutral control layer for deciding which autonomous-agent claims a lifecycle may act on. The evaluation is limited to one model family, 24 ablation tasks, and a self-hosted corpus.",
    "published": "2026-07-16",
    "updated": "2026-07-16",
    "primary_category": "cs.AI",
    "categories": "cs.AI, cs.SE",
    "comment": "48 pages, 10 figures, 29 numbered tables. Preprint v1",
    "pdf": "https://arxiv.org/pdf/2607.14890v1",
    "url": "https://arxiv.org/abs/2607.14890"
  }
]

## Obsidian intake evidence excerpt

# 论文流水线 · 2026-07-20

- status: completed
- Obsidian: `/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/OpenClaw定时任务/论文流水线/2026-07-20-论文流水线.md`
- Evidence: `/Users/gracker/.hermes/evidence/paper-pipeline/2026-07-20-论文流水线.md`
- 检索方式: `opencli arxiv recent/search/paper`；未调用 OpenClaw。

## 今日论文速报

1. **Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents**  
   - 来源: arXiv:2607.15143, 2026-07-16, cs.CR / cs.HC / cs.SE  
   - 作者: Aadesh Bagmar, Pushkar Saraf  
   - URL: https://arxiv.org/abs/2607.15143  
   - PDF: https://arxiv.org/pdf/2607.15143v1  
   - 速读: 论文把 AI coding agent 的项目初始化流程当成攻击面：README、requirements、Makefile 里的安装指令可以把 agent 引到不可信 registry、已知漏洞版本或相似包名。实验覆盖 12 个场景、5 类攻击，结论指向 harness-model 组合，而不是模型单点能力。typosquat 这种明显攻击更容易被拦住，`azurecore` / `azure-core` 这类分隔符混淆和 registry 重定向更容易漏掉。作者给出的工程解法是安装前做确定性校验：包名、来源、版本都过门禁，再允许执行。

2. **Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control**  
   - 来源: arXiv:2607.14890, 2026-07-16, cs.AI / cs.SE  
   - 作者: Jek Huang, Jeffery Hsia, Jiayi Sun, Freddie Shi, Wei Huang, Ian H. White  
   - URL: https://arxiv.org/abs/2607.14890  
   - PDF: https://arxiv.org/pdf/2607.14890v1  
   - 速读: 论文讨论 coding agent 的生命周期控制：reviewed、tested、DONE、ready-to-merge 不能只看 agent 自述，要绑定新鲜、可追踪、可机械验证的证据。作者报告 unattended-loop engine 在 10/10 场景中没有 false-DONE，本地密钥 receipt bundle 拒绝 18 类篡改且无 false accept；9,240-cell 消融里，证据门禁把 visible-pass/hidden-fail 放大从 31/1800 降到 2/1800。适合拿来对照现有 cron / agent 流程里的“完成”判定。

3. **SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration**  
   - 来源: arXiv:2607.15257, 2026-07-16, cs.AI / cs.IR  
   - 作者: Yuyao Zhang 等  
   - URL: https://arxiv.org/abs/2607.15257  
   - PDF: https://arxiv.org/pdf/2607.15257v1  
   - 代码: https://github.com/antins-labs/SearchOS  
   - 速读: SearchOS 把开放域搜索建模成“带引用的关系表补全”，用 Frontier Task、Evidence Graph、Coverage Map、Failure Memory 记录搜索状态，避免多 agent 搜索时反复撞同一堵墙。它还用 pipeline-parallel scheduling 填满空闲 agent 槽位，用 middleware harness 记录证据、检测停滞和预算耗尽。对需要长期跑的资料收集任务，这篇比单纯提高模型更接近工程改造方向。

4. **Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents**  
   - 来源: arXiv:2607.15263, 2026-07-16, cs.CR / cs.AI  
   - 作者: Paul Kassianik, Blaine Nelson, Yaron Singer  
   - URL: https://arxiv.org/abs/2607.15263  
   - PDF: https://arxiv.org/pdf/2607.15263v1  
   - 速读: 论文把安全 agent 的评测从“成功率”拉回到成本：推理、工具调用、遥测查询、补充检索都要计费。红队 CTF 任务能从更多 test-time compute 获益，蓝队 SOC 调查对工具使用纪律、遥测导航和选择性 enrichment 更敏感。这个结论可迁移到日常 agent：长任务不能只看是否完成，还要看每一步消耗和证据质量。

5. **Capturing and Exploiting Design Pattern Variability in Mobile Application Generation**  
   - 来源: arXiv:2607.15099, 2026-07-16, cs.SE  
   - 作者: Ramón Peralta, Jose-Miguel Horcas  
   - URL: https://arxiv.org/abs/2607.15099  
   - PDF: https://arxiv.org/pdf/2607.15099v1  
   - 速读: 论文把移动应用生成中的设计模式做成可配置资产，用 UVL 描述 Singleton、Strategy、Observer、Adapter、Factory Method 的结构和行为变体，再用 Jinja 模板生成 Swift 代码。它偏软件产品线和模型驱动工程，对 Android 不是直接命中，但对“生成代码如何保住架构质量”有参考价值。

6. **On the Adoption of AI Coding Agents in Open-source Android and iOS Development**  
   - 来源: arXiv:2602.12144, 2026-02-12, cs.SE / cs.AI；MSR 2026 Mining Challenge track accepted  
   - 作者: Muhammad Ahmad Khan, Hasnain Ali, Muneeb Rana, Muhammad Saqib Ilyas, Abdul Ali Bangash  
   - URL: https://arxiv.org/abs/2602.12144  
   - PDF: https://arxiv.org/pdf/2602.12144v1  
   - 速读: 这是今天的 Android 相关补充候选。作者分析 AIDev 数据集里 193 个 Android / iOS 开源仓库的 2,901 个 AI-authored PR。Android 项目收到的 AI PR 数量约为 iOS 的 2 倍，接受率 71%，iOS 为 63%。feature、fix、ui 这类常规任务更容易合并，refactor、build 这类结构性改动成功率更低、处理时间更长。

## 值得精读的论文

1. **首选: Setup Complete, Now You Are Compromised**  
   推荐理由: 它把 agent 安全问题落到项目初始化这一段：读文档、装依赖、跑 setup。这正是 coding agent 最常被授权执行、也最容易被当成“准备工作”的环节。精读时应重点看 12 个攻击场景、5 类攻击定义、不同 harness-model 组合的差异、确定性 pre-install check 的实现边界。

2. **备选: Proof-or-Stop**  
   推荐理由: 它给了一个可操作的 agent 证据门禁框架，和 Hermes cron 单任务化的要求很贴：不能只让 agent 说完成，要能绑定输入状态、输出证据、测试结果和生命周期动作。精读时应核对 10 个机制测试、18 类篡改、9,240-cell 消融设计，以及“proof”在论文里只指门禁证据，不等于程序语义正确。

3. **备选: SearchOS-V1**  
   推荐理由: 长周期 web research / paper pipeline 的失败常见于重复搜索、证据散落、覆盖缺口没人记录。SearchOS 的 Evidence Graph、Coverage Map、Failure Memory 可以作为论文流水线后续改造的参考。

## Android/Agent 相关性

- **Android 约束检查**: 本次没有采用 Android 18 / API 38+ 相关内容。Android 相关候选集中在移动开发、GUI agent、Android/iOS 开源 PR 数据，没有触碰 Android 17 / API 37 之后的平台 API 断言。
- **对 Android 工程的价值**: `2602.12144` 直接给出 Android 开源仓库中 AI PR 的接受率、任务类型差异和平台差异；`2607.15099` 对移动代码生成的架构质量有间接参考。
- **对 Agent 工程的价值**: `2607.15143` 指向依赖安装前门禁，`2607.14890` 指向证据绑定的生命周期控制，`2607.15257` 指向持久搜索状态，`2607.15263` 指向成本敏感评测。这四篇组合起来，正好覆盖 agent 的输入、执行、搜索、评估四个环节。

## 工作日 brief（周一至周五；周末写“今日不更新”）

今天是周一，brief lane 更新。

- **今天最该看**: `2607.15143`。如果只能读一篇，就看它的攻击分类和 pre-install check。它能直接变成 coding agent / cron pipeline 的安全门禁清单。
- **今天适合加入候选队列**: `2607.14890` 和 `2607.15257`。前者适合写“Agent 不能自证完成”，后者适合写“搜索任务要有状态，不要靠对话历史硬撑”。
- **今天可暂缓**: `2607.15099`。移动方向相关，但示例偏 Swift 和设计模式变体建模，不是 Android 性能或平台机制的一线材料。
- **风险提醒**: `Proof-or-Stop` 的数据来自一个模型家族、24 个消融任务和自托管语料，不能把结果外推成所有 agent 系统都适用。`Setup Complete` 的结论也要结合具体 harness 权限模型看。

## 建议下一步

1. 建议把 `2607.15143` 作为今日精读包候选，下载 PDF 后建立 canonical package：`论文/AI-2026-07-20-setup-complete-now-you-are-compromised/`。
2. 精读时先抽取这几类信息：攻击面定义、12 个场景、5 类攻击、模型与 harness 配对差异、pre-install check 规则、作者承认的限制。
3. 把 `2607.14890` 放入 agent 工程候选队列，后续可写成 Hermes cron 质量门禁参考：claim 不能直接触发 lifecycle transition，必须有新鲜证据。
4. 把 `2607.15257` 放入 paper pipeline 改造参考，优先借鉴 Coverage Map 和 Failure Memory，减少重复检索。

## 今日精选

1. AI coding agent 的供应链风险开始从“代码生成错了”前移到“项目还没跑起来，setup 已经被投毒”。
2. agent 生命周期里的 DONE / tested / reviewed 都应该被当成待验证断言，不能直接当状态用。
3. 长周期搜索 agent 需要显式状态：任务前沿、证据图、覆盖缺口、失败记忆。只靠聊天历史，预算越长越容易绕圈。

## 可直接发布文案

今天看到一篇很值得读的 agent 安全论文：**Setup Complete, Now You Are Compromised**。它盯的不是“模型会不会写出漏洞代码”，而是更靠前的一步：AI coding agent 读 README、装依赖、跑 Makefile 的时候，普通项目文档就可能变成攻击入口。

作者测试了 12 个场景和 5 类攻击。结果很工程：明显的 typosquat 容易被拦，像 `azurecore` / `azure-core` 这种相似包名、registry 重定向、来源混淆更容易漏；同一个模型换
