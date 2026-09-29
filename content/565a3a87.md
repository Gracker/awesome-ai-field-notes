# AIOS 架构深度解析与 Android Agent OS 演进全景

**AIOS 是目前学术界最完整的 LLM Agent 操作系统原型**，其核心设计将 LLM 实例抽象为"CPU 核心"，通过系统调用层为上层 Agent 应用提供统一的调度、内存、存储、工具和访问控制服务。AIOS 已发表 8 篇论文，被 COLM 2025、ICLR 2025、NAACL 2025 收录，GitHub 获 5,387 星。但 AIOS 是纯用户态 Python 实现，运行在 FastAPI 之上，并未触及真正的操作系统内核层。与此同时，Android 平台正从"操作系统"向"智能系统"演进——Google 的 AICore/AppFunctions、三星的多 Agent 架构、A2A 协议的标准化，正在工业侧构建一套完整的移动端 Agent OS 基础设施。两条路径的交汇点，是 AIOS 的 OS 抽象概念如何映射到 Android 的分层架构中。

---

## 一、AIOS Kernel 的七大模块与实现细节

AIOS 内核由 Rutgers 大学 Yongfeng Zhang 团队开发，代码仓库位于 `github.com/agiresearch/AIOS`，核心代码在 `aios/` 目录下，运行时入口在 `runtime/launch.py`。整个内核以 **FastAPI 服务** 形式启动（默认端口 8000），通过 uvicorn 提供 HTTP 接口。

**LLM Core（`aios/llm_core/`）** 是核心计算单元。每个 LLM 实例被抽象为一个"核心"（Core），类比传统 OS 的 CPU 核心。`LLMAdapter` 类负责统一接口，支持 9 种后端：OpenAI、Anthropic、Google Gemini、Groq、Deepseek、Novita（云端 API），以及 HuggingFace、Ollama、vLLM（本地推理）。路由逻辑在 `routing.py` 中实现，`address_request()` 方法处理所有 LLM 系统调用。配置通过 `config.yaml` 管理 API Key 和后端地址。

**Agent Scheduler（`aios/scheduler/`）** 集中管理所有请求队列，维护 LLM Queue、Memory Queue、Storage Queue、Tool Queue 四个独立队列。实现了两种调度策略：**FIFO 调度器**（`fifo_scheduler.py`，批处理间隔默认 1.0 秒，不支持上下文中断，适合吞吐优先场景）和 **Round Robin 调度器**（`rr_scheduler.py`，时间片默认 1.0 秒，支持上下文保存/恢复，适合多 Agent 交互场景）。调度策略由 `config.yaml` 中的 `use_context_manager` 字段自动选择。

**Context Manager（`aios/context/simple_context.py`）** 处理 LLM 推理过程的中断与恢复。对闭源模型使用 **文本快照**（保存已解码文本），对开源模型使用 **logits 快照**（保存 beam search 状态树），论文报告恢复后 BLEU/BERT 分数达到 1.0。该模块不由调度器调度，而是在 LLM Core 内部触发。

**Memory Manager（`aios/memory/`）** 管理 Agent 运行时的交互历史（对话记录、工具调用结果），使用 **ChromaDB 或 QdrantDB** 作为向量数据库后端支持语义检索。当内存占用达到可配置阈值（默认 80%）时，执行 **K-LRU 淘汰策略**，将低频数据交换到磁盘。SDK 暴露 `create_memory`、`get_memory`、`update_memory`、`delete_memory`、`search_memories`、`create_agentic_memory` 六个接口。其中 `create_agentic_memory` 集成了 A-MEM 系统（基于 Zettelkasten 方法的自组织记忆网络，arXiv:2502.12110，154 次引用）。

**Storage Manager（`aios/storage/`）** 提供持久化存储，核心是 **LSFS（Logical Semantic File System）**——一个语义文件系统，使用 all-MiniLM-L6-v2 嵌入向量建立文件语义索引，支持自然语言检索。论文（ICLR 2025）报告语义检索准确率提升 **20-24%**，文件访问速度提升 **92%**。支持 Redis 后端实现文件回滚。SDK 暴露 `mount`、`create_file`、`write_file`、`retrieve_file`、`rollback_file`、`share_file` 等接口。

**Tool Manager（`aios/tool/manager.py`）** 管理外部工具的加载、参数验证和冲突解决。使用 hashmap 监控工具实例的实时使用计数，检查并发限制。在 AIOS 1.0 版本中，Tool Manager 被重新设计为集成 **VM Controller 和 MCP Server**，为 Computer-Use Agent 提供沙箱化的计算机交互环境。工具以子进程（MCP Server）形式在内核初始化时启动。

**Access Manager** 提供基于权限组的跨 Agent 数据访问控制。每个 Agent 分配权限组，通过 hashmap 映射 Agent ID 到权限组。对不可逆操作（删除、覆写、权限修改）强制要求用户确认。访问控制系统调用不经过调度器，而是内联验证。

---

## 二、系统调用层与 SDK 的接口设计

AIOS 的系统调用层（`aios/syscall/syscall.py`）是连接 Agent 应用与内核模块的桥梁。`SyscallExecutor` 类将上层的 `LLMQuery`、`MemoryQuery`、`StorageQuery`、`ToolQuery` 对象转换为类型化的系统调用对象，每个系统调用绑定一个独立 Python 线程（继承 `Thread` 类），最大并发线程数 250。

**系统调用执行流程分 7 个阶段**：FastAPI 端点接收 HTTP 请求 → `SyscallExecutor.create_syscall()` 创建类型化系统调用 → 调用被加入对应全局队列 → 请求线程阻塞等待（`syscall.start()` + `syscall.join()`）→ 调度器线程从队列取出并处理 → 资源管理器的 `address_request()` 执行实际操作 → 调度器通过 `syscall.set_response()` 返回结果并触发 `syscall.event.set()` 解除阻塞。

**AIOS SDK（Cerebrum）** 是独立仓库（`github.com/agiresearch/Cerebrum`），PyPI 包名 `aios-agent-sdk`，发表于 NAACL 2025。SDK 采用四层模块化架构（LLM Layer、Memory Layer、Storage Layer、Tool Layer），每层通过类型化 Query 对象映射到内核系统调用。Agent 开发遵循标准结构：`entry.py`（主逻辑）、`config.json`（元数据与依赖声明）、`meta_requirements.txt`（额外依赖）。SDK 提供 **框架适配器**，支持 AutoGen、Open-Interpreter、MetaGPT 等框架的 Agent 无需修改即可运行在 AIOS 上——适配器定位框架核心函数并重定向到 AIOS 系统调用。

部署模式有四种：**Mode 1**（本地内核，Agent 和内核在同一机器）、**Mode 2**（远程内核，Agent 通过 HTTP API 访问远程服务器，专为移动/边缘设备设计）、**Mode 2.5**（远程开发模式）、**Mode 3/4**（个人远程内核/虚拟内核，开发中）。

---

## 三、AIOS 的分层设计与真实 OS 交互分析

AIOS 的分层架构包含三层：Application Layer（Agent 应用）、Kernel Layer（AIOS Kernel + 传统 OS Kernel 并列）、Hardware Layer（CPU、GPU、内存、磁盘）。

**关键事实：AIOS 内核是纯用户态实现。** 整个系统运行为一个 Python 进程（FastAPI + uvicorn），不涉及任何 Linux 内核模块、系统调用拦截或特权操作。所谓的"系统调用"实际上是 **应用层 HTTP 请求**，与真正的操作系统系统调用（如 `read()`、`write()`、`mmap()`）在实现层级上完全不同。

AIOS 对底层 OS 的实际依赖包括：GPU 驱动（CUDA，用于本地 LLM 推理）、网络 I/O（HTTP 请求云端 LLM API）、文件系统操作（LSFS 底层读写）、进程管理（MCP Server 作为子进程启动）、线程管理（Python Thread → pthreads → OS 线程）。这些全部通过标准 OS API 访问，AIOS 不需要也不使用任何特权操作。

这意味着 AIOS 的"内核"本质上是一个 **应用层资源管理框架**，其价值在于抽象和调度层面的设计思想，而非真正的 OS 内核级实现。2026 年初仓库中新增了 `aios-rs/` 目录——一个实验性的 Rust 骨架，定义了 context、memory、storage、tool、scheduler、llm 的 trait 接口，可能是向系统级语言迁移的信号。

---

## 四、AIOS 项目的最新进展（2024-2026）

AIOS 项目的演进可分为五个阶段：

**概念期（2023.12）**：发表愿景论文（arXiv:2312.03815），提出 LLM = OS 内核、上下文窗口 = 内存、外部存储 = 文件系统、工具 = 设备的概念映射，35 页纯概念论文。

**原型期（2024.3-11）**：发表核心系统论文（arXiv:2403.16971），实现基础调度器、上下文管理器、内存/存储管理器。同期发表 CoRE 编译器（arXiv:2405.06907）和 LSFS 语义文件系统（arXiv:2410.11843，ICLR 2025）。

**成熟期（2024.11-2025.3）**：完成重大架构重构，发布 Cerebrum SDK（NAACL 2025），v0.2.2 版本引入完整系统调用架构、多框架适配器、Agent Hub、Web UI 和终端 UI。

**平台期（2025.4-8）**：发表 AIOS Server（arXiv:2504.14411，去中心化 Agent 网络，DHT + Gossip 协议发现，延迟 <200ms），LiteCUA/AIOS 1.0（arXiv:2505.18829，MCP Server 架构的 Computer-Use Agent，OSWorld 基准 **14.66%** 成功率，超过 Friday 11.11% 和 GPT-4o 11.21%）。核心论文被 **COLM 2025** 收录。

**当前（2025末-2026初）**：新增 Rust 骨架 `aios-rs/`，持续修复 Ollama 集成、工具调用问题。未发现原生移动端部署的讨论或实现——移动设备仅作为 Mode 2 的瘦客户端。

---

## 五、Android 平台的 Agent OS 能力现状

### AICore 与 Gemini Nano：系统级 AI 推理服务

**AICore** 是 Android 14 引入的系统级服务，负责管理 Gemini Nano 模型的生命周期、运行时推理和安全特性。其架构路径为：App → ML Kit GenAI APIs → AICore SystemService → Gemini Nano → 硬件加速器（TPU/NPU）。AICore 遵循 Private Compute Core 隐私规范，网络隔离（不能直接访问互联网），请求独立处理（不保留输入/输出数据），一次处理一个 App 的推理请求以防止跨应用数据泄露。

API 层面，Google 在 I/O 2025 正式发布 **ML Kit GenAI APIs**（`com.google.mlkit:genai-prompt:1.0.0-beta1`），提供 Summarization、Proofreading、Rewriting、ImageDescription、SpeechRecognition 五个高级 API 和一个通用 Prompt API。每个 API 底层由 Gemini Nano 基础模型 + LoRA 适配器 + 优化推理参数 + 评估管线组成。AICore 强制执行每应用推理配额、每日电池配额、仅前台执行限制。

**Private Compute Core（PCC）** 自 Android 12 引入，是一个系统级安全沙箱。PCC 内的功能完全网络隔离，处理原始传感器数据（摄像头、麦克风、GPS、屏幕内容、通知、剪贴板），仅以推理结果（预测、建议、字幕）形式输出。**Android System Intelligence（ASI）** 是 PCC 的主要消费者，驱动 Now Playing、Smart Reply、Live Caption、Screen Attention、Live Translate 等 20+ 智能功能。

### AppFunctions：移动端的 MCP 等价物

**AppFunctions 是 Android 16（API 36）引入的平台级特性**，Google 官方将其定位为"MCP 的移动端等价物"。它允许应用向 AI Agent 暴露结构化的可调用函数。

架构分两个核心组件：**AppFunctionService**（`android.app.appfunctions.AppFunctionService`，应用侧实现，通过 `BIND_APP_FUNCTION_SERVICE` 权限保护，仅允许系统进程绑定）和 **AppFunctionManager**（`@SystemService(Context.APP_FUNCTION_SERVICE)`，系统级注册中心，管理全局函数注册表）。函数发现通过 **AppSearch 框架** 实现——应用安装/更新/设备启动时，AppFunctionManager 触发重新索引，元数据以 OpenAPI 风格的 `AppFunctionStaticMetadata` 文档存储。

Jetpack 库栈为 `androidx.appfunctions:appfunctions:1.0.0-alpha05`，开发者通过 `@AppFunction` 注解标记暴露的函数，`@AppFunctionSerializable` 标记可序列化参数类型。三星 Galaxy S26 已在生产环境中使用 AppFunctions——Gemini 通过此接口调用 Samsung Gallery、Calendar、Notes、Tasks 的功能。

**Android 17**（预计 2026 年 Q2）将扩展 AppFunctions 覆盖范围。同时引入 **UI Automation Framework**——一个系统级 AI Agent 框架，允许 Gemini 在没有 AppFunctions 的应用上通过 UI 自动化完成多步骤任务（首批类别：外卖、生鲜、打车，在 Galaxy S26/Pixel 10 上的美国/韩国市场试运行）。

### 三星的多 Agent 系统架构

三星 Galaxy S26 系列采用 **三 Agent 并行架构**：Google Gemini（执行跨应用 Agentic 任务）、Perplexity（网络搜索查询）、Samsung Bixby（设备端助手，使用升级的自研 LLM）。三者通过统一入口（侧键长按）访问。

安全架构层面，三星构建了 **Personal Data Engine（PDE）**（设备端个人数据学习，加密存储于 Knox Vault 硬件安全区）、**KEEP（Knox Enhanced Encrypted Protection）**（按应用隔离数据加密）、**Knox Matrix Trust Chain**（跨设备安全监控）。Exynos 2600 处理器（2nm GAA，业界首款）的 NPU 首次支持 **硬件级虚拟化安全和混合后量子密码学**。

---

## 六、A2A 协议与移动端集成路径分析

**A2A（Agent-to-Agent）协议** 由 Google 于 2025 年 4 月发布，当前版本 v0.3（2025.7），已捐赠给 Linux 基金会，150+ 组织参与。协议基于 **HTTP(S) + JSON-RPC 2.0**，支持 SSE 流式传输和 gRPC（v0.3 新增）。核心抽象包括 Agent Card（`/.well-known/agent.json`，声明身份、能力、认证方式）、Task（带生命周期的工作单元）、Message/Part/Artifact（通信内容载体）。

**A2A 目前不适合直接用于 Android 设备端本地 Agent 通信。** 原因有四：（1）传输层不匹配——A2A 使用 HTTP，Android 本地进程间通信使用 **Binder IPC**（内核级、零拷贝），性能差异数个量级；（2）发现机制不匹配——A2A 使用网络可达的 `/.well-known/agent.json`，Android 使用 PackageManager、IntentFilter、AppSearch；（3）安全模型不匹配——A2A 使用 OAuth/API Key，Android 使用 Linux UID/GID、签名验证、SELinux 策略；（4）资源约束——移动设备的电池和计算资源有限，HTTP 解析和 SSE 连接的开销对本地通信而言过于浪费。

**可行的集成路径有三条**：（1）**跨设备 Agent 通信**——三星 Knox Matrix 已支持跨 Galaxy 设备的安全监控，A2A 可为手机、平板、手表、笔记本间的 Agent 通信提供标准化协议；（2）**云端到设备的 Agent 桥接**——Gemini 云端 Agentic 任务需要调用设备端操作时，A2A 处理云侧编排，AppFunctions 处理设备侧执行；（3）**A2UI 协议扩展**——允许 Agent 生成声明式 JSON UI，在移动端原生渲染（Jetpack Compose/SwiftUI）。

A2A 概念向 Android 本地的映射关系为：Agent Card → AppFunctions 元数据 + IntentFilter 声明；HTTP/JSON-RPC → Binder IPC + ContentProvider；Agent Discovery → AppSearch 索引 + PackageManager 查询；Task 生命周期 → JobScheduler/WorkManager；SSE 流 → BroadcastReceiver/LiveData/Kotlin Flow；认证 → Android 权限模型 + 签名级权限。

---

## 七、AIOS 模块在 Android 平台的层次映射

将 AIOS 的七大模块概念映射到 Android 的四层架构（Linux Kernel → HAL/Runtime → Framework → Application），每个模块的最佳归属层级不同。

### 适合作为 Android System Service 实现的模块

**LLM Core** 的功能在 Android 上由 **AICore SystemService** 承载——已有成熟实现。AICore 管理 Gemini Nano 模型的加载、推理调度、配额控制和安全隔离，通过 Binder IPC 暴露给上层。若要支持多模型（类似 AIOS 的多后端路由），可在 AICore 内部扩展模型注册表和路由逻辑。

**Agent Scheduler** 适合作为独立 SystemService 实现。Android 已有 `ActivityManagerService`（进程调度）和 `JobScheduler`（后台任务调度）作为参考模式。Agent Scheduler 需管理 Agent 进程优先级、LLM 推理请求队列、时间片分配和上下文切换。实现为 SystemService 可以利用 Binder IPC 接收跨进程的调度请求，并与 AICore 协调推理资源分配。

**Tool Manager** 对应 **AppFunctionManager**——Android 16 已经实现了这个概念。AppFunctionManager 作为 `@SystemService(Context.APP_FUNCTION_SERVICE)` 注册在 SystemServiceRegistry 中，通过 AppSearch 框架实现函数发现，通过 Binder IPC 和 `BIND_APP_FUNCTION_SERVICE` 权限实现安全的函数调用。

**Access Manager** 适合作为 SystemService 实现，与 Android 现有的 `PackageManagerService`（权限管理）和 SELinux 策略引擎配合工作。需要扩展的是：Agent 粒度的权限组定义、跨 Agent 数据访问控制策略、不可逆操作的用户确认流程。

### 适合在 Framework 层以 Manager API 暴露的模块

**Memory Manager** 的语义记忆管理功能适合在 Framework 层实现为 `AgentMemoryManager`，暴露 CRUD + 语义检索 API。底层可使用 AppSearch（Android 已内置的结构化搜索框架）或系统级向量数据库。淘汰策略（K-LRU）在 Framework 层即可实现，无需内核支持。关键设计决策：Memory Manager 需要与 PCC 集成以确保 Agent 记忆数据的隐私安全。

**Context Manager** 的 LLM 推理中断/恢复功能适合在 Framework 层实现，作为 AICore 的上层扩展。文本快照方案在 Framework 层即可完成（保存已生成 token 序列），logits 快照方案需要与 AICore 内部的推理引擎协调（可能需要 AICore API 扩展支持推理状态的导出/导入）。

**Storage Manager** 的语义文件系统功能适合在 Framework 层实现为 `AgentStorageManager`，底层依赖 Android 标准 ContentProvider 和 MediaStore API 进行文件操作，叠加向量索引层实现语义检索。Agent 间文件共享可复用 Android 的 `FileProvider` 机制。

### 适合在 Runtime 层（可能演进为 Agent Runtime）实现的能力

Android Runtime（ART）当前是 Mainline 模块，通过 Google Play 系统更新独立升级。其混合 JIT/AOT 编译策略、Profile-Guided Optimization、改进的 GC（使用 `userfaultfd` 系统调用）已为 AI 工作负载优化。ART 可能的演进方向包括：

Agent 生命周期管理——ART 已管理应用进程的创建、初始化和回收，可扩展为管理 Agent 进程（包含 Agent 元数据、能力声明、依赖关系）。Agent SDK 运行时——类似 AIOS 的 Cerebrum SDK 提供的框架适配能力，可在 ART 层提供标准化的 Agent 基类和系统调用代理。轻量级 Agent 沙箱——利用 ART 的进程隔离能力，为每个 Agent 提供独立的执行环境。

### 真正需要 Linux Kernel 层支持的能力

**cgroup 资源隔离**：为 Agent 进程组设置 CPU、内存、GPU 资源配额。Android 已使用 cgroup v2 进行应用进程分组（前台/后台/受限），可扩展为 Agent 优先级分组。**TEE（可信执行环境）**：Agent 处理敏感数据时需要硬件级安全保证。三星 Knox Vault 和 Android Keystore 底层依赖 ARM TrustZone TEE。PCC 的隐私保证部分依赖 TEE 实现。**内存隔离**：`userfaultfd` 系统调用支持 ART GC 优化；`seccomp-bpf` 沙箱限制 Agent 可用的系统调用集合；`mmap` 用于高效的模型权重加载和共享（多 Agent 共享同一模型权重的 CoW 映射）。**Binder IPC 性能**：跨进程 Agent 通信的延迟和吞吐量直接取决于 Binder 内核驱动的性能。

---

## 八、竞品与学术参考的对标分析

在 Agent OS 领域，AIOS 占据的是"Agent 内核级 OS 抽象"这一独特定位。其他项目分布在不同的抽象层次上。

**OS-Copilot**（上海 AI Lab，arXiv:2402.07456）是单 Agent 框架，采用 Planner-Configurator-Actor 三组件架构和 DAG 任务规划。其核心创新是自主工具生成——Agent 动态生成新工具并通过 RAG 存入过程记忆供后续复用。与 AIOS 的关键区别：OS-Copilot 构建单个通用 Agent，AIOS 管理多个并发 Agent 的资源分配。OS-Copilot 没有调度器、上下文切换和多 Agent 管理概念。

**Microsoft AutoGen / Agent Framework**（38k+ 星，企业级）提供事件驱动的 Agent 运行时，具有本地和分布式两种模式。分布式模式使用 gRPC Host-Worker 架构，概念上接近 OS 进程管理。正在向 Microsoft Agent Framework 演进，合并 Semantic Kernel，增加 Workflow 抽象、状态管理、检查点/暂停/恢复。**与 AIOS 的关键区别**：AutoGen 是生产级 Agent 编排框架，不使用 OS 内核隐喻，没有 LLM 核心抽象、内存管理或存储管理的 OS 级概念。

**LangGraph**（v1.0，LinkedIn/Uber/Klarna 生产使用）是基于图执行模型的 Agent 运行时，提供持久化执行、Human-in-the-loop、短期/长期记忆。创始人 Harrison Chase 的定义是：LangChain = Agent 框架，LangGraph = Agent 运行时。**这是工业界最接近 AIOS Agent 运行时概念的实现**，但采用图工作流而非 OS 内核隐喻。

**Apple Intelligence** 是唯一的大规模生产级 OS 集成 AI 方案。3B 参数设备端模型 + LoRA 适配器动态加载/切换 + Private Cloud Compute 服务端模型。WWDC 2025 发布的 Foundation Models 框架允许开发者用约 3 行 Swift 代码访问设备端模型。**与 AIOS 的关键区别**：Apple Intelligence 增强现有 OS 功能而非管理自治 Agent，没有多 Agent 调度概念，但其设备端模型部署和隐私架构是最成熟的。

**Karpathy LLM OS 愿景**（2023.10 提出，2025 年扩展为"Software 3.0"）将 LLM 类比为新 OS 的内核进程：推理能力 = CPU，上下文窗口 = RAM（~128K token），知识检索 = 文件系统，token 生成速率 = 时钟频率（~20Hz）。他将当前阶段比作 1960 年代大型机/分时系统时代。

2026 年 2 月，福冈工业大学和新加坡国立大学发表了一篇关于 Agent OS 形式化抽象的论文，提出 **Semantic Memory Management Unit（SMMU，语义分页的层级内存）**、**Reasoning Interrupt Handler（RIH，工具调用作为硬件中断）**、**Cognitive Synchronization Pulses（CSP，事件驱动多 Agent 同步）** 和 **Cognitive Scheduler（防止资源抖动）**，声称 0-20 个 Agent 线性扩展，20-40 个次线性扩展。

---

## 结论：从 AIOS 到 Android Agent OS 的路径

AIOS 的核心贡献在于 **概念框架的完整性**——它是第一个将 OS 内核的所有关键抽象（调度、上下文管理、内存、存储、工具、访问控制）系统性地映射到 LLM Agent 管理领域的项目。但其纯 Python 用户态实现决定了它是一个研究原型，而非可直接部署的系统。

Android 平台实际上已经在工业级别实现了 AIOS 概念的核心子集：**AICore 对应 LLM Core**（更成熟的模型管理和推理服务），**AppFunctionManager 对应 Tool Manager**（更安全的函数发现和调用机制），**PCC 对应 Access Manager**（硬件级隐私保证）。尚未实现但有明确需求的是：**Agent Scheduler**（多 Agent 推理请求的优先级调度和时间片管理）、**Agent Memory Manager**（运行时语义记忆的统一管理）、**Context Manager**（LLM 推理状态的中断/恢复）。

最具建设性的方向不是将 AIOS 移植到 Android，而是 **借鉴 AIOS 的架构思想，在 Android 已有的 SystemService/Framework 架构上增量构建缺失的 Agent 管理能力**。具体而言：在 SystemServer 中新增 `AgentSchedulerService` 和 `AgentAccessService`；在 Framework 层增加 `AgentMemoryManager` 和 `AgentContextManager`；扩展 ART 以支持 Agent 进程的元数据管理和生命周期控制；利用 Linux Kernel 的 cgroup、TEE、seccomp 提供资源隔离和安全保证。A2A 协议则作为跨设备和云端 Agent 通信的标准，与 AppFunctions 形成本地-远程互补架构。