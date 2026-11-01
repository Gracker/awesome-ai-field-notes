# 去重报告 · 2026-11-02 (weekly-maintain-dedup)

## 总览
- 条目数: 3022 -> 3022（不变；本轮 0 归档、0 合并、0 URL 修复、0 标题修复、0 补链、0 删除——全扫描无动作项的干净周）
- 上轮基线: 2890（2026-10-26 dedup 报告），本周 intake 净增 +132；其中 added_date > 2026-10-26 的 active 新条目 118 条全部纳入本轮扫描
- Active: 2325，Archived: 658，score-pending: 39
- 展示卡片 2248 / 内容页 2138 / 7 频道（与 pre-run 完全一致；0 数据变更故 0 增量为预期）

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
- active-vs-active 0 组（全库同 normalized-URL 组均为 active+archived 已解决形态）。

### 2. www/apex 折叠扫描
- 按「host 去 www 后整 URL 再 normalized_url_key」口径折叠（保留 path+query），0 组碰撞，无回潮。

### 3. 本周新增条目（118 条 active）重复检查
- URL normalized key 与标题 key 对全库（含 archived）碰撞: 0 组（append_entries 拦截正常，本周 intake 无重复入库）。

### 4. 精确同标题 active 组
- 12 组（上轮处置后 13 组；差值 1 组为 community-review 2026-10-28 已归档 `ae1c0b14`，与 `d74a7da1` 同标题同源、publication URL 重定向至后者 blog URL）。12 组全部双向 related 齐全（0 缺链），URL 互不相同，按双视角/双来源既定策略保留，无新增组。

### 5. fuzzy 标题相似扫描（title_key SequenceMatcher ≥ 0.88，跨全库 active）
- 共 6 对（上周 8），全部为上周已研判对且双向互链齐全，维持现状：`b03e02c0`/`a278a014`、`a40dec6e`/`3887fc82`、`4fb3bd4e`/`efaw158d`、`784b2c06`/`ad4e5293`、`21f855ac`/`65f18ea8`、`efa67a45`/`ed2cbcca`。无新对。

### 6. 影子条目清查
- 旧口径（无 URL 且 local_path 指向他人 content 文件）: 0 条。
- 跨语言/content-URL 口径（active 无 URL 条目正文出现其他 active 条目 normalized URL）: 候选 12 个，逐一比对后**全部与 2026-10-26 排除/待人工清单完全重合**，无新增影子、无归档动作：
  - 日报型（多推文聚合）: `41071ca3`、`c1484164`
  - 多主题/高链接数: `7f5b0c2f`（51 URL）、`8534a84c`、`80df7c07`（25 URL）
  - 仅命中 bare-domain（anthropic.com 首页）: `7b4f7b20`、`ad6f9ec4`、`fe920d24`
  - 存疑待人工（评论/综述/基准页型，标题自成立题）: `946806dc`、`e742a94e`、`ea3fcf10`、`ai-code-gen-benchmark-2026-06-09`

### 7. 微信 4-key 同 tuple 组
- 跨标题碰撞仍仅 `yzi1wbrv` vs `z1jgz9it`（corrupt crawl URL 案例，延续第七周），按 guard 继续挂起待人工，不 canonicalize、不合并。

## 标记待人工（延续，非本轮新增）
- [ ] `z8jjvpnw`：标题仍为占位 `Z8Jjvpnw`（延续第八周；本轮直查确认未修复，内容仍为 JS chrome/噪音，保持挂起）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题 4-key 碰撞（延续第七周）
- [ ] `21f855ac`：Petri 捐赠公告无 URL 副本，已与 `65f18ea8` 互链，待人工确认后归档
- [ ] `946806dc`：正文含 7 个不同 URL（疑似小型日报），guard 拒绝归档；可能与 `7e5d8972` 同源
- [ ] `e742a94e` / `80df7c07` / `ea3fcf10` / `ai-code-gen-benchmark-2026-06-09`：评论/综述/基准页型候选，证据不足不归档
- [ ] `antautomd`：URL 为 bare `https://www.anthropic.com`（首页无路径），正文亦无真实文章 URL 可锚定
- [ ] `cac1bcda`：无 URL，正文为 X 页面 crawl 残渣，标题为截断引语

## 附加扫描（信息项）
- 占位标题 active（hash 形标题 / title==id）: 1 条（`z8jjvpnw`，延续）
- 时效归档扫描: active 且 added_date < 2026-05-06（>180 天）且 score ≤ 3 的 article/x_post = 10 条（上周 3 条；新增 7 条为 4 月末 import 首次越线：`mcp_dev_summit_2026_001`、`gemini_3_1_pro_2026_001`、`gemini_cli_0_39_2026_001`、`microsoft_agent_framework_1_0_2026_001`、`claude_design_2026_001`、`openai_goblin_problem_2026_001`、`gemini31_flash_tts_2026_001`；延续上周口径，仅记录不动作）
- active 缺 content 文件: 114 条（上周 107；属 content-fetcher 任务范围，非 dedup 职责）

## 验证
- `scripts/validate-schema.py`: 3022 条，0 错误，66 警告（历史 summary_zh 过短等遗留警告，非本轮引入）
- `python3 scripts/generate-site.py`: 首跑在 dist 目录遇 iCloud 瞬时 `OSError: [Errno 11] Resource deadlock avoided`（残留空目录 `dist/entry 2`，类同 2026-10-17 Errno 66 案例；复查全库 *.icloud 占位 0、计数基线一致），**重试一次即通过**——2248 展示卡片 / 2138 内容页 / 7 频道
- 条目数基线: worktree = HEAD = origin/main = 3022（ls-remote `5bc9abc` 与 tracking ref 一致，提交前后均校验）
- `data/entries.json` 本轮零字段变更，count 3022 不变；`openclaw/content/` 无游离文件

## 变更文件
- `openclaw/logs/dedup-report-2026-11-02.md`（本报告）
- `metadata/stats.json`（generate-site 构建时间戳刷新；卡片/内容页计数与 pre-run 一致，无数据变化）
