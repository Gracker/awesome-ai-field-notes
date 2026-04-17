# POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation

- **arXiv ID**: 2601.11816
- **作者**: Zahra Moslemi (UC Irvine), Keerthi Koneru (Accenture), Yen-Ting Lee (UC San Diego), Sheethal Kumar (Accenture), Ramesh Radhakrishnan (Accenture)
- **发表时间**: 2026-01-16
- **来源**: arXiv preprint
- **主题**: Agentic AI / 企业自动化 / 治理框架

---

## 核心问题

企业后台工作流（如应付账款、合同审查）要求 AI 系统必须满足：可审计（full execution traces）、策略对齐（policy-aligned）、操作可预测（operationally predictable）、副作用可管控。这些需求通用型 multi-agent 系统往往无法满足。本文要解决的核心问题是：如何在保持 agent 灵活性的同时，为企业级 agentic AI 添加可验证的治理能力。

---

## 创新点

### 1. 将 Plan 建模为 Type-Checked DAG（Typed Plan Synthesis）

不是让 LLM 自由生成执行路径，而是把执行计划建模为有类型约束的有向无环图（DAG），每个节点是 agent 调用，边必须满足 I/O 类型兼容性。这种方法在编译时就能排除类型不匹配的错误，而不是等到运行时才发现。关键约束包括：输入兼容性、合规排序（parse→validate→risk/approval）、并发限制。

### 2. Diversity-as-First-Class-Constraint（多样性作为一等约束）

现有系统通过 prompt 采样生成多个 plan 然后去重，POLARIS 反其道而行之：在生成阶段就强制要求候选计划两两结构不同（不同 agent 集合、边结构或阶段顺序），同时保持类型安全。这通过数学约束实现：∀i≠j, p_i ≁ p_j，即不存在两个等价的计划。实验证明这种结构多样性直接提升了最终选择的鲁棒性。

### 3. Rubric-Based Reasoning Selector（基于评分标准的推理选择器）

选择器不是简单的"哪个 plan 最好"，而是用一个多维评分函数：
U(p;τ) = w₁·compliance(p) + w₂·sequencing(p) + w₃·parsimony(p) + w₄·prior(p)
每个维度可审计，选择结果以 JSON 形式输出包含 chosen_index 和 reason，支持 fail-fast 拒绝。

### 4. Validator-Gated Bounded Repair Loop（验证器门控的有界修复循环）

文档解析是后台流程的主要失败模式（OCR 噪声、布局漂移），但直接重做整个解析成本高且无针对性。POLARIS 在解析后插入验证循环，验证器给出具体失败反馈（缺失字段、无效值），解析器仅针对失败字段定向重做，最多 L_max 次（通常 2-3 次）。循环在通过验证或预算耗尽时终止，后者触发人工审核或降级路径，保证系统始终有可预测的 SLA。

### 5. Compiled Policy Guardrails（编译时策略护栏）

不同于运行时检查，PolicyRetrieval 将供应商政策编译为可执行检查，在副作用发生之前就阻断或路由危险操作。策略包括：未知供应商检测、额度超限（需审批凭证）、币种不匹配。此外支持重复检测（lookback 窗口内相同供应商+发票号）、黑白名单、分级风险路由（auto-approve / review / block）和 provenance 强制（缺少 PO/收货/审批记录自动标记违规）。

### 6. Anomaly Detection with Robust MAD Baselines（鲁棒 MAD 基线的异常检测）

使用修正 Z-score 基于供应商维护的金额基线做异常检测：z(x;v) = |x - median_v| / (1.4826·MAD_v)，阈值 k_mad=3.5。供应商数据稀疏时自动回退到行业/全局统计，避免误报。同时应用日期合理性规则（issue/due/payment 日期不能在未来）。

---

## 关键实验数据

### 发票字段提取（Synthetic Suite, 160 张发票，4 个场景）

| 场景 | Precision | Recall | F1 |
|------|-----------|--------|-----|
| VU (未知供应商) | 0.9722 | 1.0000 | 0.9859 |
| VL (噪声/布局漂移) | 0.8214 | 1.0000 | 0.9020 |
| CC (清洁集) | 0.9667 | 0.9355 | 0.9508 |
| CM (月末批量) | 1.0000 | 0.9444 | 0.9714 |
| **TOTAL** | **0.9453** | **0.9680** | **0.9565** |

关键结论：VL 场景 precision 下降但 recall 仍为 1.0，说明系统宁可多提取也不漏字段；噪声场景以 precision 换 coverage 是合理权衡。

### 策略违规检测（Synthetic Suite）

| 场景 | TPV | FPV | FNV | TNV | Precision | Recall | F1 |
|------|-----|-----|-----|-----|-----------|--------|-----|
| VU | 8 | 1 | 0 | 0 | 0.8889 | 1.0000 | 0.9412 |
| VL | 1 | 1 | 2 | 2 | 0.5000 | 0.3333 | 0.4000 |
| **TOTAL** | 9 | 2 | 2 | 15 | **0.8182** | **0.8182** | **0.8182** |

关键结论：VU 场景策略违规检测精确，VL 场景召回率低源于上游解析噪声，说明解析质量直接限制下游治理效果。

### 异常检测（MAD, k=3.5）

| 场景 | TP | FP | FN | TN | Precision | Recall | F1 |
|------|----|----|----|----|-----------|--------|-----|
| VL | 6 | 5 | 1 | 0 | 1.0000 | 0.8333 | 0.9091 |
| CM | 9 | 4 | 0 | 5 | 1.0000 | 1.0000 | 1.0000 |
| **TOTAL** | 26 | 9 | 1 | 16 | **1.0000** | **0.9000** | **0.9474** |

关键结论：Precision=1.0，说明 MAD 基线方法在有足够数据时极其可靠；CM 场景（月末批量）达到 perfect detection，说明周期性数据模式被有效捕获。

### SROIE 标准测试集（4 字段提取）

| 指标 | 值 |
|------|-----|
| Overall Precision | 0.8189 |
| Overall Recall | 0.8045 |
| Overall F1 | 0.8116 |
| Company 准确率 | 0.8500 |
| Address 准确率 | 0.8500 |
| Date 准确率 | 0.7600 |
| Total 准确率 | 0.7576 |

---

## 局限

1. **评估局限于单一领域（金融发票）**：虽然论文声称框架可泛化到供应链、HR、合规等其他受监管领域，但实验仅覆盖发票处理场景。跨领域迁移时策略规则、异常基线和 agent 角色定义都需要重新设计，缺乏跨领域统一 benchmark 验证。

2. **Synthetic 测试集规模较小**：40 张合成发票分布在 4 个场景，每个场景仅 10 张；SROIE 虽为真实数据但仅为 4 字段提取任务（company/address/date/total）。在更大规模、更多样化的企业文档类型（合同、报表、邮件附件）上的表现尚未验证。

3. **修复循环的效果受限于 LLM 能力**：bounded repair loop 的效果依赖 LLM 能根据 validator 反馈准确聚焦失败字段；如果 LLM 持续无法正确理解反馈（例如遇到极端噪声或布局完全陌生的文档），循环会在 L_max 次后降级，而此时仍无有效输出。

---

## 对 AI 工程实践的启示

### 1. 类型化 + 计划合成是提升 Agent 可靠性的关键路径

POLARIS 的核心洞察是：让 LLM 自由发挥（best-of-N prompt sampling）不如让它在结构化约束下生成多样化的候选计划，再由专用 selector 评估。这比单纯增大模型或加 few-shot examples 更可控。对于需要高可靠性的 AI 应用（不仅仅是企业后台），在 agent 调用前加入类型检查和计划约束可以显著降低运行时错误率。

### 2. 策略治理必须与执行解耦，且在副作用发生前完成

传统的 AI 治理往往是事后审计，POLARIS 提出了"compiled policy guardrails"——在 API 调用或外部系统交互之前完成策略检查。这意味着 AI Agent 的工程实现需要预留独立的策略执行层，而不是把策略检查混在 agent prompt 里。对于 MTK 的 UX 性能场景，可以在执行 agent 任务前预置功耗/性能策略护栏，防止 agent 做出导致设备过热或内存溢出的操作。

### 3. Validator-Gated Repair Loop 是一个可复用的工程模式

bounded repair loop 将"发现问题 → 针对性修复 → 重新验证"封装为一个可配置次数的闭环，这个模式可以迁移到任何需要迭代改进的 agent 场景：不仅限于文档解析，也可以用于代码生成（编译失败 → 修复 → 重新编译）、测试用例生成（测试失败 → 修复 → 重新运行）。关键是验证器和修复器必须独立模块化，validator 给出可操作的反馈而非笼统的失败信号。

### 4. 评估基准需要包含治理维度，不仅仅是准确率

论文指出 AgentBench、WebArena 等现有 benchmark 缺乏 policy compliance、audit-trace completeness 等企业治理维度。这对整个 AI Agent 领域是一个重要提醒：当你为某个场景构建 agent 评测体系时，需要同时定义"什么样的错误是不可接受的"（policy violation）和"什么样的 trace 是可审计的"，否则无法真正评估系统在受监管环境中的可用性。
