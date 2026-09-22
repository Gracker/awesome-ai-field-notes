# Package Manager Threat Model, Revisited

> 原文链接: https://nesbitt.io/2026/09/22/package-manager-threat-model-revisited.html
> 作者: Andrew Nesbitt
> 发布时间: 2026-09-22
> 来源笔记: OpenClaw定时任务/AK-RSS-Digest（89源精选）/2026-09-22

## 摘要（AAIF 提取）

Andrew Nesbitt 把五月发布的包管理器 CWE 清单与 threat model 设计问题在 10 个真实包管理器上持续跑了四个月，并将两份清单合并为长期维护页面 `/package-manager-threat-model/`。核心数字与结论：

- **公告规模**：5 月中旬以来 126 份公告，涉及 23 个包管理器与注册中心，约为该集合历史总量的四分之一；主要由三轮集中审计贡献——pnpm（6-7 月 20 份）、Homebrew（13 份）、Flatpak（单日 10 份）；OCI registry 实现在重走自托管语言 registry 五年前的授权/DoS bug。
- **路径遍历仍居首**（33 份），且绝大多数来自 manifest 字段（`name`/`version`/`bin`/entry-point/lockfile alias/patch target/hash-as-directory）而非压缩包条目；uv/pip/pdm/conda 五周内先后被报同一 entry-point 遍历，Composer 的 `bin` 字段修复在一个月内被绕过。
- **可命名的重复模式**：server-controlled response header → credential leakage，9 份公告同一机制（registry A 返回 `Location`/`Link`/`WWW-Authenticate` realm 指向主机 B，客户端带着凭证跟随）：ORAS 3 次、Renovate 4 次、Cargo/Homebrew 各 1 次。
- **两类方法互补**：CWE 机械扫描抓出 4 处可预测临时文件、6 处凭证进日志、5 处包控文本未剥离进终端（单点低危，合起来是纪律问题）；attacker-goal 设计问题抓到机械扫描够不着的高危接缝。Brakeman/CodeQL 的产出与人工审计几乎完全不重叠。
- **对抗式复核**：让一个"论证该发现是错的"的 agent 做二审，驳回了约 1/5 原始发现（看着像 SSRF 实则经过过滤中继、看着像反序列化实则三帧之外设了 `permitted_classes`）；每条驳回都沉淀为一条原本无文档的不变量。页面因此要求负结果清单与未验证假设清单作为标准输出。
- **新增设计问题**：feature composition——两个特性各自的前置信任假设在接缝处对不上，权限被另一特性针对别人资源的产物满足，两轮审计中最高危发现都属此类，无 CWE 对应、无可 grep 调用；sandbox hand-off——受限构建写回 install manifest/步骤清单/缓存条目后，工具以完整权限执行，边界实际移到了校验者身上。
- **其他新增条目**：CDN/中间件层（rubygems.org 的 Fastly 缓存 per-user API key 事故，bug 在 Rack 中间件顺序而非控制器代码）、镜像与缓存代理（Artifactory/Nexus/Verdaccio 改变名字权威性、yank 传播、校验和复验、凭证作用域）、工具自身发布管线（10 个审计中 6 个有发现：无校验和安装脚本、浮动 tag CI action 持发布凭证等）、编辑器/LSP（未安装前第一段执行的代码）、CWE-693 扩展为保护机制绕过、CWE-326 弱参数。

> 新公告约 19/20 能归入既有条目；第二十条就是上面这些新增维度的来源。清单稳定，但接缝类问题仍要靠设计问题清单去问。
