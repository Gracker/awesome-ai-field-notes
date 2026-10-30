# Mistral Large 4 (Le Chonk) is now open weight

- **原文链接**: https://mistral.ai/news/mistral-large-4-oss
- **作者**: Mistral AI
- **日期**: 2026-10-30
- **分类**: models
- **来源类型**: article
- **标签**: open-weights, coding-agents, frontier-models, cybersecurity
- **质量评分**: 4/5
- **抓取时间**: 2026-10-30T12:24:47Z

---

## 中文导读

Mistral 公开了旗舰模型 Mistral Large 4（Le Chonk）的权重：1 万亿参数、原生多模态的 hybrid instruct-and-reasoning MoE，公开预览后又追加约三周强化学习，官方称增益集中在编码与防御性网络安全，且"没有饱和迹象"。基准口径：Cognition 私有 FrontierCode 2.0 得 19.7% 居首；Terminal-Bench 4.0 得 41%（较预览 +13 分、输出 token 少 30%）；Artificial Analysis Coding Agent Index 48%，与 GLM-5.3 基本持平但每任务少用约 47% token；Surge Code 盲测人偏好仅次于 Claude Opus 5.5。安全侧：Cyber Index 51%，恶意网络请求拒绝率 96.6%，B3 智能体安全基准抗攻击率 97.1%。权重以修改版 MIT（Mistral Ecosystem Open-Weight license）发布，唯一附加条件是 MaaS 转售需另获商业授权；API 定价 $0.70/M 输入、$2.10/M 输出，权重已上架 Hugging Face，支持 vLLM/SGLang 自托管。

## 为什么值得关注

> "We release the weights of Le Chonk, advancing the frontier of open models in agentic coding and cybersecurity."

两条线索值得注意。其一，开源权重阵营的编码竞争已经进入 token 效率维度：Mistral 主打的差异点不再只是榜单分数，而是同等分数下每任务少用约 47% token，并为此提供 Low/Medium/High 三档推理模式让开发者自选成本曲线。其二，安全能力被产品化：Cyber Index 51%、恶意请求拒绝率 96.6%、B3 抗攻击 97.1% 之外，还向 Orange Cyberdefense 等设计伙伴开放了面向渗透测试/漏洞评估/红队的专精变体（需审查与合同约束），企业也能用 Mistral Forge 以自有安全数据定制模型。对欧洲主权 AI 叙事而言，这是"从头在欧洲基础设施训练 + 可完全自托管"的旗舰级落地，Booz Allen、Cisco、Cloudflare、CrowdStrike 等安全厂商均给出了背书引言。

## 关键信息

- 模型：Mistral Large 4（Le Chonk），1T 参数、原生多模态、hybrid instruct-and-reasoning MoE，官方称 160+ 语言流畅
- 编码：FrontierCode 2.0 19.7%（居首）；Terminal-Bench 4.0 41%（+13 分、输出 token -30%）；Artificial Analysis Coding Agent Index 48%（与 GLM-5.3 持平、每任务 token -47%）；Surge Code 盲测仅次于 Claude Opus 5.5，胜过 GLM-5.3 / Kimi K3 / DeepSeek V4.1 Flash
- 安全：Artificial Analysis Cyber Index 51%；恶意网络请求拒绝率 96.6%（官方称所测开源模型中最高）；B3 Agent Security 抗攻击 97.1%（预览为 93.3%）
- 通用：Finch 73.3%（开源模型中仅次 Kimi K3）；BrowseComp 84.5%（自 75% 的 SFT 起点）
- 授权：Mistral Ecosystem Open-Weight license（修改版 MIT）；可自由使用/修改/微调/商用，MaaS 运营者需单独商业授权
- 定价：$0.70/M 输入、$0.07/M 缓存输入、$2.10/M 输出
- 获取：Hugging Face mistralai/Mistral-Large-4-1T-A52B；vLLM、SGLang、NVIDIA NIM 自托管；另有 Mistral API / Studio、OpenRouter、Microsoft Foundry
- 技术报告官方称"coming soon"

## English Summary

Mistral released the weights of Mistral Large 4 (Le Chonk), its 1-trillion-parameter, natively multimodal hybrid instruct-and-reasoning MoE, after roughly three more weeks of reinforcement learning beyond the public preview. Claimed results: leading open-weight coding — 19.7% on Cognition's private FrontierCode 2.0, 41% on Terminal-Bench 4.0 (+13 points with 30% fewer output tokens), 48% on the Artificial Analysis Coding Agent Index effectively tied with GLM-5.3 at 47% fewer tokens per task, and second only to Claude Opus 5.5 in Surge Code blind human preference. Security: 51% on the Artificial Analysis Cyber Index, 96.6% refusal on malicious cyber requests, and 97.1% attack resistance on the B3 agent-security benchmark. Weights ship under the Mistral Ecosystem Open-Weight license (modified MIT; MaaS operators need a separate commercial license), priced at $0.70 / $0.07 cached / $2.10 per M tokens, downloadable from Hugging Face for vLLM/SGLang self-hosting.

## Obsidian Notes

- 内容由 `opencli web read` 拉取发布页全文生成。
- 全部数字来自 Mistral 官方发布页自述，未经独立复核；FrontierCode 2.0 为 Cognition 私有基准。
