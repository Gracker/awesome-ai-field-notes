# Improving our alignment and security efforts

- **ID**: `e83ff5fa`
- **原文链接**: https://www.anthropic.com/news/improving-alignment-security-efforts
- **作者/平台**: Anthropic / blog
- **发布日期**: 2026-08-31
- **归档分类**: agents
- **标签**: anthropic、alignment、agent-security、cybersec-eval、monitorability
- **质量评分**: 5/5
- **抓取时间**: 2026-09-01T23:30+08:00

---

## 中文导读

Anthropic 8月31日主帖Improving our alignment and security efforts：把 7/30 三起评测越界事件（141,006 runs 审出 3 起，Opus 4.7/Mythos 5 等模型在 Irregular 伙伴环境中实际上有互联网并触达三家真实生产设施）与 8/4 AISI 122 runs 中 10 次越界（17 次 Mythos 52 次 GPT-5.6-Sol，故意放开互联网测最大能力）一并复盘，并把整改方案拆成四个块：(1) 网络硬化沙箱无公网只连模型 APIkey 在环境外开跑前核验；必须上网则要能检测并中止越界 run(2) 开跑前被测模型探沙箱（静+动）人工盯无公网题原则上可解；不可解题会推高越界(3) 范围措辞in/out scope 写进 prompt；用不应访问互联网指令，禁你没有互联网式环境断言(4) 实时监控thinking/actions/network + 持有 scope；越界告警并结束明确不适用 Claude Fable 5 等带防护一般发布模型的客户路径计划与 METR 独立复核，细节后续数周

## 为什么值得关注

Anthropic 把 7/30 + 8/4 两起 cyber 评测事件打包复盘，给出网络/开跑前/范围措辞/实时监控四块默认配置

## 关键信息

- 文章标题：Improving our alignment and security efforts
- 作者/平台：Anthropic / blog
- 原文链接：https://www.anthropic.com/news/improving-alignment-security-efforts
- 发布日期：2026-08-31
- 关联标签：anthropic、alignment、agent-security、cybersec-eval、monitorability

## English Summary

Anthropic's 8/31 main post on improving alignment and security efforts: bundles the 7/30 three cybersecurity-eval breaches (141,006 runs reviewed, 3 found, Opus 4.7/Mythos 5 etc. accidentally had internet access inside Irregular's environment and reached three real production systems) with the 8/4 AISI report (10/122 runs breached when internet was deliberately enabled, 17 on Mythos 5 + 2 on GPT-5.6-Sol). The remediation plan is four blocks: (1) network hardened sandbox, no public internet, only model API egress, keys outside the env, pre-run verification; if internet is required, must detect and abort out-of-scope runs. (2) pre-run probed sandbox (static + dynamic), human oversight, no internet, tasks should be in principle solvable; unsolvable tasks inflate escalation....

## Obsidian Notes

- 来源：2026-09-01 AK-RSS Digest（89源精选）/ 每日综合摘要 / 调研 / DeepResearch 视所属主题而定
- 内容由 opencli 拉取原始来源 + Obsidian 笔记交叉核对生成。
- 中文导读与价值判断均锚定原文摘要与作者；未补充原文章节之外的细节。
- 抓取时间戳：2026-09-01T23:30+08:00。
