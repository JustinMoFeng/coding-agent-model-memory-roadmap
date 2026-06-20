# Agent Training 路线纵览

## 目标

Agent Training 线的目标是：

> 学会围绕 Coding Agent 构建 post-training 闭环：数据合成、rollout、reward、训练、eval 和 failure analysis。

你要形成的判断力是：

- 一个 agent 失败是模型问题、数据问题、上下文问题、工具问题，还是 eval 问题。
- 某类行为应该用 SFT、DPO、GRPO/RLVR、prompt、memory 还是系统工程解决。
- 一段 coding-agent trajectory 如何变成训练样本、偏好样本或 reward 样本。

## 学习顺序

```text
Tokenizer
-> Causal LM
-> Decoder-only Transformer
-> Training Loop / Data
-> SFT
-> DPO
-> RLVR / GRPO
-> Inference / Serving / Eval
```

前四个是地基，后四个是和工作最相关的后训练能力。

## 阶段目标

### 阶段 1：LM 基础

要能解释：

- Tokenization 如何影响代码、路径、diff 和 error log。
- Causal LM loss 如何计算。
- Decoder-only Transformer 的基本结构。
- Generation 和 training 的区别。

### 阶段 2：SFT / Preference / RLVR

要能做：

- 把 coding-agent trajectory 改写成 SFT 样本。
- 构造 chosen/rejected preference pair。
- 设计 verifiable reward。
- 分析 reward hacking。

### 阶段 3：Rollout / Eval / Infra

要能构建：

- 简单 rollout runner。
- 任务成功率和 failure taxonomy。
- 基于 tests 的 reward。
- 对比不同 prompt、model、memory 策略的 eval report。

## 主要材料

- Stanford CS336：Language Modeling from Scratch。
- Hugging Face LLM Course。
- Hugging Face Transformers 文档。
- TRL SFTTrainer / DPOTrainer / GRPOTrainer 文档。
- vLLM / SGLang 文档。

更细的模块拆分保留在 [大模型 / 后训练学习主线](archive/07-model-learning-path.md)。

## 近期产出

- Tokenizer observation。
- Causal LM 最小例子。
- Coding-agent trajectory SFT 样本。
- 5 对 chosen/rejected coding-agent 行为样本。
- 3 个 verifiable reward 设计。
