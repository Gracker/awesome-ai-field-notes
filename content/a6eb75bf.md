# 深度拆解：新一代智能体手机的路线之争

---
id: "7490488377179900198"
cubox_url: https://cubox.pro/web/card/7490488377179900198
url: https://mp.weixin.qq.com/s?__biz=Mzk0NDcwNTc1OQ==&mid=2247483912&idx=1&sn=2282e48602310b1a5829fd8dc9f73867&chksm=c26a9d099cffa19baba7e1308ccf6106d9e79e496e9c9140ff8e6d69db44a5844af4b4dba5ab&mpshare=1&scene=1&srcid=0821VusxpB2udXL6q5cGuCih&sharer_shareinfo=7ef3ccca8d75a96baf119b190ca0273b&sharer_shareinfo_first=7ef3ccca8d75a96baf119b190ca0273b
tags: []

---
# 深度拆解：新一代智能体手机的路线之争

Skill、MCP、GUI Agent——同样号称"智能体 手机"，背后是截然不同的技术哲学。本文从系统架构视角，拆解三条路线的底层实现差异与各自代价。

[Read in Cubox](https://cubox.pro/web/card/7490488377179900198)  
[Read Original](https://mp.weixin.qq.com/s?__biz=Mzk0NDcwNTc1OQ==&mid=2247483912&idx=1&sn=2282e48602310b1a5829fd8dc9f73867&chksm=c26a9d099cffa19baba7e1308ccf6106d9e79e496e9c9140ff8e6d69db44a5844af4b4dba5ab&mpshare=1&scene=1&srcid=0821VusxpB2udXL6q5cGuCih&sharer_shareinfo=7ef3ccca8d75a96baf119b190ca0273b&sharer_shareinfo_first=7ef3ccca8d75a96baf119b190ca0273b)  

---

2026 年 WAIC 上，"智能体手机"成了最热的话题之一。各家展台前都围满了人，但凑近看，这些产品的技术底座不完全一样。

有的在重写 Android 的框架源码，有的在调 API 的原子操作，有的在用视觉模型看屏幕点击。**它们解决的是同一个问题，走的是三条完全不同的路。**
> **核心结论（先说在前面）**
>
> 智能体手机的竞争，表面看是"谁的模型更聪明"，底层其实是**"谁选对了让智能体动手的机制"** 。围绕这个机制，业界分成了三个阵营：
>
> **阵营一 · Skill 派** （清华 AOHP开源项目 / 华为 HarmonyOS 7 / 本地移植openclaw Demo）------让智能体**运行脚本代码** 做事，核心矛盾是"Node/Python 运行时放哪跑"；
>
> **阵营二 · MCP 派** （阶跃 Step AOS）------让智能体**调用语义化原子操作** ，需要有一个强端侧模型来决策；
>
> **阵营三 · GUI Agent 派** （豆包等）------让智能体**看屏幕、点界面** ，通用性最强，但可控性和可逆性最弱。

*** ** * ** ***

## 阵营一：Skill 派------给智能体一份"说明书"

### 什么是 Skill

Skill 是 Anthropic AgentSkills / OpenClaw 开源规范的核心概念。它本质上是**一份写给智能体看的说明书** （通常是一个 SKILL.md 文件），告诉智能体"这件事怎么做、什么时候用、调哪些工具"。

Skill 的形态很弹性：可以只是说明文档，也可以附带可执行脚本，甚至可以在里面接 MCP。**当 Skill 带脚本时，智能体需要把脚本跑起来完成任务** ------这就引出了 Skill 路线的核心矛盾：**Node/Python 运行时，放在哪跑？**

*** ** * ** ***

### 清华 AOHP 开源项目------深改 Android，把运行时"焊"进手机

> 开源地址：github.com/aohp-os/aohp^\[1\]^  
> 论文：arxiv.org/abs/2606.23449^\[2\]^

清华大学开源的 AOHP 项目选择了最激进的方式，通过其开源源码解析画出其架构改造如下图所示：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F1UQO7NGicXexCsCdib65wYB1gnIJwRKiatIbjPSfgoCDfHp67gGg6zr0j45QhlPwWCbKoOupW267ibScKdMb32rqxYXoNW8Dxyia2ou4MM8KhHmE%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D0)

该项目直接 fork 并修改了 Android 框架心脏 frameworks/base，在系统里新增了 **32 个 AOHP 专属文件（共 7120 行代码）** ，并在 SystemServer.java 的第 1779 行注册了 12 个新系统服务，与 AMS/WMS 等原生服务平级开机启动。这些服务包括：

*
  • **AohpVaultService** （保险箱）：密码存 token，明文只在系统内部注入，不经过 AI 大脑
*
  • **AohpTaintTrackerService** （污点追踪）：全程追踪敏感数据流向
*
  • **AohpSecurityBridgeService** ：策略门控 + 人机确认 + 审计
*
  • **AohpAgentViewService** ：截图在系统层按敏感区域打码再输出
*
  • **AohpVirtualDisplayService** ：改造虚拟显示管理

此外，system/core 里还有一个自写的原生容器守护进程 aohp-containerd（C++ 2178行）。这是整套 Skill 执行能力的核心------它是**真·Linux 容器** ：用 unshare(CLONE_NEWNS) 建挂载命名空间 + chroot 进 Alpine Linux 根目录 + cgroup 限制资源，容器内跑**完整的 Node 24 + Python + OpenClaw** 。

**与 Termux 的本质差异** ：

很多人会问，这不就是手机版 Termux 吗？差别很大。Termux 是普通 App，靠 proot（用户态 ptrace）伪装 chroot，无需 root，但有性能损耗。AOHP 的 aohp-containerd 是 init 启动的**特权 daemon** ，有 SYS_ADMIN/SYS_CHROOT capability，还有自定义 SELinux 域------用的是真内核级隔离，原生速度。同样是"在 Android 上跑 Node"，前者假装，后者真跑。差别正是**肯不肯付 OS 级深改的代价** 。
> **诚实的边界** ：该项目的主力验证平台是 Cuttlefish（Google 的虚拟 Android 设备，跑在 Linux 服务器上），真实手机的规模化运行尚未得到公开验证。

*** ** * ** ***

### 华为 HarmonyOS 7------"搬架构，不搬执行环境"

华为走了截然不同的方向：端侧只养 ArkTS + 受限 Shell 两种本地运行时，Node/Python 的重任务通过"subAgent 委托机制"发到云侧执行。

华为在 HarmonyOS Skill 开发规范 V6 中对此有原话："Python / Node.js 在终端设备不具备运行时，通过 subAgent 子任务委托到 PC 或云侧执行，结果回传。"

这套设计的战略逻辑华为自己总结得很准：**"搬架构，不搬执行环境"** ------学了 OpenClaw 的设计范式（SKILL.md frontmatter 字段明文自称"与 AgentSkills 开源规范保持一致"），但不把 Node/Python 运行时搬进手机。

和清华、豆包在 Android 上做文章不同，**华为走的是 HarmonyOS 自建 AI-Native 路线** ------不是在别人的地基上改造，而是从自家操作系统底层重新设计一套面向智能体的能力体系。它把 2100+ 系统能力做了 Skill 化封装，端侧配了 ArkTS 原生执行器，配合 load_skill 工具按需渐进加载，让智能体用到哪个能力才加载哪个，省 token 也省内存。

这条路线的价值在于：**当你能掌控整个操作系统，就可以从系统层为智能体铺好"合法行动的轨道"** ，而不必像第三方那样在存量系统的权限夹缝里腾挪。这也是为什么华为的方案在能力覆盖和系统集成度上，天然比"改造派"更从容。
> 注：华为归入 Skill 派，是因为其 AgentSkills/OpenClaw 技术范式一致（SKILL.md 规范、subAgent 委托机制）；但它是自建 OS，不改 Android，改造深度不与清华开源项目类比。

*** ** * ** ***

### 本地 openclaw 移植到 Android 平台的 Demo------想端侧跑，撞墙后退守


![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fsz_mmbiz_png%2F1UQO7NGicXewyXHwydWicIpoV7BVRvfBQ5t9jfqrsJ6aDkDV2DalaDbEKRCrytsaVPBulvp7XVfmGMJ8SjiafHgYDrxRSIo3LKfhfRgbXEIXicc%2F640%3Fwx_fmt%3Dpng%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D1)

之前在账号分享过把openclaw源码移植到Android平台的文章，这是一个将 OpenClaw 移植到 Android 的验证性实践，出发点是站在**第三方开发者视角** ------拿不到厂商源码，只能在存量 Android 上用普通 App + SDK 做。

系统由 5 个独立 APK 组成（AIDL 跨进程）：

*
  • voice-assistant：语音 / 对话入口，智能体工具循环
*
  • gateway-service：Ktor WebSocket（端口 8765），端侧 gateway
*
  • memory-service：三层记忆（Session→Daily→Curated），RRF 混合检索，纯 Kotlin
*
  • skills-service：Skill 调度，支持 5 种执行模式
*
  • intent-service：无障碍捕屏 → ONNX 端侧意图分类 → 主动建议

端侧已接了多种 SDK 在本机运行部分操作：Kotlin 原生 Skill（KOTLIN_NATIVE 模式）、厂商 Tools SDK 结构化操作（约 194 项，走系统 Binder）、端侧 GUI 自动化（无障碍+虚拟屏）。

**一段真实的失败记录** ：曾把 libnode 编译进工程，结果 V8 引擎与 Android Bionic libc 的兼容问题导致 fatal crash，不得不禁用，端侧 gateway 改用 Ktor（Kotlin），把需要 Node/Python 的重 Skill 委托到个人腾讯云 OpenClaw 执行。

操控采用三通道并存：

1.
   1. **厂商 Tools SDK（结构化 API）** ：通过厂商预装意图服务，发送结构化 tool_calls（194 项操作），走系统 Binder 执行
2.
   2. **VLM 驱动 GUI（坐标点击）** ：截图 → 运营商侧云端 VLM 规划 → 坐标 GUI 循环；支持无障碍后端和虚拟屏+root 注入后端
3.
   3. **Skill 委托** ：重 Python Skill 经 REMOTE_PROXY / AGENT_SESSION 反连个人腾讯云 OpenClaw 执行

> root 权限**仅** 为 GUI Agent 后台虚拟屏拿到执行权限而引入（App 沙箱内拿不到），并非改内核、也非常态提权。这是第三方受限条件下的权宜之计。

*** ** * ** ***

### Skill 路线的根本规律

> **运行时的"OS 深改门票"** ：
>
> *
>   • 想让 Node/Python 运行时跑在手机本地 → 必须付 OS 级深改的代价（清华AOHP开源项目做到了，但在实验设备）
> *
>   • 不想深改 OS → 把运行时委托到云端（华为HarmonyOS 7、本地 Demo → 腾讯云）
> *
>   • 在普通 App 层硬塞 Node → 往往撞墙失败（libnode / Bionic 不兼容）

*** ** * ** ***

## 阵营二：MCP 派------调用"原子操作"

### 与 Skill 的本质区别

MCP（Model Context Protocol）是另一套哲学。Skill 让 AI "跑代码"，MCP 让 AI "调工具"------通过标准化的 tool-call 循环，调用预先封装好的语义化原子操作："打开日历"、"发送消息"、"下单"。

智能体不运行任何用户代码，因此**根本不需要 Node/Python 运行时，OS 不用针对这部分大改** 。

阶跃的 Step AOS 走的就是这条路，架构如下图所示：

![](https://cubox.pro/c/filters:no_upscale()?imageUrl=https%3A%2F%2Fmmbiz.qpic.cn%2Fmmbiz_jpg%2F1UQO7NGicXeyBvPHSkVswsFeJibwE837GDfMzQmAOqb4rGTsdF3c7JRfHZONwEEeOx6iahPNfBAEkw5T274ubIbOXDHFNSdHiaLNaSHfKMYoSxQ%2F640%3Fwx_fmt%3Djpeg%26from%3Dappmsg%26watermark%3D1%23imgIndex%3D2)

7月13日发布会的核心动作：**把手机端能力拆解成数千个最小原子操作，以 MCP 标准对外暴露** ，同时将 Android/Linux/RTOS 内核保留，在其上叠加一层 Agent 运行层。

### 端云协同：双脑分工

走 MCP 路线省掉了运行时的代价，但代价转移到了另一头：**需要一个足够强的"决策者"来判断下一步调哪个原子操作** 。这正是阶跃在端侧压强多模态模型的原因。

从公开披露的架构来看，阶跃采用模型矩阵双脑分工：

*
  • **端侧（System 1）** ：强多模态模型，处理实时感知、环境理解、快速反应式决策。阶跃称其 Step Edge 端侧模型在 29 项同类基准评测中全球第一，GUI/智能体/终端任务国内第一。
*
  • **云端（System 2）** ：大模型处理复杂多步规划，配合 Harness 脚手架调度整个执行环流。

阶跃自己描述其云端执行环境为"即便在当今 Agent 行业也颇为激进的**脚手架（Harness）系统** "------这是其云端"智能体执行环境"而非裸 LLM 的关键证据。

### MCP 的天然优势：可信可见可撤回

语义化原子操作还带来了传统 GUI 点击流无法实现的能力------**可信可见可撤回** ：

*
  • **可见** ：原子操作语义化，系统可以旁白"正在预订明晚8点餐厅"，而不是"点击(340,720)"
*
  • **可信** ：密码走保险箱+token，明文只在端侧操作边界注入，不经过云端
*
  • **可控** ：高危操作（付款/删除/发消息）执行前弹人类确认门（HITL）
*
  • **可撤回** ：可逆操作有逆操作可重放；不可逆但可取消的有延迟提交窗口（类似 Gmail undo-send）

这套四维框架在 GUI 路线里天然难以实现------原始点击流没有语义，无从求逆。

*** ** * ** ***

## 阵营三：GUI Agent 派------看屏幕、点界面

这条路线让智能体**用视觉模型看屏幕截图，规划操作步骤，再把点击和输入注入到真实 App 界面** 。它最大的特点是**通用** ------不需要 App 提供任何接口，任何应用都可以操控。

这也是豆包手机目前的主力路线，三星、华为、Google 也在逐步引入这种能力，但多数厂商将其作为"兜底长尾 App"的补位手段，而非核心架构。

GUI Agent 的优势在通用性，挑战在于：操作的可逆性差、部分 App 出于风控会主动限制自动化操作，以及端侧执行与记忆层的打通仍需要持续打磨。

*** ** * ** ***

## 一张表：三条路线的代价矩阵


维度

Skill 派

MCP 派（阶跃）

GUI Agent 派
**行动机制**
加载并运行脚本代码

调用语义化原子工具

视觉看屏 + 坐标注入
**OS 改造深度**
深（端侧）或零（委托云端）

最浅（不改内核）

框架层（定制ROM）
**是否需要运行时**
是，核心矛盾在于放哪

否，OS 可轻改

否，但需虚拟屏特权
**覆盖范围**
取决于 Skill 生态

取决于 MCP 接入

通用，但有限制
**可信可见可撤回**
部分支持

天然支持（原子操作）

难（原始点击流）
**端侧模型**
云端 LLM 为脑（清华）

端侧强模型决策

云端 VLM 规划

*** ** * ** ***

## 结语

三条路不是互斥的。从已有的实践来看，更可能的走向是分层协作：

**MCP/API 做主力** ------接入了 MCP 的应用直接走语义操作，可信可撤回；**GUI Agent 托底长尾** ------对于没有 MCP 接入的应用，靠视觉看屏点击先把任务跑通；**Skill 扩展能力边界** ------当你需要 AI 执行一段业务逻辑（不只是调工具），Skill 体系提供了标准化的扩展接口。

真正决定谁走得远的，未必是模型多聪明，而是**系统层有没有为智能体留出一条合法、可信、可治理的行动通道** 。

*** ** * ** ***

#### 引用链接

[1] github.com/aohp-os/aohp: *https://github.com/aohp-os/aohp*   
[2] arxiv.org/abs/2606.23449: *http://arxiv.org/abs/2606.23449v1*   





> 备注：微信原文经 opencli 抓取失败，以上为 Cubox 快照存档。

> Source: https://mp.weixin.qq.com/s?__biz=Mzk0NDcwNTc1OQ==&mid=2247483912&idx=1&sn=2282e48602310b1a5829fd8dc9f73867
> Captured: 2026-08-21 (AAIF daily-intake-evening)