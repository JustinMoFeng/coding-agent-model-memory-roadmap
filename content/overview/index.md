# 路线总览

这个系统服务一条主线：

> 以模型后训练为主线，以 Coding Agent Memory 为研究问题，以 Coding Agent 为工程落地场景。

未来一年最重要的能力不是“学完所有 AI”，而是：

> 能把真实 Coding Agent 的失败转化成数据、reward、eval 和 post-training 实验。

## 要学什么

整体分成三块。

### 1. Agent Training / 模型后训练

目标是理解模型行为如何被数据和目标函数塑造。

重点包括：

- Tokenizer、causal LM、decoder-only Transformer。
- SFT、DPO、GRPO/RLVR。
- Coding task 数据合成。
- Rollout、reward、eval、failure analysis。
- Post-training infra：serving、batch rollout、日志、数据版本。

详情见 [Agent Training 路线纵览](agent-training.md)。

### 2. Coding Agent Memory

目标是把研究生阶段的 Memory 方向落到 Coding Agent 场景里。

重点包括：

- Episodic memory：issue、commit、task run、debug trajectory。
- Semantic memory：repo structure、module responsibility、coding convention。
- Procedural memory：可复用 workflow、skill、test/fix pattern。
- Memory 写入、检索、更新、遗忘和冲突处理。
- Memory-specific eval。

详情见 [Memory 路线总览](memory.md)。

### 3. 科研与工程能力

目标是同步提升读论文、写论文、做工程和做实验的能力。

重点包括：

- 论文卡片。
- 实验日志。
- 周计划和每日进度。
- 技术报告和 paper-style draft。
- 小实验代码和成熟项目 repo 的组织方式。

详情见 [科研能力提升](research-skill.md)。

## 当前执行入口

- [2026-06-22 至 2026-06-28 周计划](../weeks/2026-06-22/index.md)
- [Multica Memory 调研指南](../topics/multica-memory-reading-guide.md)
- [周计划模板](../reference/templates/week-plan-template.md)
- [每日进度模板](../reference/templates/daily-log-template.md)

## 维护原则

- 周计划只写计划，不写每日流水。
- 每日进度写到当周目录下的日期页。
- 专题细节单独放到 `topics/`。
- 小实验代码放 `labs/`。
- 成熟项目单独建 GitHub repo，并在这里写项目说明和实验报告。
