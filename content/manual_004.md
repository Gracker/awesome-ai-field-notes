# On-Device LLM Deployment · Edge · Mobile · 2026-06-14

## 原始内容

# On-Device LLM Deployment · Edge · Mobile · 2026-06-14

## TL;DR · 六件事

### 1️⃣ **量化谱系已基本完整**：从 8-bit 到 1.58-bit 都有"工程可用"方案
- A1 LLM.int8() 揭示 emergent outliers → A2 SmoothQuant 解决 W8A8 → A3 AWQ 解决 W4 weight-only → A4 BitNet 把 weights 推到 1-bit
- 一条清晰的"low-bit LLM" 技术演进链：每一步都保留精度或仅掉极小点
- —— **2026 on-device LLM 不再是"能不能跑" 的问题，而是"几 bit 最优" 的工程选择

### 2️⃣ **Sub-billion 架构已被重新定义**：deep-and-thin + MoE 成为新范式
- A5 MobileLLM 发现 sub-billion 下"deep-and-thin + embedding sharing + GQA"最优
- A6 Apple Intelligence 验证 sub-3B + LoRA + 量化 + 隐私架构可以 ship 给 millions
- B1 MobileMoE 把 MoE 拉到 sub-billion，识别"moderate sparsity + fine-grained + shared" 甜点
- B2 Dense2MoE 用 LF-UC 把已有 dense LLM 转换为 on-device MoE
## 摘要

量化谱系已基本完整：从 8-bit 到 1.58-bit 都有"工程可用"方案。Sub-billion 架构已被重新定义：deep-and-thin + MoE 成为新范式。Mobile NPU 进入"软件/硬件协同"时代。
## 元数据

- **来源**: {'platform': 'arxiv', 'author': 'ArXiv / Google Scholar / Semantic Scholar', 'original_date': '2026-06-14'}
- **分类**: learning
- **标签**: #paper, #llm, #on-device, #quantization, #edge, #mobile
- **评分**: 5
- **添加日期**: 2026-06-14
