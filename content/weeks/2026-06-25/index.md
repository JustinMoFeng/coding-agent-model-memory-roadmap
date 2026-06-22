# 2026-06-25 至 2026-06-28：启动周 - LM 基础与 Multica Memory 调研

时间建议：2026-06-25 至 2026-06-28。

说明：2026-06-22 至 2026-06-24 是期末复习与考试时间，不纳入本周学习计划。第一周只安排周四、周五、周六、周日四天，目标是轻启动，不追求一次性塞满。

## 1. 介绍

### 简单介绍

这一周是启动周，目标不是大量推进，而是建立后续三个月到一年路线的共同语言。核心是把模型后训练和 Coding Agent Memory 放到同一个问题里：Agent 的行为如何被 token、上下文、memory、数据和训练目标共同塑造。

本周用一条很小的模型链路和一个具体工程系统开局：A 线打通 `token -> causal LM loss -> SFT data`，B 线调研 Multica 如何管理 issue、task、metadata、execution history 和 skills。

### A 线要学什么

从 post-training 的视角理解 decoder-only LM。重点不是完整推导 Transformer，而是明白语言模型如何通过 next-token prediction 学习行为，以及为什么 coding-agent trajectory 可以变成训练数据。

主要材料：

- CS336 的 tokenizer / language modeling intro。
- Hugging Face LLM Course 的 tokenizer 内容。
- Hugging Face Transformers 的 causal language modeling 文档。
- TRL SFTTrainer / dataset formats 文档。

本周做到：能解释 tokenizer、causal LM loss、generation 和 SFT data format 的关系，并能把一个简化 coding-agent trajectory 改写成 SFT 样本。完整 A 线学习主线见 [大模型 / 后训练学习主线](../../archive/07-model-learning-path.md)。

### B 线要学什么

围绕 Multica 做第一轮代码和产品调研。重点不是全仓库通读，而是识别其中哪些机制已经像 long-term memory，尤其是 task run、issue metadata、execution history 和 skills。

主要材料：

- Multica `README.zh-CN.md` / `README.md`。
- `CLI_AND_DAEMON.md` 中 issue、comment、metadata、execution history 相关部分。
- `server/internal/daemon/prompt.go`。
- `server/internal/service/task.go`。
- `server/internal/handler/issue_metadata.go`。
- skill 相关代码。

本周做到：能说明 Multica 的核心对象和 task lifecycle，并能把 issue、comment、task run、metadata、skill 映射到 episodic / semantic / procedural memory。详细 Multica 调研路径见 [Multica Memory 调研指南](../../topics/multica-memory-reading-guide.md)。

### 本周不做什么

- 不做完整 MemoryAgent 实现。
- 不做 DPO/GRPO 推导。
- 不做 Multica 全量架构 review。
- 不从零训练模型。
- 不深入 Transformer 公式和分布式训练。

## 2. 每日安排

每日学习进度不要直接写在本页。本页只维护计划；每天完成后更新对应日期页：

- [2026-06-25](2026-06-25.md)
- [2026-06-26](2026-06-26.md)
- [2026-06-27](2026-06-27.md)
- [2026-06-28](2026-06-28.md)

| 日期 | A 线 | B 线 | 产出 |
|---|---|---|---|
| [2026-06-25](2026-06-25.md) | 建立模型后训练主线，理解 `token -> loss -> SFT data` | 读 Multica README，整理核心对象 | 主线笔记初稿；Multica 对象表 |
| [2026-06-26](2026-06-26.md) | Tokenizer 与 coding-agent 数据形态 | 读 issue/comment/metadata/execution history | tokenizer 观察；memory-like 命令清单 |
| [2026-06-27](2026-06-27.md) | Causal LM、SFT format、generation 参数 | 读 prompt construction 与 task lifecycle | SFT 样本例子；task lifecycle 图 |
| [2026-06-28](2026-06-28.md) | 整理最小模型链路 | 整理 episodic / semantic / procedural memory 映射 | 周复盘；给老师/师兄对齐的短版总结 |

## 3. 每周交付

本周至少交付这些文件：

```text
notes/2026-06-25-lm-foundation.md
notes/2026-06-25-multica-code-reading.md
notes/2026-06-25-episodic-semantic-memory.md
logs/2026-06-25-weekly-review.md
```

其中 `2026-06-25-lm-foundation.md` 至少包含：

- Tokenizer 对中文、代码、diff/error log 的 5 条观察。
- 一个 causal LM 输入、label、loss 的最小例子。
- 一个 coding-agent trajectory 改写成 SFT 样本的例子。

`2026-06-25-multica-code-reading.md` 至少包含：

- Multica 核心对象图。
- Task lifecycle 图。
- Issue metadata 分析。
- Skill 和 memory 的关系。

`2026-06-25-episodic-semantic-memory.md` 至少包含：

- Episodic memory 在 Coding Agent 中对应什么。
- Semantic memory 在 Coding Agent 中对应什么。
- Multica 机制到 memory 类型的映射表。

## 4. 本周在整体路线中的作用

这是启动周，作用是把两条线接到同一个问题上：Coding Agent 的行为如何被上下文、memory、数据和后训练共同塑造。

A 线本周只学最小模型基础，是为了后面进入 SFT、DPO、GRPO 时不漂浮。你需要先理解语言模型的训练目标，才能理解为什么 trajectory、preference pair 和 verifiable reward 可以改变 agent 行为。

B 线本周选择 Multica，是因为它已经把 issue、task、runtime、execution history 和 skill 组织成了一个 agent 工作系统。这个系统天然适合用来思考 long-term memory：哪些是事件型记忆，哪些是结构化状态，哪些是沉淀后的技能。

本周完成后，第二周可以自然进入两件事：A 线学习 Transformer block / attention 的基本结构；B 线开始设计 Coding Agent Memory 的第一版 schema，包括 episodic event、semantic fact、procedural skill、source/evidence/confidence 和 expiry/status。
