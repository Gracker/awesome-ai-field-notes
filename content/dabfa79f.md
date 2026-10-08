# openTPU: An open-source AI accelerator, developed by AI

- **ID**: dabfa79f
- **原文链接**: https://github.com/FeSens/openTPU
- **作者**: FeSens (GitHub)
- **日期**: 2026-10-07（收录）
- **分类**: infra
- **来源类型**: github
- **标签**: open-source-hardware, ai-accelerator, fpga, systemverilog, agents
- **质量评分**: 4/5
- **抓取时间**: 2026-10-08T04:26:36Z

---

## 中文导读

openTPU 是一个由 AI 设计的开源 AI 加速器完整实现：硬件设计（SystemVerilog RTL）、指令集、位精确模拟器、kernel 语言与编译器、驱动真实 PCIe 卡的主机软件，全部在一个可端到端通读的 monorepo 里。设计跑在 Inspur YPCB-00338 卡（Xilinx Kintex-7 xc7k480t，双通道 DDR3）上，实测运行 10 个现代模型的真实权重——LFM2.5-230M int8 解码 59.0 tok/s（4-bit 85.8 tok/s）、Qwen3-0.6B 21.6/31.3 tok/s，最大覆盖到 Qwen3.5-4B 与 Gemma 4 E4B——且卡上产出的 token 与模拟器逐位一致。项目承接 auto-arch-tournament 的思路，问两个问题：AI agent 在硬件设计上能走多远？能不能造出运行自己推理的芯片？演示里 otpu-chat 在卡上跑 LFM2.5-230M，otpu-smi 实时显示卡利用率与 DRAM 带宽。它同时是个教学项目：想理解 AI 加速器从 Python 里的 matmul 到导线的完整链路，这是一个可以整库读完的样本。

## 为什么值得关注

RTL/ISA/模拟器/编译器/主机软件全链路开源，且经过真实 FPGA 验证、token 级对齐模拟器——说明这是可运行、可验证的完整设计，不是演示级 demo。对 agent 能力边界而言，这是罕见的硬证据：硬件设计这种容错极低的领域，agent 已经能交付真卡上跑得动的芯片。Build B 之后 DRAM 带宽已压到峰值的 91-94%，说明设计还在被持续调优。

## 关键信息

- 仓库：https://github.com/FeSens/openTPU
- 硬件：Inspur YPCB-00338（Xilinx Kintex-7 xc7k480t，双通道 DDR3-1066，峰值 17.1 GB/s），133.33 MHz，四列 systolic 矩阵单元 + stream engine
- 实测：LFM2.5-230M int8 解码 59.0 tok/s（4-bit 85.8 tok/s）；Qwen3-0.6B 21.6/31.3 tok/s（int8/4-bit）；覆盖 LFM2.5/LFM2/Qwen3/Qwen3.5/Gemma 4/SmolLM3/Phi-4-mini 共 10 个模型
- 正确性：每种配置的卡上 token 与位精确模拟器逐位一致
- 组件：SystemVerilog RTL、ISA、位精确模拟器、kernel 语言与编译器、主机软件
- 关联标签：open-source-hardware, ai-accelerator, fpga, systemverilog, agents

## English Summary

openTPU is a complete open-source AI accelerator developed by AI: SystemVerilog RTL, ISA, bit-exact simulator, kernel language with compiler, and host software in one readable monorepo. Running on a real PCIe FPGA card (Xilinx Kintex-7 xc7k480t, dual DDR3), it executes ten modern models with real weights — LFM2.5-230M at 59.0 tok/s int8 decode (85.8 tok/s at 4-bit), up to Qwen3.5-4B and Gemma 4 E4B — with card output matching the simulator bit for bit. It asks how far AI agents can go at hardware design, and whether they can build the chip that runs their own inference.

## Obsidian Notes

- 内容由 `opencli web read` 抓取 GitHub README 全文生成（opencli-first 成功）。
- 中文导读与关键信息锚定在 README 明示的硬件型号、实测吞吐表与组件清单上；README 之外的细节未补充。
