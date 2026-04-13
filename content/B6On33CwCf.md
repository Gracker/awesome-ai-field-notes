# 深度调研：DroidClaw vs Open-AutoGLM

> **调研时间**：2026-04-12
> **耗时**：约 15 分钟
> **类型**：对比分析（开源 Android AI Phone Agent）

## 摘要

DroidClaw 和 Open-AutoGLM 是 2025-2026 年两个最具代表性的开源 Android AI Phone Agent 项目，均通过「感知屏幕 → LLM 推理 → ADB 执行」的循环实现手机自动化。但二者在**架构哲学、感知方式、模型策略、生态定位**上差异显著：DroidClaw 走「轻量实用主义」路线——Bun/TypeScript、accessibility tree 为主、任意 LLM、旧机复用；Open-AutoGLM 走「学术工程化」路线——Python、视觉语言模型为主、专用 9B 模型、渐进式强化学习训练。本文从架构、感知、模型、部署、生态、局限性六个维度进行深度对比，并给出选型建议。

---

## 1. 项目概况

### DroidClaw

| 维度 | 详情 |
|------|------|
| **GitHub** | [unitedbyai/droidclaw](https://github.com/unitedbyai/droidclaw) |
| **官网** | [droidclaw.ai](https://droidclaw.ai) |
| **语言** | Bun + TypeScript |
| **版本** | v0.5.3（含 Android APK） |
| **组织** | unitedbyai（社区驱动） |
| **定位** | 把旧 Android 手机变成 AI agent，无需 API，像人一样操作 app |
| **核心理念** | 「不需要 API、不需要集成开发，装好 app、告诉 agent 目标就行」 |
| **社区** | Discord 活跃，Dashboard 可视化管理 |

### Open-AutoGLM

| 维度 | 详情 |
|------|------|
| **GitHub** | [zai-org/Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) |
| **论文** | arXiv 2411.00820「Autonomous Foundation Agents for GUIs」 |
| **语言** | Python |
| **模型** | AutoGLM-Phone-9B / 9B-Multilingual（GLM-4.1V 架构） |
| **组织** | zai-org（智谱 AI） |
| **定位** | 基础级 GUI agent 框架，学术研究 + 工程落地双线推进 |
| **核心理念** | 渐进式强化学习训练，自我进化的课程学习，面向真实 GUI 场景 |
| **生态** | Midscene.js 适配、智谱 AI 输入法产品化、开发者激励活动 |

---

## 2. 架构对比

### 2.1 核心循环

二者都采用经典的 **Perception → Reasoning → Action** 循环，但实现方式截然不同。

**DroidClaw**：
```
目标输入 → dump accessibility tree (uiautomator dump)
→ 解析 XML → 提取交互元素 + 坐标
→ 发送给 LLM（screen state + goal + history）
→ LLM 返回 {think, plan, action}
→ 通过 ADB 执行 → 检查目标完成 → 循环
```

**Open-AutoGLM**：
```
任务输入 → 截图 (screencap) → 视觉语言模型理解屏幕
→ 多步规划（含思维链 CoT）
→ 生成操作序列 → ADB 执行
→ 敏感操作确认 / 人工接管 → 循环
```

### 2.2 感知方式（核心差异）

| 特性 | DroidClaw | Open-AutoGLM |
|------|-----------|-------------|
| **主感知** | Accessibility tree（结构化 XML） | 截图 + 视觉语言模型 |
| **备选感知** | Vision fallback（tree 为空时截图） | 无需备选（本身就是视觉） |
| **信息粒度** | 精确：元素类型、文本、坐标、状态 | 语义：整体视觉理解 |
| **适用场景** | 原生 Android app 效果好 | 所有可截图的 UI |
| **弱项** | Flutter/React Native/Game 的 tree 不完整 | 对小文本/密集 UI 可能不如结构化数据 |

**关键判断**：Accessibility tree 是「结构化感知」——知道每个按钮的类型、文本、是否可点击；Vision model 是「语义感知」——理解整体布局和视觉含义。前者精确但脆弱（依赖 app 正确暴露 accessibility），后者鲁棒但模糊。

### 2.3 容错机制

**DroidClaw 的工程化容错**（非常细致）：
- **Stuck loop detection**：屏幕 3 步不变 → 注入恢复提示，按动作类型区分（tap 失败 vs swipe 失败）
- **Repetition tracking**：滑动窗口追踪最近动作，同一坐标点 3+ 次则强制换策略
- **Drift detection**：agent 连续导航动作（swipe/back/wait）无实际交互 → 推回执行
- **Vision fallback**：tree 为空自动切截图模式
- **Action feedback**：每步结果（成功/失败 + 消息）反馈给 LLM

**Open-AutoGLM 的安全机制**：
- **敏感操作确认**：支付、密码等场景自动暂停等待确认
- **人工接管**：登录、验证码场景支持回调让人类介入
- **最大步数限制**：默认 100 步，防止无限循环

---

## 3. 模型策略对比

### 3.1 DroidClaw：LLM-Agnostic

DroidClaw **不绑定任何特定模型**，支持任意 OpenAI 兼容 API：

| Provider | 说明 |
|----------|------|
| **Groq** | 免费层可用，推荐入门 |
| **Ollama** | 完全本地，支持 llama3.2 等 |
| **OpenAI** | GPT-4o 等 |
| **OpenRouter** | 多模型路由 |
| **Bedrock** | AWS 部署 |

优势：灵活、成本低、可随时换模型。劣势：非专门训练，通用 LLM 对 GUI 操作的理解深度有限。

### 3.2 Open-AutoGLM：专用模型

| 模型 | 说明 |
|------|------|
| **AutoGLM-Phone-9B** | 中文手机应用优化 |
| **AutoGLM-Phone-9B-Multilingual** | 英文场景优化 |
| **架构** | GLM-4.1V-9B-Thinking（与 GLM-5 同源） |
| **训练** | 渐进式在线课程强化学习 |

**渐进式训练**是其核心创新：
- 自我进化课程学习（self-evolving curriculum）
- 基于失败尝试自动生成新训练任务
- 结果监督的奖励模型
- 自适应强化学习策略

部署方式：
- **云端 API**：智谱 BigModel、ModelScope
- **本地部署**：vLLM / SGLang 推理引擎，需要 GPU（9B 模型）

### 3.3 模型策略判断

| 维度 | DroidClaw | Open-AutoGLM |
|------|-----------|-------------|
| **门槛** | 低（免费 LLM 即可） | 中（需 GPU 或 API 费用） |
| **上限** | 取决于选用的 LLM | 专用训练，GUI 场景上限更高 |
| **成本** | 几乎为零（Ollama 本地） | API 调用费或 GPU 成本 |
| **可定制** | 换 prompt 换模型 | 微调模型权重 |

---

## 4. 功能与能力对比

### 4.1 操作能力

| 操作 | DroidClaw (28 个 action) | Open-AutoGLM |
|------|-------------------------|-------------|
| 基础交互 | tap/type/enter/longpress/clear/paste/swipe/scroll | Tap/Type/Swipe/Long Press/Double Tap |
| 导航 | home/back/launch/switch_app/open_url/open_settings/notifications | Launch/Back/Home/Wait |
| 系统级 | shell/keyevent/pull_file/push_file/screenshot | — |
| 剪贴板 | clipboard_get/clipboard_set | — |
| 复合技能 | read_screen/submit_message/copy_visible_text/wait_for_content/find_and_tap/compose_email | Take_over（人工接管） |

**DroidClaw 明显更丰富**：28 个原子操作 + 7 个复合技能，覆盖了 shell 命令、文件传输、剪贴板等系统级能力。

### 4.2 应用支持

**DroidClaw**：不维护应用白名单，只要 accessibility tree 可解析就行。提供 35 个预置 workflow（messaging/social/productivity/research/lifestyle）。

**Open-AutoGLM**：明确维护 50+ Android 应用支持列表 + 60+ 鸿蒙原生应用，分类覆盖社交通讯/电商/美食/出行/视频/音乐/生活服务。

### 4.3 设备支持

| 维度 | DroidClaw | Open-AutoGLM |
|------|-----------|-------------|
| **Android** | ✅ USB + WiFi ADB | ✅ USB + WiFi ADB |
| **iOS** | ❌ | ✅ WebDriverAgent |
| **鸿蒙** | ❌ | ✅ HDC 工具链 |
| **远程控制** | ✅ Tailscale | ✅ WiFi/网络 |

### 4.4 运行模式

| 模式 | DroidClaw | Open-AutoGLM |
|------|-----------|-------------|
| **交互模式** | 输入目标，实时执行 | ✅ 交互模式 |
| **Workflow** | JSON 多步任务编排 | ✅ 指定任务执行 |
| **Flow（确定性）** | YAML 固定序列，无 LLM | ❌ |
| **Python API** | ❌（TypeScript） | ✅ PhoneAgent 类 |
| **APK** | ✅ v0.5.3 Android APK | ❌ |
| **Dashboard** | ✅ app.droidclaw.ai | ❌ |

---

## 5. 部署与上手对比

### DroidClaw

```bash
curl -fsSL https://droidclaw.ai/install.sh | sh  # 一键安装
# 或手动：
brew install android-platform-tools
curl -fsSL https://bun.sh/install | bash
git clone https://github.com/unitedbyai/droidclaw.git && cd droidclaw
bun install && cp .env.example .env
# 配置 .env（选 Groq 免费最快）
bun run src/kernel.ts
```

- **最低要求**：Bun + ADB + API Key（或 Ollama）
- **最快上手**：5 分钟
- **硬件要求**：无 GPU 需求（LLM 走云端或 Ollama CPU）

### Open-AutoGLM

```bash
pip install -r requirements.txt && pip install -e .
# 需安装 ADB Keyboard 到手机
# 需部署模型服务（本地 GPU 或云端 API）
python main.py --base-url https://open.bigmodel.cn/api/paas/v4 \
  --model "autoglm-phone" --apikey "your-key" "打开美团搜索火锅"
```

- **最低要求**：Python 3.10+ + ADB + 模型服务
- **最快上手**：15-30 分钟（云端 API）/ 1-2 小时（本地 GPU）
- **硬件要求**：本地部署需 GPU（9B VLM，建议 16GB+ 显存）

---

## 6. 局限性对比

### 6.1 共同局限

- **银行/金融 app**：FLAG_SECURE 阻止截图
- **生物认证**：无法绕过指纹/面部识别
- **加密锁屏**：无法解锁
- **验证码/CAPTCHA**：需人工接管
- **跨应用数据隔离**：无法访问其他 app 私有数据

### 6.2 各自特有局限

**DroidClaw**：
- Flutter / React Native / Game 的 accessibility tree 不完整
- WebView 支持有限
- 拖拽/多指手势不支持
- Android 12+ 剪贴板限制
- 通知栏交互有限
- 依赖 Bun 运行时（非标准 Node.js）

**Open-AutoGLM**：
- 模型体积大（9B），本地部署门槛高
- 中文优化版英文能力弱，反之亦然
- 依赖智谱生态（BigModel API / ModelScope）
- 无确定性 Flow 模式（每次都要过模型）
- 无 Dashboard / 可视化管理
- 学术项目色彩较浓，生产级文档和测试覆盖待验证

---

## 7. 关键发现

1. **感知哲学是最本质的差异**：DroidClaw 的 accessibility tree 是「精确但脆弱」的结构化感知，Open-AutoGLM 的视觉模型是「模糊但鲁棒」的语义感知。这决定了二者在不同 app 类型上的表现差异。

2. **DroidClaw 工程化程度更高**：28 个原子操作、7 个复合技能、stuck detection / repetition tracking / drift detection 三重容错、确定性 Flow 模式、APK + Dashboard，是一个「拿来就能用」的工具链。

3. **Open-AutoGLM 学术深度更高**：arXiv 论文、渐进式强化学习训练、专用 9B VLM、iOS + 鸿蒙多平台支持、Midscene.js 生态适配，是一个「有理论支撑有产品落地」的基础框架。

4. **LLM-Agnostic vs 专用模型**是选型的核心决策点：追求灵活低成本选 DroidClaw，追求 GUI 场景上限选 Open-AutoGLM。

5. **二者互补而非替代**：DroidClaw 的 accessibility tree 感知可以作为 Open-AutoGLM 视觉感知的补充；DroidClaw 的工程化容错机制值得 Open-AutoGLM 借鉴。

---

## 8. 选型建议

| 场景 | 推荐 | 理由 |
|------|------|------|
| **快速原型 / 个人玩具** | DroidClaw | 5 分钟上手，免费 LLM，旧机即可 |
| **生产级手机自动化** | Open-AutoGLM | 专用模型、鸿蒙/iOS 支持、安全机制 |
| **学术研究** | Open-AutoGLM | 有论文、有训练框架、可复现 |
| **多平台覆盖** | Open-AutoGLM | Android + iOS + 鸿蒙 |
| **完全离线 / 隐私优先** | DroidClaw | Ollama 本地 LLM，无云端依赖 |
| **复杂工作流编排** | DroidClaw | Workflow + Flow 双模式 + Dashboard |
| **中文 app 深度优化** | Open-AutoGLM | 中文版专门训练，50+ app 适配 |

---

## 参考资料

[1] [unitedbyai/droidclaw - GitHub](https://github.com/unitedbyai/droidclaw) - DroidClaw 官方仓库，Bun/TypeScript 实现
[2] [zai-org/Open-AutoGLM - GitHub](https://github.com/zai-org/Open-AutoGLM) - Open-AutoGLM 官方仓库，Python 实现
[3] [AutoGLM: Autonomous Foundation Agents for GUIs - arXiv 2411.00820](https://arxiv.org/abs/2411.00820) - 渐进式训练框架论文
[4] [droidclaw.ai](https://droidclaw.ai) - DroidClaw 官网，含安装脚本和文档
[5] [AutoGLM-Phone-9B - HuggingFace](https://huggingface.co/zai-org/AutoGLM-Phone-9B) - 中文优化模型权重
[6] [AutoGLM-Phone-9B-Multilingual - HuggingFace](https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual) - 多语言模型权重
[7] [Midscene.js AutoGLM 适配指南](https://midscenejs.com/zh/model-common-config.html#auto-glm) - iOS/Android 跨平台自动化
[8] [智谱 AI 输入法](https://autoglm.zhipuai.cn/autotyper/) - AutoGLM 产品化落地

---

_调研完成于 2026-04-12 00:20 CST，基于 GitHub 仓库文档、arXiv 论文、Gemini 联网搜索交叉验证。_
