# 去重报告 · 2026-09-28 (weekly-maintain-dedup)

## 总览
- 条目数: 2466 -> 2466（不变；本轮仅 related 补链 2 处 + URL 修复 1 处，无新增无删除无归档）
- Active: 1821（上周 1732，本周 intake 净增 89），Archived: 606，score-pending: 39
- 上次周维护: 2026-09-21（基线 2377）
- 展示卡片 1589 / 内容页 1496，与 pre-run 一致（本轮未新增条目和内容页）
- 时效归档扫描: active 且 added_date > 180 天且 score ≤ 3 的 article/x_post = 0 条，无归档动作

## 本轮扫描结果

### 1. 硬 normalized-URL 重复
active-vs-active 1 组：`ed4dc19a` vs `ffd9dfec`（LessWrong Astra and Fable，同 URL 不同 score），双向 related 已存在，两条为不同抓取视角，按保守原则维持现状（与前两周一致）。active+archived 已解决形态 11 组，同上周。

### 2. active 无 URL 条目
195 条（上周口径 0 为"影子条目"数：无 URL 且标题与 URL 条目同标题的 active，本轮该口径仍为 0）。195 条无 URL active 均为 6 月初批量导入的旧类目（local_path 指向站点外 Obsidian 笔记），属周维护 local-path 校验职责，非重复，不处理。

### 3. 同标题 active 双胞胎
精确同标题 active 组 14 组（上周 16 组口径含已解决形态）。13 组早已双向 related；本轮动作 1 组：
- `d2a8f1c7`（blog.cloudflare.com/python-workers-ga，score 4，2026-09-23）
- `f486924c`（simonwillison.net/2026/Sep/21/cloudflare-python-worker，score 3，2026-09-24）
- 同一事件（Cloudflare Python Workers GA）两个来源视角，补双向 `related`，保留两条不合并。

### 4. 微信 4-key 跨标题碰撞
- `yzi1wbrv` vs `z1jgz9it`：仍共享同一 4-key tuple（ corrupt crawl URL 案例），按 guard 继续挂起待人工。
- 新发现 `6ebadca4`（active）vs `ed827be1`（archived）同 4-key 同主题（Hermes Agent Self-Improving），标题仅弯引号/直引号之差——即 09-07 报告已双向 related 的已知对，archived 一侧不激活，维持现状，不算碰撞。

### 5. URL 修复（1 条，本轮主要动作）
- `z8jjvpnw`（上周挂起的 JS 资源 URL）：原 URL 为微信前端资源 `mmbizappmsg/.../mprdev-0.2.5.js',`。本轮在其本地 content 页（微信"环境异常"验证页转储）的 `window.cgiData.target_url` 中找到第一方目标 URL：`https://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA==&mid=2247559664&idx=1&sn=f5278b02015b4eb6b01787c035ca051c`，据此仅修复 `url` 字段（本地 grounding，符合 suspicious-url-repair 决策规则）。curl/opencli 实测该目标 URL 当前也落在验证墙（17KB、空 title、无 verify 提示、非错误页），文章真实标题无法恢复，**标题仍为 ID 派生占位 `Z8Jjvpnw`，继续挂起待人工**。条目不删除。

### 6. 标记待人工
- [ ] `z8jjvpnw`：URL 已按本地转储修复为真实文章参数，但标题仍为占位，需人工补标题（或在确认文章已 404 后处理）
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题碰撞（延续）

### 7. 其他
- active URL 多 https:// / CJK 内嵌 / 尾部残渣（除上条已修复外）：0 条
- entry id 重复：0；缺 title/score：0
- active 空 summary_en+summary_zh 双空：185 条（均为 one_liner 有值的历史条目，上周口径 52 为"双空且 one_liner 也弱"的子集；纯字段口径下无"完全无任何可读摘要"的 active 条目）

## 验证
- `data/entries.json`: dict 结构，entries=2466=total_entries，本地=HEAD=origin/main=2466（提交前）
- `scripts/validate-schema.py`: 2466 条，0 错误，55 警告（历史 summary_zh 过短，非本轮引入）
- `npm run build`: 成功，1589 展示卡片 / 1496 内容页 / 7 频道（与 pre-run 一致，无新增页面为预期）
- 触碰条目 content 页均存在非空；openclaw/content/ 无游离文件

## 变更文件
- `data/entries.json`（related +2 引用；z8jjvpnw url 修复 1 处）
- `metadata/stats.json`（构建时间戳）
- `openclaw/logs/dedup-report-2026-09-28.md`（本报告）
