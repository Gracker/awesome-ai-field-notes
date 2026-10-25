# 去重报告 · 2026-10-26 (weekly-maintain-dedup)

## 总览
- 条目数: 2890 -> 2890（不变；本轮 48 归档、1 URL 修复、1 标题修复、51 组 related 互链（双向去重添加）、0 删除）
- 上轮基线: 2781（2026-10-19 dedup 报告），本周 intake 净增 +109；其中 added_date > 2026-10-19 的 active 新条目 99 条全部纳入本轮扫描
- Active: 2194（本轮开始时 2242），Archived: 657（609），score-pending: 39
- 展示卡片 2117 / 内容页 2014 / 7 频道（pre-run 2162/2059；差值 -45 为 48 条归档中已被渲染侧合并/无独立页部分，条目数为唯一硬不变量）

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
- active-vs-active 0 组（全库同 normalized-URL 组均为 active+archived 已解决形态；处置后复扫仍为 0）。

### 2. www/apex 折叠扫描
- 口径修正：本轮按「host 去 www 后整 URL 再 normalized_url_key」折叠（保留 path+query），0 组碰撞，10-14 修复的 seangoedecke 形态无回潮。
- 首版按 (host, path) 忽略 query 的分组把 HN `/item?id=` 与微信 `/s?__biz=` 全并成一组，属假阳性，该口径已废弃。

### 3. 本周新增条目（99 条 active）重复检查
- 与全库 normalized-URL / 标题碰撞: 0 组（append_entries 拦截正常）。

### 4. 精确同标题 active 组
- 14 组（上周 12），全部双向 related 齐全（0 缺链）。其中 `qhnleufw`/`wlxsv45l` 经正文证据升级为同文重复对并处置（见第 7 节），处置后余 13 组，URL 互不相同，按双视角/双来源保留。

### 5. fuzzy 标题相似扫描（title_key SequenceMatcher ≥ 0.88，跨全库 active）
- 共 8 对（上周 19）。2 对为上周已研判对（`b03e02c0`/`a278a014`、`a40dec6e`/`3887fc82`，维持现状）；`efa67a45`/`ed2cbcca` 已互链维持。新研判 5 对：
  - `223537a9`/`997d84c3`: 升级为跨语言影子对（正文均含 twin 的 X 帖 URL），双双归档至 `a09cdbbd`（见第 6 节）。
  - `4fb3bd4e`（无 URL，正文为 tw93.fun 博客原文 15K）vs `efaw158d`（Tw93 X 帖）: 同作者双视角，补双向 related。
  - `d0fd8a1b`（I/O 2026 新闻页）vs `b10a3315`（Pichai 博客页，s=4）: 同事件两篇官方页面，补双向 related。
  - `784b2c06`（cubox 转存）vs `ad4e5293`（justin3go 原文）: 同文转载对，补双向 related；并修复 `784b2c06` 标题缺失顿号（"CodexClaude Code" → "Codex、Claude Code"，以其正文 H1 为据）。
  - `21f855ac` vs `65f18ea8`: `21f855ac` 正文与 `65f18ea8` 英文原文逐字同段，但其文件不含官方 URL，归档 guard 拒绝 → 维持 active，补双向 related，列待人工。

### 6. 影子条目清查（本轮主项：跨语言影子 / content-URL 扫描）
- 旧口径（无 URL 且 local_path 指向他人 content）: 0 条。
- 新口径：active 无 URL 条目的 content 文件中出现其他 active 条目 normalized URL → 扫出 59 个候选。逐一 guard（twin active + 有 URL + twin 自有 content 页；正文确含 twin URL；正文去重 URL 数 ≤ 6 防日报型误判）后**归档 46 条**（status: archived，updated_date=2026-10-26，与 twin 双向 related，count 不变；无 score 吸收——shadow 均 s=3，不高于任一 twin）。
- 家族分布（twin → 归档数）: `a09cdbbd`(Allie Miller 帖) ×11、`62057772`(Karpathy Farzapedia) ×5、`kc757q9l`(Gemini 3.1 Flash TTS) ×4、`digest_2026-06-16_01`(吴恩达新课) ×3、`60d9c4aa`/`ivt6f9u6`/`7e5d8972`/`cca27327`/`b37b2087`/`65f18ea8`/`bengiaf07` 各 ×2、其余 10 twin 各 ×1（`natural-language-autoencoders`、`claude_opus_47_mythos_2026_001`、`kzfvoq4f`*、`gemini_3_flash_cli_2026_001`、`05v1ff6t`、`jnaqutdjulvp1t2swszqd`、`b7e2m384`、`3a6ca5b0`、`096adf05`、`3ad225aa`、`5sbgmacr`）。
- 排除不动作 13 条：日报型 `41071ca3`/`c1484164`（AI 影响力日报正文天然含多条推文 URL）；多主题 `7f5b0c2f`/`8534a84c`；仅命中 bare-domain 的 `7b4f7b20`/`ad6f9ec4`/`fe920d24`；字体 URL 噪音 `cac1bcda`；存疑转待人工 4 条（见标记）+ guard 拒绝 1 条（`946806dc`，正文 7 个 URL）。
- 附带处置：微信同文对 `qhnleufw`（短链）vs `wlxsv45l`（__biz 全参数）经正文证据（同公众号硅基思维、同标题、同正文探针、同 epoch 发布时间残渣）归档短链侧；`7bf35471` 的 URL 为推特网页字体文件（abs.twimg.com woff2，crawl 残渣），正文锚定真实 X 帖 URL 后修复 URL 并归档该侧（保留 `kzfvoq4f`，两者 s=3 无吸收）。归档合计 48 条。

### 7. 微信 4-key 同 tuple 组
- 实际同 tuple 组共 7 组: 6 组为同标题 active+archived 已解决形态；跨标题碰撞仍仅 `yzi1wbrv` vs `z1jgz9it`（corrupt crawl URL 案例），按 guard 继续挂起待人工，不 canonicalize、不合并（连续第六周）。
- 本轮新处置: `qhnleufw`/`wlxsv45l` 同标题同文对（短链 vs 全参数 URL 形态），归档短链侧（见第 6 节）。

### 8. 可疑 URL（active）
- 扫描器口径（多 https:// / CJK 内嵌 / 尾部残渣 / 未 trim / 非法 scheme / 空格）: 0 条。
- 口径外发现并处置 1 条: `7bf35471` URL 为字体文件（由 content-URL 扫描暴露，正文锚定修复后归档）。

### 9. 完整性
- entry id 重复: 0；缺 title: 0；active 缺 score: 0；related 悬挂引用: 0
- entries=2890=total_entries，dict 结构合法；active 同 normalized-URL 组复扫 = 0

## 标记待人工
- [ ] `z8jjvpnw`：标题仍为占位 `Z8Jjvpnw`（延续）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题 4-key 碰撞（延续第六周）
- [ ] `21f855ac`：Petri 捐赠公告无 URL 副本，正文与 `65f18ea8` 英文原文逐字同段但文件无官方 URL；已互链，建议人工确认后归档
- [ ] `946806dc`：正文含 7 个不同 URL（疑似小型日报），guard 拒绝归档；可能与 `7e5d8972`（81k interviews）同源
- [ ] `e742a94e` / `80df7c07` / `ea3fcf10` / `ai-code-gen-benchmark-2026-06-09`：评论/综述/基准页型候选，正文引用他人条目 URL 但标题自成立题，证据不足不归档
- [ ] `antautomd`：URL 为 bare `https://www.anthropic.com`（首页无路径），正文亦无真实文章 URL 可锚定；标题指向 Claude Code Auto Mode 文章
- [ ] `cac1bcda`：无 URL，正文为 X 页面 crawl 残渣，标题为截断引语；疑 MiniMax M2.7 相关，需人工定性

## 附加扫描（信息项）
- 占位标题 active（hash 形标题 / title==id）: 1 条（`z8jjvpnw`，延续）
- 时效归档扫描: active 且 added_date > 180 天且 score ≤ 3 的 article/x_post = 3 条（`hn_llm_agents_2026_003` / `hermex_001` / `hermes_001`，均为 4 月老 import 首次越过 180 天线；本轮仅记录不动作）
- active 缺 content 文件: 107 条（上周 106；属 content-fetcher 任务范围，非 dedup 职责）

## 验证
- `scripts/validate-schema.py`: 2890 条，0 错误，65 警告（历史 summary_zh 过短，与上周持平，非本轮引入）
- `python3 scripts/generate-site.py`: 成功——2117 展示卡片 / 2014 内容页 / 7 频道（pre-run 2162/2059）
- 条目数基线: worktree = HEAD = origin/main = 2890（提交前后均校验）
- `data/entries.json` 本轮仅字段级变更（48 条 status→archived + updated_date、related 补链、1 URL、1 标题），count 2890 不变；`openclaw/content/` 无游离文件

## 变更文件
- `data/entries.json`（48 归档、1 URL 修复、1 标题修复、51 组 related 互链，count 不变）
- `openclaw/logs/dedup-report-2026-10-26.md`（本报告）
- `README.md` / `openclaw/README.md` / `metadata/stats.json`（站点重建统计更新）
