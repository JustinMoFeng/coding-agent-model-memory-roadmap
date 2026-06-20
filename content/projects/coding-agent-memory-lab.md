# 项目：Coding Agent Memory Lab

## 目的

构建一个研究 Coding Agent 长期 memory 的受控环境。

核心问题：

> 什么 memory 会帮助 Coding Agent，什么时候会伤害它，以及能否通过训练让模型更好地使用 memory？

## 建议仓库结构

```text
coding-agent-memory-lab/
├── README.md
├── memory/
│   ├── schema.py
│   ├── store.py
│   ├── writer.py
│   ├── retriever.py
│   └── updater.py
├── agent/
│   ├── loop.py
│   ├── prompts/
│   └── tools.py
├── tasks/
│   ├── useful_memory/
│   ├── irrelevant_memory/
│   ├── stale_memory/
│   ├── conflicting_memory/
│   └── corrected_memory/
├── eval/
│   ├── run_eval.py
│   ├── metrics.py
│   └── failure_taxonomy.md
├── data/
│   ├── memories/
│   └── trajectories/
└── reports/
```

## Memory Schema

每条 memory 包含：

- `memory_id`
- `type`: repo, user, task, bug
- `content`
- `source`
- `evidence`
- `confidence`
- `created_at`
- `updated_at`
- `expires_at`
- `status`: active, stale, corrected, deleted
- `tags`

## 第一版

先构建最简单但有用的系统：

- JSON 或 SQLite memory store。
- Structured write API。
- Hybrid retrieval 可选，第一版可以先用简单 filter 和 keyword search。
- Agent 在 planning 前检索 memory。
- Agent 在任务完成后写入 memory。
- Eval 比较 no-memory 和 memory-enabled 两种模式。

## Evaluation Design

### Baselines

- No memory。
- Naive memory：retrieve top-k text memories。
- Structured memory：按 type、recency、confidence 和 task relevance 检索。

### Task Types

Useful memory：

- 正确 memory 应该提升成功率。

Irrelevant memory：

- Agent 应该忽略不适用的 memory。

Stale memory：

- Agent 应该在使用旧 memory 前验证。

Conflicting memory：

- Agent 应该用当前 repo evidence 解决冲突。

Corrected memory：

- Agent 应该在未来 session 中遵守用户纠正。

## Metrics

从这些指标开始：

- Task success rate。
- Correct memory retrieval rate。
- Harmful memory use rate。
- Stale memory verification rate。
- User correction adherence。
- Repeated mistake rate。

定性分析：

- Memory 是否改变了 plan？
- Memory 是否造成错误自信？
- Agent 是否用当前文件验证 memory？
- 任务完成后是否写入了有用的新 memory？

## 和训练的连接

Memory lab 应该给 Agent training lab 产出训练数据。

### SFT Data

Demonstrations 中 agent 应该：

- 检索相关 memory。
- 验证 memory。
- 在 plan 中使用 memory。
- 任务完成后更新 memory。

### DPO Data

Chosen：

- 有证据地使用相关 memory。

Rejected：

- 忽略相关 memory。
- 不验证就使用 stale memory。
- 跟随 irrelevant memory。

### GRPO/RLVR Data

Reward：

- Task success。
- 正确运行测试。
- 正确 memory update。
- 没有 harmful stale memory use。

## 第一批研究问题

- 哪些 memory 类型真的提升 Coding Agent 成功率？
- Structured memory 是否优于 naive retrieval？
- Stale memory 多大概率会伤害 agent？
- 模型能否被训练成使用 memory 前先验证？
- Preference data 能否减少 harmful memory use？

## 作品价值

这个项目应该展示：

- Research problem formulation。
- Agent system design。
- Memory evaluation design。
- 从 memory engineering 到 model post-training 的连接能力。

