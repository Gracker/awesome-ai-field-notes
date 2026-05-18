---
title: "Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket"
date: 2026-04-29
source: google
category: infra
tags: [GCS, PyTorch, Colossus, Rapid-Bucket, fsspec, training, data-pipeline]
quality_score: 4
status: fetched
---

## 加速 AI：将 Google Colossus 引入 PyTorch（通过 GCSFS 和 Rapid Bucket）

**发布日期：2026年4月29日 | 来源：Google Cloud Blog**

### 概述

通过将基于 Google Colossus 存储架构的 Rapid Storage 通过行业标准的 fsspec 接口直接集成到 PyTorch，我们使研究人员和开发者能够让他们的 GPU 比以往更加繁忙。

### 挑战：保持 GPU 有数据可算

随着模型规模增长，数据加载和检查点保存往往成为训练的主要瓶颈。标准的基于 REST 的存储访问难以满足现代分布式训练极端吞吐量和低延迟要求，浪费宝贵的 GPU 资源。

### Rapid Bucket：通过双向 gRPC 实现 Rapid Storage

我们的新 Rapid Bucket 解决方案在专用区域桶中提供高性能对象存储。通过绕过传统 REST API 并利用持久化的 gRPC 双向流，我们将支撑 YouTube 和 Google Search 的文件系统有状态协议 Colossus 的强大能力直接带到了 PyTorch 生态系统。

### 核心性能指标

- **极致吞吐量：** 15+ TiB/s 聚合吞吐量
- **超低延迟：** 通过直接路径连接显著降低延迟
- **无需重写代码：** fsspec.open() 接口保持不变——零迁移成本

### 技术内幕

- **有状态 gRPC 流：** 双向流将每次操作的开销降至最低。
- **直接路径：** Rapid Bucket 通过 Google Direct Connectivity 将客户端直接连接到底层 Colossus 文件，消除额外网络跳数。
- **区域共置：** 存储与计算放置在同一区域（如 us-central1-a），消除跨区域延迟。
- **自动检测：** gcsfs 自动检测 Rapid Bucket，并将内部流量透明地从 HTTP 升级到双向 gRPC。

### 实际效果

- **训练时间：** 使用 Rapid Bucket 的 100 步训练总时间减少 23%
- **读取吞吐量：** 提升 4.8 倍（顺序和随机读取）
- **写入吞吐量：** 提升 2.8 倍

### 开始使用

```python
import gcsfs

# 初始化文件系统
fs = gcsfs.GCSFileSystem()

# 写入 Rapid bucket
with fs.open('my-zonal-rapid-bucket/data/checkpoint.pt', 'wb') as f:
    f.write(b"model data...")

# 追加到现有对象
with fs.open('my-zonal-rapid-bucket/data/checkpoint.pt', 'ab') as f:
    f.write(b"appended data...")
```

---
**参考链接：**
- [GCSFS GitHub](https://github.com/fsspec/gcsfs)
- [Rapid Bucket 文档](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket)
- [性能基准测试](https://github.com/fsspec/gcsfs/blob/main/docs/source/rapid_storage_support.rst)

---

## Speeding Up AI: Bringing Google Colossus to PyTorch via GCSFS and Rapid Bucket

**Published: April 29, 2026 | Source: Google Cloud Blog**

### Overview

By integrating Rapid Storage—powered by Google's Colossus storage architecture—directly with PyTorch via the industry-standard fsspec interface, we are enabling researchers and developers to keep their GPUs busier than ever before.

### The Challenge: Keeping GPUs Fed

As model sizes grow, data loading and checkpointing often become the primary bottlenecks in training. Standard REST-based storage access can struggle to meet the extreme throughput and low-latency requirements of modern distributed training.

### Rapid Bucket: Rapid Storage via Bi-directional gRPC

Our new Rapid Bucket solution provides high-performance object storage in dedicated zonal buckets. By bypassing legacy REST APIs and utilizing persistent gRPC bidirectional streams, we have brought the power of Colossus directly to the PyTorch ecosystem.

### Key Performance Metrics

- **Extreme Throughput:** 15+ TiB/s aggregate throughput
- **Ultra-Low Latency:** Significant latency reduction via direct path connectivity
- **No Code Rewrites:** fsspec.open() interface remains identical—zero migration effort

### Under the Hood

- **Stateful gRPC Streaming:** Bi-directional streaming minimizes per-operation overhead.
- **Direct Path:** Rapid Bucket connects clients directly to underlying Colossus files via Google Direct Connectivity.
- **Zonal Co-location:** Storage placed in the same zone as compute, eliminating cross-zone latency.
- **Auto-detection:** gcsfs automatically detects Rapid Bucket and upgrades internal traffic transparently.

### Results

- **Training Time:** 23% reduction in 100-step training total time using Rapid Bucket
- **Read Throughput:** 4.8x improvement (sequential and random reads)
- **Write Throughput:** 2.8x improvement

### Get Started

```python
import gcsfs

# Initialize the filesystem
fs = gcsfs.GCSFileSystem()

# Writing to a Rapid bucket
with fs.open('my-zonal-rapid-bucket/data/checkpoint.pt', 'wb') as f:
    f.write(b"model data...")

# Appending to an existing object
with fs.open('my-zonal-rapid-bucket/data/checkpoint.pt', 'ab') as f:
    f.write(b"appended data...")
```

---
**References:**
- [GCSFS on GitHub](https://github.com/fsspec/gcsfs)
- [Rapid Bucket Documentation](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket)
- [Performance Benchmarks](https://github.com/fsspec/gcsfs/blob/main/docs/source/rapid_storage_support.rst)
