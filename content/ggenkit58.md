# 宣布 Genkit Middleware：拦截、扩展并强化您的代理应用

**原文：**[Announcing Genkit Middleware: Intercept, extend, and harden your agentic apps](https://developers.googleblog.com/en/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/) | Google Developers Blog

---

[Genkit](https://genkit.dev/) 是一个开源框架，用于为任何平台构建全栈、AI 驱动和代理化的应用程序，支持 TypeScript、Go、Dart 和 Python。构建 production-ready 的代理化应用程序和 AI 功能需要的不仅仅是强大的模型和精心设计的提示词。您可能需要重试和回退以实现最大可靠性，在破坏性工具调用之前进行人工批准，以及在各层实现可观察性。

Genkit 通过中间件（middleware）解决这些问题：可组合的钩子，拦截生成调用（包括工具执行循环）并注入自定义行为。中间件系统目前在 TypeScript、Go 和 Dart 中可用，Python 支持即将推出。

---

## Genkit 中间件的工作原理

Genkit 中的每个 `generate()` 调用都会运行一个工具循环：模型产生输出，任何请求的工具执行，结果反馈到新的模型调用，循环重复直到模型完成。中间件钩子在这个循环的三个层面附加：

| 钩子 | 运行时机 | 典型用途 |
|------|----------|----------|
| **Generate** | 工具循环迭代一次 | 上下文注入、消息重写、对话级逻辑 |
| **Model** | 模型 API 调用一次 | 重试、回退、缓存、延迟日志 |
| **Tool** | 工具执行一次 | 人在环、沙箱、每工具日志 |

---

## 预构建中间件

Genkit 为常见场景提供了几种预构建的中间件解决方案。

### 1. Retry（重试）

自动重试瞬态错误（`RESOURCE_EXHAUSTED`、`UNAVAILABLE` 等）上的失败模型 API 调用，使用带抖动的指数退避。只会重试模型调用；周围的工具循环不会重放。

### 2. Fallback（回退）

当主模型在指定的一组错误代码上失败时，切换到替代模型。在主模型超出配额时回退到完全不同的提供商标记很有用。

### 3. Tool Approval（工具批准）

将工具执行限制为白名单。任何不在列表上的工具都会触发中断，实现人在环确认，然后操作才继续进行。

### 4. Skills（技能）

扫描目录中的 `SKILL.md` 文件并将其内容注入系统提示。还暴露一个 `use_skill` 工具，以便模型按需加载特定技能。

### 5. Filesystem（文件系统）

通过注入的工具（`list_files`、`read_file`，以及启用写入时的 `write_file` 和 `edit_file`）为模型提供对本地文件系统的 scoped 访问。路径安全得到强制执行，因此模型永远无法逃逸根目录。

---

## 构建自定义中间件

预构建的中间件涵盖了常见场景，但系统的真正力量在于编写您自己的中间件。想象您正在构建一个代理化客户支持应用，需要确保模型从不提及竞品或内部定价数据。与其在每个提示中编码这些规则，不如用中间件确定性强制执行。

自定义中间件在所有语言中都遵循一个简单的契约：提供一个名称和一个返回所需钩子的工厂函数。工厂在每个 `generate()` 调用时被调用一次，您只需实现您需要的钩子。

**大约 20 行代码的完整自定义内容过滤器示例**：

```go
type ContentFilter struct {
    ForbiddenTerms []string `json:"forbiddenTerms"`
}

func (ContentFilter) Name() string { return "app/contentFilter" }

func (f ContentFilter) New(ctx context.Context) (*ai.Hooks, error) {
    return &ai.Hooks{
        WrapModel: func(ctx context.Context, p *ai.ModelParams, next ai.ModelNext) (*ai.ModelResponse, error) {
            resp, err := next(ctx, p)
            if err != nil { return nil, err }
            text := strings.ToLower(resp.Text())
            for _, term := range f.ForbiddenTerms {
                if strings.Contains(text, strings.ToLower(term)) {
                    return nil, fmt.Errorf("content filter: response contains %q", term)
                }
            }
            return resp, nil
        },
    }, nil
}
```

您甚至可以组合和堆叠不同的中间件解决方案。中间件从左到右堆叠，列出的第一个是最外层包装器：

```go
resp, err := genkit.Generate(ctx, g,
    ai.WithModelName("googleai/gemini-flash-latest"),
    ai.WithPrompt("What CRM should our customer use?"),
    ai.WithUse(
        &middleware.Retry{MaxRetries: 3},  // outer
        &ContentFilter{ForbiddenTerms: []string{"CompetitorCRM", "RivalCo", "internal price"}}, // inner
    ),
)
```

---

## 开发者 UI 体验

您可以使用 Genkit [开发者 UI](https://genkit.dev/docs/go/devtools/) 来检查、测试和调试您的应用程序，包括中间件执行。注册中间件后，它会在 Dev UI 中可见：您可以检查其配置、跟踪每个钩子层的执行，并测试不同的组合。

---

*来源：Google Developers Blog（2026年5月14日）*