# 论文阅读系统

## 原则

论文不是为了“读过”，而是为了服务研究问题。

这条路线默认的阅读问题是：

> 这篇论文对 Coding Agent 的数据、训练目标、reward、eval 或 memory 行为有什么启发？

不要写被动 summary。每篇笔记都必须包含自己的判断。

## 阅读层级

### Level 1：快速筛选

时间：15-20 分钟。

读：

- Abstract。
- Introduction。
- Figure 1 或 method overview。
- Main result table。
- Limitations。

判断：

- 是否必须精读。
- 是否作为参考保留。
- 是否暂时跳过。

### Level 2：工作阅读

时间：60-90 分钟。

提取：

- Problem。
- Method。
- Data。
- Training objective。
- Evaluation。
- Baselines。
- Limitations。
- 和自己方向的关系。

产出：

- 使用 `reference/templates/paper-note.md` 写一篇 paper note。

### Level 3：复现阅读

时间：多个 session。

只对可能影响你项目的论文做这一级。

提取：

- 具体数据构造方式。
- Model 和 training details。
- Prompt 或 trajectory format。
- Evaluation protocol。
- Ablations。
- Implementation assumptions。

产出：

- 复现计划。
- 最小实验。
- Failure analysis。

## 论文类别

### Model / Post-Training

目的：

- 理解模型行为如何被数据和目标函数塑造。

问题：

- Objective 在奖励什么行为？
- 数据格式是什么？
- 方法针对什么 failure？
- Eval 如何证明行为改变了？

### Coding Agents

目的：

- 理解软件工程任务、benchmark 和 agent loop。

问题：

- Benchmark 实际测的是什么？
- Reward 是否可执行？
- 任务是真实的还是合成的？
- 常见 failure modes 是什么？

### Memory / Long Context

目的：

- 理解长期状态、检索、更新和遗忘。

问题：

- 论文里把什么称为 memory？
- Memory 是 external、parametric 还是 context-based？
- Memory 如何写入和检索？
- 是否有真实 memory evaluation？

### AI Infra / Serving

目的：

- 理解足够的系统知识，支撑 post-training 和 rollout。

问题：

- 它解决了什么瓶颈？
- 这个瓶颈对 rollout、training 还是 inference 重要？
- 工具暴露了什么抽象？
- 什么情况下你自己的实验会需要它？

## 每周论文目标

最低要求：

- 每周 1 篇 serious paper note。

更好：

- 1 篇 serious note。
- 2 篇 triage notes。

不要优化论文数量。优化可复用的观点和实验想法。

## 弱笔记信号

如果一篇笔记只是在写：

- “这篇论文提出……”
- “方法提升了……”
- “实验表明……”

那它通常不够有用。

好的笔记应该写：

- “这篇对我有用的是……”
- “这个 eval 的问题是……”
- “这个数据构造可以迁移到……”
- “对 Coding Agent Memory 来说，主要限制是……”
- “最小复现实验可以是……”
