# 写作与研究习惯

## 原则

不要等项目完成后才开始写。

写作是把模糊工程现象变成研究问题的过程。

## 四个长期文档

全年持续维护这四类文档。

### 1. Research Questions

作用：

- 记录研究问题如何收敛和变化。

推荐格式：

```text
Question:
Why it matters:
Current hypothesis:
Evidence so far:
Next experiment:
```

### 2. Paper Notes

作用：

- 把论文转化为可复用的研究积木。

模板：

- `reference/templates/paper-note.md`

### 3. Experiment Log

作用：

- 保证结果可复现。
- 避免重复踩坑。
- 记录 negative results。

模板：

- `reference/templates/experiment-log.md`

### 4. Draft

作用：

- 逐步积累 paper-style report。

一开始只需要有标题结构：

```text
Title
Abstract
Introduction
Related Work
Problem Setup
Method
Experiments
Results
Failure Analysis
Limitations
Conclusion
```

后面逐步填充。

## 每周写作

每周写一页，回答：

- 我这周尝试了什么？
- 我学到了什么？
- 什么失败了？
- 下一个具体问题是什么？

这份记录要短、具体、诚实。不要太早追求文风。

## 月度研究复盘

每月底写：

- 一段模型侧进展。
- 一段 Memory 侧进展。
- 一段工程进展。
- 一段写作或研究清晰度进展。
- 一个明确决定：继续、调整或停止某条线。

## 论文式思考

任何项目都强制套这个结构：

- Problem：什么失败或空缺存在？
- Setting：它发生在哪里？
- Method：你改变了什么？
- Data：什么样本用于训练或测试？
- Metric：如何知道有帮助？
- Baseline：和什么比较？
- Ablation：哪个组件重要？
- Limitation：在哪里失败？

如果某一项缺失，项目还不够清楚。

## 写作目标

第 3 个月：

- 10-15 篇 paper notes。
- 8-12 份 experiment logs。
- 1 篇短 internal report。

第 6 个月：

- 25-35 篇 paper notes。
- 1 份 memory taxonomy report。
- 1 份 post-training experiment report。

第 9 个月：

- 1 篇带 preliminary results 的 paper-style draft。
- 1 个 polished project README。

第 12 个月：

- 1 篇完整 technical report。
- 1 个 open-source-ready repository。
- 可选：workshop-style submission。
