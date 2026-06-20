# Memory 路线总览

## 目标

Memory 线的目标是：

> 构建面向 Coding Agent 的长期记忆问题定义、系统原型和评测方法。

这不是普通 RAG demo，而是要回答：

- Agent 应该记住什么？
- 什么时候写入 memory？
- 如何检索、更新、遗忘？
- 如何处理冲突、过期和错误 memory？
- 如何证明 memory 真的改善了长期任务表现？

## Memory 类型

### Episodic Memory

事件型记忆，记录发生过什么。

在 Coding Agent 中包括：

- issue
- comment thread
- task run
- run messages
- commit / PR
- test failure
- debug trajectory

### Semantic Memory

语义型记忆，记录稳定知识。

在 Coding Agent 中包括：

- repo structure
- module responsibility
- API contract
- coding convention
- test command
- bug pattern
- user preference

### Procedural Memory

过程型记忆，记录怎么做。

在 Coding Agent 中包括：

- reusable skill
- fix workflow
- test workflow
- deployment workflow
- review checklist

## 近期主线

第一阶段先调研 Multica。

重点看：

- task lifecycle 如何形成 episodic memory。
- issue metadata 如何作为 structured task memory。
- execution history 如何支持回溯和经验提取。
- skill 如何接近 semantic/procedural memory。

详细调研路径见 [Multica Memory 调研指南](../topics/multica-memory-reading-guide.md)。

## 后续产出

- Coding Agent Memory taxonomy。
- Memory schema v1。
- Memory eval set。
- Multica / OpenCode / 其他框架的可插拔 memory layer 设计。
- Memory-aware coding-agent eval report。
