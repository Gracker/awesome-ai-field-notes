# Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models

- **ID**: dbefb9b7
- **原文链接**: https://arxiv.org/abs/2611.26590
- **作者**: Jiahao Huang, Jun Wang
- **日期**: 2026-11-19
- **更新**: 2026-11-19
- **分类**: models
- **来源类型**: paper
- **标签**: interpretability, vlm, global-workspace, probing
- **质量评分**: 3/5
- **抓取时间**: 2026-11-24T15:45:00Z

---

## 中文导读

VLM 把视觉和文本信息整合进输出，但输出本身看不到内部概念表示。论文借全局工作空间理论（GWT）框架提出多模态 Jacobian lens MC-Lens：视觉编码器与语言解码器两个 lens 把中间状态映射到解码器输出词表定义的共享语义空间，跨模态比较概念可及性，并支持对内部概念做干预实验。四个发现：多模态概念信息在中间状态可读、且按任务需要被选择性访问，readout carrier 从单 token 扩展到 token 集；反事实实验表明被访问的概念信息确实参与下游计算与推理；两个 J-space 指标比隐状态余弦更清晰地追踪跨模态概念对齐的发展，且可靠的选择性访问比概念可及性更晚出现；跨 VLM 家族与规模存在共享的可及性、选择性与干预效应模式。

## 为什么值得关注

用 GWT 给 VLM 内部概念加工建实验框架是个有趣的交叉：MC-Lens 把"概念可读"推进到"概念被选择、被使用"的因果验证，"选择性访问比可及性更晚出现"这类发展性结论对训练跨模态对齐有直接参考价值。可解释性方法层面，Jacobian lens + token 集 readout carrier 也是可复用的工具。

## 关键信息

- 标题：Probing the "Conscious" Mind: Selective Access and Global Workspace in Vision-Language Models
- arXiv：2611.26590，2026-11-19，cs.AI/cs.CV/cs.LG
- 框架：全局工作空间理论（GWT）——并行过程选择信息、整合进共享工作空间、供专门过程使用
- 工具：MC-Lens 多模态 Jacobian lens；视觉编码器/语言解码器两个 lens 映射到解码器词表定义的共享语义空间；readout carrier 扩展到 token 集；支持内部概念干预
- 发现：概念信息可读且任务依赖地选择性访问；反事实证明其参与下游计算推理；J-space 指标追踪对齐发展，选择性访问晚于可及性；跨模型家族共享模式

## English Summary

Vision-language models integrate visual and textual information, but their outputs do not reveal internal concept representations. Framed by global workspace theory (GWT), the paper introduces the Multimodal Concept Lens (MC-Lens), a multimodal Jacobian lens whose vision-encoder and language-decoder lenses map intermediate states into a shared semantic space defined by the decoder's output vocabulary, comparing concept accessibility across modalities and supporting internal concept interventions. Findings: multimodal concept information is readable in intermediate states and selectively accessed as tasks require, with readout carriers extended from one name token to a token set; counterfactual experiments show accessed concept information participates in downstream computation and reasoning; two J-space metrics track the development of cross-modal concept alignment more clearly than hidden-state cosine, and reliable selective access develops later than concept accessibility; across VLM families and sizes, accessibility, query-dependent selectivity and intervention effects show shared patterns despite different internal organisation.

## Obsidian Notes

- 元数据与摘要由 `opencli arxiv paper 2611.26590 -f json` 抓取（abstract 全文锚定）。
- HF 日榜热度与选题背景出自 Obsidian 摘要笔记《AI前沿一手源 2026-11-24》。
- 中文导读与价值判断锚定在摘要声明的 lens 构造与四组实验发现上。
