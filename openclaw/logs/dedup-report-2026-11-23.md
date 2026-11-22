# 去重报告 · 2026-11-23 (weekly-maintain-dedup)

## 总览
- 条目数: 3464 -> 3464（不变；本轮 0 归档、0 合并、0 URL 修复、0 补链 —— clean-sweep 周，连续第二周零动作）
- 上轮基线: 3329（2026-11-16 dedup 报告），本周 intake 净增 +135；`added_date >= 2026-11-16` 的全部 135 条新条目均纳入本轮扫描，当前全部 active
- Active: 2766 / Archived: 698（当前分布；变动来自本周 intake，非本轮动作）
- 展示卡片 2688 / 内容页 2566 / 7 频道（generate-site 持平，预期内）

## 本轮动作
无。全量扫描未发现可安全执行的去重/修复动作，`data/entries.json` 本轮零字段改动。

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
- active-vs-active 0 组。

### 2. www/apex 折叠扫描
- 按「host 去 www 后整 URL 再 normalized_url_key」口径（保留 path+query），0 组碰撞，无回潮。

### 3. 本周新增条目（135 条，>= 2026-11-16 全口径）重复检查
- URL normalized key 对全库（含 archived）碰撞: 0 组；标题 key 对全库碰撞: 0 组。append_entries 拦截正常，本周 intake 无重复入库。

### 4. 精确同标题 active 组
- 12 组（11-16 报告记 10 组，差额系两轮计数口径差异，非数据变化；12 组全部早于本周窗口）。全部双向 related 齐全（缺链 0），URL 互不相同，按双视角/双来源既定策略保留；0 组涉及本周新增条目。

### 5. fuzzy 标题相似扫描（lenratio>=0.80 预过滤，SequenceMatcher >= 0.88，new-vs-active；另对历史研判对逐对复核）
- 本周新增 135 条 vs 全库 active: 0 对命中。
- 历史已研判 8 对逐对复核: `a837f575`/`469c12ee`、`abea8210`/`b37b2087`、`b03e02c0`/`a278a014`、`a40dec6e`/`3887fc82`、`4fb3bd4e`/`efaw158d`、`784b2c06`/`ad4e5293`、`21f855ac`/`65f18ea8`、`efa67a45`/`ed2cbcca` —— 全部 active、双向互链齐全、双侧均有 content 文件，维持现状。

### 6. 影子条目清查（active 无 URL 条目正文含其他 active 条目 normalized URL，distinct <= 6 口径）
- 候选 8: 已知 carryover 5 条（`8534a84c`、`41071ca3`、`c1484164`、`ea3fcf10`、`e742a94e`，延续不归档）+ 新候选 3 条 `7b4f7b20`、`ad6f9ec4`、`fe920d24`。
- 3 条新候选经逐一核查均为 **bare-domain 误报，按 guard 排除不归档**: 三者正文（X 帖抓取件）仅含 `antautomd` 的 artifact 首页链接 `https://www.anthropic.com`，与 antautomd 的 normalized key 碰撞；实际标题/内容为完全不同的文章（Claude Opus 4.6 BrowseComp eval 泄露 X 帖 / Anthropic 81,000 人质性研究 X 帖 / Anthropic Interviewer X 帖），标题相似度扫描（>=0.60）0 命中，无双胞胎。
- `antautomd` 自身 content 页同样只锚定首页链接，无可修复的真实文章 URL，bare-URL 挂起延续。

### 7. 微信 4-key 同 tuple 组
- 共 7 组，与 11-16 完全一致: 6 组为已解决形态（active 有 content + archived 孪生，双向 related 齐全）；active+active 跨标题碰撞仍仅 `yzi1wbrv` vs `z1jgz9it`（corrupt crawl URL 案例，延续第十一周），按 guard 继续挂起待人工，不 canonicalize、不合并。

### 8. 新增条目可疑 URL 扫描（static-asset / bare-domain / multi-http / URL 内 CJK）
- 135 条新增中 0 条。

### 9. 占位标题 active
- 1 条（`z8jjvpnw`，标题 `Z8Jjvpnw`，title==id 口径复核，延续第十一周；内容仍为 JS chrome/噪音，保持挂起）。

### 10. 全局单向 related 扫描（active -> active 所有 related 边）
- 0 条（本周新增条目未引入单向链）。

### 11. 新增条目 local_path 抽查
- 135 条中 0 条非标准 —— 本周 intake 全部为 canonical `content/{id}.md` 或省略，无 vault 源笔记指针回潮（11-04 口径）。

### 12. 时效归档扫描（active 且 added_date < 2026-05-23 且 score <= 3 的 article/x_post）
- 14 条（上周同口径 0 条系时间窗差异）: 上周已记录的 10 条（`hn_llm_agents_2026_003`、`hermex_001`、`hermes_001`、`mcp_dev_summit_2026_001`、`gemini_3_1_pro_2026_001`、`gemini_cli_0_39_2026_001`、`microsoft_agent_framework_1_0_2026_001`、`claude_design_2026_001`、`openai_goblin_problem_2026_001`、`gemini31_flash_tts_2026_001`）+ 本周首次越线 4 条（`ac_agview01`、`tx_know01`、`ldb_v2201`、`html_md01`）。延续四周既定口径，仅记录不动作。

## 标记待人工（延续，非本轮新增）
- [ ] `z8jjvpnw`：标题仍为占位 `Z8Jjvpnw`（延续第十一周）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题 4-key 碰撞（延续第十一周）
- [ ] `21f855ac`：Petri 捐赠公告无 URL 副本，已与 `65f18ea8` 互链，待人工确认后归档
- [ ] `946806dc`：正文含 7 个不同 URL（小型日报型），guard 拒绝归档
- [ ] `e742a94e` / `80df7c07` / `ea3fcf10` / `ai-code-gen-benchmark-2026-06-09`：评论/综述/基准页型候选，证据不足不归档
- [ ] `antautomd`：URL 为 bare `https://www.anthropic.com`（本轮复核：自身 content 亦无真实文章 URL 可锚定）
- [ ] `cac1bcda`：无 URL，正文为 X 页面 crawl 残渣
- [ ] `2755621b`：URL 为 bare `https://pleasedonotescape.com/`（项目首页；无 content 文件，不修复仅标记，延续观察）

## 附加扫描（信息项）
- active 缺 content 文件口径延续（属 content-fetcher 任务范围，非 dedup 职责）。
- 新增 crawl-artifact 复核: 0（本周新增 135 条无可疑 URL，local_path 全部合规）。

## 验证
- `scripts/validate-schema.py`: 3464 条，0 错误，68 警告（遗留，非本轮引入，与上周持平）
- `python3 scripts/generate-site.py`: 2688 展示卡片 / 2566 内容页 / 7 频道（持平，entries.json 零改动）
- 条目数基线: worktree = HEAD = origin/main = 3464（提交前后均校验）
- `data/entries.json`: dict 形态，3464 不变，`len(entries) == total_entries`

## 变更文件
- `openclaw/logs/dedup-report-2026-11-23.md`（本报告）
- `metadata/stats.json`（generate-site 构建时间戳刷新）
- `data/entries.json`：零改动（count 3464 不变）
