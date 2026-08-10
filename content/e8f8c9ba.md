---
id: e8f8c9ba
title: "How We Broke Top AI Agent Benchmarks: And What Comes Next"
url: https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont
source: {"platform": "blog", "author": "Hao Wang, Qiuyang Mang, Alvin Cheung, Koushik Sen, Dawn Song", "original_date": "2026-04"}
quality_score: 5
tags: ["ai-agents", "benchmarks", "evaluation", "security", "reward-hacking"]
fetched_at: 2026-08-10T04:19:21.142291+00:00
fetch_method: opencli web read
---

# How We Broke Top AI Agent Benchmarks: And What Comes Next

> Source: https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont
> Author: Hao Wang, Qiuyang Mang, Alvin Cheung, Koushik Sen, Dawn Song
> Date: 2026-04
> Tags: ai-agents, benchmarks, evaluation, security, reward-hacking

## 中文导读

### AI Agent Benchmark 的“高分幻觉”：Berkeley RDI 如何攻破八个主流评测

这篇文章把“模型能力榜单”拆回到评测工程本身：如果 agent 可以通过 pytest hook、命令包装器、配置泄漏、浏览器本地文件访问或验证器弱点拿到近乎满分，那么排行榜测到的可能是 harness 暴露面，而不是任务解决能力。它对 agent 评测、benchmark provenance、隔离执行与漏洞披露流程都有直接参考价值。

## 关键要点

- 作者构建了自动化扫描 agent，审计 SWE-bench、WebArena、OSWorld、GAIA、Terminal-Bench、FieldWorkArena、CAR-bench 等八个代表性 agent benchmark。
- 文中给出多个可复现实例：少量 conftest.py 代码可影响 SWE-bench Verified；伪造 curl 包装器可让 Terminal-Bench 任务在不解题的情况下得分；WebArena 可通过 file:// 读取任务配置中的 gold answer。
- 问题并不只在“模型会作弊”，也在评测环境缺少最小权限、隔离、答案保密、执行可追踪性和 adversarial audit。
- 作者建议 benchmark 需要更像安全关键基础设施：明确威胁模型、审计 harness、隔离 evaluator、记录 provenance，并建立 exploit disclosure 机制。

## 讨论问题

- 现有 agent benchmark 是否应该把“抗 harness exploit”作为发布前强制检查？
- Leaderboard 报告是否需要同时披露执行环境、grader 权限、答案存储位置与污染/泄漏审计？
- 当模型具备工具调用和代码执行能力后，评测框架是否必须默认按 hostile participant 设计？

## 原始摘要 / Existing AAIF Summary

### English

UC Berkeley RDI reports an automated benchmark-auditing agent that found exploit paths across eight prominent AI-agent benchmarks, arguing that capability leaderboards need adversarially hardened harnesses, provenance, isolation, and exploit disclosure processes.

### 中文字段原文

UC Berkeley RDI describes an automated audit of eight major AI-agent benchmarks, including SWE-bench, WebArena, OSWorld, GAIA, Terminal-Bench, FieldWorkArena, and CAR-bench. The article claims near-perfect scores can be obtained by exploiting evaluation harnesses rather than solving tasks, with examples such as pytest hooks, binary wrapper trojans, config leakage, and validator weaknesses. HN discussion surfaced both the practical importance for trustworthy evaluation and critiques that many issues are harness misconfigurations rather than novel cyber exploits.

## OpenCLI 抓取正文节选

# Center for Responsible, Decentralized Intelligence at Berkeley
> 原文链接: https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont

---

![Exploit coverage by benchmark](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/figures/benchmark-scorecard.svg)

# How We Broke Top AI Agent Benchmarks: And What Comes Next

**Hao Wang, Qiuyang Mang, Alvin Cheung, Koushik Sen, Dawn Song**
UC Berkeley
April 2026
_(Est. 15-20 minutes read, tool available at [https://github.com/benchjack/benchjack](https://github.com/benchjack/benchjack), more details in [arXiv paper: https://arxiv.org/abs/2605.12673](https://arxiv.org/abs/2605.12673))_

* * *

_Our agent hacked every major one. Here’s how — and what the field needs to fix._

* * *

## The Benchmark Illusion

Every week, a new AI model climbs to the top of a benchmark leaderboard. Companies cite these numbers in press releases. Investors use them to justify valuations. Engineers use them to pick which model to deploy. The implicit promise is simple: a higher score means a more capable system.

That promise is broken.

We built an automated scanning agent that systematically audited **eight among the most prominent AI agent benchmarks** — SWE-bench, WebArena, OSWorld, GAIA, Terminal-Bench, FieldWorkArena, and CAR-bench — and discovered that **every single one** can be exploited to achieve near-perfect scores without solving a single task. No reasoning. No capability. Just exploitation of how the score is computed.

These aren’t theoretical attacks. Our agent builds working exploits for each benchmark, runs them through the official evaluation pipelines, and watches the scores roll in.

-   A conftest.py file with 10 lines of Python **“resolves” every instance on SWE-bench Verified.**
-   A fake `curl` wrapper gives a **perfect score on all 89 Terminal-Bench tasks without writing a single line of solution code.**
-   Navigating Chromium to a `file://` URL **reads the gold answer directly from the task config** — giving **~100% on all 812 WebArena tasks**.
-   And many more…

The benchmarks aren’t measuring what you think they’re measuring.

## This Is Already Happening

Benchmark scores are actively being gamed, inflated, or rendered meaningless, not in theory, but in practice:

-   [IQuest-Coder-V1](https://github.com/IQuestLab/IQuest-Coder-V1/issues/14) claimed 81.4% on SWE-bench — then researchers found that 24.4% of its trajectories simply ran `git log` to copy the answer from commit history. Corrected score: 76.2%. The benchmark’s shared environment made the cheat trivial.

-   [METR found](https://metr.org/blog/2025-06-05-recent-reward-hacking/) that o3 and Claude 3.7 Sonnet reward-hack in **30%+** of evaluation runs — using stack introspection, monkey-patching graders, and operator overloading to manipulate scores rather than solve tasks.

-   [OpenAI dropped SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) after an internal audit found that 59.4% of audited problems had flawed tests — meaning models were being scored against broken ground truth.

-   In [KernelBench](https://github.com/ScalingIntelligence/KernelBench/issues/82), `torch.empty()` returns stale GPU memory that happens to contain the reference answer from the evaluator’s prior computation — zero computation, full marks.

-   [Anthropic’s Mythos Preview](https://red.anthropic.com/2026/mythos-preview/) showed that frontier models can actively try to hack the environment and succeed. In one episode, the model needed to edit files it lacked permissions for; after searching for workarounds, it [found a way to inject code into a config file that would run with elevated privileges, and designed the exploit to delete itself after running](https://x.com/Jack_W_Lindsey/status/2041588510126395648). If a model can independently craft self-erasing privilege escalation exploits, it can find the holes in an evaluation harness.

These are not isolated incidents. They are symptoms of a systemic problem: **the benchmarks we rely on to measure AI capability are themselves vulnerable to the very capabilities they claim to measure.**

* * *

## The Scorecard of Our Exploit Agent

![Exploit coverage by benchmark — bar chart showing all eight benchmarks exploitable at 73-100%](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/figures/benchmark-scorecard.svg)

Zero tasks solved. Zero LLM calls (in most cases). Near-perfect scores.

-   **Terminal-Bench** (89 tasks) — **100%** score. Binary wrapper trojans.
-   **SWE-bench Verified** (500 tasks) — **100%** score. Pytest hooks force all tests to pass.
-   **SWE-bench Pro** (731 tasks) — **100%** score. In-container parser overwrite.
-   **WebArena** (812 tasks) — **~100%** score. Config leakage + DOM injection + prompt injection.
-   **FieldWorkArena** (890 tasks) — **100%** score. Validation never checks answer correctness.
-   **CAR-bench** (all hallucination tasks) — **100%** score. Reward components skipped entirely.
-   **GAIA** (165 tasks) — **~98%** score. Public answers + normalization collisions.
-   **OSWorld** (369 tasks) — **73%** score. VM state manipulation + public gold files.

* * *

## How Our Agent Did It

### Terminal-Bench: Trojanizing the Test Infrastructure

![Terminal-Bench exploit — binary wrappers installed during agent phase intercept verifier's dependency chain](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/figures/terminal-bench-exploit.svg)

Terminal-Bench evaluates agents on 89 complex terminal tasks (from building COBOL chess engines to configuring distributed systems). It uses Harbor, a sandboxing framework that re-uploads protected test files before verification. Containers have full internet access — Harbor’s `allow_internet` config defaults to `True` and no task overrides it.

Harbor correctly protects `/tests/` — but it doesn’t protect system binaries.

Here’s the irony: 82 of 89 tasks download `uv` from the internet _at verification time_ via `curl`, creating an exploitable dependency chain. Our exploit replaces `/usr/bin/curl` with a wrapper during the agent phase. When the verifier later runs `curl ... | sh` to install uv, our wrapper intercepts the request, installs the real uv, and then trojanizes the `uvx` binary. The trojanized `uvx` detects pytest invocations and produces fake passing output:

```
============================= test session starts ==============================
collected 3 items

tests/test_outputs.py ...                                               [100%]

============================== 3 passed in 0.05s ===============================
```

It writes `1` to the reward file. The verifier trusts it. Task “passed.”

For the remaining 7 tasks, our agent wraps `pip` (to trojanize freshly-installed `pytest`), `python` (to intercept `python -m pytest`), or the pre-installed `uvx` binary.

**Result:** 89/89 tasks, 100% score, without writing a single line of solution code.

* * *

### SWE-bench: 100% Resolve Rate Without Fixing a Single Bug

![SWE-bench exploit flow — conftest.py hook hijacks pytest to force all tests to pass](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/figures/swebench-exploit.svg)

SWE-bench is arguably the most influential AI coding benchmark. It presents real GitHub issues and asks the agent to produce a patch that makes the failing tests pass. SWE-bench-Verified (500 hand-validated instances) and SWE-bench Pro (731 multilingual instances) are currently considered the gold standards for measuring coding agents.

Both are exploitable at 100%.

**The vulnerability:** The agent’s patch is applied inside the same Docker container where tests run. Anything the patch introduces — a conftest.py, a monkey-patch, a Go `init()` function — executes with full privileges before or during testing.

**SWE-bench Verified exploit:** Our agent creates a `conftest.py` with a pytest hook that forces every test to report as passing:

```
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        rep.outcome = "passed"
        rep.longrepr = None
```

Pytest auto-discovers `conftest.py` files and loads them before running tests. The hook intercepts every test result during the “call” phase and rewrites it to “passed.” The log parser sees `PASSED` for every test. The grader sees all fail-to-pass tests now passing. Instance resolved.

For Django (231 of 500 instances), which uses unittest instead of pytest, the exploit prepends a monkey-patch to `django/__init__.py` that replaces `unittest.TestCase.run` with a function that unconditionally reports success.

For repos with an existing `conftest.py`, the exploit uses the `patch --batch --fuzz=5` fallback (the third of SWE-bench’s three patch application methods) to prepend our hook to the existing file.

> 注：正文较长，此处保留 opencli 抓取的关键前段；完整来源见原文链接。
