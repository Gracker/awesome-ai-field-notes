# ⚡ 基础设施

推理部署 / RAG / 微调 / 评测 / 多模态 — 共 **46** 条活跃资源

## 📅 2026-05-02

### [Anthropic 正在与英国 AI 芯片初创 Fractile 洽谈采购推理芯片](/entry/akye56py) 📄
@The Information · ⭐⭐⭐3 🌐 · 2026-05-02

据 The Information 报道，Anthropic 正在与英国 SRAM 基 AI 芯片初创公司 Fractile 进行早期洽谈，计划在 2027 年 Fractile 产品上市后采购其推理芯片。随着 Anthropic 销售额爆发式增长，现有服务器供应（来自 Google、Amazon、Nvidia）已面临压力。此举反映了 AI 公司正在积极多元化芯片供应链，以应对日益增长的推理算力需求。Fractile 的 SRAM 基方案代表了一种不同于传统 GPU 的推理加速路径。

`Anthropic` `AI芯片` `Fractile` `推理` `供应链`

---

## 📅 2026-04-30

### [Building with Gemini Embedding 2: Agentic multimodal RAG and beyond](/entry/696f3474) 📄
⭐⭐⭐⭐4 🌐 · 2026-04-30

Gemini Embedding 2 正式GA，是首个将文本、图像、视频、音频和文档映射到统一语义空间的多模态嵌入模型。支持超过 100 种语言，单次调用可处理 8192 token 文本、6 张图像、120 秒视频、180 秒音频和 6 页 PDF。通过 task prefix 实现非对称检索，显著提升 Agentic RAG 和视觉搜索精度。法律平台 Harvey 借此 Recall@20 提升 3%，视觉搜索 Match@20 从 60% 提升至 87%。

`gemini` `embedding` `multimodal` `RAG` `vision-search`

---

## 📅 2026-04-26

### [awesome-gpt-image-2: World&#x27;s largest GPT Image 2 prompt library](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) ⭐4,266
@YouMind-OpenLab · ⭐⭐⭐3 🌐 · 2026-04-26

awesome-gpt-image-2 是目前最大的 GPT Image 2 提示词库，每日更新，汇集 1800+ 精选提示词并附带预览图，支持 16 种语言。GPT Image 2 的核心能力：精准文字渲染（中日英）、跨图一致性、商业级插画输出、故事板/IP 角色生成、多语言设计海报。同时提供 YouMind GPT Image 2 Prompts Gallery 在线画廊，支持分类浏览和 AI 一键生成。GitHub 2558 Stars。

`gpt-image-2` `openai` `prompt-library` `image-generation` `multimodal`

---

## 📅 2026-04-18

### [Google推出企业版Android Studio Gemini：隐私保护的企业级AI编程辅助](/entry/gok4hbw1) 📄
@Sandhya Mohan (Google) · ⭐⭐⭐⭐4 🌐 · 2026-04-18

Google在Android Studio中推出企业版Gemini，提供超越消费版的高级隐私保护：客户代码和输入不用于训练共享模型，数据由客户自有，SOC 1/2/3和ISO/IEC 27001等多项认证覆盖，并支持Private Google Access、VPC Service Controls和细粒度IAM权限。面向对数据安全有要求的大中小企业，标志着AI编程辅助工具进入企业合规时代。

`android` `gemini` `google` `enterprise` `code-assist`

---

## 📅 2026-04-11

### [破局Agent时代：ARIES RISCV+AI架构分析](/entry/jvblhpoud3ey) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-04-11

ISSCC 2026 展示的 ARIES 架构代表了 AI 芯片从算力怪兽向有脑子的行动派的进化路线。ARIES 通过 RISC-V CPU 集成（调度控制前额叶）+ 280MB 大容量 SRAM + CIM 存内计算，实现 PD/AF 融合方案（拒绝 NVIDIA/Groq 的物理分离路线），以 14nm 工艺在能效比上超越 4nm GPU。其三引擎 NPU Core（TCE/TME/VCE）+ 相似性感知 TCAM + LUT 非均匀量化，构成 Agent 时代芯片的差异化竞争力。

`risc-v` `ai-chip` `agent-era` `in-memory-computing` `cim`

---

### [破局Agent时代：ARIES RISCV+AI架构分析](/entry/n3m8itb5) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-04-11

本文深度分析 ISSCC 2026 展示的 ARIES 芯片架构，这是一款专为 AI Agent 时代设计的 RISC-V+AI 异构 SoC。核心创新三点：第一，将 RISC-V CPU 直接集成进 SoC 核心区作为调度单元，解决传统 NPU 控制流跳回 Host CPU 的 PCIe 时延问题；第二，采用统一 Tile + 独立时钟域替代 PD/AF 物理分离，同一硬件动态切换算力密集和访存密集模式；第三，堆 280MB 片内 SRAM + CIM 存内计算消灭访存瓶颈，通过 LUT-based 多精度量化在 14nm 工艺实现超越 4nm GPU 的能效比（YOLO 系列 10.12x FPS/W 提升）。ARIES 代表了 Agent 时代逻辑控制与极致算力耦合的实用主义芯片设计路线。

`risc-v` `ai-chip` `npu` `llm-inference` `agent`

---

## 📅 2026-04-10

### [&quot;Philosophers warn us not to be satisfied with mere learning, but to add practice and then training.&quot; | Revue](https://newsletter.stoicallytyped.com/issues/philosophers-warn-us-not-to-be-satisfied-with-mere-learning-but-to-add-practice-and-then-training-725262#/)
⭐⭐⭐3 🌐 · 2026-04-10

&quot;Philosophers warn us not to be satisfied with mere learning, but to add practice and then training.&quot; | Revue
StoicallyTyped Newsletter - Hey happy Monday!I&#x27;m on vacation! I have some time before I start my new job and am taking advantage of all this free time to visit f
Read in Cubox  
Read Original
&quot;Philosophers warn us not to be satisfied with mere learning, but to add pract...

`Newsletter`

---

## 📅 2026-04-06

### [搞懂缓存机制，从Gemma4到Claude Code省80%Token](/entry/otjpnj3j) 📄
@MinLiBuilds · ⭐⭐⭐⭐⭐5 🇨🇳 · 2026-04-06

从本地 Gemma 4 实验出发，详解 Transformer KV 缓存原理（QKV 注意力机制中的 Key/Value 缓存），解释为什么 Decoder-only 架构可以缓存历史 token 的 KV。逆向分析 Claude Code 的缓存实现，Anthropic 做了一整套精密的缓存工程。理解后可让同样的套餐多撑 3-5 倍。

`kv-cache` `claude-code` `token-optimization` `transformer` `caching`

---

### [AI工具设计：为什么需要理解用户心理](/entry/e1ed05fa) 📄
@Avi Chawla · ⭐⭐⭐⭐4 🌐 · 2026-04-06

Avi Chawla 通过 Claude Code 案例详细解析了 LLM Prompt Caching 的技术原理与工程实践。核心观点：KV Cache 将计算复杂度从 O(n^2) 降至 O(n)，静态前缀（系统指令、工具定义、项目上下文）可被缓存并以 0.1x 价格读取。Claude Code 实测 92% Cache Hit Rate，实现 81% 成本降低（$6.00 -&gt; $1.15）。三大工程原则：不要在会话中修改工具定义、不要中途切换模型、不要在缓存前缀中注入状态变量。

`prompt-caching` `kv-cache` `claude` `cost-optimization` `agent`

---

### [用 LLM + Obsidian 构建个人知识库：基于 Karpathy 的&quot;LLM Knowledge Bases&quot;工作流](/entry/n28eerxp) 📄
@yanhua1010 · ⭐⭐⭐⭐4 🇨🇳 · 2026-04-06

基于 Karpathy 的 LLM Knowledge Bases 工作流，将知识库管理类比为 CI/CD：原始资料→编译产物→运行时输出三层分离。用 Obsidian + Claude Code 实现三层目录结构：raw/（摄取）、wiki/（编译成品）、平台目录（发布）。三个摄取入口（Web Clipper、Podwise、手动剪藏），编译环节包含逐篇摘要、概念抽取、索引更新。强调增量编译和质量保障。

`obsidian` `llm` `knowledge-base` `karpathy` `compile`

---

### [My self-sovereign / local / private / secure LLM setup, April 2026](/entry/4abfo505) 📄
⭐⭐⭐⭐4 🌐 · 2026-04-06

Vitalik Buterin 分享其本地私有 LLM 使用方案。隐私安全目标：防止远程模型获取隐私数据、防止 LLM 越狱攻击、防止后门和软件漏洞。硬件测试：NVIDIA 5090 (90 tok/s)、AMD 128GB 统一内存 (51 tok/s)、DGX Spark (60 tok/s)，推荐 5090 或 AMD 方案。软件栈：NixOS + llama-server（替代 Ollama，因能更好利用 GPU）+ llama-swap。Agent 工具方面讨论了 OpenClaw 的安全问题，强调沙箱隔离的重要性。附带 ComfyUI 本地图像/视频生成测试。

`local-LLM` `privacy` `security` `Vitalik` `self-sovereign`

---

### [用 Obsidian + Claude 搭个人知识库：核心架构实践](/entry/f71nn8lk) 📄
@yanhua1010 · ⭐⭐⭐3 🇨🇳 · 2026-04-06

Obsidian + Claude 搭建个人知识库的核心架构实践。核心思路：把笔记库当代码仓库来&quot;编译&quot;。三层目录结构：原料/（只读，Claude 不可修改）→ 摘要/（Claude 结构化编译产物）→ 沉淀/（Query 高质量回答落文件）。两个元文件：CLAUDE.md（控制 AI 行为的最高宪法）和 index.md（全局目录 + TLDR，Claude 检索时先扫再深读）。日常工作流三个动作：Ingest（逐篇处理）、Query（好回答存文件）、Lint（定期健康检查）。防腐化底线：重要断言必须有来源、新旧冲突报 diff 不覆盖、区分事实和推论。

`Obsidian` `Claude` `知识库` `CLAUDE.md` `个人知识管理`

---

### [V 神本地 LLM 环境配置](/entry/5hd30k75) 📄
@马天翼 · ⭐⭐⭐3 🇨🇳 · 2026-04-06

V 神分享的本地大模型环境配置博客。从硬件选型开始，详细讨论如何构建一套满足隐私、安全、离线要求的 Local LLM 环境。特别值得注意的细节：为了减少飞机上离线情况下的模型幻觉，他把 1GB 维基百科内容都存了下来方便模型自我核实。同时也考虑了预算有限朋友的硬件推荐方案。

`本地LLM` `Vitalik` `隐私` `离线` `硬件配置`

---

## 📅 2026-04-05

### [Karpathy 最新方法论：把 LLM 当编译器用，知识管理该换个思路了](/entry/ryn4vd8o) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-04-05

解读 Andrej Karpathy 2026 年 4 月提出的 LLM 知识库方法论。核心类比：把 LLM 当编译器，原始资料当源代码，生成 Wiki 当可执行文件。三层目录结构：raw/（原始素材）、wiki/（LLM 编译产出的结构化 Markdown）、output/（查询结果和衍生输出）。四步工作流：摄入（Ingest）到编译（Compile）到查询（Query）到健康检查（Lint）。与 RAG 的关键区别：RAG 是查询时实时检索（临时性），Karpathy 的方法是提前编译（持久性），查询结果自动回写 Wiki。适用规模约 40 万字，不需要向量数据库。

`Karpathy` `knowledge-management` `LLM` `wiki` `obsidian`

---

### [LLM Knowledge Bases](/entry/nha3a46y) 📄
@Andrej Karpathy · ⭐⭐⭐⭐4 🌐 · 2026-04-05

Karpathy 分享他用 LLM 构建个人知识库的工作流：raw/ 目录存放原始文档，LLM 增量&quot;编译&quot;成 .md wiki（含摘要、反向链接、概念分类文章）；用 Obsidian 作为 IDE 前端查看原始数据、编译产物和可视化；wiki 达到约 100 篇文章/40 万字后，可以直接向 LLM agent 提问复杂问题。关键发现：不需要 fancy RAG，LLM 自己会维护索引文件和文档摘要。输出形式包括 Markdown 文件、幻灯片（Marp 格式）、matplotlib 图像。还会用 LLM 做 wiki 健康检查（不一致数据、缺失数据、新文章候选）。

`LLM` `知识库` `Obsidian` `Markdown` `RAG`

---

## 📅 2026-03-30

### [当 AI Agent 开始直接调用数据，基础设施该如何进化？Data for AI Meetup 深圳站回顾](/entry/nMGRQWXE) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-03-30

当 AI Agent 开始直接调用数据，基础设施该如何进化？Data for AI Meetup 深圳站回顾

---

## 📅 2026-03-11

### [AI 是一块“五层蛋糕”](/entry/nivhloc2) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-03-11

Read in Cubox  
Read Original
**2026 年 3 月 10 日 作者 黄仁勋**
AI 是塑造当今世界的强大力量之一。它并非仅仅是一款巧妙的应用程序，也不是单一的模型，而是如同电力和互联网一样必不可少的基础设施。
AI 依托真实的硬件、能源和经济体系运行。它可以将原材料大规模地转化为智能。每家公司都将应用 AI， 每个国家/地区都将发展 AI。
要理解 AI 为何以这种方式发展，我们需要从基本原理进行推理，并了解计算领域发生了哪些根本性变化。

`Inference`

---

### [Quantifying infrastructure noise in agentic coding evals](/entry/itikhf3n) 📄
@Anthropic Engineering · ⭐⭐⭐⭐4 🌐 · 2026-03-11

Anthropic工程团队量化了Agent编程评测中的基础设施噪声问题。发现即使在相同环境下重复运行相同的Agent评测，结果也会因网络延迟、API负载、容器调度等因素产生显著波动。这对SWE-Bench、Terminal-Bench等评测的可靠性提出了挑战。提出了减少噪声的方法论建议。

`anthropic` `evaluation` `agentic-coding` `benchmarks` `noise`

---

## 📅 2026-03-09

### [MeKi —— 用 ROM 扩展端侧 LLM，而不是继续硬堆计算](/entry/3cd7qdt3) 📄
@允许动态投影、归一化、非线性映射这些复杂结构存在，以保证模型能学到足够好的知识表达；部署前，再把这些东西折叠到静态查表结构里。于是： · ⭐⭐⭐⭐4 🇨🇳 · 2026-03-09

**论文**：MeKi: Memory-based Expert Knowledge Injection for Efficient LLM Scaling  
**精读日期**：2026-03-09  
**定位**：面向 Android / 端侧 AI / 性能优化 / SmartPerfetto 方向的深度解读

---

## 一、论文要解决的问题
### 1.1 真正的问题不是“模型不够大”，而是“手机端的资源结构不匹配”
在服务器上，做大模型最直接的办法就是：
- 增加参数量；
- 增加推理时计算；
- 用更大的显存和更强的 GPU 接住它。

但到了手机端，这套思路就开始失效：
…

`perfetto` `on-device` `agent` `android` `llm`

---

## 📅 2026-03-08

### PocketLLM: Enabling On-Device Fine-Tuning for Personalized LLMs
⭐⭐⭐3 🇨🇳 · 2026-03-08

## 1. 核心问题
这篇论文解决的是“端侧个性化”中最现实的拦路虎：**微调内存开销**。很多工作证明了“可以做微调”，但通常在树莓派或实验环境，离手机实用化很远。PocketLLM 的价值在于把问题拉回到真实手机场景。

## 2. 论文贡献（按价值排序）
1) **明确瓶颈优先级**：在端侧微调中，内存是可行性门槛；算力更多影响时延。
2) **方法选择正确**：采用无导数优化绕开梯度/优化器状态，直接打掉最大内存项。
3) **实机验证**：在 OPPO Reno 6 上给出可复现实验（RoBERTa-large 与 OPT-1.3B）。

## 3. 关键数据的含义
- RoBERT…

`perfetto` `on-device` `fine-tuning` `coding` `android`

---

## 📅 2026-02-28

### [Qwen3.5-122B-A10B Pooled on Dual Mac Studio M4 Max with Exo + Thunderbolt 5 RDMA](/entry/3pu0nwgt) 📄
@TrevinPeterson · ⭐⭐⭐⭐4 🌐 · 2026-02-28

24+ 小时调试后，在两台 Mac Studio M4 Max 上通过 Exo + Thunderbolt 5 RDMA 实现了 Qwen3.5-122B-A10B 的完整池化运行。持续吞吐约 52 tok/s，并发 c=2 稳定（p95 约 10.37 秒）。提供了完整的 Day-0 实操指南，包含精确命令与失败检查关卡。

`qwen` `mac-studio` `rdma` `exo` `local-inference`

---

## 📅 2026-01-05

### [2026 AI First 系列（三）：在被替代之前变得有价值——新经济下的生存法则](/entry/6nrmpv7z) 📄
⭐⭐⭐⭐4 🇨🇳 · 2026-01-05

2026 AI First 系列（三）：在被替代之前变得有价值——新经济下的生存法则
**第一件事**：你在做reinforcement learning from human feedback（RLHF）。每次你
Read in Cubox  
Read Original
**第一件事**：你在做reinforcement learning from human feedback（RLHF）。每次你修正AI的输出，每次你选择一个答案而不是另一个，你都在教它什么是好的、什么是不好的。
**第二件事**：你在数字化你的直觉。那些你&quot;凭感觉&quot;做出的判断，那些你&quot;基于经验&quot;的决策，正在被转化为数据点。AI在学习你的思维模式。

---

## 📅 2025-12-06

### [State of AI | OpenRouter](/entry/1iaxb3xe) 📄
@OpenRouter + a16z · ⭐⭐⭐⭐⭐5 🌐 · 2025-12-06

OpenRouter 联合 a16z 的 100 万亿 token LLM 使用分析。核心发现：开源模型采用率提升、创意角色扮演和编程是最热门任务、Agent 推理模式兴起、&#x27;Glass Slipper&#x27;留存效应。含开源 vs 闭源、地理分布、成本动态等多维度数据。

`OpenRouter` `a16z` `LLM` `100T-tokens` `agentic`

---

## 📅 2025-12-03

### [Qualcomm Snapdragon X2 Elite微架构](https://mp.weixin.qq.com/s?__biz=MzkzMTA2NjgzMA==&mid=2247488554&idx=1&sn=1e38328c97b182f71c139e0fc69447da)
@亦安 · ⭐⭐⭐3 🇨🇳 · 2025-12-03

基于 Chip&amp;Cheese PPT 解读高通第三代 Oryon 核心微架构。3 cluster 18 核最高 5GHz，共享 L2 16MB/cluster，9宽 decode/retire，ROB 650+。L1-Miss-L2-Hit 21 cycle，96KB DCache。L2 TLB 标称 8K entry（实测约 1.5K-2K）。前代的渐进优化。

`Qualcomm` `Snapdragon` `Oryon` `CPU` `微架构`

---

## 📅 2025-10-20

### [Anthropic 揭秘：上下文工程如何让 Agent 专注核心任务](/entry/6zoniwix) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-10-20

Anthropic 揭秘：上下文工程如何让 Agent 专注核心任务
Anthropic 揭秘让 AI 更靠谱的「上下文工程」
Read in Cubox  
Read Original
&gt; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
你有没有过这样的体验？跟 AI 聊得久了，它突然 &quot;失忆&quot;------ 前面提过的关键信息没了下文，甚至答非所问；让它处理复杂任务，比如分析大数据库、写长代码，它越往后越混乱...... 其实不是 AI &quot;不认真&quot;，而是它的 &quot;注意力&quot; 有限。

`Anthropic` `LLM` `Agent` `Inference` `Transformer`

---

## 📅 2025-07-08

### [GPU到底是如何工作的？这篇AI Infra入门全部告诉你](/entry/swk7j22h) 📄
@binnnliu · ⭐⭐⭐⭐4 🇨🇳 · 2025-07-08

# GPU到底是如何工作的？这篇AI Infra入门全部告诉你 ?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2Fj3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg) &gt; 大模型推理服务到底怎么跑起来的？大模型推理服务的运行过程中，CPU和GPU分别负责哪些工作？ &gt; 用GPU一定比CPU跑的快么？哪些场景需要用GPU? GPU最初的使...

`[]` `inference` `大模型`

---

## 📅 2025-04-06

### [[译] AI计算民主化 第七部分：如何看待Triton与Python eDSLs？](/entry/MIOvnhLW) 📄
⭐⭐⭐⭐4 🇨🇳 · 2025-04-06

AI编译器的根本性权衡：既要通过抽象底层细节来实现易用性和可扩展性，但现代生成式AI工作负载又需要可编程性和硬件控制来实现极致性能。

---

## 📅 2025-03-11

### [AI 代理可观测性 - 演变标准与最佳实践](/entry/piwjuvv3) 📄
@Guangya Liu (IBM), Sujay Solomon (Google) · ⭐⭐⭐⭐4 🇨🇳 · 2025-03-11

AI 代理可观测性 - 演变标准与最佳实践
AI 代理将在 2025 年成为人工智能的下一个重大飞跃，AI 代理的可观测性变得尤为重要，特别是在将这些代理扩展以满足企业需求时。没有适当的监控、追踪和日志记录机制，诊断问题、提高效率和确保 AI 代理驱动应用的可靠性将面临挑战。
Read in Cubox  
Read Original
作者：Guangya Liu (IBM), Sujay Solomon (Google)
AI 代理将在 2025 年成为人工智能的下一个重大飞跃。从自主工作流到智能决策，AI 代理将为各行业的众多应用提供动力。然而，随着这一演变，AI 代理的可观测性变得尤为重要，特别是在将这些代理扩展以满足企业需求时。没有适当的监控、追踪和日志记录机制，诊断问题、提高效率和确保 AI 代理驱动应用的可靠性将面临挑战。

`Anthropic` `LLM` `Agent` `Inference`

---

## 📅 2025-02-04

### [DeepSeek-R1 论文解析——人工智能领域的 RL LLM 新时代？](https://mp.weixin.qq.com/s?__biz=MzUzNzg4Nzc3MQ==&mid=2247485126&idx=1&sn=0b59ea812a2f0eedcf7de12986d99cbd&chksm=fbafde0216ffbfe4fbb5099f6ad2c2cb83630ee86c5da54ae9ec7cd75c1ed986d99f28a30760&mpshare=1&scene=1&srcid=0204EBmVUAlccQp8G0Kw32Dm&sharer_shareinfo=a4cb3d9e576db809f2a6e609010b59f5&sharer_shareinfo_first=a4cb3d9e576db809f2a6e609010b59f5)
⭐⭐⭐3 🇨🇳 · 2025-02-04

# DeepSeek-R1 论文解析——人工智能领域的 RL LLM 新时代？ DeepSeek-R1 论文解析——人工智能领域的 RL LLM 新时代？ 近年来，人工智能 (AI) 领域取得了快速发展，大型语言模型 (LLM) 为通用人工智能 (AGI) 铺平了道路。OpenAI的 o1 是 一个出色的模型，它引入了创新的推理时间扩展技术，可显著增强推理能力。然而，它仍然是闭源的。 今天，我们深入研究了 DeepSeek 推出的开创性研究论文 DeepSeek-R1。这篇题为&quot;DeepSeek-R1：通过强化学习激励大型语言模型中的推理能力&quot;的 论文介绍了一种最先进的开源推理模型，以及使用大...

`deepseek` `llm` `fine-tuning` `[]` `openai`

---

## 📅 2024-12-25

### [AI 技术的停滞，是革命的开始 – 虹线](/entry/zlsa1lat) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-12-25

Read in Cubox  
Read Original
1866 年，西门子的一位工程师发明了人类第一台直流发电机。
40 年后，通用电气在 1906 年开始量产真正让电灯普及的第一代白炽灯泡。
在这两者之间的半个世纪里，人类世界依然黑暗，电气的技术革命好像没有发生。
但，这只是因为我们身处后世，才能如此轻描淡写地将这 40 年一笔带过。对于当时的人们来说，电气技术的发展，是他们眼皮底下一天天展开的：第一条电报线路的铺设，第一个电话的接通，第一辆电车的开动，每一次技术的进步，都在真切地改变着他们的生活，只是它没有快到让当时的每个人都在一个时间点集体惊呼&quot;啊，电气革命终于来了！&quot;

`ChatGPT` `OpenAI` `Fine-tuning` `Inference` `Speech`

---

## 📅 2024-12-14

### [微信正式发布多模态大模型POINTS1.5](/entry/BZwVgqGU) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-12-14

?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_gif%2Fj3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ%2F640%3Fwx_fmt%3Dgif%26from%3Dappmsg)

---

## 📅 2024-09-03

### [0x1 Underlying LLMs](/entry/4u7v4niw) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-09-03

Read in Cubox  
Read Original
LLM (Large Language Models) 的风头一时无两，席卷万千行业。业内不乏有关于 LLM 的研究和讨论，但鲜有立足终端的视角。团队上半年曾有过对 GPT 进终端的分析，但 LLM 日新月异，旧分析已经不完全跟得上变化了。适逢年底规划季，尝试重新梳理 LLM 的现状，预判未来变化的趋势，希望能为迷茫的同仁提供思考的角度，也希望获得战斗在一线的友军的指点。
求砖 \&amp; 免砖申明：
不包含 LLM 入门介绍，够时间可以报吴恩达的免费课程和 NVIDIA 与 LlamaIndex 合力出品的；不够时间也有 Andrej Karpathy 的 一小时入门；
非算法出身，如有错漏之处，恳请指正；力争能让 RD、PM、DA 们都能看懂，如果不明处，欢迎讨论；
终端 LLM 应用有一定不...

`LLM` `RAG` `Inference` `LLaMA` `Multimodal`

---

## 📅 2024-05-14

### [GPT-4o：OpenAI 发布最强人机交互模型](/entry/gjncoa3h) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-05-14

# GPT-4o：OpenAI 发布最强人机交互模型 ChatGPT 免费版持续升级中，模型更强，交互更流畅... 早在 5 月 11 日，Sam 就在推文中表示：OpenAI 并没有推出 GPT-5，或搜索引擎，但团队一直在努力研发一些认为大家会喜欢的新东西（感觉就像是魔法一样）！ ?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_png%2F90Kxd0FAJJeDZbFzQkrjxIfcnRxziahTJZPicyxQOgbg5C88suDBEfiaZg2mjE226NZDIEOxWDr27kHz7fMvNEkSA%2F640%3Fwx_fmt%...

`[]` `gpt-4` `gpt-4o` `openai` `chatgpt`

---

## 📅 2024-03-05

### [查看浏览器Browsers的内核版本, 可以用 navigator.userAgent - 掘金](/entry/j4Ev6hzf) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-03-05

查看浏览器Browsers的内核版本, 可以用 navigator.userAgent 在浏览器控制台输入:navigator.userAgent 几乎所有主要浏览器都支持 navigator.use

---

## 📅 2024-03-03

### [【哥飞评站】AI贴纸生成网站 StickerBaker 的SEO评测报告和改进建议（4000字）](/entry/BZMiTd8i) 📄
⭐⭐⭐⭐4 🇨🇳 · 2024-03-03

受社群里 @damo 老板的启发，哥飞决定从今天开始一个新栏目，不定期点评一些网站，说说他们有哪些做得好的地方，有哪些还值得改进的地方。

---

## 📅 2023-12-26

### [2023: The Year of AI](/entry/f4uptczq) 📄
⭐⭐⭐⭐4 🌐 · 2023-12-26

Explore the significant AI advancements, impactful partnerships, and legal debates that defined 2023.
Read in Cubox  
Read Original
AI has undoubtedly made waves in 2023 and here we spotlight the most significant stories of the year poised to shape the future of this groundbreaking industry:
*Correction: In the original blog post published on December 22, 2023, the title &quot;AI Re...

`ChatGPT` `LLM` `Midjourney`

---

## 📅 2023-11-29

### [黄仁勋领导的 Nvidia 如何推动 AI 革命 [译]](/entry/iE9BadvV) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-11-29

这家公司的 CEO，黄仁勋，把所有筹码压在了一种全新的芯片上。如今 Nvidia 已跻身世界最大公司之列，他的下一步会怎样？

---

## 📅 2023-05-17

### [70款ChatGPT插件评测：惊艳的开发过程与宏大的商业化愿景 - 知乎](/entry/wvhfogqr) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-05-17

70款ChatGPT插件评测：惊艳的开发过程与宏大的商业化愿景 - 知乎
TL;DR: 我们对ChatGPT的插件商店中总共70款插件进行了评测。区别于Chrome，AppStore等平台的代码开发范式，开发者仅使用自然语言就可以开发ChatGPT插件，并由GPT模型自行决定在使用过程中是否调用插件。约八成插件…
Read in Cubox  
Read Original
Shimmer: Nutrition Coach
**TL;DR:** 我们对ChatGPT的插件商店中总共70款插件进行了评测。区别于Chrome，AppStore等平台的代码开发范式，开发者仅使用自然语言就可以开发ChatGPT插件，并由GPT模型自行决定在使用过程中是否调用插件。约八成插件集中于购物、餐饮、旅行、住房和求职场景，其余分布在教育、财经咨讯、内容社区和编程技术场景...

`ChatGPT` `OpenAI` `Prompt Engineering` `Benchmark`

---

## 📅 2023-05-07

### [ChatGPT背后的语言模型简史](/entry/c6i3ddwj) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-05-07

ChatGPT的火爆出圈，让大家对NLP语言模型的发展历程产生了浓厚的兴趣。本文将从深度学习在NLP领域的发展历程，到大语言模型的发展历程，再到大语言模型的未来展望，带你一起了解NLP语言模型的发展历史。 本文处于初稿状态，可能存在很多错误，如果你有不同的看法，欢迎不吝赐教，先行感谢！ ChatGPT的火爆出圈，让大家对自然语言处理（Natural Language Processing）语言模型的发展历程产生了浓厚的兴趣。本文将从深度学习在NLP领域的发展历程，到大语言模型的发展历程，再到大语言模型的未来展望，带你一起了解NLP语言模型的发展历史。 想必很多人对ChatGPT涌现出的多领域能...

`[]` `chatgpt`

---

## 📅 2023-03-22

### [真·万字长文:可能是全网最晚的chatgpt技术总结](/entry/qiwV8Dd1) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-03-22

最近ChatGPT可以说是火遍了全世界，作为由知名人工智能研究机构OpenAI于2022年11月30日发布的一个大型语言预训练模型，他的核心在于能够理解人类的自然语言，并使用贴近人类语言风格的方式来进行回复。模型开放使用以来，在人工智能领域引起了巨大的轰动，也成功火出了技术圈。从数据上看，ChatGPT用户数在5天内就达到了100万，2个月就达到了1亿；另外，在很多非人工智能领域，已经有机构在尝试用ChatGPT去做一些智能生成的事。…

---

### [AIGC图像生成的原理综述与落地畅想](/entry/onqk9vx5) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-03-22

基于Stable Diffusion扩散模型的综述
Read in Cubox  
Read Original
AIGC，这个当前的现象级词语。本文尝试从文生图的发展、对其当前主流的 Stable Diffusion 做一个综述。以下为实验按要求生成的不同场景、风格控制下的生成作品。
GAN 系列算法开启了图片生成的新起点。GAN的主要灵感来源于博弈论中零和博弈的思想，通过生成网络G（Generator）和判别网络D（Discriminator）不断博弈，进而使G学习到数据的分布。
1.
   G是一个生成式的网络，它接收一个随机的噪声z（随机数），通过这个噪声生成图像。
2.
   D是一个判别网络，判别一张图片是不是&quot;真实的&quot;。它的输入参数是x，x代表一张图片，输出D（x）代表x为真实图片的概率，如果为1，就代表100%是真实的图片。

`AIGC` `Stable Diffusion` `Embedding` `Transformer` `Diffusion`

---

## 📅 2023-03-16

### [GPT-4 重磅发布，有哪些升级和变化？](/entry/7pp7rfh8) 📄
@qizailiu，腾讯 IEG 算法研究员 · ⭐⭐⭐⭐4 🇨🇳 · 2023-03-16

# GPT-4 重磅发布，有哪些升级和变化？ 作者：qizailiu，腾讯 IEG 算法研究员 &gt; 昨天 OpenAI 发布最新里程碑 AI 语言模型 GPT-4，GPT-4 是一个大型多模态模型（接受图像和文本输入，输出为文本），目前虽然在许多现实世界场景中的能力不如人类，但在各种专业和学术基准上表现出人类水平。 本文主要参考 OpenAI 关于 GPT4 的官方 Blog，目前各公众号关于 GPT4 的内容基本来自官方 Blog、技术报告和官方视频内容。相关内容传送门： 官方 ChatGPT Plus 体验地址：&lt;https://chat.openai.com/auth/login?nex...

`[]` `prompt` `gpt-4` `openai` `chatgpt`

---

## 📅 2023-02-14

### [ChatGPT 算法原理](/entry/02qyib4a) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-02-14

每一代GPT模型的参数量都爆炸式增长，堪称“越大越好”。2019年2月发布的GPT-2参数量为15亿，而2020年5月的GPT-3，参数量达到了1750亿。 还是有很多读者对于ChatGPT充满期待（幻想？梦想），今天给大家分享技术层… 每一代GPT模型的参数量都爆炸式增长，堪称&quot;越大越好&quot;。2019年2月发布的GPT-2参数量为15亿，而2020年5月的GPT-3，参数量达到了1750亿。 还是有很多读者对于ChatGPT充满期待（幻想？梦想），今天给大家分享技术层面的拆解，读完之后是否是会理性一点呢？enjoy～ 文末推荐几篇直接采访ChatGPT创始人视角的文章，共赏enjoy～ 去年1...

`transformer` `fine-tuning` `[]` `gpt-4` `openai`

---

## 📅 2023-02-07

### [ChatGPT背后的经济账](/entry/u2o9qdqv) 📄
⭐⭐⭐⭐4 🇨🇳 · 2023-02-07

ChatGPT能否取代Google、百度这样的传统搜索引擎？为什么中国不能很快做出ChatGPT？当前，对这些问题的探讨大多囿于大型语言模型（LLM）的技术可行性，忽略或者非常粗糙地估计了实现这些目标背后的经济成本，从而造成对LLM的开发和应用偏离实际的误判。 本文作者从经济学切入，详细推导了类ChatGPT模型搜索的成本、训练GPT-3以及绘制LLM成本轨迹的通用框架，为探讨LLM成本结构和其未来发展提供了可贵的参考视角。 * LLM驱动的搜索已经在经济上可行 ：粗略估计，在现有搜索成本结构的基础上，高性能LLM驱动搜索的成本约占当下预估广告收入/查询的15%。 * 但经济可行并不意味着经济...

`llm` `[]` `prompt` `inference` `chatgpt`

---

## 📅 2022-03-18

### [一文读懂 Fragment 的方方面面](/entry/VkExTygi) 📄
⭐⭐⭐⭐4 🇨🇳 · 2022-03-18

Fragment 是 Android 中历史十分悠久的一个组件，在 Android 3.0 （API 级别 11）的时候推出，时至今日已成为 Android 开发中最常用的组件之一。在一开始的时候，引入 Fragment 的目的是为了在大屏

---

## 📅 2022-01-20

### [【开放阅读】2021 年度十大数字应用（服务） – Dailyio](/entry/XBaDFs3i) 📄
⭐⭐⭐⭐4 🇨🇳 · 2022-01-20

本文选自付费邮件通讯「iPad Power User」，这是一份聚焦 iPad、iPadOS 与个人生产力的邮件通讯产品，通过不断探索与生活、工作息息相关的数字工具与方法论，为订阅读者提供中文互联网领域最优质的数字工具使用技巧、应用（服务）推荐以及数字化思考，欢迎试读、订阅。

---
