# Early progress on accelerating drug development with Claude

- **ID**: fdf27bf9
- **原文链接**: https://www.anthropic.com/research/early-progress-drug-development
- **作者**: Anthropic（Team Science）
- **日期**: 2026-10-27（Published Oct 27, 2026）
- **分类**: industry
- **来源类型**: article
- **标签**: anthropic, life-sciences, drug-development, deep-research, hackernews
- **质量评分**: 4/5
- **抓取时间**: 2026-10-28T12:24:53Z

---

## 中文导读

Anthropic 生命科学团队发布进展报告：过去数月与 BigHat Biosciences、Bristol Myers Squibb、Divergence Labs、Enveda、Generate Biomedicines、The Column Group 六家新药研发机构开展深度研究合作，并启动自有药物发现工作（收购一人公司 Mithril Medicine，针对罕见儿童型肌营养不良）。公司策略是把 AI 嵌入药物研发全链条——靶点选择、分子设计、生产放大、监管申报与临床试验——而非只做分子初筛，瓶颈分布在整个流程。已产出首个用于评估药物靶点价值的 Claude skill。文中明确所有工作仍处早期、以临床前为主；若当前轨迹延续，远期目标是食物过敏、罕见儿童病与多种癌症的药物。

## 为什么值得关注

这份报告的价值不在「AI 制药」的叙事，而在它给出了可核对的具体结果（抗体设计数量、变体测试数、质检页数、时间节省百分比）和明确的局限性声明（临床前为主）。它把药物研发描述为瓶颈分布在全流程的任务集合，并以真实管线合作来定位模型强弱边界——这是判断 AI for Science 进展时更可校准的一手材料。

## 六个合作案例与自有项目（数据来自原文）

- **Generate Biomedicines（模态工程 / CAR-T）**：六名科学家用 Claude Code 重新设计 CAR-T 疗法的基因序列片段，最短方案比标准版短约 70%；实验室测试中免疫细胞受体产量约为原来的 10 倍，肿瘤杀伤更高效、活性持续更久。
- **Divergence Labs（hit generation / 食物过敏）**：针对「把 IgE 从免疫细胞上解离」的双臂抗体思路，Claude 将目标转化为设计计划后，在约一个月内基本自主生成约 35,000 个抗体设计；早期测试两臂均有 hit——3 个设计可紧密结合 IgE，20 个可使其解离，其中 3 个解离效果优于标准药物。
- **BigHat Biosciences（lead optimization）**：Claude 接入其实验数据系统 Reccy，10 周内制造并测试约 1,010 个变体；期间团队怀疑标准热稳定性/聚集指标有误导，Claude 与研究员重分析原始数据、提出新指标与实验方案变更，主预测成立。最终最佳版本结合力提升 10 倍以上，癌靶 lead 溶解温度高 18°C，长效 lead 聚集慢 100 倍以上。
- **Enveda（生产与申报）**：把全部生产文档接入 Claude 做质检，在 1,061 页文档测试中抓住人工评审发现的全部 11 个问题、并多报 7 个人工遗漏，人工复核时间从 25 小时以上降至不足 3 小时（-89%）；两份监管文件初稿其一 4 小时完成（人工约需 3 个月），另一份经标准人工复审仅 1 处小错。
- **The Column Group / Pleiades（公司创建）**：新公司 Pleiades 用 Claude 让小团队并行更多、更复杂的药物管线；其首个 Claude skill 用于评估药物靶点是否值得投入，已在 45 个靶点-疾病对上完成评估。
- **Bristol Myers Squibb（临床试验规划）**：用 Claude 分析专有数据、生成临床研究计划并估计试验成功概率；双方计划 2027 年扩展到管线层面决策。
- **自有项目 / Mithril Medicine**：收购的一人公司创始人 Cody Tranbarger 曾用 Claude 协调 11 个外部实验室的合同、物流与实验；一种肌营养不良候选疗法从想法到小鼠阳性结果不足 18 个月，若数据继续成立，最快 2028 年底进入人体临床试验。

## 公司层面的配套动作

- **Claude Science**：面向研究者的 AI 工作台；
- 为生命科学家提供 Claude credits；
- **Life Sciences Verification Program**：让受信任机构在更宽松的安全配置下使用最强模型（常规防护会阻碍正当生物研究）；
- 开放生命科学客座研究员（guest investigators）提案征集。

## English Summary

Anthropic's life sciences team reports months of deep research partnerships with six medicine-development organizations — BigHat Biosciences, Bristol Myers Squibb, Divergence Labs, Enveda, Generate Biomedicines, and The Column Group — plus in-house drug discovery via the Mithril Medicine acquisition. The strategy is to embed AI across the entire drug development pipeline (target identification, molecule design, manufacturing, regulatory filings, clinical trials) rather than any single step, because the bottlenecks are distributed throughout. Concrete early results include ~35,000 largely autonomous antibody designs in about a month with hits on both arms (Divergence Labs), 1,010 lead variants tested in 10 weeks with >10x tighter binding, +18°C stability and >100x slower clumping (BigHat), and an 89% reduction in manufacturing-document review time with 7 issues humans missed (Enveda). The company is explicit that everything remains early and mostly preclinical; stated long-term goals include medicines for food allergies, rare childhood diseases, and several cancers.

## Source Excerpts

> "There is no single problem to solve; the bottlenecks are distributed all throughout the drug development process. The best way to identify and work through these bottlenecks is to get deeply involved in real drug programs, across many different disease areas and stages of development."

> "All of this research is still at an early stage. In particular, so far it is mostly preclinical — that is, for the most part, it isn't yet at the stage where the drugs are being tested in humans."

## Obsidian Notes

- 抓取路径：`opencli web read` 导航被拒（Navigation rejected）→ `curl --http1.1 -4` 直取 Next.js 预渲染页成功；正文锚定为页面可见文本（约 12,000 字符）。
- 本页为 content-fetcher 内容回填：全部案例数据取自 2026-10-27 发布的原文；条目元数据来自 `data/entries.json`，本次不改动条目数据。
- 发现渠道含 Hacker News（tags: hackernews）。
