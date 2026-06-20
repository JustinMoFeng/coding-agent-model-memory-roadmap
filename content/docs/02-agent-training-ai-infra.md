# 工程线 A：Agent 训练与 AI Infra

## 目标

建立运行和分析 Coding Agent post-training 闭环的能力。

目标闭环：

```text
task source -> data synthesis -> rollout -> reward/eval -> training -> analysis -> improved data
```

这条线会逐渐靠近 AI Infra，但边界要清楚：

> 只学习直接服务 post-training、rollout、reward 和 eval 的基础设施。不要过早进入泛 infra。

## 核心能力

### 1. Coding Task 数据合成

学习从这些来源构造任务：

- Issue。
- Pull request。
- Commit。
- Test failure。
- Code review comment。
- 文档变化。
- Synthetic bug injection。

关键问题：

- 输入上下文是什么？
- 期望输出是什么？
- 任务是否可验证？
- 数据要针对什么 failure mode？
- 任务需要 coding、reasoning、tool use 还是 memory？

预期产物：

- Task schema。
- 数据生成脚本。
- 去重和过滤 pipeline。
- 一批经过人工抽查的小数据集。

### 2. Agent Rollout 收集

学习让模型在真实 Coding Agent loop 中执行任务：

```text
observe repo -> inspect files -> edit -> run command -> read error -> revise -> submit patch
```

关键问题：

- 允许哪些 action？
- Tool call 如何表示？
- Observation 如何截断或总结？
- 命令失败如何进入下一步？
- Rollout 什么时候终止？

预期产物：

- 本地 sandbox runner。
- Trajectory schema。
- 成功和失败任务的 rollout logs。
- 基础指标：success rate、edit count、command count、runtime、failure reason。

### 3. Reward 和 Evaluation

Reward 来源：

- Unit tests。
- Static checks。
- Lint 或 type checks。
- Patch minimality。
- Human preference。
- 谨慎使用 LLM-as-judge。
- Trajectory quality signals。

关键问题：

- Reward 是否可验证？
- Reward 是否容易被 hack？
- 它衡量 final success 还是 process quality？
- 它是否只在 memory 有用时奖励 memory use？
- 是否有 held-out eval set？

预期产物：

- Eval runner。
- Reward function registry。
- Failure taxonomy。
- Evaluation report template。

### 4. 训练方法

从简单开始，逐步加深：

1. SFT on successful trajectories。
2. DPO on preferred vs rejected trajectories。
3. GRPO/RLVR for verifiable tasks。
4. 更复杂的 RLHF 只在前三步不够时再进入。

关键问题：

- 训练想改变什么行为？
- Baseline 是什么？
- Control group 是什么？
- 训练提升了真实任务成功率，还是只学会了输出格式？
- 提升能否跨 repo 和 task type 泛化？

预期产物：

- 最小 SFT training script。
- 最小 DPO training script。
- 最小 GRPO/RLVR experiment。
- 训练前后的行为对比。

### 5. Post-Training Infra

按需学习的基础设施：

- vLLM 或 SGLang：serving 和 rollout。
- TRL：SFT、DPO、GRPO 小实验。
- verl 或 OpenRLHF：更大规模 RLHF/RLVR workflow。
- Ray 或 multiprocessing：parallel rollout。
- Weights & Biases、TensorBoard 或本地 logging。
- Dataset versioning。
- Checkpoint 和 config management。

不要一开始就把 infra 做满。先让一个小闭环在本地跑通，再根据真实瓶颈加 infra。

## 里程碑

### A1：Toy Post-Training Loop

构建：

- 20-50 个 toy coding 或 reasoning tasks。
- SFT dataset。
- Tiny training run。
- Before/after eval。

成功标准：

- 闭环能端到端跑通。
- 结果被记录下来。
- 至少人工检查 10 个 failure cases。

### A2：Coding Rollout Runner

构建：

- 本地 repo task runner。
- Tool-call trajectory logging。
- Unit-test based reward。

成功标准：

- 同一任务可以在不同 model 或 prompt 设置下重复运行。
- 能比较 rollout 和 failure reason。

### A3：Preference Training

构建：

- Chosen/rejected trajectory pairs。
- DPO experiment。
- 用 task success 和 trajectory quality 评测。

成功标准：

- 能解释 DPO 后行为发生了什么变化。
- 能指出退化样例。

### A4：Verifiable Reward Training

构建：

- 一小批 executable reward tasks。
- GRPO/RLVR-style experiment。
- Reward hacking analysis。

成功标准：

- 能区分真实任务提升和 reward overfitting。

## 阅读优先级

读论文和文档是为了解决工程问题，不是收集名字。

优先主题：

- Instruction tuning 和 SFT。
- RLHF 和 reward modeling。
- DPO 和 preference optimization。
- RLVR 和 GRPO-style training。
- Coding-agent benchmark 和 synthetic data。
- Serving 和 rollout systems。

## 最终要展示的能力

这条线结束后，你应该能够：

- 设计 Coding Agent trajectory 的训练数据 schema。
- 运行一个小型 post-training 实验。
- 构建带 executable reward 的 eval set。
- 检查训练前后的模型行为变化。
- 解释扩大 rollout 和 training 所需要的 infra。

