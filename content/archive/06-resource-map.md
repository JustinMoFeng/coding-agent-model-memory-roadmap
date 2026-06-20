# 资源地图

这个文件用于维护课程、工具、论文和系统资源。列表要保持克制，只加入能服务路线的资源。

## 课程

### Stanford CS336: Language Modeling from Scratch

用途：

- Language model 基础。
- Tokenization。
- Training。
- Scaling。
- Systems 和 post-training 背景。

链接：

- https://cs336.stanford.edu/

### Stanford CS224N

用途：

- NLP 和 Transformer 背景。
- Attention 和 representation learning。

链接：

- https://web.stanford.edu/class/cs224n/

### Hugging Face LLM Course

用途：

- Transformers、Datasets、Tokenizers 和训练 workflow 实践。

链接：

- https://huggingface.co/learn/llm-course/

## Post-Training 工具

### TRL

用途：

- SFT。
- DPO。
- GRPO。
- 小型 post-training 实验。

链接：

- https://huggingface.co/docs/trl/

### verl

用途：

- RLHF/RLVR-style training systems。
- 更大规模 post-training workflows。

链接：

- https://verl.readthedocs.io/

### OpenRLHF

用途：

- RLHF 和 preference training system reference。

链接：

- https://openrlhf.readthedocs.io/

## Serving 和 Rollout

### vLLM

用途：

- Efficient inference。
- Batched rollout serving。
- KV cache 和 throughput 理解。

链接：

- https://docs.vllm.ai/

### SGLang

用途：

- LLM serving 和 agentic workflow serving。
- Structured generation 和 high-throughput inference。

链接：

- https://docs.sglang.ai/

## Memory 和 Agent Framework

### LangGraph Memory / Persistence

用途：

- Agent state。
- Persistence。
- Memory engineering ideas。

链接：

- https://docs.langchain.com/oss/python/concepts/memory
- https://docs.langchain.com/oss/python/langgraph/persistence

### LlamaIndex

用途：

- RAG、indexing 和 retrieval concepts。

链接：

- https://developers.llamaindex.ai/

## Benchmarks 和 Coding Agents

### SWE-bench

用途：

- 软件工程任务评测。
- Issue-to-patch benchmark 设计。

链接：

- https://www.swebench.com/

### SWE-smith

用途：

- Synthetic software-engineering task generation ideas。

链接：

- https://swesmith.com/

## 论文桶

### Language Modeling

- Attention Is All You Need。
- Scaling Laws for Neural Language Models。
- Chinchilla。

### Post-Training

- InstructGPT。
- Direct Preference Optimization。
- KTO。
- DeepSeek-R1 或相关 RLVR 报告。

### Coding Agents

- ReAct。
- Reflexion。
- SWE-bench。
- SWE-agent style systems。
- SWE-smith。

### Memory

- MemGPT。
- Generative Agents。
- Long-context 和 retrieval-augmented generation papers。
- Agent memory evaluation papers。

## 如何新增资源

新增前先回答：

- 它支持哪条线：agent training、memory 还是 writing？
- 它帮助回答什么具体问题？
- 它是 primary source、official doc 还是高质量实现？
- 它会改变我构建或评测什么吗？

