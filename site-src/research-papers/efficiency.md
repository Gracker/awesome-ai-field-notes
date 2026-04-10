# 效率优化

Efficiency — 3 条活跃资源

### [Android 17 DeliQueue：二十年来最重要的消息队列架构重写](#) 
by @Shai Barack, Charles Munger (Google) | ⭐⭐⭐⭐⭐ 5/5 | 🇨🇳

**Android 17的核心架构重写：lock-free MessageQueue，丢帧降4-7.7%，启动快9.1%**

Android 17用lock-free混合数据结构DeliQueue替换了存在20年的MessageQueue实现。实际用户设备上实现丢帧率降低4%-7.7%、应用启动速度提升9.1%。这不是Binder IPC改造，而是对Android所有UI线程运行核心——Looper/Handler消息调度机制的根本性重构。每个应用的main线程、SystemUI、Launcher乃至system_server中的HandlerThread都依赖MessageQueue，这个单点性能改进具有全局传导效应。面向SDK 37及以上默认启用。
 `android-17` `deliqueue` `messagequeue` `lock-free` `performance` `frame-drop` `app-launch`

---
### [Android 16 MessageQueue 优化调研报告](#) 
by @Manus AI | ⭐⭐⭐⭐ 4/5 | 🇨🇳

**Android 16 MessageQueue重构：lock-free数据结构消除锁竞争**

调研Android 16对MessageQueue的重构优化。采用lock-free数据结构（Treiber stack和ConcurrentSkipListSet）解决优先级翻转问题。新实现几乎完全消除锁竞争，显著提升系统响应性和用户体验，特别是在冷启动等关键场景中。
 `android-16` `messagequeue` `lock-free` `treiber-stack` `performance` `priority-inversion`

---
### [MLGO: A Machine Learning Framework for Compiler Optimization – Google AI Blog](https://ai.googleblog.com/2022/07/mlgo-machine-learning-framework-for.html) 
 (2022-12-06) | ⭐⭐⭐⭐ 4/5 | 🌐

**ML for compiler optimization 的工业级实践，RL 替代启发式决策的里程碑**

Google 介绍 MLGO 框架，首个工业级将 ML 系统性集成到 LLVM 编译器的通用框架。使用强化学习训练神经网络替代编译器中的启发式决策。两个具体优化：1) Inlining-for-size：通过 RL 策略替代内联启发式，在 30k 模块上训练的策略可泛化到其他软件，实现 3%-7% 代码体积缩减（Fuchsia OS 上达 6.3%）；2) Regalloc-for-performance：寄存器分配优化，提升 0.3%-1.5% QPS。训练后的策略通过 XLA AOT 嵌入编译器，无运行时依赖。
 `MLGO` `compiler-optimization` `LLVM` `reinforcement-learning` `inlining` `register-allocation` `Google`

---