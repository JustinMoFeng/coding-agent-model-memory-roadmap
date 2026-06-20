# 一年路线

## 总览

一年分成四个阶段。阶段不是严格课表，而是每个时期主要施加的学习压力。

```text
阶段 1：模型与后训练基础
阶段 2：Memory 问题定义
阶段 3：训练与评测闭环
阶段 4：研究沉淀与作品化
```

建议时间分配：

- 55% Agent 训练、post-training 和模型基础。
- 25% Coding Agent Memory。
- 15% 工程实现。
- 5% 学术写作和复盘。

写作占比看起来小，但必须每周做。

## 阶段 1：模型与后训练基础

时间：2-3 个月。

目标：

> 建立足够的模型侧理解，能判断数据、目标函数和 reward 如何塑造模型行为。

重点主题：

- Decoder-only Transformer。
- Tokenization 与 causal language modeling。
- 训练数据质量和 scaling intuition。
- SFT 与 instruction tuning。
- Preference optimization：DPO、IPO/KTO 类思想、reward modeling。
- RLHF 与 RLVR/GRPO 的概念和实践。
- 推理基础：KV cache、batching、vLLM/SGLang 式 serving。

实践产出：

- 一个小型 language model 训练 notebook 或脚本。
- 一个 toy SFT 实验。
- 一个 toy DPO 或 GRPO 实验。
- 一篇短报告：从 Coding Agent 行为角度比较 SFT、DPO 和 GRPO。

阶段退出标准：

- 能解释 SFT、DPO、RLHF、RLVR 分别在优化什么。
- 能读 post-training 论文并识别其中的数据、目标函数、reward 和 eval。
- 能跑一个最小训练任务并检查 loss、sample 和 failure case。
- 能判断一个行为问题应该由数据、reward、系统 prompt 还是 memory 处理。

## 阶段 2：Memory 问题定义

时间：2-3 个月。

目标：

> 把 Coding Agent Memory 从宽泛兴趣变成具体机制和可评测任务。

重点主题：

- Short-term、episodic、semantic、procedural memory。
- Repo memory：项目结构、模块职责、代码规范、测试命令。
- User memory：偏好、风格、约束、历史反馈。
- Task memory：当前目标、尝试过的修复、失败命令、中间发现。
- Bug memory：历史 bug 模式、回归风险、之前的修复方式。
- Write policy：什么时候写，写什么。
- Retrieval policy：query 构造、排序、recency、confidence、grounding。
- Update 和 forgetting：冲突解决、过期、纠错、删除。

实践产出：

- 一份 Coding Agent Memory taxonomy。
- 一个最小跨 session Coding Agent Memory 原型。
- 一个 memory eval set，覆盖 useful、irrelevant、stale、conflicting memory。
- 一份 memory-related Coding Agent failure taxonomy。

阶段退出标准：

- 能区分 RAG、context management 和 long-term memory。
- 能定义 memory 成功和失败案例。
- 能构造 memory 必要而不是装饰性的任务。
- 能用 eval 而不是 anecdotes 判断 memory 是否有帮助。

## 阶段 3：训练与评测闭环

时间：3 个月。

目标：

> 把 memory 行为连接到 post-training 数据、reward 和 eval。

重点主题：

- 面向 Coding Agent Memory 的合成任务构造。
- 有 memory / 无 memory 的 trajectory 收集。
- Memory 使用的正负样本。
- Agent trajectory 的 SFT 数据格式。
- Memory-aware action 的 preference pair。
- Coding task 的 verifiable reward。
- Eval design、污染检查和 ablation。

实践产出：

- 一批 memory-dependent coding-agent tasks。
- 一套 trajectory schema。
- 一个无 memory baseline agent。
- 一个 memory-enabled agent。
- 一个围绕 memory-use trajectory 的 SFT 或 DPO 小实验。
- 一份 eval report，至少包含：
  - no memory
  - retrieved memory only
  - structured memory
  - trained memory-use behavior

阶段退出标准：

- 至少展示一个可测的行为提升。
- 能解释收益来自 retrieval、training、prompting 还是数据变简单。
- 能指出 memory 伤害表现的失败案例。
- 能写出包含表格、例子和 limitation 的实验报告。

## 阶段 4：研究沉淀与作品化

时间：3-4 个月。

目标：

> 把前面的工程和实验整理成完整研究 artifact 和职业作品集。

重点主题：

- Related work 组织。
- Problem statement 和 contribution framing。
- Method 描述。
- Experiment protocol。
- Ablation 和 failure analysis。
- Reproducibility 和 open-source presentation。

实践产出：

- 一个 polished GitHub repository。
- 一篇 paper-style technical report。
- 一个简洁的项目 README 或 project page。
- 一份 slide deck，解释 motivation、method 和 results。
- 可选：workshop paper 或内部分享。

阶段退出标准：

- 能用 3 分钟、15 分钟和论文形式讲清项目。
- 能 defend eval design。
- 能解释哪些方法没用，以及为什么。
- 能提出下一步研究问题。

## 每周操作系统

每周要形成一个小闭环：

```text
read -> implement -> evaluate -> write -> refine
```

建议节奏：

- 2 次：模型 / post-training。
- 1 次：Memory 论文或系统设计。
- 2 次：工程实验。
- 1 次：写作和复盘。
- 1 次：休息、补缺或深入 debug。

每周交付物：

- 一篇 paper note。
- 一个工程 commit 或可运行实验。
- 一份 experiment log 或 research log。

## 月度复盘

每月底回答：

- 哪个模型侧概念更清楚了？
- 哪个 Memory 问题更具体了？
- 哪个工程 artifact 已经能跑了？
- 什么失败了，原因是什么？
- 哪条线应该从计划里删掉？
- 下一个最小可产生证据的实验是什么？

