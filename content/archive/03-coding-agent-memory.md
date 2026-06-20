# 工程线 B：Coding Agent Memory

## 目标

构建一个具体、可评测的 Coding Agent Memory 系统。

目标闭环：

```text
interaction -> memory write -> memory organization -> retrieval -> action -> evaluation -> memory update
```

重点不是做一个通用 RAG app，而是研究长期 memory 如何影响 Coding Agent 的长期行为。

## Memory 类型

### 1. Repo Memory

Agent 应该记住的仓库信息：

- 项目结构。
- 模块职责。
- 常见入口。
- 测试命令。
- 构建命令。
- 代码规范。
- 依赖约束。
- 已知脆弱区域。

例子：

```text
这个 repo 的后端测试使用 `pytest tests/api`，前端测试使用 `pnpm test`。
```

### 2. User Memory

Agent 应该记住的用户信息：

- 偏好风格。
- Review 偏好。
- 输出格式要求。
- 风险偏好。
- 常见指令。
- 重复反馈。

例子：

```text
用户偏好简洁 final answer，并明确列出测试结果。
```

### 3. Task Memory

Agent 在长任务内和跨任务应该记住的信息：

- 当前目标。
- 已检查文件。
- 已尝试假设。
- 已运行命令。
- 已观察错误。
- 已尝试 patch。
- 之前尝试失败的原因。

例子：

```text
Import error 的原因是 package path resolution，不是缺少 dependency。
```

### 4. Bug Memory

Agent 应该记住的历史 bug 信息：

- 症状。
- 根因。
- 修复方式。
- 新增测试。
- 回归风险。
- 相似文件或模块。

例子：

```text
这个 repo 之前的 auth bug 经常来自 middleware 和 API route 之间 session cookie name 不一致。
```

## Memory 操作

### Write

关键问题：

- 什么应该被存储？
- 谁决定存储：用户、agent 还是规则？
- 这条 memory 是否有证据支撑？
- 它是稳定事实还是临时状态？
- 是否需要过期时间？

错误写入很危险。Memory 系统不能把猜测写成长期事实。

### Retrieve

关键问题：

- 使用什么 query？
- 检索应该用 text search、embedding、structured filters 还是 hybrid？
- Recency 是否重要？
- 是否展示 source evidence？
- 多少条 memory 进入 context？

检索好坏应该由是否帮助任务判断，而不是只看语义相似度。

### Update

关键问题：

- 新证据和旧 memory 冲突时怎么办？
- Memory 应该覆盖、版本化还是标记 stale？
- 用户能否纠正 memory？
- 系统能否解释为什么检索出某条 memory？

### Forget

关键问题：

- 哪些 memory 应该过期？
- 哪些 memory 太具体、敏感或低置信？
- 如何处理用户删除请求？
- 如何防止 stale memory 伤害任务成功率？

## 评测任务

Memory eval 要围绕 controlled contrasts 构建。

### Useful Memory

没有 memory 很难，有正确 memory 明显更容易。

例子：

- 用户之前说过 repo 使用非标准测试命令。
- Agent 必须修 bug 并运行正确测试。

指标：

- 有 memory 和无 memory 的 task success 对比。

### Irrelevant Memory

Memory 存在，但不应该影响当前任务。

例子：

- 修后端逻辑时检索到了旧的前端风格偏好。

指标：

- Irrelevant memory 是否导致干扰或错误修改。

### Stale Memory

Memory 以前正确，但现在错误。

例子：

- Repo 以前使用 Jest，现在迁移到了 Vitest。

指标：

- Agent 是否会根据当前文件验证 memory。

### Conflicting Memory

两条 memory 互相矛盾。

例子：

- 一条 memory 说用 `pnpm`，另一条说用 `npm`。

指标：

- Agent 是否先寻找证据再行动。

### Corrected Memory

用户纠正了某个长期偏好或 repo fact。

例子：

- 用户说：“以后不要再用旧测试命令。”

指标：

- 未来行为是否体现 correction。

## 里程碑

### B1：Memory Taxonomy

构建：

- Memory categories。
- 每类 memory 的 schema。
- 正例和反例。

成功标准：

- 能稳定分类真实 Coding Agent memory。

### B2：Minimal Memory Store

构建：

- Structured memory store。
- Write API。
- Retrieve API。
- Update 和 delete API。
- Source 和 confidence 字段。

成功标准：

- Agent 可以跨 session 持久化 memory。
- 检索出的 memory 带 source metadata。

### B3：Memory-Aware Agent Loop

构建：

- 规划前检索 memory 的 agent loop。
- 任务完成后写入 memory。
- 用户纠正后更新 memory。

成功标准：

- 能跑 multi-session tasks，并检查 memory 对行为的影响。

### B4：Memory Eval Set

构建：

- 30-100 个 controlled memory tasks。
- 标注 memory type 和 expected behavior。
- Metrics 和 failure categories。

成功标准：

- 能比较 no-memory、naive-memory、structured-memory agents。

## 和模型训练的连接

当 memory 行为可测之后，把它转成训练数据：

- SFT：正确使用 memory 的 demonstrations。
- DPO：memory-grounded action vs ignored-memory action。
- GRPO/RLVR：基于任务成功和 memory verification 的 reward。

目标是从外部 memory 规则走向模型行为：

> 模型应该学会什么时候信任 memory，什么时候验证 memory，什么时候忽略 memory，什么时候更新 memory。

