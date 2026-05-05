# 性能工具 Perfetto (5)：可视化 UI 的使用办法

- **来源**：微信公众号
- **原文链接**：https://mp.weixin.qq.com/s?__biz=Mzg5Mjc0OTk2OQ==&mid=2247486148&idx=1&sn=933f8d2090bd10e2daccc373aee0caff
- **作者**：未知
- **日期**：2026-05-05

之前详细的介绍了 perfetto 抓取日志的办法，这些办法都会获得一个 pftrace 文件，我们只需要将这个文件在 https://ui.perfetto.dev 加载即可显示。本文介绍可视化 UI 的一些基础使用办法。

## 打开 Perfetto UI

默认界面只需要点击 Open trace file 将 perfetto/tracebox 抓到的日志上传上去即可。

## 调度全景图

以调度轨迹为例，CPU Scheduling 行显示 sched_switch 事件，代表整个系统上的调度情况。从粗的角度来看，CPU6、7、8、2、10、14、5 几个 CPU 上运行的任务事件比较密集，可以大致了解当前系统环境的性能状态。

## Ftrace Events

Ftrace Events 代表 ftrace 提供的信息，这是原始 ftrace ring buffer 的信息。因为这份日志抓的是调度轨迹，所以只看到了 sched_wakeup（蓝色）和 sched_switch（黄色）的事件，也就是任务什么时候被唤醒、什么时候切换。

## 调度关键指标

Scheduler 行提供了调度的关键指标：
- **Runnable Thread Count（可运行线程数）**：值持续很高说明线程太多、CPU 竞争激烈；突然飙高可能有大量线程被同时唤醒
- **Uninterruptible Sleep Thread Count（不可中断睡眠线程数）**：值持续 > 0 说明系统有 I/O 瓶颈；突然升高可能是某个线程在做大量 I/O
- **Active CPU Count（活跃 CPU 数）**：总 CPU 数减去运行 swapper/N 的 CPU 数

## Clock Snapshots

Perfetto 是生产者消费者模型，生产者可以多个，时钟源也是多个。通过 Clock Snapshots 中的对照关系，Perfetto 可以把不同数据源的时间转换到统一的时间轴进行对比。

Perfetto 默认支持 BOOTTIME、REALTIME、TAI、MONOTONIC、SCHEDCLOCK、CGLAST 等时钟类型，也支持自定义时间戳统一。

## SQL 查询

Perfetto 的精髓在于能够 SQL 查询，例如：
`: select * from slice` 可以查找所有的 slice
`: select * from thread_state where state like "%running%"` 可以统计所有 running 状态

掌握这些技巧就可以初步看到系统的性能状态，接下来可以详细介绍 SQL 进行 trace 分析。

## 参考资料

- Perfetto UI 官方文档：https://ui.perfetto.dev
