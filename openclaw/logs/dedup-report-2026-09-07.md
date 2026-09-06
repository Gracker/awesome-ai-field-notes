# 去重报告 · 2026-09-07 (weekly-maintain-dedup)

## 总览
- 条目数: 2173 -> 2173（不变，仅 related 字段补齐）
- Active: 1470（不变），Archived: 654（不变），score-pending: 49（不变）
- 上次周维护: 2026-08-31 (d9190f6)

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
11 组（同上周），全部 active:1 + archived:1 已解决形态，无 active-vs-active 重复。

### 2. 微信 4-key 同条目组
7 组（同上周），全部为 active 孪生 + archived 影子已解决形态。跨标题碰撞组维持现状：
- `yzi1wbrv` (Claude Code 浏览器自动化) vs `z1jgz9it` (Google I/O 2024) 共享同一 4-key tuple，仍为待人工确认
- `ed827be1` (archived) vs `6ebadca4` (active) 同 4-key、同主题（Hermes Agent Self-Improving），标题差异仅一处弯引号/直引号；本轮只补双向 `related`，不归档合并（archived 一方为早期不同引号抓取，已归档）

### 3. 同标题 active 双胞胎软重复（7 对补 related）
均为不同来源域（X vs 博客、WeChat vs GitHub、simonwillison vs embracethered 等），代表同一事件的不同视角/解读，按 skill 原则保留全部条目、补双向 related：
- 84245f6d <-> ngiorjuh  (OpenAI Agents SDK: archive + github)
- 620c2c09 <-> acf45c2e  (AISI unsanctioned agent report: simonwillison + aisi.gov.uk)
- 146822d4 <-> 0620f79b (Claude Code Opus 5 automode: simonwillison + embracethered)
- c7ae024c <-> 20919fd9  (rumour bug security: anil.recoil + simonwillison)
- de87b052 <-> a8381bb9  (sean goedecke model strength)
- 5711341a <-> 77633995  (misaligned reward seeker: alignment.anthropic + x)
- 6ebadca4 <-> ed827be1  (Hermes Agent Self-Improving 微信同文 active+archived 互链)

剩余其他 385 组精确同标题但实为不同事件或一人多名译法的情况，弱证据，不动。

### 4. active 无 URL 影子条目
0 个新影子（上次 d9190f6 已清完），无新归档。

### 5. 占位符/空摘要 active
28 条，全部 score=3 且有 URL（多为抓取失败或英文低信号条目）。本轮不动（按 skill 建议保守处理；如需降级为 score-pending 留给 content-fetcher 后续重抓）。

### 6. URL 形态异常（重复 https:// / 中文标注）
0 条（与 2026-08-31 一致）。

### 7. active 中 X 模板 status URL
0 条（自 2026-08-24 后无新增 active 模板形态）。

### 8. active 缺内容文件
262 条。本轮不动（属于 content-fetcher 任务范围，非 weekly-dedup 职责）。

### 9. entry id 重复
无。

## 验证
- `data/entries.json`: dict 结构，entries=2173=total_entries，本地=HEAD=origin/main=2173
- 仅 `related` 字段变更（新增 14 条引用），条目数不变，无 status/归档操作
- `scripts/validate-schema.py`: 0 错误 / 51 警告（与 HEAD 数量级一致；warnings 均为 summary_zh 过短遗留，count must not decrease 规则不禁止）
- `generate-site.py`: 成功，展示卡片 1299、内容页 1212、7 channels（与 pre-run 一致）

## 待人工确认（延续）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题碰撞
- [ ] 28 条 score=3 有 URL 的占位符 active 条目（建议 content-fetcher 重抓或降级 score-pending）

## 变更文件
- `data/entries.json` (+37/-14, related 字段)
- `metadata/stats.json` (+1/-1, last_updated 时间戳)
