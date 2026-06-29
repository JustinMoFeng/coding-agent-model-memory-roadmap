# BPE Tokenizer Lab

This lab is for implementing a minimal byte-level BPE tokenizer by hand.

Teaching mode rule: the core implementation should be written by the learner.
The files here provide structure, milestones, and sanity checks only.

## Goal

Build a small tokenizer that can:

- train byte-pair merge rules from text,
- encode text into token ids,
- decode token ids back to the original text,
- preserve arbitrary UTF-8 text, including Chinese and code snippets.

## Milestones

### 1. Byte baseline

Start from UTF-8 bytes.

Checkpoint:

- every input string can become a sequence of byte tokens,
- decoding those byte tokens reconstructs the original string.

### 2. Pair statistics

Given a current token sequence, count adjacent token pairs.

Checkpoint:

- on a tiny string, you can inspect the most frequent pair by hand,
- ties are handled deterministically.

### 3. BPE training

Repeatedly merge the most frequent pair until the target vocabulary size or
merge count is reached.

Checkpoint:

- each merge creates one new token,
- sequence length should usually shrink after a useful merge,
- merges are stored in order.

### 4. Encoding

Apply learned merges to new text.

Checkpoint:

- merges are applied in training order,
- unseen text still encodes because the base vocabulary is bytes,
- `decode(encode(text)) == text`.

### 5. Observations

Record at least five observations for:

- Chinese text,
- Python code,
- git diff text,
- error logs,
- whitespace and numbers.

## First Toy Inputs

Use these before larger examples:

```text
aaabdaaabac
the cat in the hat
hello hello
你好，世界
def train_bpe(text): return text
```

## Suggested Commands

Run the tests after you write the implementation:

```sh
python -m pytest labs/bpe-tokenizer/test_bpe_tokenizer.py
```

Run a quick manual inspection:

```sh
python labs/bpe-tokenizer/inspect_tokenization.py
```
