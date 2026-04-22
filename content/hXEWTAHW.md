# TRL 异步 GRPO：解耦推理与训练，RL Scaling 新一代方法解析

**原文来源：** Thom Wolf (@Thom_Wolf) · X (Twitter)  
**原文链接：** https://x.com/Thom_Wolf/status/2045817727705628714  
**抓取时间：** 2026-04-22  
**标签：** #RLHF #PPO #AsyncGRPO #TRL #numerical-precision #LLM

---

## 原文

**Deep content post alert** A technical deep dive for your Sunday morning, somewhere between a short detective story 🕵️ and a tutorial on RLHF 🧑🏫

We recently added AsyncGRPO in the TRL library to decouple inference and training and scale much faster and harder. As a sanity check, we ran it on a trivial setup (reward = −len, optimal policy = emit EOS immediately). To our surprise it did not converge!

This led us to a known but poorly understood issue: when the training forward pass runs in FP32 while the inference engine (vLLM) runs in BF16, RLHF often breaks. People have noticed this before and called it "numerical instability" or "noisy gradients." Nobody had pinpointed the actual mechanism. We did in this deep dive by @DirhousssiAmine

We instrumented the training loop and decomposed the importance sampling ratio as: log r = α + β, where α is the true policy change (in BF16 space) and β is the precision gap between the training forward pass and a BF16 forward on the same weights. See it like this:

> α = how much the policy actually changed since the rollout (same precision, different time).  
> β = how much the trainer and inference engine disagree about the same policy (same weights, different precision).

The ratio sees α + β and PPO can't tell them apart.

Empirically, β is small at the token level (O(1e−2–1e−1)) but it is not an innocent random noise that would wash out over time. We found it to be structured, persistent, and worse for certain tokens: it has a consistent negative bias, correlates with the advantage, and is up to 50x larger on low-probability tokens. However, despite all these concerning properties, none of them explain the mechanism. We saw that just disabling clipping leads to stable convergence meaning that β noise alone does not explain the failure.

We tested every plausible explanation and ruled them out one by one:

- ⭐️ **Treating β as pure noise:** keeping β but disabling clipping leads to stable convergence.
- ⭐️ **FP32 backward:** You're optimizing a function (FP32) that's slightly different from the one you deploy (BF16). So you might be climbing the wrong hill. Turns out the hills are close enough: using FP32 gradients with a clean ratio (β removed) converges and is actually more effective at improving the deployed BF16 policy.
- ⭐️ **Multiplicative distortion of the advantage:** Since β correlates with the advantage, you might think it systematically over-reinforces good tokens and under-suppresses bad ones, warping what the optimizer thinks is good vs bad. We measured this directly and the per-token gradient weights are identical whether β is there or not.
- ⭐️ **BF16 quantization / boundary crossings:** at low learning rates, most FP32 weight updates are too small to change the BF16 representation at all. So you might think vLLM just never sees the updates and that's why it stalls. However if boundary crossings were the problem, you'd expect the failing run to have fewer of them than the converging run. But both runs start with nearly identical boundary crossing rates.

What we discovered is that the failure mode only appears when β enters the PPO clipped objective. And this was our hint to the real mechanism.

Because PPO clips the ratio, small perturbations from β push r outside the trust region even when the underlying policy has not meaningfully changed. The clipped branch is selected, the gradient is exactly zero.

We call this **phantom clipping**: tokens are treated as if they exceeded the trust region when the change is purely numerical!

And this is not a marginal effect. At early training, the policy has barely moved (α ≈ 0), so the clipping decision reduces to whether |β| > 0.2. Yet roughly 18% of tokens get phantom-clipped! And because RL is closed-loop, the damage compounds: the deployed policy barely improves, future rollouts carry the same information, and the system locks into a permanent stall.

To make it a testable hypothesis, we confirmed causality with targeted interventions: removing β from the ratio, forcing r = 1, or keeping β but disabling clipping all restore convergence. Runs only fail when β is present in the clipped ratio. No exceptions.

The issue is not general numerical noise. It is a specific interaction between precision mismatch and PPO's clipping mechanism: the precision gap perturbs the ratio in a way that induces zero gradients where there should be signal.

We concluded with a set of recommended fixes (strongest first): match precisions (FP16 everywhere, or BF16 autocast with FP32 master weights), compute the ratio from a BF16 shadow forward pass, or widen ε to disable clipping.

Full write-up with experiments, interactive explanation and analysis at: https://t.co/SY86ZRNIcL

(Amine also wrote an X article which is very cool but you'll loose the interactive graphics and animations 😭)

---

## 中文翻译

**深度内容预警** 技术深潜，适合周日的早晨，介于短篇侦探故事🕵️和RLHF教程🧑‍🏫之间。

我们在 TRL 库中最近添加了 AsyncGRPO，以解耦推理与训练，实现更快、更大规模的扩展。作为合理性检验，我们在简单实验环境（reward = −len，最优策略 = 立即发出 EOS）上运行了它。结果出乎意料——没有收敛！

这把我们引向了一个已知但理解不深的问题：当训练前向传播运行在 FP32，而推理引擎（vLLM）运行在 BF16 时，RLHF 经常崩溃。之前人们注意到过这个问题，称之为"数值不稳定"或"梯度噪声"。没有人能精确定位真正的机制。我们通过 @DirhousssiAmine 的深度研究做到了。

我们在训练循环中插入测量工具，将重要性采样比率分解为：log r = α + β，其中 α 是真实策略变化（在 BF16 空间中），β 是训练前向传播与同一权重上 BF16 前向传播之间的精度差距。可以这样理解：

> α = 自 rollout 以来策略实际改变了多少（相同精度，不同时间）。  
> β = 训练器和推理引擎对同一策略的不一致程度（相同权重，不同精度）。

比率看到的是 α + β，而 PPO 无法将它们区分开来。

从经验上看，β 在 token 级别很小（O(1e−2–1e−1)），但它并非会随时间消散的无害随机噪声。我们发现它是有结构的、持续存在的，对某些 token 更严重：它有持续的负偏置，与 advantage 相关，在低概率 token 上最多可达到 50 倍之大。然而，尽管所有这些令人担忧的特性，没有一个能解释这个机制。我们发现只要禁用 clipping 就能稳定收敛，这意味着 β 噪声本身并不能解释失败。

我们逐一检验了每一种看似合理的解释，并逐一排除了：

- ⭐️ **将 β 视为纯噪声：** 保留 β 但禁用 clipping 可导致稳定收敛。
- ⭐️ **FP32 反向传播：** 你优化的函数（FP32）与部署的函数（BF16）略有不同。所以你可能在爬错误的海丘。结果发现两座海丘足够接近：使用清除 β 后的干净比率的 FP32 梯度能够收敛，而且实际上对改进部署的 BF16 策略更有效。
- ⭐️ **优势的多重扭曲：** 由于 β 与 advantage 相关，你可能认为它系统性地过度强化好的 token、压制坏的 token，扭曲了优化器认为的好与坏。我们直接测量了这一点，无论 β 是否存在，每个 token 的梯度权重都是相同的。
- ⭐️ **BF16 量化/边界跨越：** 在低学习率下，大多数 FP32 权重更新太小，根本无法改变 BF16 表示。所以你可能认为 vLLM 根本没看到更新，这就是停滞的原因。然而如果边界跨越是问题所在，你会期望失败 run 的边界跨越次数比收敛 run 更少。但两个 run 的边界跨越率起点几乎相同。

我们发现的失效模式只在 β 进入 PPO 裁剪目标时才会出现。这给了我们指向真正机制的线索。

由于 PPO 对比率进行裁剪，β 的小扰动会推动 r 超出信任区域，即使底层策略并未实质性改变。裁剪分支被选中，梯度恰好为零。

我们称之为 **幽灵裁剪（phantom clipping）**：token 被当作超出了信任区域来处理，而实际上变化纯粹是数值性的！

而且这不是边缘效应。在训练早期，策略几乎没有移动（α ≈ 0），所以裁剪决策归结为 |β| > 0.2 是否成立。然而大约 18% 的 token 遭受了幽灵裁剪！而且因为 RL 是闭环的，损害会复合：部署的策略几乎不改进，未来的 rollout 携带相同信息，系统锁定在永久停滞中。

为了使其成为可检验的假设，我们通过针对性干预确认了因果关系：从比率中移除 β、强制 r = 1、或保留 β 但禁用 clipping 都恢复了收敛。run 只有在 β 存在于裁剪比率中时才会失败。没有例外。

问题不是一般的数值噪声。它是精度不匹配与 PPO 裁剪机制之间的特定相互作用：精度差距以某种方式扰动比率，在应该有信号的地方产生零梯度。

我们给出了一组推荐修复方案（按有效性排序）：匹配精度（全链路 FP16，或 BF16 自动转换加 FP32 主权重）、从 BF16 影子前向传播计算比率、或扩大 ε 以禁用裁剪。

完整报告含实验、交互式解释和分析：https://t.co/SY86ZRNIcL

（Amine 也写了一篇 X 文章，非常酷，但你将失去交互式图形和动画 😭）
