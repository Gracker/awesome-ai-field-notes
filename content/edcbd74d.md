# There are no lossless transformations of natural-language text

> Source: https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text
> Author: Sophie Alpert
> Original date: 2026-06-25
> Added by: AAIF daily-intake-evening 2026-08-13

## 摘要
Sophie Alpert 的写作政策把 AI 改稿问题落到“自然语言没有无损变换”这一原则：每次重写都会改变含义，作者必须为每句话负责，写作本身就是思考，读者时间比作者时间更贵。它适合团队制定 AI 写作边界：可以用工具辅助，但不能把没有理解的句子外包给模型。

## English Summary
The essay argues that natural-language text cannot be transformed losslessly: edits change meaning, and writers remain responsible for every sentence. It frames writing as thinking and warns teams against outsourcing meaning to an AI rewrite pass.

## 入库理由
- quality_score: 4
- category: learning
- tags: ai-writing, writing-policy, llm-collaboration, natural-language
- one_liner: AI 改稿不是无损压缩；没有理解就交给模型重写，会丢掉意义。

## Obsidian evidence excerpt
```markdown
模型把自己推理痕迹当权威上下文"这件事直接抛到台面——对做 red team / agent 防御的工程师必须读。
  摘要：原论文（alphaxiv 2608.09867）发现同一家族模型共用加密密钥，导致 frontier 模型的 reasoning 块可以被喂回 Haiku 类弱模型，prompt 诱导输出未加密的原 thought；所有模型在漏洞报告后都已封堵，但截获的 GPT-5.5 原始推理片段（如"Need app.css truncated"）首次公开。
  链接：https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/

## 3. Sophie Alpert (via Simon Willison)：There are no lossless transformations of natural-language text
- 标题：让 ChatGPT 帮你改稿是单向信息损耗——这是 Clay 团队的官方 AI 写作政策
  评分：8.2/10
  推荐语：Clarity 比典型的"AI 别用了" / "AI 随便用" 都更落地：把"你必须为每句话负责" / "长文不是更好" / "读者时间 > 你的时间" 这些原则变成具体的可执行政策，AI 协作团队可以直接照搬。
  摘要：全部四条原则是"为每句话站桩 / 写作就是思考 / 写稿时间 > 阅读时间 / 长 ≠ 好"——核心是"自然语言没有无损变换"：每次改写都改变意义，如果改写者没有最细的脑内模型，信息就丢失；引一句"个人化在标准 loss 函数下就是带弯路的回归均值"。
  链接：https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text

## 4. Gary Marcus：Circular financing reaches new heights
- 标题：华尔街的钱用来帮 Nvidia 客户买 Nvidia——Jim Chanos 隔空附议
  评分：7.6/10
  推荐语：把 Nvidia 最后一轮 $500B 融资归属、NVDA 5Y CDS 翻倍、Chanos 暗示"2031 国会听证"三个证据拼成单页短文，比 Ed Zitron 的长版更适合在群里直接转图——同时支持 Ed Zitron 上条"70% AI 营收押注两家不可持续实验室"的判断。
  摘要：作者引用 The Information 表格展示 NVIDIA 用同一笔资金循环买自家 GPU 的结构；Holger Zschaepitz 推文指出 NVDA 5 年 CDS 自 5 月底从 41.6 翻至 77.5；Chanos 直言"下次他们同桌讲 AI 融资，估计是在 2031 国会"。
  链接：https://garymarcus.substack.com/p/breaking-circular-financing-reaches

## 5. iDiallo：Where Did the Productivity Gains Go?
- 标题：把 KPI 提高 10 倍那天，你的工位就被"reset"了——AI 时代这条规律没变
  评分：7.5/10
  推荐语：把"AI 让经理自己写 app"这件当下热议的事根回到一个 2010 年代非营利组织数据录入员的真实经历；"高产成为新基线，然后是 baseline reset" 这条规律的现成案例，比纯理论更好读。
  摘要：作者 2010 年代在非营利组织用 Excel 表单 + 校验流程把录入效率从 12 条/天提到 100+ 条/天，结果新基线成了"经理对合理产量的预设"，自己被裁后接替者无法达到新基线也被裁；他把今天的 AI 写 app 现象接到同一台机器——高产可以被 API 拿走，但高产变成代价是同一条循环。
  链接：https://idiallo.com/blog/where-did-the-productivity-gains-go

---

## 今日共筛 50 源

- 命中 AK 口味（AI agents / frontier AI / 深度操作洞见 / 高密度非鸡汤长文）：13 条
- 入围正文级打分 ≥ 7.5：5 条
- 昨日已收录、本日 RSS 重复出现的（5 条核心 + 多条观察项）：见昨日 digest，本次不重复收录
- 跳过但保留链接作为观察项：见下方"观察项"

## 观察项（未达 7.5 分门槛，列出来作记录）
- #6 Anthropic：How Claude marks AI-generated content（EU AI Act Article 50(2) 合规细则，原始文档级，7.2）
- #7 Pluralistic (Cory Doctorow) 已转 Lauren Leek 原文同主题（昨日已收录）
- #8 Anthropic 透明度水印 + C2PA /
```

## Fetched source body
# There are no lossless transformations of natural
> 作者: Sophie Alpert
> 发布时间: 2026-06-25T00:00:00.000Z
> 原文链接: https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text

---

## There are no lossless transformations of natural-language text

June 25, 2026

_In my work at [Clay](https://www.clay.com/careers) I recently wrote an internal policy on acceptable use of AI writing by engineers, and I’m sharing it here. It’s my hope that one day better AI tools might be able to help us think, but until then I fear that using AI to write does the exact opposite._

Good writing is a tool to clearly communicate ideas from your brain into someone else’s.

As of 2026, AI models — despite their coding ability — are not yet at a point where their unedited output will achieve this goal; you as an author need to take the time to make sure that all of the ideas in the writing are the ideas that you personally intend to convey (including the structure and wording that determines which ideas are emphasized) and that the documents are a good use of your readers’ time.

It’s allowed to use AI tools while brainstorming or drafting your writing and certainly while proofreading, but make sure to consider the following principles while doing so:

-   **You must stand behind every idea and every sentence in your docs.** It is your responsibility to make sure that the entire document is representative of your own thoughts before you share it. If a reviewer asks, “What did you mean by this line?”, it’s not acceptable to reply with “Oh sorry, AI wrote that, just ignore it.” You will confuse your readers (and waste their time) if you present them things that are not genuinely representative of your thoughts. In some cases, readers will recognize and call out the incongruous parts; in others, they will be misled as to what your actual thoughts are.

-   **Writing is thinking.** Spending time on the writing process — on deciding what to emphasize and how to structure your ideas clearly — teaches you more about your topic. If you circumvent this process, you will probably walk away with a poorer understanding of the subject matter. In many cases, written artifacts like tech specs, project status updates, and incident retrospectives serve as a “proof of thought”. The artifact itself is not the only goal; instead, _detailed thinking about the problem_ is the goal. Outsourcing the creation of these documents to AI (so that you can skip the thinking) risks circumventing this very purpose. Even if working with AI helps you think through a problem, you’ll understand it better if you thoroughly review the result yourself.

-   **More time should be spent authoring a document than consuming it.** If you generate a document from a short prompt then ask your readers to go through the longer output, you are disrespecting their time. They can always talk to ChatGPT themselves if they want to. Most docs are written by one person but are read by many people, so any extra time that readers need to spend to understand what you meant incurs a multiplicative cost on the team’s time. Conversely, if you spend extra time to make your document clear and concise before sending it, you are paying a one-time cost that every reader will benefit from.

-   **Longer is not better.** Pascal once wrote, “I have made this \[letter\] longer than usual because I have not had time to make it shorter.” AI makes it much easier to generate a long doc, and one of its strategies is to include many sentences that don’t say much at all and detract from the actual content. If you are producing a longer piece of writing from a shorter prompt, consider instead just sharing the prompt itself. If you use AI to edit without lengthening, vacuous sentences are less of a risk but your meaning may still get obscured.

    There are no lossless transformations of natural-language text — every rewrite and rephrase changes the meaning of your writing, and if this is done by an entity that doesn’t have the most detailed mental representation of what you personally were trying to communicate, information will be lost. Readers will appreciate hearing _your_ thoughts, even at the expense of supposed “polish”.

It’s also OK to quote AI generations verbatim that don’t meet the above standards if you mark them clearly as such. Sometimes it’s useful to say like “Claude offered this idea, do you think it’s worth looking more into?”, and this is allowed.

As AI tools improve over time at theory of mind and get better at writing, it may make sense to lean more heavily on them, but the principles above will remain important.
