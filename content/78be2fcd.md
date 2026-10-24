# Software is slow because of bad design, not slow languages

- **ID**: 78be2fcd
- **原文链接**: https://seangoedecke.com/software-is-slow-because-of-bad-design-not-slow-languages/
- **作者**: Sean Goedecke
- **日期**: 2026-10-23
- **分类**: coding
- **来源类型**: article
- **标签**: performance, ai-agents, profiling, rewrite
- **质量评分**: 4/5
- **抓取时间**: 2026-10-24 (Asia/Shanghai)，grounded in vault full-text sources

---

## 中文导读

Goedecke 反驳「让 AI 把代码重写成更快语言就会更快」：真实程序大多 I/O 绑定——CRUD 请求约 50% 时间在查库，重写只能压另外 50%，Amdahl 上限 2 倍、实践约 1.5 倍。真撞 CPU 瓶颈的地方，慢语言早有 C 库接着（markdown 渲染走 cmark-gfm、Python 矩阵靠 PyTorch/TensorFlow）；Actual Computer 把 tiktoken 重写成汇编的 4-23 倍收益，他归因于摆脱正则依赖的重设计而非汇编本身。引 Cantrill 2018 年 C 改 Rust：朴素写法预期慢 20% 反而快 30%，原因是 Rust 内部偏好 B 树、缓存更友好。文末补 lobste.rs 反方：有 commenter 说单请求几百次查询本就未必「I/O 绑定」，顶楼 commenter 列出浏览器布局引擎、3D 渲染、文字处理、神经网络都是 CPU 绑定；他自估这类程序约占 CRUD 程序的 5%，却占公开讨论的一半以上。

## 为什么值得关注

给「用 agent 优化性能」这条流行路线做了一次扎实纠偏：让 agent 去 profile、找热点、改设计顺序（缓存、异步、并行、合 SQL），比让它把代码翻译成另一门语言有用得多。那 5% 的 CPU 绑定世界，恰好是这类文章最容易替读者做决定的地方。

## 关键信息

- I/O 绑定论证：50% 查库 → 语言重写上限 2x，实践 1.5x
- 慢语言热点已有 C 库承接：cmark-gfm / PyTorch / TensorFlow
- tiktoken 汇编重写（Actual Computer）：收益来自重设计，不是汇编
- Cantrill 2018：朴素 Rust 重写快 30%（B 树缓存友好）
- 结论：让 agent profile + redesign，而不是 rewrite in Rust

## English Summary

Sean Goedecke pushes back on the 'have AI rewrite it in Rust' theory of performance: most real programs are I/O-bound, so a CRUD site spending half its request time in the database caps a C rewrite at 2x (about 1.5x in practice); slow languages already delegate hot paths to C libraries like cmark-gfm and PyTorch, and even Actual Computer's assembly tiktoken rewrite owes its speedup to redesigning away from regexes rather than the assembly itself. He cites Bryan Cantrill's 2018 C-to-Rust port, where a naive rewrite came out 30% faster thanks to Rust's cache-friendlier B-tree. lobste.rs commenters counter that CRUD is not always I/O-bound; Goedecke estimates CPU-bound programs are roughly 5% of CRUD programs but over half of public discussion. His takeaway for the agent era: ask the agent to profile, find hotspots, and redesign what the program does instead of translating the language.

## Obsidian Notes

- Fetched via AK-RSS-Digest 89源精选 2026-10-24 run; vault source: `OpenClaw定时任务/AK-RSS-Digest（89源精选）/source/2026-10-24-sean-goedecke-software-slow-bad-design.md` (full text, 11.9 KB).
- Fetched 2026-10-24 via the evening intake pipeline; entry appended through pipeline_utils with URL dedup precheck.
