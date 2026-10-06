# 社区评审报告 · 2026-10-07 (community-review)

## 总览
- 条目数: 2616 -> 2616（不变；本轮 0 合并、0 归档、0 删除，纯元数据修复）
- Active: 1971, Archived: 606, score-pending: 39（与 2026-10-05 dedup 基线口径一致）
- 本轮共修复 30 项元数据：24 个占位标题 + 2 条损坏 juejin URL + 4 个失效 local_path
- 展示卡片 1890 / 内容页 1799 / 7 频道，与 pre-run 一致（无新条目、无新内容页）

## 修复 1：占位标题（24 条 active）
2026-06-23 批量导入产生 ID 派生哈希标题（如 `16Htfbpp`），上轮 dedup 只挂起了 1 条
（z8jjvpnw），本轮全库扫描发现共 25 条。全部通过 pipeline_utils 修复，
每条新标题都在该条目自己的 content/{id}.md 首屏（首行标题/正文）中验证过：
Hermes 从 0 到 1 教程；Claude Code 做私人教练：AI 会议复盘系统；Android×鸿蒙×AI 技术刊
#第12期；科学家的消亡 / AI 会终结科学，还是会引发一场新的革命？；Agent Harnesses are how
you build agents...；GPT-5.5 + GPT-Image-2：用 AI 重塑设计到工程交付；The dream is: the
model remembers what you said before；oh-my-codex 安装与常用命令；Android×AI 技术刊#第11期；
全面解析：如何部署 Conway Agent，开启链上 AI 生存游戏；ChatGPT 问世两年，我在 AI 的辅助下
成为了一名 iOS 业余开发者；AI Fast Track：5天免费邮件课；Shipping at Inference Speed；
Android×鸿蒙×AI 技术刊#第10期；LLM Council 进阶：多模型分析 Skill；6551 开源 X + 全网
新闻源 MCP + Skill；Claude Code 免翻上手教程，以及改用 GLM 指南；使用 Gemini Embedding 2
构建：代理式多模态 RAG 及更多；Harness Engineering——Claude Code 设计指南；通过 Siri 启动
「快捷指令」连接 ChatGPT API；Anthropic Managed Agents：它是什么，和 Claude Code 有什么
区别；Android Native 内存泄漏：原理、检测与案例分析；Pi: The Minimal Agent Within OpenClaw；
我死过三次。

## 修复 2：juejin URL 尾部残渣（2 条）
- `2lrsppi0`: `.../7514684482998304822Android` -> `https://juejin.cn/post/7514684482998304822`
- `8uey92b2`: `.../7510900838765248522Kotlin` -> `https://juejin.cn/post/7510900838765248522`
（与 dedup skill「明显粘贴残渣」保守修复模式一致：只去掉尾部粘贴词，正文标题已各自 ground）

## 修复 3：失效 local_path（4 条）
- `b482b19f`: `content/discovery/.md`（空文件名）-> `content/b482b19f.md`
- `2f383058`: `content/discovery/ai-in-mathematics.md` -> `content/2f383058.md`
- `7bd44733`: `content/discovery/frontier-os-llm.md` -> `content/7bd44733.md`
- `7a48d6db`: `content/discovery/ultrasound-brain.md` -> `content/7a48d6db.md`
（4 条均指向自己已存在的 canonical content 文件）

## 保持挂起（非本轮新增）
- [ ] `z8jjvpnw`：URL 与内容文件均为 JS chrome，无法 ground 真实标题，继续挂起待人工
- [ ] 微信 `yzi1wbrv` vs `z1jgz9it` 跨标题 4-key 碰撞（guard：不 canonicalize、不合并）
- [ ] `ed4dc19a` vs `ffd9dfec` LessWrong 同 URL 双视角（双向 related，连续第三周维持现状）
- 观察项（不处理）：14 条 active 有 one_liner 但 summary_zh/en 为空，均带完整内容页；
  25 条 2026-06-23 导入条目无 URL 属旧导入类目，留给后续 content-fetcher/人工

## 无冲突验证
- 修复后的 24 条与全库 active 精确同标题组（16 组）零交集，全部是修复前已存在的
  双向 related 旧对；同 normalized-URL active 组仍只有 ed4dc19a/ffd9dfec 1 组

## 验证
- `scripts/validate-schema.py`: 2616 条，0 错误，59 警告（历史 summary_zh 过短，非本轮引入）
- `python3 scripts/generate-site.py`: 成功，1890 卡片 / 1799 内容页 / 7 频道（与 pre-run 一致）
- count 基线: 2616 = pre-run = HEAD；本轮 data/entries.json 走 load/modify/save 全程
- 30 项修复逐条 reread-verify PASS；0 skip

## 变更文件
- `data/entries.json`（24 title + 2 url + 4 local_path + updated_date 字段）
- `openclaw/logs/community-review-2026-10-07.md`（本报告）
- `metadata/stats.json`（构建时间戳）
