# Amazon saves millions by replacing Sonnet 4.6 with Strands Decider

- **ID**: 2eaebfdb
- **原文链接**: https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider
- **PDF**: N/A
- **作者**: Carr Onstott, Mehul Jaiswal, Strands Agents Team
- **日期**: 2026-11-09
- **更新**: N/A
- **分类**: industry
- **来源类型**: article
- **标签**: production-ai, cost-optimization, decision-models, aws
- **质量评分**: 4/5
- **抓取时间**: 2026-11-11T12:24:38Z

---

## 中文导读

Strands Agents 团队案例：两名 Amazon 工程师把全球最大内部工单系统之一的标注任务从 Claude Sonnet 4.6 换成决策模型 Strands Decider。决策模型不生成文本——输入状态与一组选项，输出每个选项的概率加置信度，正好匹配工单标注（状态=工单，选项=20 类标签目录）。团队先用 Decider 2B 试点，再切换到效果更好的 E4B（Gemma 4 构建），在独立工单集上胜过生产环境 Sonnet。E4B 跑在 SageMaker ml.g5.xlarge（单卡 A10G 24GB）上，占用约 19 GiB，单请求约 640ms，单实例每小时可处理约 5600 张工单。实测每张工单：平均调用时长从 4215ms 降到 897ms（-78%），token 从 6724 降到 2010（-70%），Lambda 执行时长降 74%；成本从每百万工单约 $22,200 降到约 $500（约 44 倍，98% 削减），一年省下数百万美元。迁移用 AppConfig 三态开关（BEDROCK/DUAL/DECIDER）在真实流量上并行对比并裁决每一处分歧，回滚只是 45 秒的配置变更。另有一个值得记住的坑：JSON 键顺序会移动决策模型输出概率最多 0.19，团队因此对所有请求按键排序。

## 为什么值得关注

Amazon 用决策模型替换 Sonnet 4.6 标注工单：每百万工单 2.2 万降到 500 美元。

这是"LLM 任务拆解"的一个干净样本：当任务本质是闭集选择（固定标签目录）、量极大、且旧路径时延敏感时，把生成式 LLM 换成只输出概率的决策模型能同时拿到 44 倍成本差和 78% 时延差，而且质量不降反升。方法上最值得抄的是三态开关灰度：BEDROCK/DUAL/DECIDER 三态让新旧模型在真实流量上并行，逐条裁决分歧，比任何离线评测都有说服力，且回滚成本接近零。文中还给出了明确的适用边界：标签需要解释文本、目录每周变化、或上下文塞不进几千 token 的任务不适合；决策模型 4096-token 窗口内的长工单要裁剪最旧评论。JSON 键顺序影响概率（最高 0.19）这个发现对所有把决策模型挂在 API 后面的人都有直接警示价值。

## 关键信息

- 背景：Amazon 内部工单系统用 Claude Sonnet 4.6 标注工单（客户升级、容量请求、自动告警、安全发现等，共 20 类），每张工单携带长系统提示生成 JSON
- 方案：Strands Decider E4B（Gemma 4 构建；2B 版试点后弃用）——不生成文本，输入工单状态 + 选项列表，输出各选项概率与置信度；20 个标签改写为 1-2 句判据作为选项，外加 none 选项；长工单裁剪最旧评论以适应 4096-token 窗口
- 部署：SageMaker ml.g5.xlarge（A10G 24GB），模型占用约 19 GiB，单请求约 640ms，单实例约 5600 工单/小时；SQS 队列触发 Lambda，AppConfig 控开关，CDK 定义 Beta/Gamma/Prod 三阶段
- 实测对比：平均调用时长 4215ms → 897ms（-78%）；每工单 token 6724 → 2010（-70%）；Lambda 平均执行时长 -74%；质量上 E4B 在独立工单集上胜过生产 Sonnet
- 成本：Sonnet $0.0222/工单（$3/$15 每百万输入/输出 token，Bedrock）vs Decider 约 $0.0005/工单（$1.408/实例小时，SageMaker）；每百万工单约 $22,200 → 约 $500，约 44 倍（98% 削减）
- 灰度方法：AppConfig 三态开关 BEDROCK（仅 Sonnet）/ DUAL（并行对比）/ DECIDER（仅决策模型）；DUAL 期间逐条裁决分歧
- 坑与教训：JSON 键顺序改变输出概率最多 0.19，已改为按键排序发送；适用边界=闭集选择、高量、时延敏感；标签需要解释文本/目录频繁变化/上下文超窗则不适用
- 出处：https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider（2026-11-09）

## English Summary

Strands Agents team case study (2026-11-09): two Amazon engineers replaced Claude Sonnet 4.6 with Strands Decider - a decision model that cannot generate text, returning a probability plus confidence per option - for ticket labeling in one of the world's largest internal ticketing systems (20 category types). After a Decider 2B pilot, the E4B Gemma 4 build beat production Sonnet on a separate ticket set and runs on SageMaker ml.g5.xlarge (~19 GiB, ~640 ms/request, ~5,600 tickets/hour/instance). Per ticket: average call time 4,215 ms -> 897 ms (-78%), tokens 6,724 -> 2,010 (-70%), Lambda duration -74%; cost ~$22,200 -> ~$500 per million tickets (~44x cheaper, 98% reduction). Migration used a three-way AppConfig switch (BEDROCK/DUAL/DECIDER): both models labeled real traffic and every disagreement was judged, with rollback a 45-second config change. Notable pitfall: JSON key order changed output probabilities by up to 0.19, so requests now send sorted keys. Applicability boundary: closed choice catalogs, high volume, latency-sensitive tasks only.

## Obsidian Notes

- 内容获取路径：`opencli web read` 失败（Navigation rejected），改用 curl 抓取页面 HTML 并解析正文（约 5.9k 字符全文），关键事实（指标表、成本、开关机制、坑）均取自页面正文；抓取时间 2026-11-11。
- 中文导读与价值判断均锚定在页面正文事实上；未引用页面之外的二手报道。
- 现代站点生成器按 `content/2eaebfdb.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
