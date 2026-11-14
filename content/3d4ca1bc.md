# Classical Energies Learn to Reason 1,000x Faster than Looped Models

- **ID**: 3d4ca1bc
- **原文链接**: https://arxiv.org/abs/2611.17309
- **PDF**: https://arxiv.org/pdf/2611.17309v1
- **作者**: Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- **日期**: 2026-11-12
- **更新**: 2026-11-12
- **arXiv 分类**: cs.AI, cs.LG
- **来源类型**: paper (arxiv)
- **标签**: arxiv, energy-based-models, reasoning, looped-models, benchmarks
- **质量评分**: 4/5
- **抓取时间**: 2026-11-14T04:21:50Z

---

- **分类**: models

## 中文导读

把 1980 年代的 Hopfield & Tank 能量模型改成可学习版本，单 GPU 上毫秒级训练就解掉 Sudoku-Extreme / Maze-Unique，比 looped 模型至少快 1000 倍、推理 FLOPs 少 282 倍以上。本页由 arXiv 元数据与摘要生成。

## 为什么值得关注

把 1980 年代的 Hopfield & Tank 能量模型改成可学习版本，单 GPU 上毫秒级训练就解掉 Sudoku-Extreme / Maze-Unique，比 looped 模型至少快 1000 倍、推理 FLOPs 少 282 倍以上。两点更值得记：能量下降自带早停与难度自适应算力，可能是从数据训练推理的另一条路线；以及作者明说——这类可被平凡求解的基准已无法检验 looped 推理的可扩展性。

## 关键信息

- 论文标题：Classical Energies Learn to Reason 1,000x Faster than Looped Models
- 作者：Benjamin Hoover, Hugh Blayney, James C. R. Whittington
- arXiv：https://arxiv.org/abs/2611.17309
- 发布时间：2026-11-12
- arXiv 分类：cs.AI, cs.LG
- 关联标签：arxiv, energy-based-models, reasoning, looped-models, benchmarks

## English Abstract

Looped models have emerged as a prominent paradigm for reasoning, with successes on simple reasoning puzzles such as Sudoku-Extreme and Maze-Unique. However, these models can be unstable, slow to train, and use many parameters and FLOPs to solve simple puzzles. Descent on an energy not only mitigates these issues but also offers advantages: built-in early stopping, compute that adapts to problem difficulty, fast training without differentiating through a solver, and interpretable weights that learn the constraints of the puzzle. Here we demonstrate this with a learned version of Hopfield & Tank's energy from the 80s, which we term CRAM, solves 99.996% of Sudoku-Extreme and 100% of Maze-Unique test puzzles after 42 ms and 132 ms of training on one GPU, at least 1,000x faster than looped models on these tasks. CRAM also matches baseline looped models at their highest accuracy on Sudoku-Extreme using at least 282x fewer inference FLOPs. Our work suggests two things. First, that energies are an extremely promising direction for training reasoning from data. Second, a caution against using trivially solvable benchmarks like Sudoku and Maze to test the scalability of looped reasoning techniques.

## English Summary

Looped models reason on puzzles like Sudoku-Extreme and Maze-Unique but can be unstable, slow to train, and parameter/FLOP-heavy. The authors turn Hopfield & Tank's 1980s energy into a learned model, CRAM: descending on an energy gives built-in early stopping, compute that adapts to problem difficulty, fast training without differentiating through a solver, and interpretable weights that learn puzzle constraints. CRAM solves 99.996% of Sudoku-Extreme and 100% of Maze-Unique test puzzles after 42 ms and 132 ms of training on one GPU - at least 1,000x faster than looped models - and matches baseline looped models at their highest Sudoku accuracy using at least 282x fewer inference FLOPs. Two takeaways: energies are a promising direction for training reasoning from data, and trivially solvable benchmarks like Sudoku and Maze no longer test the scalability of looped reasoning techniques.

## Obsidian Notes

- 内容由 `opencli arxiv paper` 拉取 arXiv 元数据与摘要生成。
- 中文导读与价值判断均锚定在条目已有摘要、论文摘要、作者、日期与分类信息上；未补充论文摘要之外的实验细节。
