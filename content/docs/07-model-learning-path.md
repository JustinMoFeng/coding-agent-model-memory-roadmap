# 大模型 / 后训练学习主线

这条线不要按“Transformer、RAG、Agent、RLHF 都看一点”的方式学。建议按一个主问题串起来：

> 一个 Coding Agent 的行为，如何从 token、模型结构、训练数据、后训练目标、rollout 和 eval 中被塑造出来？

也就是说，你不是为了变成“会背大模型概念的人”，而是为了能判断：

- 某个 agent 失败是模型能力问题、数据问题、prompt/context 问题、reward 问题，还是 eval 问题。
- 某类行为应该用 SFT、DPO、RLVR、数据过滤、memory 机制还是系统工程解决。
- 一段 coding-agent trajectory 如何变成训练样本、偏好样本或 reward 样本。

## 学习顺序

推荐顺序：

```text
M1 Tokenizer
M2 Causal LM
M3 Decoder-only Transformer
M4 Training Loop / Data
M5 SFT
M6 Preference Optimization / DPO
M7 RLVR / GRPO
M8 Inference / Serving / Eval
```

前四个是基础，后四个才是和你工作最贴的后训练能力。

## M1：Tokenizer

### 要学什么

- Token、vocab、BPE / SentencePiece 的基本思想。
- Tokenization 对中文、代码、路径、diff、error log 的影响。
- 为什么 tokenizer 是模型行为的一部分，而不只是预处理工具。

### 推荐材料

主材料：

- Stanford CS336：Lecture 1 / Overview and Tokenization  
  https://cs336.stanford.edu/

实践材料：

- Hugging Face LLM Course：Tokenizer 相关章节  
  https://huggingface.co/learn/llm-course/

### 必须产出

- 对中文、代码、diff、error log 做 tokenizer 观察。
- 写出 5 条对 Coding Agent 的影响。

### 和 Coding Agent 的连接

- 文件路径、函数名、错误日志、JSON、patch 都会经过 tokenizer。
- Token 切分会影响复制标识符、生成 diff、解析错误日志的稳定性。

## M2：Causal LM

### 要学什么

- Next-token prediction。
- Causal mask。
- Logits、softmax、cross entropy。
- Training 和 generation 的差异。
- Greedy decoding、sampling、temperature、top-p。

### 推荐材料

主材料：

- Hugging Face Transformers：Causal language modeling  
  https://huggingface.co/docs/transformers/en/tasks/language_modeling

补充材料：

- Hugging Face LLM Course：Training a causal language model from scratch  
  https://huggingface.co/learn/llm-course/chapter7/6

### 必须产出

- 用自己的话解释：为什么 GPT 类模型只能看左边 token。
- 写一个最小例子：输入 tokens、labels、loss 分别是什么。
- 说明为什么同一个 prompt 多次 rollout 结果可能不同。

### 和 Coding Agent 的连接

- Agent 每一步 action 也是生成下一个 token 序列。
- Tool call、命令、patch、final answer 都是模型生成行为。
- Rollout 的随机性会影响 agent eval。

## M3：Decoder-only Transformer

### 要学什么

- Embedding。
- Positional encoding / RoPE 的直觉。
- Self-attention。
- MLP。
- Residual、LayerNorm。
- KV cache 的直觉。

### 推荐材料

主材料：

- Stanford CS336：Architecture / Hyperparameters 相关 lecture  
  https://cs336.stanford.edu/

补充材料：

- CS224N Transformer 相关 lecture  
  https://web.stanford.edu/class/cs224n/

### 必须产出

- 画出 decoder-only block。
- 写一个 mini attention 或 tiny GPT forward。
- 能解释 KV cache 为什么能加速 generation。

### 和 Coding Agent 的连接

- 长上下文、工具历史、memory 注入都会占 context。
- KV cache、context length、attention cost 会影响长程 agent 的运行成本。

## M4：Training Loop / Data

### 要学什么

- Dataset、batch、sequence length。
- Loss curve。
- Validation。
- Overfitting。
- Data cleaning、dedup、mixture。
- Scaling intuition。

### 推荐材料

主材料：

- Stanford CS336：Assignment 1 Basics、Data lectures  
  https://cs336.stanford.edu/

实践材料：

- Hugging Face Datasets / Trainer 基础  
  https://huggingface.co/docs/transformers/

### 必须产出

- 跑一个极小 causal LM 或直接跑官方 tutorial。
- 记录 loss、sample、失败输出。
- 写出数据质量如何影响模型行为。

### 和 Coding Agent 的连接

- Coding 后训练高度依赖数据质量。
- 真实 issue、commit、test、review、trajectory 都是潜在数据源。

## M5：SFT

### 要学什么

- Instruction tuning。
- Prompt-completion dataset。
- Conversational dataset。
- Assistant-only loss / completion-only loss。
- Trajectory SFT。

### 推荐材料

主材料：

- TRL SFTTrainer  
  https://huggingface.co/docs/trl/en/sft_trainer

数据格式材料：

- TRL Dataset formats and types  
  https://huggingface.co/docs/trl/main/en/dataset_formats

### 必须产出

- 把一个 Coding Agent trajectory 改写成：
  - language modeling 格式
  - prompt-completion 格式
  - conversational 格式
- 说明三种格式各自适合什么训练目标。

### 和 Coding Agent 的连接

- 成功轨迹可以用于 SFT。
- 但 SFT 可能只学到格式，不一定学到任务成功策略。
- 需要 eval 验证行为是否真的改变。

## M6：Preference Optimization / DPO

### 要学什么

- Preference pair。
- Chosen / rejected。
- DPO 和 reward model 的关系。
- 为什么偏好数据适合减少某些行为错误。

### 推荐材料

主材料：

- DPO paper。
- TRL DPOTrainer 文档。

### 必须产出

- 构造 5 对 coding-agent chosen/rejected 样例。
- 每对样例说明偏好标准。

### 和 Coding Agent 的连接

适合用 DPO 优化的行为：

- 是否读相关文件。
- 是否运行测试。
- 是否利用错误反馈。
- 是否避免无关修改。
- 是否正确使用 memory。

## M7：RLVR / GRPO

### 要学什么

- Verifiable reward。
- Outcome reward vs process reward。
- GRPO 的基本用途。
- Reward hacking。

### 推荐材料

主材料：

- TRL GRPOTrainer 文档。
- DeepSeek-R1 / RLVR 相关报告。
- Stanford CS336：Post-training / RLVR lecture。

### 必须产出

- 设计 3 个可验证 coding reward：
  - 单测通过。
  - 无无关文件修改。
  - 正确使用或更新 memory。
- 写出每个 reward 可能如何被 hack。

### 和 Coding Agent 的连接

- Coding task 天然有可执行 reward。
- 但 test pass 不是全部，还要防止过拟合、误改和 reward hacking。

## M8：Inference / Serving / Eval

### 要学什么

- KV cache。
- Batching。
- Latency / throughput。
- vLLM / SGLang 的作用。
- Eval set、metrics、failure analysis。

### 推荐材料

主材料：

- Stanford CS336：Inference / Evaluation lectures。
- vLLM docs。
- SGLang docs。

### 必须产出

- 比较两个模型或两个 prompt 的 rollout 结果。
- 固定 generation 参数，记录成功率和失败类型。

### 和 Coding Agent 的连接

- Agent 训练离不开 rollout infra。
- Eval 设计决定你是否真的知道模型变好了。

## 第一阶段最低完成标准

前 6-8 周不要求你成为训练系统专家，但至少要完成：

- 能解释 causal LM loss。
- 能解释 SFT 数据格式。
- 能构造 chosen/rejected pair。
- 能设计 verifiable reward。
- 能把 coding-agent failure 写成训练数据问题。
- 能把 memory-use behavior 写成 eval 问题。

