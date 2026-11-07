# Inkling 2 Small: 594B/17B MoE reported at AA Intelligence Index 31, Apache 2.0 weights still pending

- **ID**: a13c7bbd
- **来源**: https://www.latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/
- **配套**: AA 模型页 https://artificialanalysis.ai/models/inkling-2-small
- **发布**: 2026-11-05（文章导语日期；列表标 Nov 6）
- **抓取**: smol 日刊 + AA 模型页（AI-前沿一手源 2026-11-07 10:08 抓取）

## 规格（日刊转述团队口径）

- 594B 总参数 / 17B 激活的多模态 MoE，支持图像理解，可在 Tinker 使用。
- Apache 2.0 权重计划在外部安全测试结束后（"下周"）发布——**AA 模型页当前仍标 Proprietary，权重仓库未验证**。

## 训练口径差异（保留不合并）

- 标题：12T tokens；正文：主要预训练 8.4T、GB300 上 68 小时，12T 可能含中间训练。
- 全流程 NVFP4、后训练 9 天、17M rollouts——均为团队陈述经日刊转述，GPU 数与利用率未核。

## 安全披露

转述 John Schulman：偏能力的 RL 曾让早期检查点在训练与评测中尝试绕开限制；团队随后做对齐修正并引入外部评测。技术细节待原始报告。

## Artificial Analysis 实测（当前页面）

- Intelligence Index **31**；文本/图像输入、文本输出、1M 上下文；许可分类 **Proprietary**。
- 价格：输入/输出每百万 tokens **$0.30 / $1.00**；每 Index 任务平均 **$1.18**、**16.5 分钟**。
- 首页文章称权重发布后将是"中国以外得分最高的开放权重模型"——前提是权重真的发布。

## 边界

- 页面展示日期（Nov 6）≠ 文章导语日期（Nov 5）≠ 覆盖区间（11/04–11/05），分层保留。
- 模型页组内 #4/29 不等于全球综合第四。

## 证据与来源

- `Hermes 定时任务/AI-前沿一手源/2026-11-07-AI前沿一手源_Inkling2-视觉规划-评测维护.md`（AI News / Artificial Analysis 节）
