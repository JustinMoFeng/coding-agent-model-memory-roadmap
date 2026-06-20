# 总体定位

## 一年主线

建议的一年定位是：

> 面向长程 Coding Agent 的 post-training 与 data-centric modeling，重点研究 memory 如何变成可训练、可控制、可评测的模型能力。

这条线同时满足三个约束：

- 当前工作：你在 Trae 做 Coding 后训练和数据合成。
- 未来目标：你希望继续往模型方向深耕。
- 研究背景：Memory 是研究生阶段方向，不能放掉，而且要早点开始。

关键不是把“模型学习”和“Memory 学习”拆成两门互不相关的课，而是让 Memory 成为你训练模型能力的研究场景。

## 核心押注

未来最值得积累的能力是：

> 给定一个真实 Coding Agent 失败案例，能把它转化成数据、reward、eval 和 post-training 实验。

这要求你逐步建立判断力：

- 哪些失败是模型行为问题。
- 哪些失败是系统、工具或上下文问题。
- 哪些失败可以通过更好的数据解决。
- 哪些失败需要更好的 reward 或 eval。
- 哪些失败暴露了 memory 机制缺失。

## 两条工程线

### A 线：Agent 训练 / AI Infra

这条线服务模型能力。

核心问题：

> 如何收集、过滤、训练和评测 Coding Agent 的任务轨迹？

需要积累的能力：

- 数据合成。
- Rollout 收集。
- SFT、DPO、GRPO/RLVR。
- Reward design。
- Evaluation 和 ablation。
- Serving 与 rollout infra。

这条线会逐步接触 AI Infra，但边界要清楚：你要学的是 post-training infra，不是泛泛学云原生、K8s、CUDA 或分布式系统。

### B 线：Coding Agent Memory

这条线服务研究深度。

核心问题：

> Coding Agent 在长期项目中应该记住什么，以及如何证明这些记忆真的有帮助？

需要积累的能力：

- Memory taxonomy。
- Write / retrieve / update / forget policy。
- 冲突、过期、纠错和隐私处理。
- Memory-specific benchmark。
- 长程 Agent 行为分析。

## 汇合问题

两条线最终要汇合到这里：

> Post-training 能否提升 Coding Agent 使用长期 memory 的能力？

可以拆成更具体的问题：

- 能否构造 memory 必要且可测的 Coding Agent 任务？
- 能否合成关于 memory 使用的正负轨迹？
- SFT 能不能教会模型显式使用 memory？
- DPO 能不能让模型偏好 memory-grounded actions？
- GRPO/RLVR 能不能在可验证任务上优化 memory 使用？
- 错误 memory、过期 memory、冲突 memory 会如何影响模型行为？

## 暂时不要优化的方向

避免同时追太多东西：

- 不要一开始横向比较所有 Agent 框架。
- 不要从大规模预训练开始。
- 不要过早深挖 CUDA、Triton、Kubernetes 或复杂分布式训练。
- 不要搭一个普通 RAG demo 就把它当成 Memory 研究。
- 不要只读论文而不连接到数据、reward、eval 或 memory 行为。

## 一句话身份

> 我做 Coding Agent 的 post-training 和训练数据闭环，重点研究长期 memory 如何转化为可训练、可控制、可评测的模型能力。

