# Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs

- **ID**: 9f96bbda
- **原文链接**: https://arxiv.org/abs/2609.10355
- **PDF**: https://arxiv.org/pdf/2609.10355v1
- **作者**: Killian Steunou, Yannis Tevissen, Mounîm A. El Yacoubi
- **日期**: 2026-09-09
- **更新**: 2026-09-09
- **分类**: cs.CV, cs.CL, cs.MM
- **来源类型**: paper
- **标签**: survey, videollm, inference-efficiency, token-reduction, field-note
- **质量评分**: 4/5
- **抓取时间**: 2026-09-11T12:23:09+00:00

---

## 中文导读

VideoLLM 在 captioning/QA/检索/时序定位上表现强，但计算与内存成本随帧数和上下文长度增长，卡死了实时移动端和资源受限部署 这是系统综述：只收录报告了具体削减量（参数量每输入 FLOPs延迟内存视觉/音频 token 数）的视觉与音视频 VideoLLM 效率机制 按流水线阶段组织方法：帧采样模态编码connector 级 token 削减LLM prefilling 与解码，逐段分析瓶颈；覆盖 2022 年末以来的 VideoLLM 和至今仍在流水线里的早期帧采样/视觉编码器机制 在共享宿主模型和输入协议下汇编精度-成本对比，与异质跨论文证据区分开；指出音视频效率与标准化评测的空白；配维护中的 GitHub 仓库（momentslab/awesome-efficient-videollm）

## 为什么值得关注

VideoLLM 推理效率综述：按帧采样/模态编码/connector token 削减/prefill 解码四个流水线阶段组织方法，只收有具体削减数据的工作，附持续维护的 awesome 列表

条目锚定 arXiv 2609.10355（2026-09-09 提交，分类 cs.CV, cs.CL, cs.MM），摘要自述贡献为上述机制与结论；详细信息以论文原文为准。

## 关键信息

- 论文标题: Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs
- 作者: Killian Steunou, Yannis Tevissen, Mounîm A. El Yacoubi
- arXiv: https://arxiv.org/abs/2609.10355
- 发布时间: 2026-09-09
- arXiv 分类: cs.CV, cs.CL, cs.MM
- 关联标签: survey, videollm, inference-efficiency, token-reduction, field-note

## English Abstract

Video understanding has rapidly evolved toward video large language models (VideoLLMs): systems that couple video representations with pretrained large language models and condition generation on a textual prompt. Their strong performance on captioning, question answering, retrieval and temporal grounding comes at a computation and memory cost that grows with frame count and context length, limiting deployment in real-time, mobile and resource-constrained settings. This survey covers inference-efficiency mechanisms for visual and audiovisual VideoLLMs that report concrete reductions in parameter count, FLOPs per input, latency, memory, or visual and audio token count. We analyze bottlenecks across frame sampling, modality encoding, connector-level token reduction, and LLM prefilling and decoding. We organize methods by the pipeline stage at which they act, covering VideoLLMs developed since late 2022 together with earlier frame-sampling and vision-encoder mechanisms that remain components of current pipelines. We assemble literature-reported accuracy--cost comparisons under shared host models and input protocols wherever available, distinguish them from heterogeneous cross-paper evidence, and identify gaps in audiovisual efficiency and standardized evaluation. We maintain a repository at https://github.com/momentslab/awesome-efficient-videollm.

## English Summary

A survey of inference-efficiency mechanisms for visual and audiovisual VideoLLMs that report concrete reductions in parameter count, FLOPs per input, latency, memory, or visual/audio token count. It analyzes bottlenecks across frame sampling, modality encoding, connector-level token reduction, and LLM prefilling and decoding, organizing methods by pipeline stage; covers VideoLLMs since late 2022 plus earlier frame-sampling and vision-encoder mechanisms still in current pipelines. Assembles literature-reported accuracy-cost comparisons under shared host models and input protocols, distinguishes them from heterogeneous cross-paper evidence, identifies gaps in audiovisual efficiency and standardized evaluation, and maintains the momentslab/awesome-efficient-videollm repository.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
