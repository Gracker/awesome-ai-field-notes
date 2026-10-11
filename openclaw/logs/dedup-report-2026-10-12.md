# 去重报告 · 2026-10-12 (weekly-maintain-dedup)

## 总览
- 条目数: 2703 -> 2703（不变；本轮 0 合并、0 归档、0 URL 修复、0 新增标记，1 处 related 补链）
- 上轮基线: 2591（2026-10-05），本周 intake 净增 +112；其中 added_date > 2026-10-05 的 active 新条目 98 条全部纳入本轮扫描（其余 14 条为上轮报告落盘后当日的追加条目）
- Active: 2058（上周 1946），Archived: 606，score-pending: 39
- 展示卡片 1977 / 内容页 1880 / 7 频道，与 pre-run 一致（本轮未新增条目和内容页）

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
- 全库同 normalized-URL 组共 12 组：active-vs-active 1 组，active+archived 已解决形态 11 组（同上周）。
- active-vs-active 仍为 `ed4dc19a` vs `ffd9dfec`（LessWrong Astra and Fable，同 URL 不同 score 3/4），双向 related 已存在，两条为不同抓取视角，按保守原则继续维持现状（连续第四周）。

### 2. 本周新增条目（98 条 active）重复检查
- 与全库 normalized-URL 碰撞: 0 组新增（append_entries 的 duplicate-url/duplicate-title 拦截正常）。
- 标题相似度 fuzzy 扫描（title_key SequenceMatcher ≥ 0.88，跨全库 active）: 1 对（同一对的双向计数，`deeb3d35` vs `50e35720`，OpenAI rogue agent Wikimedia 双视角报道），处理见第 3 节。

### 3. 同标题 active 双胞胎
- 精确同标题 active 组 17 组（上周 16 组）。
- 16 组已双向 related；1 组缺链：`deeb3d35`（diff.wikimedia.org 原始报道，2026-10-06）↔ `50e35720`（simonwillison.net 转述视角，2026-10-09）——两条均为上轮去重之后流入，`50e35720` 已含正向 related，`deeb3d35` 反向缺失。本轮通过 `pipeline_utils.load_entries_data()` + 定向字段编辑 + `save_entries_data()` 补齐双向 related，count 不变。

### 4. 影子条目（无 URL 且 local_path 指向同标题 URL 条目）
- 0 条（06-2026 影子批量归档后连续保持 0）。
- 本轮将判定精确化为「local_path 指向他人 id 的 content 文件」：active 无 URL 条目共 194 条，其中 local_path 指向自身 `content/{id}.md` 的 181 条、指向站点外 Obsidian 笔记的 13 条，指向他人文件者 0 条，均为 local-path 校验职责，非重复，不处理。

### 5. 微信 4-key 同 tuple 组
- 同 (__biz, mid, idx, sn) tuple 共 7 组：5 组为同标题 active+archived 已解决形态；1 组（`ed827be1` archived vs `6ebadca4` active）标题仅引号差异、title_key 相同，判定为同文章已解决形态，不动作。
- 跨标题碰撞仍仅 `yzi1wbrv` vs `z1jgz9it`（corrupt crawl URL 案例），按跨标题碰撞 guard 继续挂起待人工，不 canonicalize、不合并（连续第四周）。

### 6. 可疑 URL（active）
- 多 https:// / CJK 内嵌 / 尾部残渣 / 未 trim / 非法 scheme：0 条。

### 7. 完整性
- entry id 重复: 0；缺 title: 0；缺 score: 0；related 悬挂引用: 0
- entries=2703=total_entries，dict 结构合法

## 附加扫描（信息项）
- 占位标题 active（hash 形标题 / title==id，community-review pattern）: 0 条，无新发现
- 时效归档扫描: active 且 added_date > 180 天且 score ≤ 3 的 article/x_post = 0 条，无归档动作

## 标记待人工（延续，非本轮新增）
- [ ] `z8jjvpnw`：URL 已按本地转储修复为真实文章参数，标题仍为占位 `Z8Jjvpnw`，需人工补标题（或确认文章已 404 后处理）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题 4-key 碰撞（延续）

## 验证
- `scripts/validate-schema.py`: 2703 条，0 错误，63 警告（历史 summary_zh 过短，非本轮引入；上周 58 条，差值来自本周新增条目自身的短摘要警告，均非错误）
- `npm run build`: 成功，1977 展示卡片 / 1880 内容页 / 7 频道（与 pre-run 一致，无新增页面为预期）
- 补链后复扫: 同标题 active 组 17 组缺失双向 related = 0；同 normalized-URL active-vs-active 组维持 1（已挂起的既有形态）
- 条目数基线: 本地 = HEAD = origin/main = 2703（提交前校验）
- `data/entries.json` 本轮仅 `deeb3d35.related` 补链，count 2703 不变；openclaw/content/ 无游离文件

## 变更文件
- `data/entries.json`（`deeb3d35` related 补链 50e35720，count 不变）
- `openclaw/logs/dedup-report-2026-10-12.md`（本报告）
- `metadata/stats.json`、`README.md`、`openclaw/README.md`（构建时间戳与内容页计数 1873->1880）
- `content/{283966b8,301544ff,5c36d3ae,65588a3f,b38064f8,bbe343cc,c885ca78}.md`（pre-run 已存在的 2026-10-11 intake 产物，已被 HEAD entries.json 引用，本轮验证非空后一并提交）
