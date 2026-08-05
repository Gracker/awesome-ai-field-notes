# Keyv and friends compromised in active Shai-Hulud supply chain attack

- **ID**: da2d8fe5
- **原文链接**: https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack
- **作者 / 日期**: Ilyas Makari / Aikido Security | 2026-08-04
- **分类**: infra
- **来源类型**: article
- **标签**: npm, supply-chain-security, credential-theft, shai-hulud, github-actions
- **质量评分**: 5/5
- **抓取时间**: 2026-08-05T15:45:26.663004+00:00

---

## 中文导读

Aikido 记录了 Keyv 维护者账号被攻破后的 Shai-Hulud npm 供应链攻击：攻击者向 keyvflat-cachefile-entry-cachecacheable 等高下载量包发布带 preinstall 的恶意版本，借 GitHub Actions provenance 正常签名发布payload 会下载 Bun 执行混淆脚本，窃取 npmGitHubAWSKubernetesVaultStripeSlack 等凭据，并利用 token 继续感染包和仓库8 月 5 日更新称至少 444 个包1381 个版本20 亿月安装量受影响

## 为什么值得关注

这次 npm 事件说明供应链攻击已从单包投毒升级成凭据窃取后的自动传播链

## English Summary

Aikido reports an active Shai-Hulud npm supply-chain worm that compromised the keyv maintainer account, published malicious preinstall payloads with valid GitHub Actions provenance, stole credentials from developer environments, and propagated to hundreds of packages.

## Obsidian Evidence

候选来自 `OpenClaw定时任务/ClawFeed24小时高价值一览/2026-08-05-ClawFeed24小时高价值一览.md` 的 ClawFeed 精选。

## Source Extract / Metadata

# Keyv and friends compromised in npm supply chain attack
> 原文链接: https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack

---

[Blog](https://www.aikido.dev/blog)![](https://cdn.prod.website-files.com/642adcaf364024552e71df01/66734db225dd2cbf1aa7d863_arrow_back.svg)[Vulnerabilities & Threats](https://www.aikido.dev/category/vulnerabilities-threats)![](https://cdn.prod.website-files.com/642adcaf364024552e71df01/66734db225dd2cbf1aa7d863_arrow_back.svg)

Keyv and friends compromised in active Shai-Hulud supply chain attack

# Keyv and friends compromised in active Shai-Hulud supply chain attack

Written by

[Ilyas Makari](https://www.aikido.dev/team-members/ilyas-makari)

Published on:

Aug 4, 2026

Last updated on:

Aug 5, 2026

On August 4, 2026, attackers compromised the GitHub account of the maintainer behind `keyv`, a key-value storage library with roughly 127 million weekly npm downloads, and used that access to inject a credential-stealing worm across the entire package family. The same maintainer owns `cacheable` (29M downloads/month), `flat-cache` (565M downloads/month), `file-entry-cache` (557M downloads/month), and several other widely-used caching utilities, all of which were swept up in the same attack.

The compromise was carried out by pushing malicious files directly to the `main` branch and then immediately cutting a new release, meaning the poisoned versions were published to npm with valid provenance signed by GitHub Actions.

**The compromised packages include:**

-   `keyv` 6.0.0 (604M/month)
-   `flat-cache` 6.1.24 (580M/month)
-   `file-entry-cache` 11.1.6 (571M/month)
-   `cacheable-request` 13.0.20 (137M/month)
-   `cacheable` 2.5.1 (30M/month)
-   `@cacheable/memory` 2.2.1 (28M/month)
-   `cache-manager` 7.2.10 (16M/month)
-   `@cacheable/node-cache` 3.1.2 (6M/month)
-   `@cacheable/utils` 2.5.1 (34M/month)
-   `@cacheable/net` 2.1.1 (3.7K/month)
-   `ecto` 5.0.1 (4.5K/month)

We are also also seeing very active community spread of this supply chain worm to other maintainers and packages, including major organizations:

-   `@deliveroo/reevent` 1.0.1
-   `@or-sdk/invitations` 1.4.9
-   `@picsart/ai-sdk` 3.32.2
-   `@qlik/embed-runtime` 1.6.4
-   `picasso.js` 2.11.6

**Update — August 5, 2026, 13:15 CEST:** At least 444 packages (across 1381 versions) have been compromised by the worm, with a combined total of over **2 billion monthly installs** at the time of writing.

## What happened

Every package in the family received two new files, `setup.mjs` and `Math_Symbol.js`, along with a `"preinstall": "node setup.mjs"` entry added to each `package.json`. Anyone who ran `npm install` against an affected version would have had `setup.mjs` execute automatically before their install completed.

`setup.mjs` is a heavily obfuscated dropper. Its only job is to silently download the Bun JavaScript runtime from github\[.\]com/oven-sh/bun/releases/download/bun-v1.3.13/ and use it to execute the real payload, `Math_Symbol.js`:

```haskell
execFileSync(<bun binary>, ['<script_dir>/Math_Symbol.js'], {
  stdio: 'inherit',
  cwd: <script_dir>
})
```

The `Math_Symbol.js` is a heavily obfuscated 728 KB JavaScript file containing credential stealers that harvest secrets from the victim's environment, encrypt the findings, and exfiltrate them to a public GitHub repository whose description reads "**Shai-Hulud: Here We Go Again**". The payload also contains worm-like propagation functionality to infect packages of other maintainers that have installed one of the compromised packages.

## What it steals

The `Math_Symbol.js` file implements a set of credential extractors, each targeting a different secret store on the victim machine.

**npm tokens**

Reads `~/.npmrc` and scans the filesystem for any other `.npmrc` files. Extracts `authToken` values and any `//registry.*:_authToken=...` entries. Validates each token live against `registry.npmjs[.]org/-/whoami` before exfiltrating.

**GitHub tokens**

Three token formats are targeted: classic PATs (`ghp_...`) and OAuth tokens (`gho_...`), GitHub App server-to-server tokens (`ghs_...`), and JWT OIDC tokens. Sources include `~/.config/gh/hosts.yml`, environment variables, and a filesystem scan.

On GitHub Actions runners, the payload also executes a shell command that reads the runner process memory directly to dump the entire secret store. It reads `ACTIONS_ID_TOKEN_REQUEST_TOKEN` and `ACTIONS_ID_TOKEN_REQUEST_URL` to steal OIDC tokens used for npm publishing.

**AWS credentials**

-   `~/.aws/credentials` and `~/.aws/config`, parsing all named profiles
-   `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` environment variables
-   EC2 Instance Metadata Service at `169.254.169.254`, trying IMDSv2 first with a fallback to IMDSv1
-   ECS container metadata endpoint at `169.254.170.2`
-   AWS Secrets Manager, calling `secretsmanager:ListSecrets` across multiple regions to enumerate and exfiltrate all secrets stored there

**Kubernetes secrets**

Reads the service account token, CA certificate, and namespace from `/var/run/secrets/kubernetes.io/serviceaccount/`. Uses the service account token to query the Kubernetes API directly and retrieve all secrets in the namespace. Also targets `KUBECONFIG` and `~/.kube/config`.

**HashiCorp Vault tokens**

Checks six sources in priority order: the `VAULT_TOKEN` environment variable, `~/.vault-token`, the GitHub Actions runner path `/home/runner/.vault-token`, several well-known container paths, a Kubernetes auth login using the stolen service account JWT, and Vault's AWS IAM auth endpoint using any stolen AWS credentials. After obtaining a token, it enumerates all KV stores via `/v1/sys/mounts` and reads every secret from KV v1 and v2 paths.

**Stripe and Slack tokens**

Scans for Stripe API keys (both test and live, `sk_` and `pk_` prefixes) and Slack tokens (`xox[baprs]-...`) across all files touched by the filesystem scanner.

**Generic filesystem scan**

A platform-aware scanner (macOS vs Linux) runs roughly 200 glob patterns across the filesystem, targeting among other things:

-   `.env`, `.env.*`, and `.envrc` files
-   Private key files (`*.pem`, `*.key`, `*.p12`, `*.pfx`, `*.jks`)
-   SSH keys and config (`id_rsa`, `id_ed25519`, `.ssh/config`)
-   Terraform state files and `.tfvars`
-   Docker registry credential files (`docker/config.json`)
-   KeePass databases (`*.kdbx`)
-   VPN configs (`*.ovpn`)
-   IDE config files including `.vscode/tasks.json` and `.claude/settings.json`

Files over 5 MB are skipped. Up to 64 concurrent reads are used. A generic regex engine is also applied across all scanned files, flagging PEM private keys, SSH public keys, Azure storage keys, database connection strings with embedded credentials, and generic `key=value` patterns matching common secret field names.

## Exfiltration

Once credentials are harvested, the payload encrypts the entire bundle before sending it anywhere. Only the attacker, who holds the corresponding RSA private key, can decrypt what gets uploaded. This means the stolen data sits in plain sight on public infrastructure but is unreadable to anyone else.

The primary exfiltration destination is a public GitHub repository whose description contains the string "**Shai-Hulud: Here We Go Again**". At the time of writing, GitHub contains roughly 1,300 public repositories matching that string, each serving as a drop point for a victim's encrypted credential bundle.

![](https://cdn.prod.website-files.com/642adcaf364024654c71df23/6a71fa87cf0901f6e761e8cd_Screenshot%202026-08-04%20at%2016.42.26.png)

If the GitHub upload fails, the payload falls back to `https://npm-cache[.]com:443/router`, a domain registered on 2026-05-22 that appears to serve no legitimate purpose. This domain is fetched dynamically from an Ethereum smart contract at `0xE1f2395ee43e45A1556EC6438a88c31B83493103`, allowing the attacker to rotate infrastructure at any time without touching the payload.

## Self-replicating worm

Beyond stealing credentials, the payload actively uses them to spread the malware to other maintainers and repositories. It has two distinct infection vectors.

**npm tarball infection**

Using the stolen npm token, the payload calls `https://registry.npmjs[.]org/-/npm/v1/tokens` to list every package that token has publish rights to, then fetches and unpacks the current tarball for each one. Before republishing, it makes the following modifications:

-   Bumps the patch version by one (e.g. `1.2.3` becomes `1.2.4`)
-   Adds `"preinstall": "node setup.mjs"` to the package scripts
-   Injects `setup.mjs` and `math_init.js` (functionally identical to `Math_Symbol.js`) into the package

It then repacks and publishes the modified tarball to the registry.

This is how the worm propagates beyond the original maintainer. After the initial compromise of the `keyv` maintainer, we observed over 400 packages being infected through community spread. These second-gene

...[truncated by AAIF intake]...
