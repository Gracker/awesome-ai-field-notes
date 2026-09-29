# Model Context Protocol (MCP) Tool Descriptions Are Smelly!

> 原文链接: https://arxiv.org/abs/2602.14878
> 作者: Mohammed Mehedi Hasan et al.
> 发布时间: 2026-02-16
> 源: arxiv

---

## 摘要

arXiv 2602.14878 对 103 个 MCP 服务器上的 856 个工具做了实证研究:从文献里归纳出工具描述的六个成分,基于此开发评分 rubric 并形式化 tool description smell。FM-based scanner 扫出来:97.1% 的工具描述至少含一处坏味道,56% 没把用途讲清;补全六个成分后任务成功率中位数 +5.85pp、部分目标完成 +15.12%,但执行步骤 +67.46%,16.67% 的案例性能回退;成分消融显示紧凑变体能保留行为可靠性同时降低 token 开销。判断:MCP 工具描述同时是文档与提示词,写细有收益,token 账单立刻跟上来;规模上去后工具目录本身就成了产品。

## English Summary

arXiv 2602.14878 empirically studies 856 tools across 103 MCP servers. The authors distill six components of a good tool description from the literature, build a scoring rubric on top of them, and formalize tool-description smells. An FM-based scanner finds that 97.1% of descriptions contain at least one smell and 56% do not even state their purpose. After augmenting descriptions to cover all six components, task success rates rise by a median of 5.85 percentage points and partial goal completion by 15.12%, but execution steps climb 67.46% and 16.67% of cases regress. Component ablations show that compact variants of different combinations often preserve behavioral reliability while cutting unnecessary tokens. The single most leveraged insight is that MCP tool descriptions are simultaneously documentation and prompts: writing them carefully pays off, but the token bill follows immediately, and at scale the tool catalog itself becomes a product.

## 为什么值得关注

主题线扩展 AAIF `mcp/tool-description/code-smell/agent-efficiency` 等主题。

## 信息源

- https://arxiv.org/abs/2602.14878
