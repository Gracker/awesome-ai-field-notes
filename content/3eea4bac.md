# Benchmark: CadQuery vs. OpenSCAD for agentic CAD work

> Source: https://modelrift.com/blog/cadquery-vs-openscad
> Author: ModelRift
> Published: 2026-09-12

## Overview

ModelRift generates OpenSCAD for every model on its platform, and periodically re-tests that choice. This controlled comparison asked a narrow question: which tool can an AI agent drive to a correct, printable, functional part *with nobody watching*? Six agents (one per cell, no cross-talk), three tasks, two tools, and every resulting STL checked by an independent parser that trusts neither tool.

## Setup

All six runs driven by Claude Opus 5 (1M context) through Claude Code. Tool versions: CadQuery 2.8.0 on Python 3.14 vs OpenSCAD 2026.06.12. The OpenSCAD side ran on ModelRift's published openscad-skill; for CadQuery they ported that skill operation-by-operation (adding an offscreen renderer and B-rep validity metrics), with identical 3D-printing design rules on both sides. Tasks: **T1** L-shaped shelf bracket; **T2** two-part snap-fit enclosure for a 50x26 PCB that must actually fit; **T3** M24x2 threaded hose-barb adapter with a true helical thread — stacked rings explicitly banned.

## Results

All six parts came out printable and clean. Capability was the boring part of the answer. Iteration count was identical (11 versions each). What differs is failure character:

- **CadQuery fails loudly and early.** Error messages are poor (`BRep_API: command not done` names neither edge nor radius), but an exception stops the run — and a stopped model cannot ship by accident. In T1 the agent had to bisect by hand to discover two R3 fillets don't fit a 4 mm wall.
- **OpenSCAD fails silently and late.** In T2 it reported zero errors/warnings across ~45 invocations while deleting mounting posts, misplacing slots, and certifying a corrupted export as clean; its Manifold backend stamped `Status: NoError` on an STL with 4 non-manifold edges and 60 zero-area triangles.
- **T3 upset:** OpenSCAD finished in one version, correct on first compile, in 43 ms — hand-writing the helix as raw vertex/face arithmetic in a single `polyhedron`. CadQuery's readable `makeHelix`+sweep worked, but `union()` silently discarded the core cylinder because the thread root sat exactly on the core radius (volume 7065 mm³ vs 10323 expected; `valid=True`, `solids=1`). Only a volume measurement caught it.
- **Renders caught nothing that mattered.** Across six runs, images caught only coarse blunders; every print-ruining defect was found by a number — volume, angle, interference test.
- **CadQuery can be interrogated; OpenSCAD cannot.** Agents asserted box/lid interference volume and read countersink angles off the B-rep; OpenSCAD agents independently wrote their own STL parsers to measure what they had built.

## Takeaways

Verifiability beats expressiveness in an agent loop: being able to ask the kernel what you just built — and assert on the answer — outweighs syntax convenience. Task shape decides more than the tool. If a pipeline leans on screenshots, it leans on the one channel that caught nothing here; force numeric assertions (wall thickness, clearance, interference volume, overhang angle) and audit the exported mesh independently, because both toolchains certified wrong geometry. ModelRift stays on OpenSCAD, adding a feature-edge renderer and a mandatory numeric check pass.

## 中文概要

ModelRift 用同一模型（Claude Opus 5 1M，经 Claude Code）驱动六个独立子智能体，在三个 CAD 任务（L 形支架、50x26 PCB 卡扣外壳、M24x2 螺纹软管接头）上对比 OpenSCAD 与 CadQuery，所有 STL 由独立解析器审计。六个零件全部可打印，迭代次数相同（各 11 版），真正的差异在失败模式：CadQuery "响亮而早"——报错难懂但会停机；OpenSCAD "沉默而晚"——T2 任务约 45 次调用零报错，却删掉了安装柱、导出损坏 STL 还自证干净（Manifold 后端把含 4 条非流形边的网格判为 NoError）。最大冷门在 T3：OpenSCAD 手写 polyhedron 真螺旋螺纹一次编译通过（43ms、1 版），CadQuery 的 union() 因螺纹根与核心柱恰好相切而静默丢掉核心柱（体积 7065 vs 10323 mm³，valid 仍为 True），靠体积测量才被抓到。渲染图六次运行没抓到任何致命缺陷，救场的全是数字。结论：对无人值守生成，可验证性压过表达力——必须强制数值断言（壁厚、间隙、干涉体积、悬垂角）并独立审计导出网格。
