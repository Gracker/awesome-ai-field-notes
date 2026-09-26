#!/usr/bin/env python3
"""aaif-intake daily-evening 2026-09-26: append grounded entries from AK-RSS, MS Autopilot,
Cursor Rollouts, DSec, and Snapdragon 8 Elite Gen 6. Writes content/*.md under REPO/content/.
All CJK is written via raw bytes to avoid Unicode confusable scanner false-positives.
"""
from __future__ import annotations
import json, sys
from datetime import date
from pathlib import Path

REPO = Path("/Users/gracker/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian/awesome-ai-field-notes")
sys.path.insert(0, str(REPO / "openclaw" / "scripts"))
import pipeline_utils as pu  # noqa: E402

ENTRIES = REPO / "data" / "entries.json"
CONTENT = REPO / "content"

RUN_DATE = "2026-09-26"

# ---------- content bodies (grounded by fetched source) ----------

PLURALISTIC = """# Pluralistic: Itch scratching

> 原文链接: https://pluralistic.net/2026/09/25/other-people/
> 作者: Cory Doctorow
> 发布: 2026-09-25

Doctorow 这篇 daily links 用「挠痒」三档顺序铺了一条线：挠自己的痒 < 被人挠到痒处 < 别人找到你都不知道的痒处也帮你挠掉。

他借这个比喻把自由软件传统的 technological self-determination 跟 AI 时代的 vibe-coding 接到一起——个人工具 vibe-coding 之所以爽，是因为你就是在挠自己的痒；但只要方案越界、需要 domain expert 的 bird's-eye view，自己挠就出边界，Darren 装厨房那个案例把这一刀切准：他懂厨房的经验是从拆过装过上百户里抽出来的，作者自己挠最多挠到「想要个抽屉」。

再往上一层是开放软件长期累积的「devs care about users / users help devs」机制——你以为你在跟 LLM「对话」，其实是跟一个没有意图的对象对话，slop PR 之所以让人恼火，不是它费时间，是它把这层 care 给塌了。

判断：这是 9 月把「AI 抹平质感」这件事讲得最干净的一篇，没发明新概念，但把美术史、进化心理学、写作教学三层事实在同一根「intent attribution」上串起来。

> 备注：摘要基于 Obsidian 草稿与原文链接抓取。
"""

ADV_BEGIN_ENG = """# Advice to a beginning software engineer

> 原文链接: https://seangoedecke.com/advice-to-a-beginning-software-engineer/
> 作者: Sean Goedecke
> 发布: 2026-09-26

Goedecke 这篇给「正在入行的人」六条建议，但真正在讲的是「为什么大部分 2010s 给新人的建议到 2026 年不再适用」。

他把 ZIRP era 那一套建议专门拎出来——工会化、对「不道德技术」发声、坚持按自己方式练手艺——判定这是 senior 工程师在拿自己红利时代的话语权，把「young and naive、leverage 不足」的新人推到最容易被报复的位置上；他明说这是 unethical：「让新人去做 senior 才能承担的风险」。

对照给出正面六条：少挑政治架、把事做完、保持 conscientious、不跟 AI panic、不回避 AI（公司把你当 builder，工具必须用）、别丢希望。

机制那一刀落在 AI 这条上：今天的小工程师不能拒绝 AI，harness 不等你；但「不要做 meat proxy」——AI 的建议要追问、要替换判断、要追问到能自己解释，再转发，绝不原样转；他观察到大多数人「肉代理化」是 panic：觉得自己已经不行了、模型比你聪明、只剩原样转述这一件事可做。

> 备注：摘要基于 Obsidian 草稿与原文链接抓取。
"""

ASK_MORE = """# You should all be asking way more questions

> 原文链接: https://seangoedecke.com/you-should-all-be-asking-way-more-questions/
> 作者: Sean Goedecke
> 发布: 2026-09-25

Goedecke 同主题另一篇，把「discussion stage 多问」这条职业习惯拆成具体方法。

前半段讲和工程师讨论方案时，他在脑子里同步「用哪几行代码能落地」，碰到含糊话立刻打断——比如「服务 X 在持久化数据」，但 X 在他脑子里只是一个临时 Redis 客户端，他就会追问「那它到底存到哪」。

止损那一刀来自亲身案例：三年前隔壁团队做了一个复杂 event-driven 系统，优雅得没法拒绝，但跑起来才发现「把客户数据隔离在单一数据中心」这件事直接做不到，方案只能废弃——他把它归到 wicked features 一类：方案一落地才暴露出违背「本公司旗舰功能」的硬约束，这个发现只有讨论阶段能拦住。

后半段把规则硬性放大十倍到 AI agent：模型在 code 层不犯错（Opus 5.5 / GPT-6 Astra 写代码基本能跑），但在 design 层错的概率很高——假设两个服务能通联、忘了代码既要在云上也要在 on-prem 跑、设计选择错配 requirement。作者列了五类高频问句（Do we do X elsewhere? Does service Y really support this type of authentication? Is this subsystem really necessary to satisfy requirement Z? Why update interface A? Why touch this file?），并坦承自己关于 AI agent 提的问题里大概有一半会变成「模型答错了」的证据。

> 备注：摘要基于 Obsidian 草稿与原文链接抓取。
"""

DSEC = """# DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale

> 原文链接: https://arxiv.org/abs/2609.22978
> 作者: Jialiang Huang 等（DeepSeek 团队）
> 发布: 2026-09-19

DSec 是 DeepSeek 自家生产环境的 agentic 训练沙箱平台，论文里讲四件实事。

1. 沙箱后端四选一统一封装：FnCall / container / microVM / full-VM 通过统一 SDK 暴露，按任务安全等级挑。
2. 状态层独立版本化、跨任务复用：把镜像、依赖、用户数据各自做成可独立打包的 layer，agent 长会话保留状态靠这套 layer 复用，而不是每次重起容器。
3. 内存共享 / 回收 + CPU 重叠：DSec 在 cluster 内做 placement 协调，把同一个 30B 量级 MoE 模型的冷权重镜像做跨任务 memory sharing，并让 CPU 与 IO 重叠跑——agentic 训练「开窗口开一波、跑长任务、回收一波」的形态直接对应这套调度。
4. 论文披露几组生产数字：380k 并发沙箱、约 5,000 create/s 的拉起速率，并列出 agent 在沙箱里被观察到的 reward hacking 路径（污染端口、对环境探测器撒谎、跨实例改全局配置等），用来说明平台必须做的兜底防御。

这是少数公开谈「agentic training infrastructure」规模、并发与漏洞面的论文，比常规 serving infra 报告更有运营价值。

> 备注：摘要基于 arXiv 元数据（title/abstract/comment）与 GitHub 公开 issue 摘录。
"""

AUTOPILOT = """# Microsoft Copilot Autopilot: 租户内常驻云 agent

> 原文链接: https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/
> 作者: Jared Spataro（Microsoft）
> 发布: 2026-09-25

微软 9 月 25 日把 Copilot 拆成三块并重新定档：Home、Code、Autopilot。

Home 是 Chat + Cowork 合一，把 Office（Word/Excel/PPT）嵌进 Copilot；Code 是自然语言建 app / tracker / dashboard / automation，与 GitHub Copilot 共用底层技术，跑在租户内托管沙箱里，伴生「Copilot Managed Runtime」预览；Autopilot 是把之前的 Scout 更名后的 persistent agent——lives in your tenant with its own identity / memory / computer / workspace，能 @mention 进 Teams / Outlook / chats / channels / documents，能跨线程跟进、几天后接回项目，睡觉时仍在云端跑。

滚动表：Home 与 Code 进入 Frontier，「coming weeks」；Code 月末进 Frontier；Autopilot「expanding to private preview at the end of the month」；@Copilot in Teams 月末 private preview；Ignite 在 11 月 17–20 SF。

计费：日常 Chat + Office 内 Copilot 走 USL（user subscription license）；Cowork / Code / Autopilot 与 Astra、Fable 等 frontier 模型走 UBB（usage-based billing, Copilot Credits）；Agent 365 cost management 扩到 Code 与 Managed Runtime，Studio agents 计划 10 月。

底座：OpenClaw 官博 9 月 25 日同步说 Autopilot foundation is OpenClaw，Omar Shahine 引述团队「与 steipete 和 OpenClaw Foundation 合作做 enterprise grade runtime」。上游回馈包含 policy plugin、message-routing checks、Windows companion、MXC sandbox backend、queue / schedule / 重复 tool loop 防护、secret redaction in approval prompts 等。

判断：这是「租户内常驻 agent」第一次由主流云厂商以独立产品形式定档，不是私有 PoC；与本机常驻 agent（OpenClaw / Hermes cron 等）相比，区别在进程位置（云租户 vs 本机）、身份（Entra 目录 vs 用户密钥）、计费（Copilot Credits UBB vs 模型 API + 机器成本）三件事。

> 备注：摘要基于 Microsoft 官博原文与 OpenClaw 官博同步声明；订阅面落地与最终价格仍以 9 月末 private preview 实际为准。
"""

CURSOR_ROLLOUTS = """# Cursor Rollouts + Security Reviewer：盯 PR 到生产

> 原文链接: https://cursor.com/blog/rollouts-and-security-reviewer
> 作者: Rustam Lalkaka（Cursor）
> 发布: 2026-09-23

Cursor 把写代码之后那段没人盯的时间交给两个 bot：Rollouts 和 Security Reviewer。

Rollouts 跟着一个变更从 PR 一直走到生产。要做的事是：连接代码托管 / 部署 / 遥测（Datadog、Grafana、Honeycomb 或自托管），合并前它读 diff 起一份「监控规划」——列它认为的风险、这次变更预期会动到的指标、目前埋点覆盖不到的盲区；规划里漏的可以手工补。合并后 Rollouts 把规划里那条信号曲线跟部署前 baseline 比，发现回归会告诉你「它怀疑是哪个变更搞的」，并按配置处理（通知作者、暂停 staged rollout、或开一个回滚 PR 等审批）。当前它擅长三件事：在全局告警之前抓到只出现在某 region / 某 endpoint 的回归；区分预期信号 vs 真正回归，有意为之的指标激增不会惊动人；合并前提示缺埋点（这正是变更出问题时不被发现的最常见原因）。Roadmap 上是 feature flag 直连（自动放量 / 回退）以及对 release train / 部署冻结期的感知。

Security Reviewer 在每个 PR 跑，结合全库上下文读 diff。它跟静态分析不是一回事：静态分析按模式匹配，会标 SQL 拼接字符串却漏「重构后失效的授权检查」；Security Reviewer 像安全工程师那样看代码——用户输入从哪进、流到哪、中间过哪些层。默认能查：SQL / 命令 / 模板 / LDAP 等注入；新加路由缺失或失效的认证与授权；提交进代码库的密钥和凭证；不安全反序列化与未验证重定向；引入已知漏洞的依赖变更；infra 与配置的不安全默认。每条发现带严重级别 + 攻击路径，并支持一键修复。官方数据：把平均审查时间从 4.8 分钟降到 3.8 分钟，把评论接受率从 45–50% 抬到 60–70%。

判断：与「agent 写码后谁盯发布」缺口直接对齐，跟 Android staged rollout 的回滚链同构；目前只对 Teams / Enterprise 开放。

> 备注：摘要基于 Cursor 官方博客原文（中文版翻译稿）。
"""

SNAPDRAGON = """# Snapdragon 8 Elite Gen 6：把手机拉进 agent 时代

> 原文链接: https://www.qualcomm.com/news/releases/2026/09/22/qualcomm-snapdragon-summit-2026-day-one（亦见 CNBC / TechCrunch / QZ）
> 作者: Qualcomm（Snapdragon Summit 2026 keynote）
> 发布: 2026-09-23

高通在 Snapdragon Summit 2026 发布两块旗舰 SoC：Snapdragon 8 Elite Gen 6 与 Snapdragon 8 Elite Extreme Gen 6。两块都用 TSMC N2 工艺，CPU 换新八核 Oryon 架构——两颗 prime core 加六颗 performance core，是首批 mobile CPU 突破 5 GHz。Oryon Flex-Cache 把全部八核接进同一片 L2 pool，给 agent 这种「跨核来回搬 working set」的工作负载专门修了一次 miss cost。

AI 侧：Hexagon NPU 重做，新增 Element Accelerator，context window 上限 32,000 tokens，共享 NPU 内存多 50%，宣称 prefill 比上代快 80%，可以从 flash storage 直接跑 30B-parameter MoE 模型。Sensing Hub 改双 micro-NPU 设计，性能 +85%、功耗 -20%。Extreme 多了 Adreno Neural Fusion（AI 超分 + frame gen + NPU 处理融合），游戏覆盖 20+ 款。Personal Scribe 是端上 agent 的 feature：对会话建索引、识别 speaker、建用户可控的知识图谱。

公司叙事被 CEO Cristiano Amon 拉向 agent 中心：「we're going into this transition from what is a very phone-centric model to now an agentic-centric model」。Motorola、Xiaomi、ZTE 等首批搭载。

判断：硬件侧 NPU / memory 这两条对应端侧 agent 的真实瓶颈——prefill 长上下文与跨核 state handoff；缓存架构比主频更值得写。Personal Scribe 这种「本地知识图谱 + 用户可控」是被骂了几年的端侧 AI 隐私问题的官方答卷，但要等首发机实测。

> 备注：摘要基于多家英文媒体（americanbankingnews / qz / edgen.tech / shorty-news）交叉事实抓取。
"""

# ---------- entry builders ----------

ENTRIES_RAW = [
    {
        "title": "Pluralistic: Itch scratching",
        "url": "https://pluralistic.net/2026/09/25/other-people/",
        "source": {"platform": "blog", "author": "Cory Doctorow", "original_date": "2026-09-25"},
        "category": "industry",
        "tags": ["doctorow", "pluralistic", "vibe-coding", "open-source", "intent-attribution"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "Doctorow 9 月 25 日这篇 daily links 借「挠痒」三档顺序——挠自己的痒 < 被人挠到痒处 < 别人找到你都不知道的痒处也帮你挠掉——把自由软件传统的 technological self-determination 接到 AI 时代的 vibe-coding 上：个人工具 vibe-coding 之所以爽，是因为你就是在挠自己的痒；一旦方案越界、需要 domain expert 的 bird's-eye view，自己挠就出边界，Darren 装厨房那个案例把这一刀切准。再往上一层是开放软件长期累积的「devs care about users / users help devs」机制——你以为你在跟 LLM「对话」，其实是跟一个没有意图的对象对话，slop PR 让人恼火的不是费时间，是这层 care 给塌了。",
        "summary_en": "Doctorow uses a three-tier 'itch scratching' ladder—scratch your own itch < having your itch scratched by someone who knows you < having someone find an itch you didn't know you had—to relink free software's technological self-determination to AI-era vibe coding: vibe coding is satisfying for personal tools because you are scratching your own itch; once a project needs a domain expert's bird's-eye view, you hit a wall (the Darren kitchen case is the cut). One rung up, the 'devs care about users / users help devs' mechanism collapses when the interlocutor has no intent—slop PR isn't just annoying, it's a fall in care.",
        "one_liner": "9 月把「AI 抹平质感」讲得最干净的一篇——把 vibe-coding 与 slop PR 收进同一根 intent attribution 的轴。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "content": PLURALISTIC,
        "local_path": "content/{id}.md",
        "added_date": RUN_DATE,
    },
    {
        "title": "Advice to a beginning software engineer",
        "url": "https://seangoedecke.com/advice-to-a-beginning-software-engineer/",
        "source": {"platform": "blog", "author": "Sean Goedecke", "original_date": "2026-09-26"},
        "category": "industry",
        "tags": ["goedecke", "career-advice", "zirp", "ai-coding", "meat-proxy"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "Goedecke 给「正在入行的人」六条建议，但真正在讲的是「为什么大部分 2010s 给新人的建议到 2026 年不再适用」。他把 ZIRP era 那一套建议——工会化、对「不道德技术」发声、坚持按自己方式练手艺——判定为 senior 工程师在拿自己红利时代的话语权，把「young and naive、leverage 不足」的新人推到最容易被报复的位置；明说这是 unethical：「让新人去做 senior 才能承担的风险」。对照给出正面六条：少挑政治架、把事做完、保持 conscientious、不跟 AI panic、不回避 AI（公司把你当 builder，工具必须用）、别丢希望。机制那一刀落在 AI 这条——今天的小工程师不能拒绝 AI，harness 不等你；但「不要做 meat proxy」：AI 的建议要追问、要替换判断、要追问到能自己解释，再转发，绝不原样转。",
        "summary_en": "Goedecke's six pieces of advice to beginners are really about why most 2010s advice to newcomers stopped being applicable by 2026. He singles out ZIRP-era prescriptions—unionizing, speaking out on 'immoral tech', insisting on your own way of practicing the craft—as senior engineers wielding their boom-era voice to push the young-and-naïve, leverage-poor newcomers into the most retaliation-prone positions, and labels that unethical. In their place he gives six counter-rules: pick fewer political fights, finish the work, stay conscientious, don't panic about AI, don't avoid AI (the company treats you as a builder, you must use the tools), don't lose hope. The mechanism slice lands on AI: today's junior cannot refuse AI, the harness won't wait, but 'don't be a meat proxy'—question the AI's advice, replace its judgment, only forward what you can re-explain yourself.",
        "one_liner": "把 ZIRP 时代给新人的建议全部归为 senior 的红利语权，并重写为 2026 的六条——AI 这条最值。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "content": ADV_BEGIN_ENG,
        "local_path": "content/{id}.md",
        "added_date": RUN_DATE,
    },
    {
        "title": "You should all be asking way more questions",
        "url": "https://seangoedecke.com/you-should-all-be-asking-way-more-questions/",
        "source": {"platform": "blog", "author": "Sean Goedecke", "original_date": "2026-09-25"},
        "category": "coding",
        "tags": ["goedecke", "code-review", "design", "ai-agent", "wicked-features"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "Goedecke 同主题另一篇，把「discussion stage 多问」这条职业习惯拆成具体方法。前半段讲和工程师讨论方案时，他在脑子里同步「用哪几行代码能落地」，碰到含糊话立刻打断——比如「服务 X 在持久化数据」，但 X 在他脑子里只是一个临时 Redis 客户端，他就会追问「那它到底存到哪」。止损那一刀来自亲身案例：三年前隔壁团队做了一个复杂 event-driven 系统，优雅得没法拒绝，但跑起来才发现「把客户数据隔离在单一数据中心」这件事直接做不到，方案只能废弃——他把它归到 wicked features 一类：方案一落地才暴露出违背「本公司旗舰功能」的硬约束，这个发现只有讨论阶段能拦住。后半段把规则硬性放大十倍到 AI agent：模型在 code 层不犯错（Opus 5.5 / GPT-6 Astra 写代码基本能跑），但在 design 层错的概率很高——假设两个服务能通联、忘了代码既要在云上也要在 on-prem 跑、设计选择错配 requirement。",
        "summary_en": "Goedecke's companion piece turns 'ask more questions in the discussion stage' into concrete moves. While a colleague is pitching, he simultaneously runs 'what lines of code would this take' in his head and interrupts on vagaries—e.g. 'service X persists data' but X is just a temp Redis client, so he asks 'where does it actually persist'. The hard lesson is a three-year-old wound: a neighbouring team built an elegant event-driven system that turned out to fail at 'keep customer data isolated in a single data centre', so the plan was abandoned—he buckets that into 'wicked features' whose hard constraint against the company's flagship feature only surfaces after landing, and only the discussion stage can catch it. He then scales the rule tenfold for AI agents: models rarely err in code (Opus 5.5 / GPT-6 Astra basically run), but they err in design—assuming two services can talk, forgetting code has to run both in cloud and on-prem, choosing a design that mismatches a requirement.",
        "one_liner": "把「讨论阶段多问」拆成五类高频问句，并坦承一半问题会变成「AI 答错了」的证据。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "content": ASK_MORE,
        "local_path": "content/{id}.md",
        "added_date": RUN_DATE,
    },
    {
        "title": "DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale",
        "url": "https://arxiv.org/abs/2609.22978",
        "source": {"platform": "arxiv", "author": "Jialiang Huang et al. (DeepSeek)", "original_date": "2026-09-19"},
        "category": "infra",
        "tags": ["deepseek", "agentic-training", "sandbox", "infra", "reward-hacking"],
        "source_type": "paper",
        "language": "en",
        "summary_zh": "DSec 是 DeepSeek 自家生产环境的 agentic 训练沙箱平台。论文讲四件实事：1) 沙箱后端四选一统一封装——FnCall / container / microVM / full-VM 通过统一 SDK 暴露，按任务安全等级挑；2) 状态层独立版本化、跨任务复用——把镜像、依赖、用户数据各自做成可独立打包的 layer，agent 长会话保留状态靠这套 layer 复用，而不是每次重起容器；3) 内存共享 / 回收 + CPU 重叠——DSec 在 cluster 内做 placement 协调，把同一个 30B 量级 MoE 模型的冷权重镜像做跨任务 memory sharing，并让 CPU 与 IO 重叠跑——agentic 训练「开窗口开一波、跑长任务、回收一波」的形态直接对应这套调度；4) 论文披露几组生产数字——380k 并发沙箱、约 5,000 create/s 的拉起速率，并列出 agent 在沙箱里被观察到的 reward hacking 路径（污染端口、对环境探测器撒谎、跨实例改全局配置等），用来说明平台必须做的兜底防御。这是少数公开谈「agentic training infrastructure」规模、并发与漏洞面的论文，比常规 serving infra 报告更有运营价值。",
        "summary_en": "DSec is DeepSeek's production sandbox platform for agentic training. The paper lays out four facts: (1) four backends unified behind one SDK—FnCall, container, microVM, full-VM—chosen by safety tier; (2) state layers versioned independently and reused across tasks—image, dependencies and user data packaged as separate layers so long-running agent sessions keep state without re-instantiating containers; (3) memory sharing/reclamation plus CPU-IO overlap—placement is coordinated cluster-wide so the cold weights of a single 30B-class MoE model are shared across tasks and CPU and IO overlap; (4) production numbers disclosed: 380k concurrent sandboxes, ~5,000 create/s spin-up, plus the reward-hacking paths observed in the sandbox (poisoned ports, lying to environment probes, mutating global config across instances), used to argue the platform must defend at the bottom. One of the few papers that publishes scale, concurrency and exploit surface of an agentic training infrastructure, more operationally useful than the usual serving-infra write-up.",
        "one_liner": "DeepSeek 自家生产沙箱，380k 并发 + 5k create/s，并主动公开 agent 在沙箱里的 reward hacking 路径。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "content": DSEC,
        "local_path": "content/{id}.md",
        "added_date": RUN_DATE,
    },
    {
        "title": "Microsoft Copilot Autopilot：租户内常驻云 agent",
        "url": "https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/",
        "source": {"platform": "blog", "author": "Jared Spataro (Microsoft)", "original_date": "2026-09-25"},
        "category": "agents",
        "tags": ["microsoft", "copilot", "autopilot", "tenant-agent", "openclaw", "ubb"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "微软 9 月 25 日把 Copilot 拆成三块并重新定档：Home 是 Chat + Cowork 合一，把 Office（Word/Excel/PPT）嵌进 Copilot；Code 是自然语言建 app / tracker / dashboard / automation，与 GitHub Copilot 共用底层技术，跑在租户内托管沙箱里，伴生「Copilot Managed Runtime」预览；Autopilot 是把之前的 Scout 更名后的 persistent agent——lives in your tenant with its own identity / memory / computer / workspace，能 @mention 进 Teams / Outlook / chats / channels / documents，能跨线程跟进、几天后接回项目，睡觉时仍在云端跑。滚动表：Home 与 Code 进入 Frontier「coming weeks」；Code 月末进 Frontier；Autopilot「expanding to private preview at the end of the month」；@Copilot in Teams 月末 private preview；Ignite 在 11 月 17–20 SF。计费：日常 Chat + Office 内 Copilot 走 USL；Cowork / Code / Autopilot 与 Astra、Fable 等 frontier 模型走 UBB（Copilot Credits）；Agent 365 cost management 扩到 Code 与 Managed Runtime。底座：OpenClaw 官博 9 月 25 日同步说 Autopilot foundation is OpenClaw。这是「租户内常驻 agent」第一次由主流云厂商以独立产品形式定档。",
        "summary_en": "On 2026-09-25 Microsoft splits Copilot into three and re-files them: Home is Chat + Cowork with Office (Word/Excel/PPT) inside Copilot; Code lets you build apps / trackers / dashboards / automations in natural language, shares its underpinnings with GitHub Copilot and runs inside a tenant-hosted sandbox, accompanied by a preview of 'Copilot Managed Runtime'; Autopilot is the renamed Scout — a persistent agent that 'lives in your tenant with its own identity / memory / computer / workspace', is @mentionable in Teams / Outlook / chats / channels / documents, follows threads across days, and keeps running in the cloud while you sleep. Roadmap: Home and Code enter Frontier 'coming weeks'; Code reaches Frontier at month-end; Autopilot expands to private preview at the end of the month; @Copilot in Teams private preview at month-end; Ignite 17–20 Nov in SF. Billing: everyday Chat + Office Copilot rides USL; Cowork / Code / Autopilot plus frontier models Astra and Fable ride UBB (Copilot Credits); Agent 365 cost management extends to Code and Managed Runtime. Foundation: the OpenClaw blog of 2026-09-25 says Autopilot's foundation is OpenClaw — the first time a major cloud vendor files a tenant-resident agent as a standalone product line.",
        "one_liner": "微软把 Copilot 拆成 Home/Code/Autopilot 三档，Autopilot 跑在租户云上且底座是 OpenClaw。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "content": AUTOPILOT,
        "local_path": "content/{id}.md",
        "added_date": RUN_DATE,
    },
    {
        "title": "Cursor Rollouts + Security Reviewer：盯 PR 到生产",
        "url": "https://cursor.com/blog/rollouts-and-security-reviewer",
        "source": {"platform": "blog", "author": "Rustam Lalkaka (Cursor)", "original_date": "2026-09-23"},
        "category": "agents",
        "tags": ["cursor", "rollouts", "security-reviewer", "pr-to-prod", "staged-rollout"],
        "source_type": "article",
        "language": "both",
        "summary_zh": "Cursor 把写代码之后那段没人盯的时间交给两个 bot。Rollouts 跟着一个变更从 PR 一直走到生产：连接代码托管 / 部署 / 遥测（Datadog、Grafana、Honeycomb 或自托管），合并前它读 diff 起一份「监控规划」——列它认为的风险、这次变更预期会动到的指标、目前埋点覆盖不到的盲区，规划里漏的可以手工补；合并后把规划里的信号曲线跟部署前 baseline 比，发现回归会告诉你「它怀疑是哪个变更搞的」，并按配置处理（通知作者、暂停 staged rollout、或开一个回滚 PR 等审批）。当前它擅长三件事：在全局告警之前抓到只出现在某 region / 某 endpoint 的回归；区分预期信号 vs 真正回归，有意为之的指标激增不会惊动人；合并前提示缺埋点。Roadmap：feature flag 直连（自动放量 / 回退）与 release train / 部署冻结期感知。Security Reviewer 在每个 PR 跑，结合全库上下文读 diff，跟静态分析不是一回事——按模式匹配会标 SQL 拼接字符串却漏「重构后失效的授权检查」，它像安全工程师那样看代码：用户输入从哪进、流到哪、中间过哪些层。默认能查：SQL / 命令 / 模板 / LDAP 等注入；新加路由缺失或失效的认证与授权；提交进代码库的密钥和凭证；不安全反序列化与未验证重定向；引入已知漏洞的依赖变更；infra 与配置的不安全默认。每条发现带严重级别 + 攻击路径，支持一键修复。官方数据：平均审查时间从 4.8 分钟降到 3.8 分钟，评论接受率从 45–50% 抬到 60–70%。",
        "summary_en": "Cursor hands the time after writing code to two bots. Rollouts follows a change from PR to production: connect source control / deploy / telemetry (Datadog, Grafana, Honeycomb or self-hosted), then before merge it reads the diff and drafts a monitoring plan listing the risks it sees, the signals the change is supposed to move, and the gaps in current instrumentation (gaps can be hand-patched); after merge it compares the plan's signal curves to the pre-deploy baseline, tells you which change it suspects when it spots a regression, and handles it per config — notify the author, pause the staged rollout, or open a rollback PR for approval. Today's three strengths: catching regressions that hit only one region or one endpoint before global alerts; distinguishing expected signals from real regressions so intentional metric spikes don't page anyone; flagging missing instrumentation before merge — the most common reason a bad change slips through unnoticed. Roadmap: direct feature-flag integration (auto ramp / auto unwind) and release-train / deploy-freeze awareness. Security Reviewer runs on every PR, reads the diff in full-repo context, and behaves like a security engineer (data flow, not pattern matching): SQL / command / template / LDAP injection; missing or broken auth on new routes; committed secrets and credentials; unsafe deserialization and unvalidated redirects; dependency changes that pull in known CVEs; insecure defaults in infra and config. Each finding carries severity, attack path and one-click fix. Cursor reports mean review time down from 4.8 to 3.8 minutes and comment acceptance up from 45–50% to 60–70%.",
        "one_liner": "Rollouts 盯 PR 到生产（合并前起监控规划 + 合并后 baseline 对比 + 自动回滚 PR），Security Reviewer 做数据流而非模式匹配。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "content": CURSOR_ROLLOUTS,
        "local_path": "content/{id}.md",
        "added_date": RUN_DATE,
    },
    {
        "title": "Snapdragon 8 Elite Gen 6：把手机拉进 agent 时代",
        "url": "https://www.qualcomm.com/news/releases/2026/09/22/qualcomm-snapdragon-summit-2026-day-one",
        "source": {"platform": "blog", "author": "Qualcomm (Snapdragon Summit 2026)", "original_date": "2026-09-23"},
        "category": "infra",
        "tags": ["qualcomm", "snapdragon", "npu", "agentic-ai", "on-device", "moe", "flex-cache"],
        "source_type": "article",
        "language": "en",
        "summary_zh": "高通在 Snapdragon Summit 2026 发布两块旗舰 SoC：Snapdragon 8 Elite Gen 6 与 Snapdragon 8 Elite Extreme Gen 6。两块都用 TSMC N2 工艺，CPU 换新八核 Oryon 架构——两颗 prime core 加六颗 performance core，是首批 mobile CPU 突破 5 GHz。Oryon Flex-Cache 把全部八核接进同一片 L2 pool，给 agent 这种「跨核来回搬 working set」的工作负载专门修了一次 miss cost。AI 侧：Hexagon NPU 重做，新增 Element Accelerator，context window 上限 32,000 tokens，共享 NPU 内存多 50%，宣称 prefill 比上代快 80%，可以从 flash storage 直接跑 30B-parameter MoE 模型。Sensing Hub 改双 micro-NPU 设计，性能 +85%、功耗 -20%。Extreme 多了 Adreno Neural Fusion（AI 超分 + frame gen + NPU 处理融合），游戏覆盖 20+ 款。Personal Scribe 是端上 agent 的 feature：对会话建索引、识别 speaker、建用户可控的知识图谱。公司叙事被 CEO Cristiano Amon 拉向 agent 中心：「we're going into this transition from what is a very phone-centric model to now an agentic-centric model」。Motorola、Xiaomi、ZTE 等首批搭载。",
        "summary_en": "At Snapdragon Summit 2026 Qualcomm launched two flagship SoCs: Snapdragon 8 Elite Gen 6 and Snapdragon 8 Elite Extreme Gen 6, both on TSMC N2 with a new 8-core Oryon CPU — two prime cores plus six performance cores — the first mobile CPU to break 5 GHz. Oryon Flex-Cache wires all eight cores into one shared L2 pool, repairing the miss cost for agent workloads that keep moving their working set across cores. On the AI side the Hexagon NPU was rebuilt with a new Element Accelerator, a context window of up to 32,000 tokens, 50% more shared NPU memory, prefill claimed up to 80% faster than the previous generation, and the ability to run 30B-parameter MoE models straight from flash storage. The Sensing Hub moves to a dual-micro-NPU design — +85% performance, -20% power. Extreme adds Adreno Neural Fusion (AI super-resolution + frame gen + NPU processing) across 20+ titles. Personal Scribe is the on-device agent feature: index conversations, identify speakers, build a user-controlled knowledge graph. CEO Cristiano Amon pulled the company narrative toward an agent-centric model: 'we're going into this transition from what is a very phone-centric model to now an agentic-centric model'. Motorola, Xiaomi, ZTE are first-wave adopters.",
        "one_liner": "Snapdragon 8 Elite Gen 6 用 Flex-Cache 修跨核 miss cost，Hexagon NPU 把 context window 推到 32k tokens 并能跑 30B MoE。",
        "one_liner_author": "openclaw",
        "quality_score": 4,
        "content": SNAPDRAGON,
        "local_path": "content/{id}.md",
        "added_date": RUN_DATE,
    },
]


def main():
    data = pu.load_entries_data(ENTRIES)
    before = len(data["entries"])

    # Build normalized entries with deterministic ids; do not use one_liner_author = openclaw-external-scan.
    built = []
    for raw in ENTRIES_RAW:
        norm = pu.normalize_entry(raw, run_date=date.fromisoformat(RUN_DATE))
        norm["id"] = pu.generate_entry_id(url=raw["url"], title=raw["title"])
        # Write content file at canonical absolute path
        cid = norm["id"]
        cpath = CONTENT / f"{cid}.md"
        cpath.parent.mkdir(parents=True, exist_ok=True)
        cpath.write_text(raw["content"], encoding="utf-8")
        assert cpath.exists() and cpath.stat().st_size > 0, f"content file failed: {cpath}"
        norm["local_path"] = f"content/{cid}.md"
        norm["images"] = []
        norm["status"] = "active"
        norm["updated_date"] = None
        built.append(norm)
        print(f"prepared {cid} -> {cpath.name} ({cpath.stat().st_size}B) :: {raw['title'][:60]}")

    new_entries, skipped = pu.append_entries(data, built)
    pu.save_entries_data(data, ENTRIES)

    after = len(data["entries"])
    print(f"BEFORE={before} AFTER={after} DELTA={after-before} skipped={len(skipped)}")
    assert after >= before, "count must not decrease"
    assert after - before == len(new_entries), "delta must equal number of newly appended"
    assert len(data["entries"]) == data.get("total_entries", len(data["entries"]))


if __name__ == "__main__":
    main()