# LazyWeights: Decode-on-Demand Edge LLMs

- **ID**: 7cdffde4
- **原文链接**: https://arxiv.org/abs/2611.17108
- **作者**: Arnab Sanyal, Gourav Datta, Sandeep P. Chinchali
- **日期**: 2026-11-12
- **来源类型**: paper (arxiv)
- **标签**: arxiv, quantization, edge-inference, huffman-coding, asic, llama.cpp
- **质量评分**: 4/5
- **抓取时间**: 2026-11-14T15:46:48Z

---

- **分类**: models

## 中文导读

端侧 LLM 在小设备卡内存容量、大设备卡内存带宽，而 GPTQ/AWQ/llama.cpp 等现役量化格式对每个码字平均花同样比特，实际码分布远不均匀。LazyWeights 不换格式：调 GPTQ 让码可压缩，再按交错 lane 做 Huffman 无损编码，在 DRAM 与 L2 之间放小解码单元按需解码，GPU kernel 原样运行。1%/3.5% 困惑度预算下比最好的 llama.cpp 格式小 5.7-31.4%；0.21 平方毫米的位精确 ASIC 解码器把 Orin 每 token 延迟/能耗最多降 36%/38%，Jetson Nano 流式 Mistral-7B 快 6.6 倍，压到 3.89 bit/权重。

## 为什么值得关注

端侧量化+硬件解码的完整账：Jetson 数字扎实，对手机 SoC 的内存带宽瓶颈同样成立。

## 关键信息

- 标题：LazyWeights: Decode-on-Demand Edge LLMs
- 链接：https://arxiv.org/abs/2611.17108
- 作者：Arnab Sanyal, Gourav Datta, Sandeep P. Chinchali
- 日期：2026-11-12
- 标签：arxiv, quantization, edge-inference, huffman-coding, asic, llama.cpp

## English Abstract (arXiv)

Memory decides which LLMs an edge device runs, and how fast: capacity on a $4$ GB Jetson Nano, bandwidth on an $8$ GB Jetson Orin Nano Super. Deployed formats (GPTQ, AWQ, $\texttt{llama.cpp}$'s K- and I-quants) spend equal bits on every integer code of a matrix, although the codes are far from uniform. $\texttt{LazyWeights}$ keeps these formats but tunes GPTQ so the codes compress, Huffman-codes them losslessly in interleaved lanes, and decodes them on demand in a small unit between DRAM and L2, so GPU kernels run unchanged and DRAM moves only coded bytes. At $1\%$ and $3.5\%$ perplexity budgets, coded Phi-3-mini, Mistral-7B and SmolLM-1.7B are $5.7-31.4\%$ smaller than the best $\texttt{llama.cpp}$ format. A bit-exact $0.21$ mm$^2$ ASIC decoder unit ($1$ GHz, $7$ nm) cuts Orin latency and energy per token by up to $36\%$ and $38\%$ ($54\%$ and $44\%$ with prompt-lookup speculation). On the Nano, $\texttt{LazyWeights}$ needs $58-64\%$ less time and $53-57\%$ less energy per token than CPU $\texttt{llama.cpp}$, and runs a streamed Mistral-7B 6.6$\times$ faster at $3.89$ bits per weight. A Huffman decoder beats an rANS decoder in rate and area at equal throughput; the ASIC decoder unit runs bit-exact on a Zynq UltraScale+ FPGA (AMD ZCU102).

## 元数据来源

- 经 opencli arxiv paper 抓取 arXiv 元数据（2026-11-14T15:46:48Z）；摘要原文如上。
- arXiv 分类：cs.LG, cs.AR, cs.CL, cs.IT
- 提交/更新：2026-11-12 / 2026-11-12

## AAIF 收录说明

- 收录批次：2026-11-14 daily-intake-evening（来源：AK-RSS 2026-11-14 / last30days 2026-11-14 / 论文流水线 2026-11-14 / X-seeds 2026-11-13 / DeepResearch 调研材料）。
