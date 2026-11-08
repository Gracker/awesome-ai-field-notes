# 去重报告 · 2026-11-09 (weekly-maintain-dedup)

## 总览
- 条目数: 3155 -> 3155（不变；本轮 1 归档、0 合并、0 URL 修复、1 孤儿重复文件删除、2 处补链）
- 上轮基线: 3022（2026-11-02 dedup 报告），本周 intake 净增 +133；其中 added_date > 2026-11-02 的 active 新条目 121 条全部纳入本轮扫描
- Active: 2458 -> 2457，Archived: 658 -> 659，score-pending: 39
- 展示卡片 2381 -> 2380 / 内容页 2261 -> 2260 / 7 频道（各 -1 为归档影子条目 `b5a533ae` 的卡片与内容页下线，属预期）

## 本轮动作
1. 归档跨语言影子条目 `b5a533ae`（Anthropic 81,000 用户经济展望研究 X 帖中文版；条目无 URL，正文含孪生条目 `e7f182c9` 的 `anthropic.com/research/81k-economics` URL）。guards 全过：孪生 active + 有 URL + 有自己的 content 页；孪生 URL 确在影子正文；影子正文 distinct URL 3 ≤ 6（排除日报型）；分数 3 vs 3 无吸收。`related` 双向补链，`updated_date=2026-11-09`。
2. 删除孤儿 tracked 重复文件 `content/b4ceed50.md`：与 `content/b5a533ae.md` 字节级完全相同（1055 字节）；entries.json（worktree 与 HEAD）均无 `b4ceed50` 条目；除自身与 `b5a533ae.md` 的 YAML frontmatter 外全库引用扫描 0 命中；文件来自早期 vault sync 提交（8a349d1）。同内容副本保留于 `content/b5a533ae.md`（随归档条目保留在库）。附带发现：`b5a533ae.md` 的 YAML frontmatter 内嵌 stale `id: b4ceed50`（仅 frontmatter 记录，站点生成按文件名取 id，无渲染影响，不改动）。

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
- active-vs-active 0 组（全库同 normalized-URL 组均为已解决形态）。

### 2. www/apex 折叠扫描
- 按「host 去 www 后整 URL 再 normalized_url_key」口径折叠（保留 path+query），0 组碰撞，无回潮。

### 3. 本周新增条目（121 条 active）重复检查
- URL normalized key 与标题 key 对全库（含 archived）碰撞: 0 组（append_entries 拦截正常，本周 intake 无重复入库）。

### 4. 精确同标题 active 组
- 12 组（与上轮持平），全部双向 related 齐全（0 缺链），URL 互不相同，按双视角/双来源既定策略保留；0 组涉及本周新增条目。

### 5. fuzzy 标题相似扫描（全 active 两两，lenratio≥0.80 预过滤，title_key SequenceMatcher ≥ 0.88）
- 共 18 对 = 12 对精确同标题组（ratio 1.0，见第 4 节）+ 6 对历史已研判对（0.886–0.971：`b03e02c0`/`a278a014`、`a40dec6e`/`3887fc82`、`4fb3bd4e`/`efaw158d`、`784b2c06`/`ad4e5293`、`21f855ac`/`65f18ea8`、`efa67a45`/`ed2cbcca`，逐一复核全部 active 且双向互链齐全）+ 0 新对。
- `d0fd8a1b`（I/O 2026: Welcome to the agentic Gemini era，0.903）与 `b10a3315`（Sundar Pichai keynote 帖）复核为同一 event 的两篇不同官方文章（blog.google 两个不同页面），且双向 related 已存在——维持现状，无动作。

### 6. 影子条目清查
- 跨语言/content-URL 口径（active 无 URL 条目正文出现其他 active 条目 normalized URL）: 候选 13 = 上轮 12 个 carryover（结论不变：日报型/多主题/bare-domain/评论综述型，均不归档）+ 本轮新发现 1 个（`b5a533ae`，已按 guard 归档，见动作 1）。

### 7. 微信 4-key 同 tuple 组
- 跨标题碰撞仍仅 `yzi1wbrv` vs `z1jgz9it`（corrupt crawl URL 案例，延续第八周），按 guard 继续挂起待人工，不 canonicalize、不合并。

## 标记待人工（延续，非本轮新增）
- [ ] `z8jjvpnw`：标题仍为占位 `Z8Jjvpnw`（延续第九周；本轮直查 status=active，内容仍为 JS chrome/噪音，保持挂起）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题 4-key 碰撞（延续第八周）
- [ ] `21f855ac`：Petri 捐赠公告无 URL 副本，已与 `65f18ea8` 互链，待人工确认后归档
- [ ] `946806dc`：正文含 7 个不同 URL（小型日报型），guard 拒绝归档
- [ ] `e742a94e` / `80df7c07` / `ea3fcf10` / `ai-code-gen-benchmark-2026-06-09`：评论/综述/基准页型候选，证据不足不归档
- [ ] `antautomd`：URL 为 bare `https://www.anthropic.com`（首页无路径，无锚定证据）
- [ ] `cac1bcda`：无 URL，正文为 X 页面 crawl 残渣
- [ ] `2755621b`：URL 为 bare `https://pleasedonotescape.com/`（项目首页；条目无 content 文件，无锚定证据，不修复仅标记，延续观察）

## 附加扫描（信息项）
- 本周新增 crawl-artifact 复核: `c12d78f0`（`fion.ac/jellyfish.pdf`）为论文 PDF 直链，条目 content 文件明确锚定该 PDF 为来源——判定合法，非 crawl 残渣。
- 新增条目 local_path 抽查: 121 条新增 active 中 0 条指向非 `content/` 路径（2026-11-04 修复后 intake 行为已正常）。
- 占位标题 active: 1 条（`z8jjvpnw`，延续；`bb5aa8c8`/`8e67caa3`/`bd81b6e2` 为真实单词标题，非占位）。
- 时效归档扫描: active 且 added_date < 2026-05-13（>180 天）且 score ≤ 3 的 article/x_post = 10 条（延续上周口径，仅记录不动作）。
- active 缺 content 文件: 124 条（上周 114；属 content-fetcher 任务范围，非 dedup 职责）。

## 验证
- `scripts/validate-schema.py`: 3155 条，0 错误（遗留警告为历史遗留，非本轮引入）
- `python3 scripts/generate-site.py`: 2380 展示卡片 / 2260 内容页 / 7 频道（2381/2261 各 -1，为 `b5a533ae` 归档下线，预期）
- 条目数基线: worktree = HEAD = origin/main = 3155（提交前后均校验）
- `data/entries.json`: dict 形态，3155 不变，`len(entries) == total_entries`

## 变更文件
- `data/entries.json`（`b5a533ae` 归档 + 双向 related 补链，count 不变）
- `content/b4ceed50.md`（删除：孤儿字节级重复文件）
- `openclaw/logs/dedup-report-2026-11-09.md`（本报告）
- `metadata/stats.json`（generate-site 构建时间戳刷新）
