# Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks

- **ID**: dc2dc4a8
- **原文链接**: https://arxiv.org/abs/2611.08281
- **PDF**: https://arxiv.org/pdf/2611.08281v1
- **作者**: Zhitao He, Chi Him Zhang, Chengru Han, Yi R Fung
- **日期**: 2026-11-05
- **更新**: 2026-11-05
- **分类**: agents
- **来源类型**: paper
- **标签**: agent-security, benchmark, social-engineering, multimodal, red-team
- **质量评分**: 5/5
- **抓取时间**: 2026-11-08T04:26:47Z

---

## 中文导读

个人 AI 智能体正面临以伪造多模态内容为载体的社会工程攻击，而现有评测大多只覆盖文本对话。Multimodal-SEA 提供 608 个由专家基于真实诈骗案例设计的交互式任务，覆盖 14 个领域、152 个攻击场景，分四个难度等级，并区分中英文环境的社会文化语境。智能体要在模拟应用中检查内容、核实请求、执行操作，攻击是否得手以可验证的工具执行日志为准，配套 harness 支持受控自适应红队测试。7 个主流多模态模型全部被攻破，攻击成功率 7.1%–34.5%；加入多模态内容使成功率从 19.9% 升至 29.2%；更强的安全指令能压低攻击成功率却无助于识别欺骗内容，部分模型的低攻击率还伴随对合法请求的过度拒答。

## 为什么值得关注

诈骗载荷早已不限于文本，而智能体恰恰握有真实操作权限。这个基准把“攻击得手”锚定在工具执行日志而非模型自供上，结果可复核；“安全指令压低成功率但不提升识别”和“更低攻击率伴随过度拒答”两个发现，对做 agent 安全评测和部署决策都是可直接引用的风险量化。

该文于 2026-11-05 提交 arXiv（分类：cs.CL）。条目已有的中文导读与英文摘要均以此页元数据为锚，不引入摘要之外的实验细节。

## 关键信息

- 论文标题：Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks
- 作者：Zhitao He, Chi Him Zhang, Chengru Han, Yi R Fung
- arXiv：https://arxiv.org/abs/2611.08281
- 发布时间：2026-11-05
- arXiv 分类：cs.CL
- 关联标签：agent-security, benchmark, social-engineering, multimodal, red-team

## English Abstract

Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchmark comprising 608 expert-designed tasks grounded in real-world fraud cases, covering 14 domains and 152 attack scenarios with prepared multimodal content. The tasks span four difficulty levels and reflect the distinct social and cultural contexts of Chinese and English environments. Agents inspect content, verify requests, and execute actions in simulated applications, with attack outcomes grounded in verifiable tool execution logs. To enable controlled red teaming of personal agents, we design a multimodal attack harness that integrates task information, attack progression control, and multimodal content construction to evaluate their intrinsic security against adaptive social engineering attacks in simulated environments. Evaluating seven widely used multimodal models across six dimensions reveals that all are vulnerable, with attack success rates of 7.1% to 34.5%. Adding multimodal content increases attack success from 19.9% to 29.2%, despite increased proactive verification coverage. Stronger safety instructions reduce attack success without improving recognition of deceptive multimodal content, while lower attack success rates for some models accompany excessive refusal of legitimate requests.

## English Summary

Multimodal-SEA is an interactive benchmark of 608 expert-designed tasks built from real-world fraud cases, spanning 14 domains, 152 attack scenarios, four difficulty levels, and distinct Chinese/English social-cultural contexts. Personal AI agents inspect content, verify requests, and act inside simulated applications, with attack outcomes grounded in verifiable tool execution logs; a multimodal attack harness enables controlled, adaptive red teaming. Across six dimensions, all seven evaluated multimodal models are vulnerable, with attack success rates of 7.1%-34.5%. Adding multimodal content raises success from 19.9% to 29.2% despite more proactive verification; stronger safety instructions lower attack success without improving recognition of deceptive content, and lower success for some models accompanies over-refusal of legitimate requests.

## Obsidian Notes

- opencli arxiv paper 2611.08281 -f json 成功返回元数据（本批次首个调用，随后 arXiv API 开始返回 429）；本页由该 JSON 的元数据与摘要回填。
- 中文导读与价值判断均锚定在论文摘要、作者、日期与分类信息上，不引入摘要之外的实验细节。
- 本文件写入 canonical content 目录（content/dc2dc4a8.md），而非 openclaw/content/；现代站点生成器按 content/{entry.id}.md 查找内容页。
