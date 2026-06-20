# 项目：Agent Training Lab

## 目的

构建一个小而真实的 Coding Agent post-training 闭环。

目标不是训练出很强的模型，而是理解完整流程：

```text
data -> rollout -> reward -> train -> eval -> analysis
```

## 建议仓库结构

```text
agent-training-lab/
├── README.md
├── configs/
├── data/
│   ├── raw/
│   ├── processed/
│   └── schemas/
├── rollout/
│   ├── runner.py
│   ├── sandbox.py
│   └── trajectory.py
├── reward/
│   ├── tests.py
│   ├── patch_quality.py
│   └── registry.py
├── train/
│   ├── sft.py
│   ├── dpo.py
│   └── grpo.py
├── eval/
│   ├── run_eval.py
│   ├── metrics.py
│   └── failure_taxonomy.md
├── analysis/
└── reports/
```

## 第一版

第一版保持很小：

- 20-50 个任务。
- 一个模型。
- 一个 baseline prompt。
- 一个 SFT run。
- 一个 eval script。
- 一份 report。

## Task Schema

每个任务包含：

- `task_id`
- `repo`
- `instruction`
- `initial_state`
- `allowed_tools`
- `expected_tests`
- `success_criteria`
- `metadata`

## Trajectory Schema

每条 trajectory 包含：

- `task_id`
- `model`
- `prompt_version`
- `steps`
- `tool_calls`
- `observations`
- `patch`
- `final_status`
- `reward`
- `failure_category`

## Evaluation Metrics

从这些指标开始：

- Task success rate。
- Test pass rate。
- Number of edits。
- Number of commands。
- Runtime。
- Failure category distribution。

之后再加：

- Patch minimality。
- Regression risk。
- Memory-use correctness。
- Human preference。

## 第一批实验

### 实验 1：SFT on Successful Trajectories

问题：

> 对成功 Coding Agent trajectory 做 SFT，会提升任务成功率，还是只是在模仿格式？

Control：

- Base model with same prompt。

Evaluation：

- Held-out task success。
- Failure categories。
- 人工 review 10 个样例。

### 实验 2：DPO on Better vs Worse Trajectories

问题：

> Preference training 能否减少可避免的 Coding Agent 错误？

Chosen examples：

- 正确定位文件。
- 运行相关测试。
- Patch 最小。
- 利用错误反馈。

Rejected examples：

- 修改无关文件。
- 忽略测试失败。
- 重复失败命令。
- 给出无依据修复。

### 实验 3：Verifiable Reward

问题：

> Executable reward 能否改善小型 Coding Agent 任务表现？

Reward：

- Tests pass。
- 无无关文件修改。
- 可选 style checks。

风险：

- Reward hacking。
- 对简单测试过拟合。

## 作品价值

这个项目应该展示：

- Model / post-training 理解。
- 数据和 reward 设计能力。
- Eval discipline。
- Practical AI infra judgment。

