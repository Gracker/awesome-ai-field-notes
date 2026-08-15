# Qwen3.8-27B-FP8

- **ID**: afb6d0b8
- **原文链接**: https://huggingface.co/Qwen/Qwen3.8-27B-FP8
- **作者**: Qwen Team
- **日期**: 2026-08-13
- **分类**: models
- **来源类型**: blog
- **标签**: qwen3.8, 27b, fp8, vision-language, hybrid-architecture, huggingface
- **质量评分**: 4/5
- **抓取时间**: 2026-08-15T04:45:00Z

---

## 中文导读

Qwen 发布 Qwen3.8-27B-FP8 权重：Qwen 开源家族迄今最强一代中的紧凑可部署 dense 模型，原生视觉语言模型（理解图像与视频，覆盖 STEM 图表、文档到小时级视频）。架构延续 Qwen3.5 基础：64 层、hidden 5120、248,320（padded）词表，混合布局为 16 组 ×（3 × Gated DeltaNet → FFN + 1 × Gated Attention → FFN）——Gated DeltaNet 线性注意力 48 V heads / 16 QK heads（head dim 128），Gated Attention 24 Q heads / 4 KV heads（head dim 256），FFN 中间维 17,408；MTP 多 token 预测训练；原生 262,144 上下文可扩展至 1M。thinking 默认开启、可按请求关闭；`reasoning_effort` 支持 xhigh（默认）/ medium / low 调节推理深度；`preserve_thinking` 默认开启，跨轮保留历史消息中的推理上下文。FP8 块量化（block size 128）性能与原模型几乎一致，兼容 Transformers / vLLM / SGLang / TokenSpeed。基准上编码与 agent 提升显著：DeepSWE 1.1 42.2（Qwen3.6-27B 为 13.3）、QwenSWEBench 79.0（49.3）、SWE-bench Pro 61.7（53.5）、CoWorkBench 70.7（61.0）、JobBench 33.4（21.8）、Agents' Last Exam Pass@1 20.4（10.6）；多模态 agent 侧 OSWorld-Verified 84.3（63.9）、WebArena-Verified 64.8（48.8）、AndroidWorld 81.9（70.3）。

## 为什么值得关注

开源系旗舰迭代，混合线性注意力（Gated DeltaNet × Gated Attention）与可控思考开关是本地部署 agent 的实用特性：262K 原生上下文 + 1M 扩展 + 27B dense + FP8，单卡可跑的"工作马"定位明确。与自家长辈对比的幅度（DeepSWE 13.3→42.2、OSWorld 63.9→84.3）显示这一代在长程 agentic 与多模态 computer-use 两条线的跃迁。注意官方提示：多轮 agent 任务中调低 reasoning_effort 不一定缩短总完成时间——单轮更快但分析不足导致失败重试，总延迟与 token 消耗反而可能上升。

## 关键信息

- 模型：Qwen3.8-27B（FP8 量化版；HF Transformers 格式权重 + 配置）
- 量化：fine-grained FP8，block size 128，性能与原模型几乎一致
- 架构：64 层；16 × (3 × DeltaNet + 1 × Attention) 混合布局；248K 词表；MTP 训练
- 上下文：262,144 原生，可扩展至 1,000,000
- 视觉语言：原生图像/视频理解（STEM 图表、文档、小时级视频）
- 思考控制：thinking 默认开（可按请求关）；reasoning_effort = xhigh | medium | low（默认 xhigh）；preserve_thinking 默认开
- 部署：vLLM / SGLang / TokenSpeed 官方 recipe；Qwen Cloud 托管版即将提供默认 1M 上下文 + 官方内置工具
- 采样建议：thinking 模式 temperature=1.0, top_p=0.95, top_k=20；instruct 模式 temperature=0.7, top_p=0.80, presence_penalty=1.5

### 文本基准（vs Qwen3.6-27B / Qwen3.7-Plus / Muse Glimmer-30B / Opus4.6 Max）

| 基准 | Qwen3.8-27B | Qwen3.6-27B | Qwen3.7-Plus | Glimmer-30B | Opus4.6 Max |
| --- | --- | --- | --- | --- | --- |
| Terminal Bench 2.1 (Terminus) | 73.0 | 63.4 | 64.0 | 51.7 | **78.2** |
| SWE-bench Pro | **61.7** | 53.5 | 57.6 | 51.2 | 53.4 |
| DeepSWE 1.1 | **42.2** | 13.3 | 14.2 | — | — |
| QwenSWEBench | **79.0** | 49.3 | 59.2 | — | 63.8 |
| CoWorkBench | **70.7** | 61.0 | 65.1 | — | 68.2 |
| JobBench | **33.4** | 21.8 | 27.6 | — | — |
| Agents' Last Exam Pass@1 | **20.4** | 10.6 | 13.2 | — | — |
| IFBench | **79.5** | 69.1 | 79.1 | 77.0 | 62.5 |
| LiveCodeBench v6 | **90.3** | 83.9 | 89.6 | — | 88.8 |

### 多模态 agent 基准（vs Qwen3.6-27B）

- OSWorld-Verified（computer use）：84.3 vs 63.9
- WebArena-Verified（browser use）：64.8 vs 48.8
- AndroidWorld（mobile use）：81.9 vs 70.3
- RecreationBench（应用重建）：47.1 vs 29.8
- SWE-MM（多模态软件工程）：38.6 vs 25.7
- Vision2Web（可视化 Web 开发）：62.9 vs 45.0

## Obsidian Notes

- 内容由 `opencli web read` 抓取 HuggingFace 模型卡全文后整理；架构参数、基准数字与 API 建议均直接来自模型卡。
- 相关条目：e6c53596（GLM-5.3）、dd378ea0（Gemini 3.7 Flash）——同期发布的三家工作马模型，DeepSWE v1.1 可横向对比：GLM-5.3 66.9 / Gemini 3.7 Flash 65.3 / Qwen3.8-27B 42.2。
