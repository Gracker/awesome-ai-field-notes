# 端侧与边缘

On-Device & Edge — 2 条活跃资源

### [Qwen3.5-122B-A10B Pooled on Dual Mac Studio M4 Max with Exo + Thunderbolt 5 RDMA](https://x.com/TrevinPeterson/status/2027404303749546459) 
by @TrevinPeterson (2026-02-28) | ⭐⭐⭐⭐ 4/5 | 🌐

**双 Mac Studio RDMA 池化跑 Qwen3.5-122B，52 tok/s 稳定吞吐**

24+ 小时调试后，在两台 Mac Studio M4 Max 上通过 Exo + Thunderbolt 5 RDMA 实现了 Qwen3.5-122B-A10B 的完整池化运行。持续吞吐约 52 tok/s，并发 c=2 稳定（p95 约 10.37 秒）。提供了完整的 Day-0 实操指南，包含精确命令与失败检查关卡。
 `qwen` `mac-studio` `rdma` `exo` `local-inference` `thunderbolt`

---
### [V 神本地 LLM 环境配置](https://x.com/fkysly/status/2040976089196167538) 
by @马天翼 (2026-04-06) | ⭐⭐⭐ 3/5 | 🇨🇳

**V 神的本地 LLM 全栈配置方案，从硬件到离线防幻觉策略。**

V 神分享的本地大模型环境配置博客。从硬件选型开始，详细讨论如何构建一套满足隐私、安全、离线要求的 Local LLM 环境。特别值得注意的细节：为了减少飞机上离线情况下的模型幻觉，他把 1GB 维基百科内容都存了下来方便模型自我核实。同时也考虑了预算有限朋友的硬件推荐方案。
 `本地LLM` `Vitalik` `隐私` `离线` `硬件配置`

---