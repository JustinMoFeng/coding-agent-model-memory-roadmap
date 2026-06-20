# 知识系统与代码组织

## 核心原则

这个仓库的核心定位是 Research OS，而不是一个单一代码项目。

推荐原则：

> 文档、路线、论文卡片、实验报告放在这里；小实验代码可以放在这里；成熟工程项目单独建 repo，并在这里做索引和研究报告。

这样可以同时满足两个目标：

- GitHub Pages 可以展示你的研究路线、论文阅读、实验日志和项目总结。
- 真正的代码项目不会被知识库结构束缚，也不会把文档仓库变成一个混乱 monorepo。

## 三类代码如何处理

### 1. 小型学习实验

适合放在本仓库的 `labs/` 下。

例子：

- tokenizer 观察脚本。
- tiny causal LM demo。
- SFT 数据格式转换脚本。
- memory schema prototype。
- eval metric toy example。

特点：

- 代码量小。
- 服务某一周学习或某篇实验日志。
- 不需要独立 release。
- 不需要复杂依赖和长期维护。

展示方式：

- 在 GitHub Pages 中写实验报告。
- 报告链接到 `labs/` 中的代码文件。

### 2. 中型研究原型

可以先放在本仓库，成熟后拆出去。

例子：

- `agent-training-lab`
- `coding-agent-memory-lab`
- memory eval set prototype
- rollout runner prototype

判断是否该拆出去：

- 是否需要独立 README。
- 是否需要独立依赖。
- 是否会被别人 clone 后单独运行。
- 是否会形成稳定 API 或 CLI。
- 是否开始产生大量代码、测试和数据。

如果满足两三条，就应该单独建 repo。

### 3. 成熟工程项目

应该单独建 GitHub repo。

例子：

- 可插拔 Coding Agent Memory 系统。
- Agent rollout/eval framework。
- Post-training data synthesis toolkit。
- Memory-aware coding-agent benchmark。

本仓库只保留：

- 项目介绍。
- 研究动机。
- 实验报告。
- 关键结果。
- 外部 repo 链接。
- 论文或技术报告。

## 推荐目录

```text
content/
  docs/
  weeks/
  topics/
  papers/
  experiments/
  projects/
  reference/templates/

labs/
  tokenizer-observation/
  sft-data-format/
  memory-schema-prototype/

scripts/
  new_week.py
  new_paper.py
  new_experiment.py
```

## GitHub Pages 展示什么

GitHub Pages 展示：

- 总体路线。
- 每周计划。
- 论文卡片索引。
- 实验报告。
- 专题调研。
- 项目说明。
- 外部项目链接。

GitHub Pages 不直接承担：

- 复杂代码运行。
- 数据库写入。
- 大文件数据管理。
- 多人实时协作。
- 动态 dashboard。

## 和妙搭这类平台的关系

第一阶段不建议把妙搭作为 source of truth。

原因：

- 研究内容需要版本管理。
- 论文和实验记录天然适合 Markdown。
- 实验报告最好和 commit、代码、数据版本关联。
- GitHub repo 更容易公开、迁移和复用。

妙搭可以后续作为：

- 展示层。
- 表单写入端。
- 内部 dashboard。
- 实验结果可视化页面。

但长期知识资产应优先保存在 Git + Markdown 中。

## 推荐工作流

新增一周计划：

```bash
python scripts/new_week.py 02 2026-06-29
```

新增论文卡片：

```bash
python scripts/new_paper.py memgpt
```

新增实验记录：

```bash
python scripts/new_experiment.py exp-001-tokenizer-observation
```

每周复盘时：

- 更新周计划状态。
- 补充论文卡片。
- 写实验记录。
- 如果有代码，链接到 `labs/` 或外部 repo。

## 最终形态

最终你会拥有两层资产：

1. Research OS：记录你如何学习、调研、实验和写作。
2. Project repos：承载真正可运行、可复用、可展示的工程项目。

这比把所有东西塞进一个仓库更稳定，也比把知识散在多个平台更容易长期维护。
