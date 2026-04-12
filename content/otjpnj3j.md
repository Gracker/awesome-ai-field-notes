## 搞懂缓存机制，从Gemma4到Claude Code省80%Token

### 一、从本地 Gemma 4 实验出发
从本地 Gemma 4 实验出发，详解 Transformer KV 缓存原理（QKV 注意力机制中的 Key/Value 缓存），解释为什么 Decoder-only 架构可以缓存历史 token 的 KV。

### 二、Transformer KV 缓存原理
Transformer KV 缓存是 QKV 注意力机制中的 Key/Value 缓存。在 Decoder-only 架构中，历史 token 的 KV 可以被缓存起来，这是理解缓存机制的基础。

### 三、Claude Code 的缓存实现
逆向分析 Claude Code 的缓存实现，Anthropic 做了一整套精密的缓存工程。理解后可让同样的套餐多撑 3-5 倍。

### 四、缓存保护原则
**保护缓存的（绿灯）：**
- 连续对话 — 前缀不变，增量缓存，一个 session 持续对话
- btw — 使用 btw 共享 session，可共享缓存
- Claude.md — 定期整理这个文件，但不要在工作到一半的时候整理

**破坏缓存的（红灯）：**
- 开新 session — 冷缓存，~20K tokens 全价重算
- 改 CLAUDE.md — Block 4 起全部失效，配好就别动
- 加减 MCP 工具 — 工具 schema 变化 = 缓存断裂，session 前配好，禁用不用的MCP
- 切换模型 — 完全失效，按阶段切，别频繁切
- /compact — 消息历史变了 = 断裂，对话 >100K 时再用
- 发呆超过 TTL — 缓存过期，1h 内说句话

### 五、缓存差异有多大
假设系统提示词 20K tokens，对话 10 轮：

- 一个 session 持续对话：1 次全价 + 9 次 1/10 = 1.9 份
- 每次开新 session：10 次全价 = 10 份

差了 5 倍。对 Pro/Max 订阅用户，这意味着同样的套餐能多干 3-5 倍的活。

### 六、保护你的缓存：Claude Code 使用姿势
理解了缓存机制，就知道什么习惯省钱、什么烧钱。

核心原则：别碰前缀，只在末尾追加

### 七、进阶想法：Cache Keep-Alive 续命
Pro/Max 用户的 TTL 是 1 小时。午饭吃 1.5 小时回来，缓存就过期了，开个冗长的会议，缓存就过期了。

原理：缓存 TTL 在每次读取时刷新。所以只要在过期前发一次匹配前缀的请求，缓存就能无限续命。

方案设想：用 tmux 或 iTerm2 AppleScript，每 55 分钟往 Claude Code 终端自动发一条prompt。

### 八、IceBearMiner 的节省80%token宝典
@IceBearMiner 也写了一篇节省80%token的宝典，大家可以验证看看。

---

## 中文

搞懂缓存机制，从Gemma4到Claude Code省80%Token

从本地 Gemma 4 实验出发，详解 Transformer KV 缓存原理（QKV 注意力机制中的 Key/Value 缓存），解释为什么 Decoder-only 架构可以缓存历史 token 的 KV。逆向分析 Claude Code 的缓存实现，Anthropic 做了一整套精密的缓存工程。理解后可让同样的套餐多撑 3-5 倍。