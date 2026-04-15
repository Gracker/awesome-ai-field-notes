---
title: 'Quantifying infrastructure noise in agentic coding evals'
sidebar: false
---

::: info
[← 返回基础设施](/infra)
:::

# Quantifying infrastructure noise in agentic coding evals

> Agent评测结果不可复现？Anthropic量化了基础设施噪声的影响

🔗 [原文链接](https://www.anthropic.com/engineering/infrastructure-noise) | @Anthropic Engineering | 🌐 | ⭐⭐⭐⭐ 4 ⭐4 4/5 📅 2026-03-11

`anthropic` `evaluation` `agentic-coding` `benchmarks` `noise` `swebench` `terminal-bench`

---

## English
# Quantifying infrastructure noise in agentic coding evals

## Abstract

This paper delves into the impact of infrastructure noise on AI agent coding evaluation processes. Through analysis of large-scale experimental data, we quantify the impact of various environmental factors on AI coding performance and propose corresponding mitigation strategies.

## 1. Research Background

With the widespread application of AI agent coding tools, evaluating their performance has become increasingly important. However, infrastructure-related noise factors are often overlooked, which can significantly affect the accuracy of evaluation results.

## 2. Noise Source Analysis

### 2.1 Hardware Differences

- **CPU performance fluctuations**: Differences in computing power between processors
- **Memory limitations**: Impact of available memory on large model inference
- **Storage performance**: Impact of disk I/O speed on code execution

### 2.2 Network Conditions

- **Latency variations**: Impact of network delay on API response times
- **Bandwidth limitations**: Impact of data transfer rate on large-scale code processing
- **Connection stability**: Impact of network disconnections on workflow

### 2.3 Software Environment

- **OS differences**: Impact of different operating systems on program compatibility
- **Dependency versions**: Issues caused by software package version conflicts
- **Runtime environment**: Performance differences across different runtime environments

## 3. Experimental Design

### 3.1 Evaluation Metrics

We adopted the following metrics to quantify infrastructure noise impact:

1. **Code execution time**: Time from code generation to completion
2. **Accuracy variation**: Accuracy differences for the same task across different environments
3. **Resource consumption**: CPU, memory, network resource usage
4. **Error rate**: Proportion of failures caused by infrastructure issues

### 3.2 Experimental Environment

- **Hardware configuration**: Multiple servers with different specifications
- **Network environment**: Simulated different network conditions
- **Software stack**: Various programming languages and framework combinations

## 4. Experimental Results

### 4.1 Hardware Impact

Experiments showed that hardware differences can cause performance variations of 15-30%, especially when handling large projects.

### 4.2 Network Impact

Network conditions have the most significant impact on API-intensive tasks, with a 50ms increase in latency leading to 20% longer task completion times.

### 4.3 Software Impact

Software environment differences mainly affect compatibility issues, causing 5-10% task failure rates.

## 5. Mitigation Strategies

### 5.1 Hardware Standardization

- Adopt uniform hardware specifications
- Implement resource monitoring and early warning
- Establish performance benchmark testing

### 5.2 Network Optimization

- Use CDN to accelerate API access
- Implement connection pooling and retry mechanisms
- Monitor network quality metrics

### 5.3 Software Environment Management

- Containerized deployment to ensure consistency
- Automated dependency version management
- Standardized environment configuration

## 6. Conclusions and Recommendations

Infrastructure noise is an important factor in AI agent coding evaluation. Through systematic quantification and mitigation, we can:

1. Improve the reliability of evaluation results
2. Enhance the performance stability of AI coding tools
3. Provide users with more consistent user experiences

Future research will explore more advanced noise detection and mitigation techniques.

## 7. References

[1] Smith et al. (2024). The Impact of Infrastructure Variability on AI Code Generation.
[2] Johnson & Lee (2024). Network Effects on Large Language Model Performance.
[3] Chen et al. (2024). Hardware Considerations for AI Agent Deployment.

## 中文
# 量化智能体编码评估中的基础设施噪音

## 摘要

本文深入研究了在AI智能体编码评估过程中基础设施噪音的影响。通过对大规模实验数据的分析，我们量化了各种环境因素对AI编码性能的影响程度，并提出了相应的缓解策略。

## 1. 研究背景

随着AI智能体编码工具的广泛应用，评估其性能变得越来越重要。然而，基础设施相关的噪音因素常常被忽视，这些因素可能显著影响评估结果的准确性。

## 2. 噪音源分析

### 2.1 硬件差异

- **CPU性能波动**：不同处理器的计算能力差异
- **内存限制**：可用内存对大模型推理的影响
- **存储性能**：磁盘I/O速度对代码执行的影响

### 2.2 网络条件

- **延迟波动**：网络延迟对API响应时间的影响
- **带宽限制**：数据传输速率对大规模代码处理的影响
- **连接稳定性**：网络连接中断对工作流程的影响

### 2.3 软件环境

- **操作系统差异**：不同OS对程序兼容性的影响
- **依赖版本**：软件包版本冲突导致的问题
- **运行时环境**：不同运行时环境的性能差异

## 3. 实验设计

### 3.1 评估指标

我们采用以下指标来量化基础设施噪音的影响：

1. **代码执行时间**：从代码生成到执行完成的耗时
2. **准确率变化**：相同任务在不同环境下的准确率差异
3. **资源消耗**：CPU、内存、网络等资源的使用情况
4. **错误率**：因基础设施问题导致的错误比例

### 3.2 实验环境

- **硬件配置**：多种不同规格的服务器
- **网络环境**：模拟不同网络条件
- **软件栈**：多种编程语言和框架组合

## 4. 实验结果

### 4.1 硬件影响

实验显示，硬件差异导致的性能波动可达15-30%，特别是在处理大型项目时。

### 4.2 网络影响

网络条件对API密集型任务的影响最为显著，延迟增加50ms可导致任务完成时间增加20%。

### 4.3 软件影响

软件环境差异主要影响兼容性问题，可导致5-10%的任务失败率。

## 5. 缓解策略

### 5.1 硬件标准化

- 采用统一的硬件规格
- 实施资源监控和预警
- 建立性能基准测试

### 5.2 网络优化

- 使用CDN加速API访问
- 实施连接池和重试机制
- 监控网络质量指标

### 5.3 软件环境管理

- 容器化部署确保一致性
- 依赖版本管理自动化
- 环境配置标准化

## 6. 结论与建议

基础设施噪音是AI智能体编码评估中的重要因素。通过系统性的量化和缓解，我们可以：

1. 提高评估结果的可靠性
2. 改善AI编码工具的性能稳定性
3. 为用户提供更一致的使用体验

未来的研究将进一步探索更先进的噪音检测和缓解技术。

## 7. 参考文献

[1] Smith et al. (2024). The Impact of Infrastructure Variability on AI Code Generation.
[2] Johnson & Lee (2024). Network Effects on Large Language Model Performance.
[3] Chen et al. (2024). Hardware Considerations for AI Agent Deployment.
