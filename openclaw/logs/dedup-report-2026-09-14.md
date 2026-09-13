# 去重报告 · 2026-09-14 (weekly-maintain-dedup)

## 总览
- 条目数: 2278 -> 2278（不变，仅 related 字段补齐）
- Active: 1633（+105 本周新增），Archived: 606（不变），score-pending: 39（不变）
- 上次周维护: 2026-09-07 (432714c)，当时基线 2173；本周 intake 新增 105 条
- 内容页: 1312，展示卡片: 1403（pre-run 一致）

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
active-vs-active 0 组。11 组为 active:1 + archived:1 已解决形态（与上周一致），无需处理。

### 2. active 无 URL 影子条目
0 个新影子（2026-08-31/09-07 两轮已清完）。status 分布与 09-07 dedup 提交完全一致，无漂移。

### 3. 同 URL 不同形态真实重复（1 组，本轮唯一修复）
- `0cd51786` (www.seangoedecke.com/dont-build-tools-for-ai-agents, 2026-09-12, score 4)
- `a17f7018` (seangoedecke.com/dont-build-tools-for-ai-agents, 2026-09-13, score 4)
- 同一篇文章（Sean Goedecke "Don't build tools for AI agents"），`www.` 与裸域两种 URL 形态，`normalized_url_key()` 不归一 host 前缀所以硬去重漏过。
- 处理：两侧内容页均 grounded 非空（0cd51786=1683B，a17f7018=8284B），摘要视角不同（AK-RSS 编译 vs 英文全文双语），按 skill 保守原则保留两条、补双向 `related`，不归档不合并。

### 4. 同标题 active 双胞胎
精确同标题 active 组共 12 组，其中 11 组本周无新增、多为不同事件/一人多名弱证据，维持现状（同 09-07 结论）。仅上节 Goedecke 组为本周新增同文，已互链。

### 5. 微信 4-key 跨标题碰撞（延续待人工）
- `yzi1wbrv` (Claude Code 浏览器自动化方案) vs `z1jgz9it` (Google I/O 2024 Gemini) 仍共享同一 4-key tuple，按 guard 不归一不合并，继续挂起。

### 6. 占位符/空摘要 active（趋势警示，非本轮动作）
- 两摘要全空的 active 条目 185 条（上周同口径约 28 条），多为 score=3 无内容文件的抓取失败条目。属 content-fetcher 职责，本轮不动，建议后续批量重抓或降级 score-pending。

### 7. 其他
- active URL 异常（多 https:// / CJK 内嵌 / X 模板）：0 条
- entry id 重复：0；缺 title/score：0

## 验证
- `data/entries.json`: dict 结构，entries=2278=total_entries，本地=HEAD=origin/main=2278
- 仅 `related` 字段变更（+2 引用），条目数不变，无 status/归档操作
- `scripts/validate-schema.py` 与 `generate-site.py` 见下方回执

## 待人工确认（延续）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题碰撞
- [ ] 185 条空摘要 active（content-fetcher 重抓或降级）

## 变更文件
- `data/entries.json`（related 字段 +2 引用）
- `metadata/stats.json`（last_updated 时间戳）
- `openclaw/logs/dedup-report-2026-09-14.md`（本报告）
