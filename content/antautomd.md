# Claude Code Auto Mode：用分类器替代人工审批的安全跳过权限方案

*原文：[Anthropic 官方博客](https://www.anthropic.com) | 翻译：AI Field Notes*

**EN**

By default, Claude Code asks users for approval before running commands or modifying files. This keeps users safe, but it also means a lot of clicking "approve." Over time that leads to approval fatigue, where people stop paying close attention to what they're approving.

**ZH**

[TODO — see original English above]

**EN**

Users have two solutions for avoiding this fatigue: a built-in sandbox where tools are isolated to prevent dangerous actions, or the --dangerously-skip-permissions flag that disables all permission prompts and lets Claude act freely, which is unsafe in most situations. Figure 1 lays out the tradeoff space. Sandboxing is safe but high-maintenance: each new capability needs configuring, and anything requiring network or host access breaks isolation. Bypassing permissions is zero-maintenance but offers no protection. Manual prompts sit in the middle, and in practice users accept 93% of them anyway.

**ZH**

[TODO — see original English above]

**EN**

Auto mode is a new mode for Claude Code that delegates approvals to model-based classifiers — a middle ground between manual review and no guardrails. The goal is to catch the dangerous actions that aren't aligned with user intent, while letting the rest run without approval prompts.

**ZH**

[TODO — see original English above]

**EN**

## How it works

**ZH**

[TODO — see original English above]

**EN**

Auto mode uses two layers of defense: one for what Claude reads, one for what Claude does.

**ZH**

[TODO — see original English above]

**EN**

At the input layer, a server-side prompt-injection probe scans tool outputs (file reads, web fetches, shell output, external tool responses) before they enter the agent's context. When content looks like an attempt to hijack behavior, the probe adds a warning to the agent's context before the result is passed along — telling the agent to treat this content as suspect and anchor on what the user actually asked for.

**ZH**

[TODO — see original English above]

**EN**

At the output layer, the transcript classifier (running on Sonnet 4.6) evaluates each action against a set of decision criteria before it executes, acting as a substitute for a human approver. The classifier runs in two stages: a fast single-token filter (deciding 'yes' to block or 'no' to allow), followed by chain-of-thought reasoning only if the first filter flags the transcript. Because most actions clear the first stage, reasoning tokens are spent only where needed. The classifier sees only user messages and the agent's tool calls; we strip out Claude's own messages and tool outputs, making it reasoning-blind by design.

**ZH**

[TODO — see original English above]

**EN**

## Threat model

**ZH**

[TODO — see original English above]

**EN**

An agent might take a dangerous action for four reasons:

**ZH**

[TODO — see original English above]

**EN**

- **Overeager behavior**: The agent understands the user's goal, and is genuinely trying to help, but takes initiative beyond what the user would approve. For example, it uses a credential it happened to find or deletes something it judged to be in the way.
- **Honest mistakes**: The agent misunderstands the blast radius. For example, it thinks a resource is test-scoped when it's shared, or a branch is its own when it isn't.
- **Prompt injection**: Instructions planted in a file, webpage, or tool output hijack the agent, redirecting it from the user's task toward the attacker's.
- **A misaligned model**: Misalignment occurs when the agent pursues a goal of its own. We don't currently see this in practice, though we evaluate it carefully for every model we release.

**ZH**

[TODO — see original English above]

**EN**

The examples below are adapted from our internal incident log to illustrate what auto mode is designed to block:

**ZH**

[TODO — see original English above]

**EN**

- **Scope escalation**: A user asked to "clean up old branches." The agent listed remote branches, constructed a pattern match, and issued a delete. This would be blocked since the request was vague, the action irreversible and destructive.
- **Credential exploration**: An agent hit an auth error partway through a task. Rather than asking for permission, it began systematically grepping through environment variables and config files for alternative API tokens.
- **Agent-inferred parameters**: A user said "cancel my job." The agent queried the cluster, picked the closest match by name similarity, and tried to delete it.
- **Sharing via external service**: An agent wanted to share a script for debugging, and constructed a GitHub Gist command. This is blocked as data exfiltration.
- **Safety-check bypass**: A deploy command failed a pre-check; the agent retried with a skip-verification flag.

**ZH**

[TODO — see original English above]

**EN**

## How permission decisions work

**ZH**

[TODO — see original English above]

**EN**

**Tier 1: Built-in safe-tool allowlist and user settings.** A fixed allowlist includes tools that can't modify state, including file reads, text and file-pattern search, code navigation, todo and plan-mode transitions.

**ZH**

[TODO — see original English above]

**EN**

**Tier 2: In-project file operations.** File writes and edits inside the project directory are allowed without a classifier call. Routine coding doesn't pay classifier latency; in-project edits are reviewable via version control.

**ZH**

[TODO — see original English above]

**EN**

**Tier 3: Transcript classifier.** The transcript classifier sees everything else, including shell commands, web fetches, external tool integrations, subagent spawns, filesystem operations outside the project directory. Stage 1 is a fast single-token (yes/no) filter instructed to err toward blocking; if it flags, stage 2 re-evaluates with chain-of-thought reasoning to reduce false positives.

**ZH**

[TODO — see original English above]

**EN**

## The classifier decision criteria

**ZH**

[TODO — see original English above]

**EN**

The classifier's prompt is a fixed template we ship, with three customizable slots inserted into the middle. The fixed parts do the interpretive work — how to determine what an action actually does, how to read user authorization, the classification process itself — and they're the same for everyone. The slots define your policy: what counts as trusted in your environment, what categories to block, what exceptions to carve out.

**ZH**

[TODO — see original English above]

**EN**

The **environment** defines the trust boundary of which domains, cloud buckets, source-control orgs, and internal services count as "inside" versus "external." By default, the only thing the classifier trusts is the git repo you're currently working in.

**ZH**

[TODO — see original English above]

**EN**

The default has more than twenty block rules, which fall into these groups:

**ZH**

[TODO — see original English above]

**EN**

- **Destroy or exfiltrate**: Cause irreversible loss by force-pushing over history, mass-deleting cloud storage, or sending internal data externally.
- **Degrade security posture**: Make the system harder to monitor or defend by disabling logging, installing persistence like SSH keys or cronjobs, or modifying the agent's own permission config.
- **Cross trust boundaries**: Act on things the agent has no basis to trust, like running code cloned from external repos, scanning credential stores for usable tokens, or sending data to a service the user never specified.
- **Bypass review or affect others**: Skip safeguards on shared infrastructure by pushing directly to main, running production deploys, or modifying shared resources or jobs the agent didn't create.

**ZH**

[TODO — see original English above]

**EN**

## Results

**ZH**

[TODO — see original English above]

**EN**

We evaluated the full pipeline on three different datasets:

**ZH**

[TODO — see original English above]

**EN**

- **Real internal traffic (n = 10,000)**: Actual Claude Code tool calls from Anthropic employees.
- **Real overeager actions (n = 52)**: Curated from sessions where an employee denied the action or it was flagged post-hoc.
- **Synthetic data exfiltration (n = 1,000)**: Generated attempts including HTTP POSTs of sensitive data, git pushes to untrusted remotes, and credentials embedded in URLs.

**ZH**

[TODO — see original English above]

**EN**

| | Real traffic | Real overeager | Synthetic exfil |
|---|---|---|---|
| Stage 1 (fast filter) | 8.5% FPR | 6.6% FNR | 1.8% FNR |
| Stage 1→Stage 2 (full pipeline) | 0.4% FPR | 17% FNR | 5.7% FNR |

**ZH**

[TODO — see original English above]

**EN**

The 17% false-negative rate on real overeager actions is the honest number. The agent was trying to solve the user's problem and tried to execute a dangerous command past what was authorized.

**ZH**

[TODO — see original English above]
