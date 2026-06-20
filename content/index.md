# Coding Agent 模型与 Memory 成长路线

这个仓库用于维护一条一年的学习、研究和工程路线：**往模型后训练方向深耕，同时保留 Coding Agent Memory 作为长期研究主线**。

核心判断：

> 以模型后训练能力为主线，以 Coding Agent Memory 为研究问题，以 Coding Agent 为工程落地场景。

更具体地说，你要逐步形成的能力是：

> 能把真实 Coding Agent 的失败转化为数据、reward、eval 和 post-training 实验。

## 总方向

这条路线分成两条工程线。

1. **Agent 训练 / AI Infra**
   - Coding task 数据合成。
   - Agent rollout 和 trajectory 收集。
   - Reward、eval 和 failure analysis。
   - SFT、DPO、GRPO/RLVR 和 post-training infra。

2. **Coding Agent Memory**
   - Repo memory、user memory、task memory、bug memory。
   - Memory 写入、检索、更新、遗忘和冲突处理。
   - Memory-specific eval。
   - 跨 session 的长期 Coding Agent 行为。

两条线最终汇合到一个研究问题：

> 如何把长期 memory 转化为 Coding Agent 可训练、可控制、可评测的模型能力？

## 仓库结构

```text
.
├── README.md
├── mkdocs.yml
├── requirements.txt
├── content/
│   ├── docs/
│   ├── weeks/
│   ├── topics/
│   ├── projects/
│   └── reference/templates/
├── labs/
└── scripts/
```

## 使用方式

不要把这个仓库当成固定课表，而是把它当成一个长期维护的研究工作台。

从这里开始执行：

- [Week 01：启动周 - 后训练视角的 LM 基础 + Multica Memory 调研](weeks/week-01.md)
- [大模型 / 后训练学习主线](docs/07-model-learning-path.md)
- [周计划模板](reference/templates/week-plan-template.md)
- [知识系统与代码组织](docs/08-research-os-and-code-organization.md)

每周至少留下三个产物：

1. 一篇论文笔记。
2. 一个工程 commit 或可运行实验。
3. 一段 research log，记录本周问题、证据、失败和下一步。

这条路线不是为了“学完所有 AI”，而是为了形成几项核心能力：

- 理解模型行为如何被数据、目标函数和后训练塑造。
- 搭建可靠的 Coding Agent 训练、rollout 和 eval 闭环。
- 把 Memory 行为抽象成研究问题、数据集、reward 和评测。
- 把工程实验写成清晰的技术报告或论文草稿。
