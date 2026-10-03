# Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Models

- **ID**: fea3fb1c
- **原文链接**: https://arxiv.org/abs/2610.02142
- **PDF**: https://arxiv.org/pdf/2610.02142
- **作者**: Juan S. Santillana
- **日期**: 2026-10-01
- **更新**: 2026-10-01
- **分类**: agents
- **来源类型**: paper
- **标签**: tool-use, evaluation, benchmarks, keyword-matching, diagnostics, safety
- **质量评分**: 4/5
- **Fetch**: 2026-10-03T04:21:07Z

---

## 中文导读

关键词匹配基准会给小模型记上它们从未真正执行的 tool use 分：一对共享 decoder/tokenizer 的西班牙语安全模型在宽松指标上几乎同分（B4: 0.660 vs 0.650），但逐字复现训练样本的检查把它们完全分开600M 模型在 6/6 样本上给出带泛化参数的合法工具调用，1B 模型在所有检查点上都是 0/6首 token 探针把 1B 的失败定位于 先验概率被 web 预训练阶段抹掉（10^-4~10^-5）；一个约 3.3 GPU 小时的定向 SFT 用少三个数量级的 token 修复它，269 条语料行上合法发射率 0.100 -> 0.959论文提出一套严格且便宜的阶梯式诊断（逐字复现首 token 探针嵌入漂移检查），并证明修复未移动触发 token 的绑定嵌入（97.7% bf16 表逐位相同）

## 为什么值得关注

关键词基准会让 1B 模型的假 tool use 得高分：首 token 先验被 web 预训练抹掉，3.3 GPU 小时定向 SFT 即可修复

以上导读与价值判断锚定论文摘要与元数据，完整英文摘要见下文。

## 关键信息

- 论文标题：Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Models
- 作者：Juan S. Santillana
- arXiv：https://arxiv.org/abs/2610.02142
- 发布时间：2026-10-01
- arXiv 分类：cs.CL
- 关联标签：tool-use, evaluation, benchmarks, keyword-matching, diagnostics, safety

## English Abstract

Keyword-matching benchmarks can credit small models for tool use they never perform. We document such a false positive in a matched-architecture pair of Spanish security language models and propose a ladder of strict, cheap diagnostics. A 661.6M parameter model (approx. 65% code/technical text; no dedicated SFT) and a 1,109M model (web-heavy multi-phase curriculum; 6B-token tool-SFT) share decoder, tokenizer, and special tokens, scoring almost identically on lenient tool-use metrics (B4: 0.660 vs. 0.650). Verbatim-reproduction checks on training examples separate them completely: the 600M emits valid tool calls with generalized arguments on 6/6 examples; the 1B does so on 0/6 across checkpoints. A first-token probe localizes the 1B's failure to a missing prior (prob. $10^{-4}$--$10^{-5}$ on <|tool_call|>), which was erased by its web-heavy training phase. A targeted SFT recipe (diverse corpus, 5x higher learning rate, 2,202 steps, ~3.3 GPU-hours) repairs the 1B using three orders of magnitude fewer tokens than the failed phase. On all 269 corpus rows, valid emission rises from 0.100 to 0.959 (600M: 0.926). On 238 unseen prompts, the repaired 1B passes 0.536 vs. the 600M's 0.428 ($p = 0.004$). Embedding-drift checks show the repair did not move the trigger token's tied embedding (97.7% of the bf16 table remains bit-identical), meaning changes live in the surrounding network. Both models over-trigger, rarely answering negative prompts without a call (0.09 for 600M, 0.17 for repaired 1B). Factorial analyses confirm all repair configurations install the format, though suppression benefits from a diverse corpus remain a hypothesis due to seed sensitivity. This cheap diagnostic ladder costs minutes of CPU time and should gate tool-use claims on small models.

## English Summary

Keyword-matching benchmarks can credit small models for tool use they never perform. A matched-architecture pair of Spanish security LMs scores almost identically on lenient tool-use metrics (B4: 0.660 vs 0.650), but verbatim-reproduction checks separate them completely: the 661.6M model emits valid generalized tool calls on 6/6 training examples, the 1,109M model on 0/6 across checkpoints. A first-token probe localizes the 1B failure to a missing prior on the tool-call trigger token (10^-4-10^-5), erased by its web-heavy training phase; a targeted SFT recipe (~3.3 GPU-hours, three orders of magnitude fewer tokens) raises valid emission from 0.100 to 0.959 on all 269 corpus rows and beats the 600M on 238 unseen prompts (0.536 vs 0.428, p=0.004). Embedding-drift checks show the repair did not move the trigger token's tied embedding (97.7% bit-identical)....

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
