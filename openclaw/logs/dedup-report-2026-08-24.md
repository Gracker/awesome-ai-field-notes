# 去重报告 · 2026-08-24 (weekly-maintain-dedup)

## 总览
- 条目数: 1956 → 1956（不变，归档制去重）
- Active: 1362 → 1292（-70），Archived: 339 → 409（+70），score-pending: 255 不变
- 站点重新生成: 1120 → 1051 展示卡片，1039 → 970 内容页（-70 页 = 本次归档的 70 个带内容页 active 条目，属预期去重语义）

## 自动处理

### 1. 合成 digest 集群清理（本周核心发现，71 条）
X 状态 URL 呈 `/status/YYYYMMDDHHMMSS_002` 时间戳模板形态（同一时刻 id 被 10 个不同作者共用；真实 X snowflake id 为 15-20 位且全局唯一，此形态 URL 不可能真实存在），标题/摘要为同一模板换 handle 生成，共 71 条，added_date 集中于 2026-06-07 至 06-21。抽查内容文件发现正文多为与标题无关的真实推文（FIFA 比分、网站导航评论等），证明标题/摘要系伪造。处理：
- **归档 69 条**（status → archived，保留条目与内容文件，未删除）
- **修复 2 条**（内容文件含真实 snowflake URL 且与正文一致，经查无 URL 冲突、snowflake 解码时间与推文内嵌时间一致）：
  - `27006455` → `https://x.com/AndrewYNg/status/2062576164657664469`：Andrew Ng 发布 LLM 高效服务课程（量化 + vLLM，与 Red Hat 合作，1077 赞）。重写标题/双语摘要/内容页，归入 learning
  - `ai_digest_006` → `https://x.com/gdb/status/2063102501847757197`：Greg Brockman「用 Codex 操作电脑有趣得多」（2320 赞，评论区讨论 Codex 作为通用计算机界面）。重写标题/双语摘要/内容页，归入 coding
- 涉及批次: ai_digest_001-010、ojm5a1gt 系列（06-09）、39788841 系列（06-10）、*_20260611180217 系列、aafn_* （06-12）、digest_2026-06-13_*、u9kvudqy 系列（06-18）、aid001-008、19923856 系列（06-21）等

### 2. 影子重复归档（1 条）
- `b995a05a`（无 URL，local_path 指向 66ebdd18.md）vs `89fa848ed0d4`（带规范微信 URL）：标题完全一致，影子内容文件含孪生标题+URL（交叉验证通过），孪生有独立内容页（9475 字符）→ 影子归档，related 双向互链

### 3. related 软关联（7 组，不合并）
- Boris Cherny 访谈中译 `1ef6890f` ↔ 原文 `a7e2bc3b`
- Auto Mode 默认化: Simon Willison `18b0dbee` ↔ Anthropic 官方 `15e161b5`
- OpenAI Agents SDK: 仓库 `ngiorjuh` ↔ 文档 `jk6udyp9`
- GPT Image 2 prompt 库: X 发布推 `a837f575` ↔ GitHub 仓库 `469c12ee`
- Prompt Engineering: Lilian Weng `987197b8` ↔ Kaggle 白皮书 `miopc080`
- Claude vs OpenAI 编程文（两个公众号版本）`qhnleufw` ↔ `wlxsv45l`
- 影子↔孪生: `b995a05a` ↔ `89fa848ed0d4`

### 4. 微信 URL 规范化
- 本周新增扫描：0 条需要处理（上周已规范化的 71 条保持稳定）

## 待人工确认（延续上周，未自动处理）
- [ ] `z1jgz9it` "Google I/O 2024" vs `yzi1wbrv` "Claude Code 浏览器自动化" 共享同一 __biz/mid/idx/sn 四元组，疑一方抓取 URL 损坏（z1jgz9it 的内容页标题为 Google I/O 文章）
- [ ] 其余 8 组同标题多 URL 软重复（多为中英/不同来源视角，建议保留 related 关联现状）

## 验证
- `data/entries.json`: dict 结构，entries=1956=total_entries，本地=HEAD=1956 ✅
- `scripts/validate-schema.py`: 0 错误 / 65 警告（与上周持平，无新增） ✅
- `npm run build`: 成功，1051 卡片 / 970 内容页 / 7 频道 ✅
- 内容页 -70 = 归档条目退出 active 展示的预期语义；2 个修复条目内容页重写且非空 ✅
- ID 无重复、URL 无硬重复组 ✅
