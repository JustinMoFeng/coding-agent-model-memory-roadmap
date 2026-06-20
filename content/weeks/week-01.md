# Week 01：启动周 - LM 基础与 Multica Memory 调研

时间建议：2026-06-22 至 2026-06-28。

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

本周做到：能解释 tokenizer、causal LM loss、generation 和 SFT data format 的关系，并能把一个简化 coding-agent trajectory 改写成 SFT 样本。完整 A 线学习主线见 [大模型 / 后训练学习主线](../docs/07-model-learning-path.md)。

### B 线要学什么

围绕 Multica 做第一轮代码和产品调研。重点不是全仓库通读，而是识别其中哪些机制已经像 long-term memory，尤其是 task run、issue metadata、execution history 和 skills。

主要材料：

- Multica `README.zh-CN.md` / `README.md`。
- `CLI_AND_DAEMON.md` 中 issue、comment、metadata、execution history 相关部分。
- `server/internal/daemon/prompt.go`。
- `server/internal/service/task.go`。
- `server/internal/handler/issue_metadata.go`。
- skill 相关代码。

本周做到：能说明 Multica 的核心对象和 task lifecycle，并能把 issue、comment、task run、metadata、skill 映射到 episodic / semantic / procedural memory。详细 Multica 调研路径见 [Multica Memory 调研指南](../topics/multica-memory-reading-guide.md)。

### 本周不做什么

- 不做完整 MemoryAgent 实现。
- 不做 DPO/GRPO 推导。
- 不做 Multica 全量架构 review。
- 不从零训练模型。
- 不深入 Transformer 公式和分布式训练。

## 2. 每日安排

### Day 1：建立主线

A 线：

- 看 CS336 课程主页，重点关注 tokenizer / language modeling intro 的课程位置。
- 阅读 [大模型 / 后训练学习主线](../docs/07-model-learning-path.md) 的 M1-M2。
- 写下 pretraining、SFT、DPO、RLVR 的一句话区别。

B 线：

- 读 Multica 的 `README.zh-CN.md` 和 `README.md`。
- 画出核心对象关系：workspace、agent、issue、comment、task、runtime、daemon、skill、squad、autopilot。

产出：

- `notes/week-01-lm-foundation.md` 初稿。
- Multica 核心对象关系图或文字版对象表。

### Day 2：Tokenizer 和数据形态

A 线：

- 看 Hugging Face LLM Course 的 tokenizer 相关内容。
- 用 `AutoTokenizer` 对中文、代码、diff/error log 做 encode/decode。
- 记录 tokenization 对 Coding Agent 的影响。

B 线：

- 读 `CLI_AND_DAEMON.md` 中 issue、comment、metadata、execution history 相关部分。
- 整理 Multica CLI 中和 memory-like state 有关的命令。

产出：

- 5 条 tokenizer 观察。
- 一份 Multica CLI memory-like 命令清单。

### Day 3：Causal LM 和 SFT 数据格式

A 线：

- 看 Hugging Face Transformers 的 Causal Language Modeling 文档。
- 搞清楚 `input_ids`、`labels`、`attention_mask` 和 causal LM loss。
- 看 TRL SFTTrainer / dataset formats，理解 prompt-completion 和 conversational dataset。

B 线：

- 读 `server/internal/daemon/prompt.go`。
- 总结 assignment task、comment-triggered task、chat task、autopilot task 的 prompt 差异。

产出：

- 一个最小 causal LM 例子：输入、label、loss 分别是什么。
- 一个 coding-agent trajectory 改写成 SFT 样本的例子。
- 一段 Multica prompt construction 总结。

### Day 4：Generation、Rollout 与 Task Lifecycle

A 线：

- 学习 greedy decoding、sampling、temperature、top-p 的基本区别。
- 思考为什么 rollout/eval 要固定 generation 参数。

B 线：

- 读 `server/internal/service/task.go` 和 `server/internal/handler/task_lifecycle.go`。
- 梳理 task 从 queued 到 started/completed/failed/cancelled 的生命周期。

产出：

- 一段说明：generation 参数如何影响 Coding Agent eval。
- 一个 task lifecycle 图。
- 一段说明：为什么 task run 是 episodic memory。

### Day 5：Issue Metadata 和 Memory 粒度

A 线：

- 思考 task-scoped memory 如何变成 SFT 数据。
- 写 3 个可能的 SFT/DPO 样本想法，不要求训练。

B 线：

- 读 `server/internal/handler/issue_metadata.go`。
- 对照 `CLI_AND_DAEMON.md` 的 Metadata 规则。
- 判断 issue metadata 适合存什么、不适合存什么。

产出：

- 一页 issue metadata 分析。
- 一页如果扩展成长期 memory，需要补哪些字段。

### Day 6：Skills 和 Semantic / Procedural Memory

A 线：

- 复盘 `token -> LM loss -> SFT data`。
- 写一个“episodic event 如何变成 semantic/procedural memory，再变成训练数据”的例子。

B 线：

- 读 skill 相关代码：
  - `server/internal/handler/skill.go`
  - `server/internal/handler/runtime_local_skills.go`
  - `server/internal/daemon/local_skills.go`
- 判断 Multica skill 和 semantic/procedural memory 的关系。

产出：

- 一页 skill 与 memory 的边界分析。
- 一页 episodic memory 与 semantic memory 在 Coding Agent 中的区别。

### Day 7：整合和对齐材料

A 线：

- 整理本周模型线笔记。
- 确认自己能解释 tokenizer、causal LM loss、SFT data 三者关系。

B 线：

- 整理 Multica 调研结论。
- 写一个可以和老师/师兄对齐的短版总结。

产出：

- `logs/week-01-review.md`。
- 一份 5 点短版调研结论：
  - 我对 Multica 的理解。
  - 它已有的 memory-like 机制。
  - Episodic memory 和 semantic memory 的映射。
  - 如果做可插拔 Coding Agent 长期记忆系统，第一版建议做什么。
  - 下周继续调研的问题。

## 3. 每周交付

本周至少交付这些文件：

```text
notes/week-01-lm-foundation.md
notes/week-01-multica-code-reading.md
notes/week-01-episodic-semantic-memory.md
logs/week-01-review.md
```

其中 `week-01-lm-foundation.md` 至少包含：

- Tokenizer 对中文、代码、diff/error log 的 5 条观察。
- 一个 causal LM 输入、label、loss 的最小例子。
- 一个 coding-agent trajectory 改写成 SFT 样本的例子。

`week-01-multica-code-reading.md` 至少包含：

- Multica 核心对象图。
- Task lifecycle 图。
- Issue metadata 分析。
- Skill 和 memory 的关系。

`week-01-episodic-semantic-memory.md` 至少包含：

- Episodic memory 在 Coding Agent 中对应什么。
- Semantic memory 在 Coding Agent 中对应什么。
- Multica 机制到 memory 类型的映射表。

## 4. 本周在整体路线中的作用

这是启动周，作用是把两条线接到同一个问题上：Coding Agent 的行为如何被上下文、memory、数据和后训练共同塑造。

A 线本周只学最小模型基础，是为了后面进入 SFT、DPO、GRPO 时不漂浮。你需要先理解语言模型的训练目标，才能理解为什么 trajectory、preference pair 和 verifiable reward 可以改变 agent 行为。

B 线本周选择 Multica，是因为它已经把 issue、task、runtime、execution history 和 skill 组织成了一个 agent 工作系统。这个系统天然适合用来思考 long-term memory：哪些是事件型记忆，哪些是结构化状态，哪些是沉淀后的技能。

本周完成后，第二周可以自然进入两件事：A 线学习 Transformer block / attention 的基本结构；B 线开始设计 Coding Agent Memory 的第一版 schema，包括 episodic event、semantic fact、procedural skill、source/evidence/confidence 和 expiry/status。
