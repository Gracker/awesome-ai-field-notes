# 去重报告 · 2026-11-16 (weekly-maintain-dedup)

## 总览
- 条目数: 3329 -> 3329（不变；本轮 0 归档、0 合并、0 URL 修复、0 补链 —— clean-sweep 周）
- 上轮基线: 3155（2026-11-09 dedup 报告），本周 intake 净增 +174；`added_date >= 2026-11-09` 的全部 174 条新条目（154 条 > 11-09 窗口 + 20 条 11-09 当日 dedup 运行后晚间入库）均纳入本轮扫描，当前全部 active
- Active: 2631 / Archived: 698（当前分布；较上轮的变动来自本周 intake 与存量 status 迁移，均非本轮动作）
- 展示卡片 2554 / 内容页 2435 / 7 频道（generate-site 持平，预期内）

## 本轮动作
无。全量扫描未发现可安全执行的去重/修复动作，`data/entries.json` 本轮零字段改动。

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
- active-vs-active 0 组。

### 2. www/apex 折叠扫描
- 按「host 去 www 后整 URL 再 normalized_url_key」口径（保留 path+query），0 组碰撞，无回潮。

### 3. 本周新增条目（174 条，>= 2026-11-09 全口径）重复检查
- URL normalized key 对全库（含 archived）碰撞: 0 组；标题 key 对全库碰撞: 0 组。append_entries 拦截正常，本周 intake 无重复入库。

### 4. 精确同标题 active 组
- 10 组（与 2026-11-11 community-review 口径一致；较 11-09 报告的 12 组 -2，差额系该轮处理结果，非本轮变化），全部双向 related 齐全（缺链 0），URL 互不相同，按双视角/双来源既定策略保留；0 组涉及本周新增条目。

### 5. fuzzy 标题相似扫描（lenratio>=0.80 预过滤，SequenceMatcher >= 0.88；另对历史研判对逐对复核）
- 本轮 pair 扫描 6 对: `a837f575`/`469c12ee`（0.993，同一 awesome-gpt-image-2 仓库的 X 转帖 vs GitHub 原仓，互链齐全）、`abea8210`/`b37b2087`（0.987，Gemini 3.1 Flash TTS blog.google vs X 帖，互链齐全）、`b03e02c0`/`a278a014`（AI Debt Part 1/Part 2 系列）+ 3 对「AI 影响力日报」不同日期（04-18/04-22/06-21，日报系列非重复）。
- 历史已研判 5 对逐对复核: `a40dec6e`/`3887fc82`、`4fb3bd4e`/`efaw158d`、`784b2c06`/`ad4e5293`、`21f855ac`/`65f18ea8`、`efa67a45`/`ed2cbcca` —— 全部 active、双向互链齐全、双侧均有 content 文件，维持现状。

### 6. 影子条目清查（active 无 URL 条目正文含其他 active 条目 normalized URL，distinct <= 6 口径）
- 候选 5: `8534a84c`、`41071ca3`、`c1484164`（日报型，正文含 5-6 个不同条目 URL）、`ea3fcf10`、`e742a94e`（评论/综述型 carryover）——均为此前已研判不归档类型，0 个新候选，0 归档。

### 7. 微信 4-key 同 tuple 组
- 共 7 组: 6 组为已解决形态（active 有 content + archived 孪生，双向 related 齐全: 3ba81f9b/5cd27591、26184842/6069359f、4e61a655/f805ddc5、hqm6txq4/8wchcs0s、ed827be1/6ebadca4、6c7b1051/f8e37279）；active+active 跨标题碰撞仍仅 `yzi1wbrv` vs `z1jgz9it`（corrupt crawl URL 案例，延续第十周），按 guard 继续挂起待人工，不 canonicalize、不合并。

### 8. 新增条目可疑 URL 扫描（static-asset / bare-domain / multi-http / URL 内 CJK / feed-doc）
- 174 条新增中 0 条。

### 9. 占位标题 active
- 1 条（`z8jjvpnw`，标题 `Z8Jjvpnw`，base62 口径复核，延续第十周；内容仍为 JS chrome/噪音，保持挂起）。

### 10. 全局单向 related 扫描（active -> active 所有 related 边）
- 0 条（2026-11-11 community-review 修复 43 条后无回潮，本周新增条目未引入单向链）。

### 11. 新增条目 local_path 抽查
- 3 条（`dd9c87ee`、`14bce339`、`18188c8a`）指向自身未来 `content/{id}.md` 且文件尚未生成 —— 属 content-fetcher 正确目标，不修复（11-04 口径）。

### 12. 时效归档扫描（active 且 added_date < 2026-05-19 且 score <= 3 的 article/x_post）
- 0 条（上周口径下的 10 条已随时间窗移出范围，仅记录）。

## 标记待人工（延续，非本轮新增）
- [ ] `z8jjvpnw`：标题仍为占位 `Z8Jjvpnw`（延续第十周）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题 4-key 碰撞（延续第十周）
- [ ] `21f855ac`：Petri 捐赠公告无 URL 副本，已与 `65f18ea8` 互链，待人工确认后归档
- [ ] `946806dc`：正文含 7 个不同 URL（小型日报型），guard 拒绝归档
- [ ] `e742a94e` / `80df7c07` / `ea3fcf10` / `ai-code-gen-benchmark-2026-06-09`：评论/综述/基准页型候选，证据不足不归档
- [ ] `antautomd`：URL 为 bare `https://www.anthropic.com`（首页无路径，无锚定证据）
- [ ] `cac1bcda`：无 URL，正文为 X 页面 crawl 残渣
- [ ] `2755621b`：URL 为 bare `https://pleasedonotescape.com/`（项目首页；无 content 文件，不修复仅标记，延续观察）

## 附加扫描（信息项）
- active 缺 content 文件: 约 124 条口径延续（属 content-fetcher 任务范围，非 dedup 职责）；本周新增 174 条中抽查 0 条 local_path 指向非 `content/` 路径。
- 新增 crawl-artifact 复核: 0（本周新增条目无可疑 URL）。

## 验证
- `scripts/validate-schema.py`: 3329 条，0 错误，68 警告（遗留，非本轮引入）
- `python3 scripts/generate-site.py`: 2554 展示卡片 / 2435 内容页 / 7 频道（持平，entries.json 零改动）
- 条目数基线: worktree = HEAD = origin/main = 3329（提交前后均校验）
- `data/entries.json`: dict 形态，3329 不变，`len(entries) == total_entries`

## 变更文件
- `openclaw/logs/dedup-report-2026-11-16.md`（本报告）
- `metadata/stats.json`（generate-site 构建时间戳刷新）
- `data/entries.json`：零改动（count 3329 不变）
