# Qwen-Image-2.1 Uncensored GGUF (abenzerps)

> 原文链接: https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF
> 作者: abenzerps
> 发现渠道: @toyxyz3（X, 2026-09-22）/ OpenClaw定时任务/X书签消化/2026-09-22

## 摘要（AAIF 提取）

Qwen-Image-2.1（Qwen 2026 年 8 月底发布的文生图模型）的 GGUF 量化仓库，基于 Qwen/Qwen-Image-2.1 原始上游权重，面向本地 ComfyUI 生图；模型卡注明 fully uncensored 版本正在开发中。

**GGUF 档位**（文件大小）：

| 量化 | 大小 | 说明 |
|---|---|---|
| Q8_0 | 7.59 GB | 量化损失最小，16GB+ 显存 |
| Q6_K | 5.88 GB | 12-16GB |
| Q5_K_M | 5.22 GB | 12GB |
| Q4_K_M | 4.60 GB | 官方推荐的大小/质量平衡点 |
| Q4_0 | 4.05 GB | 8GB 显存可跑 |

**配套文件**（打包为 ComfyUI 目录结构）：文本编码器 qwen3vl_8b（BF16 17.53GB / Int8 convrot 9.35GB，低显存推荐 Int8），VAE qwen_image_2.1_vae_bf16（676MB）。使用 ComfyUI + ComfyUI-GGUF，GGUF transformer、文本编码器、VAE 全部同仓托管。

**判断（来自消化笔记）**："uncensored"本质是去掉内容策略约束、保留原生成能力，让本地用户能跑敏感题材；量化档位与显存档位的精确对应说明 T2I 生态在向消费级硬件外溢。对本地评测者：同一权重 + 同一 prompt 在不同量化档位下的纹理/手部稳定性差异是现成的对照实验。
