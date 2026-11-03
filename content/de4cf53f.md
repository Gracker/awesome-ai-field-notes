# Scaling Git at OpenAI

- **ID**: de4cf53f
- **原文链接**: https://openai.com/index/scaling-git-at-openai
- **作者**: Aaron Friel, Taylor Blau, Ted Nyman
- **日期**: 2026-11-02
- **更新**: N/A
- **分类**: infra
- **来源类型**: article
- **标签**: git, monorepo, infrastructure, codex, agents, rust
- **质量评分**: 5/5
- **抓取时间**: 2026-11-03T15:47:11Z

---

## 中文导读

OpenAI 11-02 工程博客公开 Pando：不改 Git 协议与客户端的 monorepo 服务端，2026 年 4 月起服务生产，Rust 写成，一名工程师设计核心Codex agent 团队实现Codex 把 master 提交量四年推高 1378%，旧栈可靠性一度跌破 90%写按分支因果一致仅同 ref 冲突；读走不可变 pack 加 packfile-uri自报 push 延迟降约 80%日吞吐近 1 PB；跨分支无同一时刻快照，未开源

## 为什么值得关注

这是 agent 规模开发重塑基础设施的第一手工程披露：触发因素不是人头增长而是 Codex agent 把提交量四年推高近 15 倍；核心由一名工程师设计、Codex agent 团队实现——构建方式本身就是论点。对自建 monorepo 或大规模 CI 的团队，按分支因果一致 + pack 复用 + packfile-uri 是可对照的路线图；数字为厂商自报，但机制描述足够具体，可与 GitHub Spokes、Anthropic Scion 对照阅读。

## 关键信息

- 发布：2026-11-02，OpenAI 工程博客《Scaling Git at OpenAI》，作者 Aaron Friel / Taylor Blau / Ted Nyman；@OpenAIDevs 同日推文确认 headline 数字（push latency ~-80%、近 1 PB/日）
- 规模动因：master 落地 commit Q3 2026 vs Q1 2024 +1,378%，Q4 2026 估计 +2,442%；每次 push 触发大量 CI fetch；2025 年末 push/fetch 变慢、merge 失败增多，可靠性有时 <90%
- 写路径：入站 pack 存为 blob store 不可变对象；ref 更新（新 tip + 提供它的 pack + 依赖的更早 ref versions）写入可水平扩展 metadata store；按分支因果一致，仅同 ref 并发 push 冲突
- 读路径：不可变 pack + Git 既有 packfile-uri（返回空 inline pack + 下载链）；Express 区域缓存按 consistent hashing，命中 >99%；后台 worker 几何合并 L0-L4 cover（类 LSM）
- pack 画像：median pack < 20 KiB；堆叠分支 push p99 < 3 MiB；百万分支全量 ref advertisement 可超 100 MiB，故以 trunk 为新功能分支的 base 广告
- 生产数字（全部 vendor self-report）：median push latency 约降 80%（nearly 5x）；近 1 PB Git 数据/日且 CPU cores 很少；峰值 >57 TB packs/小时；标准云 VM clone/fetch 可打满 10 Gbps
- 工程过程：kick-off 到生产约 10 周；Rust；一名工程师定核心设计、Codex agent 团队实现；Git conformance suite for agents + deterministic simulation testing；agents（含 GPT-6 Astra）写 Lean / TLA+ 找并发 bug；先以 read/write-through proxy 迁流量，不停工
- 边界：未开源；跨分支读取无全仓同一时刻快照；全部性能数字无独立复测
- 路线对照（MarkTechPost 二手整理）：GitHub Spokes 保 Git 客户端（三阶段提交 + quorum）；Anthropic Scion 换客户端（scn，CPU/内存 footprint ~1/200）；Pando 与 Scion 均未对外产品化
- 自研 Git build：https://github.com/openai/git ，若干 client 修复回馈 upstream

## English Summary

OpenAI's Nov 2026 engineering post (Friel, Blau, Nyman) introduces Pando, a Git server backend that keeps the protocol and clients unchanged - engineers and Codex agents keep git push/fetch. In production since April 2026 after ~10 weeks; Rust; core designed by one engineer, implemented by a Codex agent team. Trigger: master commits grew +1,378% (Q3 2026 vs Q1 2024; Q4 est. +2,442%), pushing old-stack reliability below 90% at times by late 2025. Writes are causally consistent per branch: only same-ref concurrent pushes conflict. Reads serve immutable packs via packfile-uri with >99% regional cache hits, merged L0-L4 like an LSM tree. Vendor-reported: median push latency down ~80%, ~1 PB Git data/day, >57 TB packs/hour peak. Tradeoff: no repo-wide point-in-time snapshot across branches; not open source (custom build at github.com/openai/git).

## Obsidian Notes

- 内容获取路径：`openai.com` 对 curl 返回 403（bot wall）；本文数字锚定在同日 DeepResearch 材料包（2026-11-03 13:02Z 自官方工程文抓取）与 @OpenAIDevs 推文原文（opencli twitter thread 当晚取回全文，含 Pando headline 数字），MarkTechPost 二手对照表列于关键信息。
- 中文导读与关键信息不引入上述材料之外的数据；性能数字均为厂商自报（vendor self-report），已在正文标注。
- 现代站点生成器按 `content/{entry.id}.md` 查找内容页；本文件写入 canonical content 目录，而不是 `openclaw/content/`。
