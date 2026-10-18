# 去重报告 · 2026-10-19 (weekly-maintain-dedup)

## 总览
- 条目数: 2781 -> 2781（不变；本轮 0 合并、0 归档、0 URL 修复，2 对 related 补链共 4 个方向）
- 上轮基线: 2703（2026-10-12 dedup 报告；2026-10-14 community-review 另归档 3 组同 URL 对），本周 intake 净增 +78；其中 added_date > 2026-10-12 的 active 新条目 62 条全部纳入本轮扫描
- Active: 2133（上周 2058），Archived: 609（上周 606，差值即 10-14 归档 3 条），score-pending: 39
- 展示卡片 2053 / 内容页 1951 / 7 频道，与 pre-run 一致（本轮未新增条目和内容页）

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
- 全库同 normalized-URL 组共 12 组，全部为 active+archived 已解决形态；active-vs-active 0 组（上上周挂起的 `ed4dc19a` vs `ffd9dfec` 已由 2026-10-14 community-review 归档解决，自此无 active 同 URL 对）。

### 2. www/apex 折叠扫描
- 按「registered domain 去 www + path (+ 净化 query)」折叠分组 active 条目: 0 组碰撞。10-14 修复的 seangoedecke www/apex 形态无回潮。

### 3. 本周新增条目（62 条 active）重复检查
- 与全库 normalized-URL / 标题碰撞: 0 组（append_entries 拦截正常）。

### 4. 精确同标题 active 组
- 12 组（上周 17 组，下降来自 10-14 community-review 归档 3 组 + 本周口径对齐），全部双向 related 齐全（0 缺链，无需补链）。12 组 URL 互不相同，按双视角/双来源保留，不合并。

### 5. fuzzy 标题相似扫描（title_key SequenceMatcher ≥ 0.88，跨全库 active）
- 共 19 对；其中 12 对即第 4 节精确同标题组。新增 7 对非精确对逐一研判（读正文比对）：
  - `a40dec6e` vs `3887fc82`（r=0.925）: 微信原文《…我的 Harness Engineering…（上）》（第一人称实践，上下两篇）vs 36kr 版《万字总结：Harness Engineering…》（LangChain/Anthropic/OpenAI/Cursor 案例综述；正文关键句 0 命中）。**确认为不同文章、不同来源**，非重复；本轮补双向 related 互链，既方便读者对照，也防止后续扫描误判为重复。
  - `b03e02c0` vs `a278a014`（r=0.978）: The Hater's Guide To AI Debt Part 1 vs Part 2，同作者系列前后篇，不同 URL。补双向 related（系列互链）。
  - `41071ca3` / `c1484164` / `6662fd56`（两两 r=0.895）: AI 影响力日报 2026-04-18 / 04-22 / 06-21，不同日期期号，非重复；期号间互链属噪音，不链。
  - `b37b2087` vs `abea8210`（r=0.987）、`a837f575` vs `469c12ee`（r=0.993）: X 帖 vs 官方源（blog.google / GitHub repo）双视角对，已有双向 related，维持现状。

### 6. 影子条目（无 URL 且 local_path 指向他人 content 文件）
- 0 条（连续保持 0）。active 无 URL 条目 local_path: 指向自身 content 文件为主，14 条指向站点外 Obsidian 笔记（属 local-path 校验职责，非重复，不处理）。

### 7. 微信 4-key 同 tuple 组
- 实际同 (__biz, mid, idx, sn) tuple 组共 7 组（与上周持平）: 6 组为同标题 active+archived 已解决形态（含 `ed827be1`/`6ebadca4` 引号差异对，title_key 相同，不动作）。
- 跨标题碰撞仍仅 `yzi1wbrv` vs `z1jgz9it`（corrupt crawl URL 案例），按 guard 继续挂起待人工，不 canonicalize、不合并（连续第五周）。
- 口径修正: 19 条短链形态 `mp.weixin.qq.com/s/<hash>`（无 __biz/mid/idx/sn query）在本轮扫描脚本首版被空 tuple 归成一组，属假阳性；逐一核对 path 后 19 条路径全部互异（WECHAT_DUP_PATHS = {}），无碰撞，不动作。

### 8. 可疑 URL（active）
- 多 https:// / CJK 内嵌 / 尾部残渣 / 未 trim / 非法 scheme: 0 条。

### 9. 完整性
- entry id 重复: 0；缺 title: 0；active 缺 score: 0；related 悬挂引用: 0
- entries=2781=total_entries，dict 结构合法

## 附加扫描（信息项）
- 占位标题 active（hash 形标题 / title==id）: 0 条，无新发现
- 时效归档扫描: active 且 added_date > 180 天且 score ≤ 3 的 article/x_post = 0 条，无归档动作
- active 缺 content 文件: 106 条（上周 101，+5 来自本周 entry-only 批次；属 content-fetcher 任务范围，非 dedup 职责）

## 标记待人工（延续，非本轮新增）
- [ ] `z8jjvpnw`：标题仍为占位 `Z8Jjvpnw`，需人工补标题（或确认文章已 404 后处理）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题 4-key 碰撞（延续）

## 验证
- `scripts/validate-schema.py`: 2781 条，0 错误，63 警告（历史 summary_zh 过短，非本轮引入，与上周持平）
- `python3 scripts/generate-site.py`: 首跑在清理 dist/ 时遇 iCloud 文件锁（OSError Errno 11 on `dist/entry 2`，Errno 66 同族瞬态）；确认无 `*.icloud` 占位后手动清理 dist 并重跑成功——2053 展示卡片 / 1951 内容页 / 7 频道，与 pre-run 一致
- 补链后复扫: 12 组精确同标题 active 组缺失双向 related = 0；active 同 URL / www-apex 折叠碰撞 = 0
- 条目数基线: worktree = HEAD = origin/main = 2781（提交前后均校验）
- `data/entries.json` 本轮仅 4 处 `related` 字段补链，count 2781 不变；`openclaw/content/` 不存在，无游离文件

## 变更文件
- `data/entries.json`（`a40dec6e`↔`3887fc82`、`b03e02c0`↔`a278a014` related 补链，count 不变）
- `openclaw/logs/dedup-report-2026-10-19.md`（本报告）
- `metadata/stats.json`（构建时间戳；README 无变化，内容页计数不变）
