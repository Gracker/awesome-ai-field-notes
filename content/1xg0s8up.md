# UI-Voyager: 自进化 GUI 智能体

**来源:** arXiv:2603.24533

**作者:** Zichuan Lin, Feiyu Liu, Yijun Yang, Jiafei Lyu, Yiming Gao, Yicheng Liu, Zhicong Lu, Yangbin Yu, Mingyu Yang, Junyou Li, Deheng Ye, Jie Jiang

**领域:** Machine Learning (cs.LG), Artificial Intelligence (cs.AI), Computer Vision and Pattern Recognition (cs.CV)

---

## 摘要

随着多模态大语言模型（MLLM）的进步，自主移动 GUI 智能体越来越受到关注。然而，现有方法在从失败轨迹中高效学习和在稀疏奖励下进行模糊信用分配方面仍存在不足。为此，我们提出了 UI-Voyager，这是一种新型的两阶段自进化移动 GUI 智能体。

在第一阶段，我们采用拒绝微调（RFT），实现数据和模型的完全自主循环协同进化。第二阶段引入群体相对自蒸馏（GRSD），通过识别群体rollout中的关键分叉点，从成功轨迹构建密集的步级监督来纠正失败轨迹。

在 AndroidWorld 上的广泛实验表明，我们的 4B 模型达到了 81.0% 的 Pass@1 成功率，优于众多最近的基线，并超越了人类水平表现。消融和案例研究进一步验证了 GRSD 的有效性。

我们的方法代表了迈向高效、自进化、高性能移动 GUI 自动化的重要一步，无需昂贵的人工数据标注。

**arXiv ID:** 2603.24533
**提交日期:** 2026年3月25日
**PDF:** https://arxiv.org/pdf/2603.24533
