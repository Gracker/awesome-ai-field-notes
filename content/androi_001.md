# 谁才是地表最强 Android Agent 大模型？Google官方测评来了！

微信文章，来源：mp.weixin.qq.com
发布日期：2026-04-27

## 背景

现有代码评测基准（HumanEval、SWE-bench）几乎清一色面向 Python，无法覆盖 Android 开发的复杂性（Kotlin/Java 双语言、Jetpack Compose 与 View 体系并行、Gradle 构建配置、设备碎片化）。

Google 正式发布 Android Bench — 首个专门针对 Android 开发的 LLM 评测基准。

## Android Bench 设计

- 任务来源：GitHub 上 500+ Star 的真实开源 Android 项目，从 38,989 个已合并的 PR 中精选 100 道题
- 任务类型：修复 Breaking Changes、Compose 迁移、Room 数据库迁移、Hilt 依赖注入配置等
- 技术栈分布：Kotlin 71% / Java 25%，Compose 41% / View 59%
- 任务难度：小改动（<27行）46%，中等改动（27-136行）33%，大改动（>136行）21%
- 评分方式：单元测试 + Android Instrumentation 测试，独立运行 10 次取平均
- 防作弊：Canary 字符串、轨迹审查、全面开源

## 实际测评结果（2026年4月7日）

| 排名 | 模型 | 通过率 |
|------|------|--------|
| 1 (并列) | GPT-5.4 | 72.4% |
| 1 (并列) | Gemini 3.1 Pro Preview | 72.4% |
| 3 | GPT-5.3-Codex | 67.7% |
| 4 | Claude Opus 4.6 | 66.6% |
| 5 | Claude Opus 4.5 | 61.9% |
| 6 | GPT-5.2-Codex | 62.5% |
| 7 | Claude Sonnet 4.6 | 58.4% |
| 8 | Claude Sonnet 4.5 | 54.2% |
| 9 | Gemini 3 Flash | 42.0% |
| 10 | Gemini 2.5 Flash | 16.1% |

## 核心结论

1. **双王并立**：GPT-5.4 与 Gemini 3.1 Pro Preview 以 72.4% 并列第一
2. **三大阵营**：第一梯队 65%+（GPT-5.4, Gemini 3.1 Pro, GPT-5.3-Codex, Claude Opus 4.6）；第二梯队 50-65%；第三梯队 <50%
3. **差距悬殊**：第一与最后相差 4.5 倍（72.4% vs 16.1%）
4. **Gemini 2.5 Flash 垫底**：架构升级影响远超参数堆叠，轻量级模型不适合复杂工程任务

## 关键洞察

- 通用基准正在失去意义，垂直领域基准才是拉开差距的战场
- 垂直评测将成为趋势（iOS Bench, Flutter Bench, React Native Bench）
- 公开排行榜将倒逼模型在垂直领域针对性优化

## 相关链接

- Android Bench 官网：https://developer.android.com/bench
- GitHub 开源仓库：https://github.com/android-bench/android-bench

> 备注：原文抓取自微信文章内容。
