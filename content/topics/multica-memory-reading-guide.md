# Multica Memory 调研指南

这个文档承接 Week 01 的 B 线，用于集中记录 Multica 和 Coding Agent Memory 相关的详细调研路径。

Week 01 的周计划只保留执行安排；Multica 的细节放在这里。

## 调研目标

搞清楚 Multica 作为 managed agents platform，已经如何管理：

- Agent 的工作上下文。
- Issue 和 comment 形成的协作轨迹。
- Task run 和 execution history。
- Issue metadata 这种结构化状态。
- Skill 这种可复用能力沉淀。

最终要判断：

> Multica 里哪些设计已经像 long-term memory？如果要做可插拔 Coding Agent 长期记忆系统，应该插在哪里？

## 第一层：产品与架构理解

先读：

- `README.zh-CN.md`
- `README.md`
- `CLI_AND_DAEMON.md`
- `AGENTS.md`
- `CLAUDE.md` 中和架构、命令、agent workflow 相关的部分

要整理：

- 核心对象：workspace、agent、issue、comment、task、runtime、daemon、skill、squad、autopilot。
- 一个 issue 被分配给 agent 后，系统如何触发执行。
- Daemon 和本地 agent CLI 的关系。
- 为什么它支持 Claude Code、Codex、OpenCode 等多种 provider。
- 它把 agent 当成“队友”而不是“聊天机器人”的设计含义。

## 第二层：重点代码阅读路径

本阶段只读这些，不做全仓库扫描：

```text
server/internal/daemon/prompt.go
server/internal/service/task.go
server/internal/handler/task_lifecycle.go
server/internal/handler/issue.go
server/internal/handler/issue_metadata.go
server/internal/handler/skill.go
server/internal/handler/runtime_local_skills.go
server/internal/daemon/local_skills.go
server/internal/daemon/execenv/
server/migrations/
```

## 重点问题 1：Task Lifecycle

看：

- `server/internal/service/task.go`
- `server/internal/handler/task_lifecycle.go`

要回答：

- Task 有哪些状态？
- 从 queued 到 dispatched/start/complete/fail 的流程是什么？
- 哪些事件会触发 task？
- 系统如何处理 lease、cancel、retry、expired？

Memory 视角：

- 每次 task run 都是一段 episodic memory。
- run 的输入、工具调用、输出、失败原因、状态变化都可以成为后续 agent 的经验。

## 重点问题 2：Prompt Construction

看：

- `server/internal/daemon/prompt.go`
- `server/internal/daemon/execenv/`

要回答：

- Multica 给 agent CLI 的初始 prompt 包含什么？
- Assignment task、comment-triggered task、chat task、autopilot task 的 prompt 有什么区别？
- Prompt 如何指导 agent 读取 issue、comment history、附件、reply？

Memory 视角：

- Prompt 是 short-term context 的入口。
- 如果做 long-term memory，需要判断是在 prompt 进入 agent 前注入，还是通过工具检索。

## 重点问题 3：Issue Metadata

看：

- `server/internal/handler/issue_metadata.go`
- `CLI_AND_DAEMON.md` 中 Metadata 部分
- 对应 migration 中 metadata 字段

要回答：

- Metadata 的 schema 约束是什么？
- 为什么它只允许 flat KV 和 primitive values？
- 为什么写入门槛很高？
- 为什么 single-key atomic mutation 很重要？
- 它适合存什么，不适合存什么？

Memory 视角：

- Issue metadata 很像 task-scoped structured memory。
- 它适合存 `pipeline_status`、`pr_number`、`waiting_on` 等可复用状态。
- 它不适合存大段日志、单次调查过程和未验证猜测。

## 重点问题 4：Execution History

看：

- `CLI_AND_DAEMON.md` 中 Execution History 部分。
- task / run messages 相关 handler 和 service。

要回答：

- Multica 如何查看一个 issue 的历史 run？
- `run-messages` 包含什么？
- 这些历史消息如何支持 agent resume 或人类回溯？

Memory 视角：

- Execution history 是天然 episodic memory。
- 问题是如何从长日志中提取可复用知识，而不是每次塞全文。

## 重点问题 5：Skills

看：

- `server/internal/handler/skill.go`
- `server/internal/handler/runtime_local_skills.go`
- `server/internal/daemon/local_skills.go`
- `server/internal/daemon/execenv/codex_user_skills.go`

要回答：

- Skill 在 Multica 中如何创建、导入、展示、注入？
- Skill 是 workspace-level、agent-level 还是 runtime-local？
- 为什么 README 说“每个解决方案都成为可复用 skill”？

Memory 视角：

- Skill 更接近 semantic / procedural memory。
- 它不是某次任务的事件，而是从事件中沉淀出的稳定知识或操作规程。

## Episodic vs Semantic Memory

### Episodic Memory

在 Coding Agent 中可以理解为：

- 某个 issue 的一次执行经历。
- 某次 debug 的命令、错误、尝试和结论。
- 某个 PR 的 review 和修复过程。
- 某次 agent 失败或成功的 trajectory。

典型对象：

- issue
- comment thread
- task run
- run messages
- commit
- PR
- test failure

关键问题：

- 如何记录上下文？
- 如何压缩成 summary？
- 如何按任务相似性检索？
- 如何避免把一次性经验当成永久规则？

### Semantic Memory

在 Coding Agent 中可以理解为：

- 项目结构知识。
- 模块职责。
- 架构约束。
- 代码规范。
- 测试方式。
- 常见 bug 模式。
- 团队偏好。
- 抽象概念和逻辑关系。

典型对象：

- repo map
- module responsibility
- coding convention
- test command
- API contract
- reusable skill
- knowledge graph

关键问题：

- 如何从 episodic memory 中抽取 semantic memory？
- 如何验证这条 semantic memory 仍然正确？
- 如何处理冲突、过期和用户纠正？

## 初步映射表

| Multica 机制 | Memory 类型 | 粒度 | 是否可复用 | 风险 |
|---|---|---|---|---|
| Issue | episodic/task memory | task | 中 | 描述可能过时 |
| Comment thread | episodic/social memory | conversation | 中 | 噪声多 |
| Task run | episodic memory | execution | 高 | 日志长 |
| Issue metadata | structured task memory | key-value | 高 | 容量小、表达弱 |
| Skill | semantic/procedural memory | reusable knowledge | 高 | 可能过度泛化 |
| Squad instructions | semantic/procedural memory | routing rule | 高 | 路由规则过时 |
| Autopilot | procedural memory | recurring workflow | 高 | 自动化误触发 |

