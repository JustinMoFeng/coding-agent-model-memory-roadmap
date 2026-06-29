"""Minimal byte-level BPE tokenizer lab.

Teaching mode: this file intentionally contains interfaces and TODOs only.
Implement the core logic yourself, then use the tests and inspection script to
debug it.
"""

from __future__ import annotations

from dataclasses import dataclass


Token = int
Pair = tuple[Token, Token]


@dataclass
class BPEModel:
    """A trained byte-level BPE model.

    `vocab` maps token id to the bytes represented by that token.
    `merges` stores pair merges in the order learned during training.
    """

    vocab: dict[Token, bytes]
    merges: list[Pair]


def bytes_to_tokens(text: str) -> list[Token]:
    """把字符串转换成 byte-level BPE 的初始 token 序列。

    BPE tokenizer 不能直接处理 Python 的 `str`，它需要在整数序列上做统计和合并。
    这里先把文本编码成 UTF-8 bytes，再把每个 byte 的数值当作一个 token id。

    在 byte-level BPE 里，最开始的基础词表就是 256 个 byte：
    token id `0..255` 分别对应一个原始 byte。后续的 BPE 训练会在这个基础上
    统计相邻 token pair，并把高频 pair 合并成 `256, 257, ...` 这些新 token。

    这个函数是 tokenizer 的入口：`str -> bytes -> list[int]`。
    它必须保持可逆，保证后面可以通过 `tokens_to_bytes(...).decode("utf-8")`
    还原回原始文本。
    """

    # UTF-8 能表示中文、英文、emoji、代码、错误日志等文本。
    # 转成 bytes 后，每个 byte 都是 0..255 之间的整数，可以直接作为基础 token。
    utf8_bytes = text.encode('utf-8')
    return list(utf8_bytes)



def tokens_to_bytes(tokens: list[Token], vocab: dict[Token, bytes] | None = None) -> bytes:
    """把 token 序列还原成 bytes。

    这是 `bytes_to_tokens` 的反方向，也是 tokenizer 解码流程的底层步骤。
    函数只负责还原到 bytes 层，不直接返回 `str`；真正变回字符串时，再由上层
    `decode()` 调用 `.decode("utf-8")`。

    有两种情况：

    1. `vocab is None`：说明现在还没有 BPE 合并结果，所有 token 都应该是
       `0..255` 的原始 byte token，可以直接把 token 当作 byte 值。
    2. `vocab` 存在：说明 token 里可能有 `256, 257, ...` 这样的 BPE 新 token。
       这些 token 不再对应单个 byte，必须通过 `vocab[token]` 查到它代表的
       bytes 片段，再把所有片段拼接起来。

    这个函数保证 token 序列可以回到原始 bytes，是 `decode(encode(text)) == text`
    这个 round-trip 性质的基础。
    """
    pieces = []
    for token in tokens:
        # 有 vocab 时，优先按 vocab 查表。BPE 合并后的 token 可能代表多个 bytes。
        if vocab is not None and token in vocab:
            piece = vocab[token]
        else:
            # 没有 vocab，或者 token 不在 vocab 里时，把它当作原始 byte token。
            # 这里要求 token 必须在 0..255 范围内。
            piece = bytes([token])
        pieces.append(piece)
    return b"".join(pieces)


def count_pairs(tokens: list[Token]) -> dict[Pair, int]:
    """Count adjacent token pairs in the current token sequence.

    Milestone 2: use tiny inputs where you can verify the counts by hand.
    """

    count_map = {}
    for i in range(len(tokens) - 1):
        pair = (tokens[i], tokens[i+1])
        if pair not in count_map:
            count_map[pair] = 0
        count_map[pair] += 1
    return count_map


def merge_pair(tokens: list[Token], pair: Pair, new_token: Token) -> list[Token]:
    """Replace every non-overlapping occurrence of `pair` with `new_token`."""

    new_tokens = []
    i = 0
    while i < len(tokens) - 1:
        cur = (tokens[i], tokens[i+1])
        
        if cur == pair:
            new_tokens.append(new_token)
            i += 1
        else:
            new_tokens.append(tokens[i])
        i += 1

    if i == len(tokens) - 1:
        new_tokens.append(tokens[i])

    return new_tokens


def train_bpe(text: str, num_merges: int) -> BPEModel:
    """从训练文本中学习 byte-pair merge 规则，返回一个 BPE 模型。

    BPE 训练的核心流程：从 byte token 序列出发，反复找到最高频的相邻 token pair，
    把它合并成一个新 token，记录 merge 规则。每一轮都会让序列变短、词表变大。

    训练过程中维护三个状态：

    1. tokens：当前 token 序列。一开始是 `bytes_to_tokens(text)` 的 byte 序列，
       每轮 merge 后会变短。
    2. vocab：token id -> bytes 的映射。一开始是 256 个 byte token，
       每轮 merge 新增一个 token，其 bytes 是被合并 pair 的 bytes 拼接。
       vocab 用于后续 decode：看到 token id 就知道它对应什么 bytes。
    3. merges：按训练顺序记录的 pair 列表。这个顺序很重要，因为后续 encode
       新文本时必须按同样的顺序重新应用 merge。

    边界情况：
    - 如果训练文本太短（没有相邻 pair），`count_pairs` 返回空字典，提前结束。
    - 如果 `num_merges == 0`，循环不执行，返回基础 256 词表和空 merges。
    """
    tokens = bytes_to_tokens(text)
    new_token = 256
    vocab = {i: bytes([i]) for i in range(256)}
    merges = []
    for i in range(num_merges):
        pairs = count_pairs(tokens)
        if not pairs:
            break
        # 选出现次数最高的 pair；频率相同时 max 会按 pair 元组的字典序选一个，
        # 保证结果确定性。
        frequent_pair = max(pairs, key=pairs.get)
        tokens = merge_pair(tokens, frequent_pair, new_token)
        # 新 token 的 bytes = 被合并两个 token 的 bytes 拼接。
        vocab[new_token] = vocab[frequent_pair[0]] + vocab[frequent_pair[1]]
        merges.append(frequent_pair)
        new_token += 1

    return BPEModel(
        vocab=vocab,
        merges=merges
    )

def encode(text: str, model: BPEModel) -> list[Token]:
    """用训练好的 BPE 模型对新文本做编码，返回 token id 序列。

    和训练时的区别：训练时是每轮重新统计频率、选最高频 pair；
    encode 时不重新统计，而是按 model.merges 的顺序依次尝试合并。
    顺序必须和训练时一致，因为后面的 merge 依赖前面 merge 产生的 token。

    流程：
    1. 把文本转成 byte token 序列（和训练时的起点一样）。
    2. 按 merges 顺序，逐个尝试合并。如果当前序列里有这个 pair 就合并，
       没有就跳过。
    3. 所有 merge 尝试完后，返回最终的 token 序列。

    新 token id = 256 + i，i 是该 merge 在 merges 列表中的位置，
    和训练时分配的 id 完全一致。
    """
    merges = model.merges
    tokens = bytes_to_tokens(text)
    for i in range(len(merges)):
        tokens = merge_pair(tokens, merges[i], 256 + i)
    return tokens


def decode(tokens: list[Token], model: BPEModel) -> str:
    """把 token id 序列还原回原始字符串。

    两步完成：
    1. tokens_to_bytes(tokens, model.vocab)：查 vocab，把每个 token id
       还原成对应的 bytes 片段，拼接成完整的 bytes。
    2. .decode("utf-8")：把 bytes 解码回 Python 字符串。

    必须保证 encode -> decode 的 round trip：
    decode(encode(text, model), model) == text
    """
    return tokens_to_bytes(tokens, model.vocab).decode("utf-8")

if __name__ == "__main__":
    text = "你好，世界！ Hello, world! 😊"
    tokens = bytes_to_tokens(text)
    result = tokens_to_bytes(tokens)
    print("round trip")
    print("text:   ", text)
    print("tokens: ", tokens)
    print("bytes:  ", result)
    print("decoded:", result.decode("utf-8"))
    print("ok:     ", result.decode("utf-8") == text)

    english_tokens = [72, 101, 108, 108, 111]
    english_bytes = tokens_to_bytes(english_tokens)
    print("\nraw byte tokens: English")
    print("tokens: ", english_tokens)
    print("bytes:  ", english_bytes)
    print("decoded:", english_bytes.decode("utf-8"))

    chinese_tokens = [228, 189, 160]
    chinese_bytes = tokens_to_bytes(chinese_tokens)
    print("\nraw byte tokens: Chinese")
    print("tokens: ", chinese_tokens)
    print("bytes:  ", chinese_bytes)
    print("decoded:", chinese_bytes.decode("utf-8"))

    vocab = {
        97: b"a",
        98: b"b",
        99: b"c",
        256: b"ab",
        257: b"abc",
    }
    bpe_tokens = [257, 256, 99]
    bpe_bytes = tokens_to_bytes(bpe_tokens, vocab)
    print("\nBPE tokens with vocab")
    print("tokens: ", bpe_tokens)
    print("bytes:  ", bpe_bytes)
    print("decoded:", bpe_bytes.decode("utf-8"))

    pair_tokens = [1, 2, 1, 2, 1]
    print("\ncount pairs: tiny ids")
    print("tokens: ", pair_tokens)
    print("counts: ", count_pairs(pair_tokens))

    pair_text = "hello hello"
    pair_text_tokens = bytes_to_tokens(pair_text)
    print("\ncount pairs: text")
    print("text:   ", pair_text)
    print("tokens: ", pair_text_tokens)
    print("counts: ", count_pairs(pair_text_tokens))

    print(merge_pair([1, 1, 1], (1, 1), 256))
    # 期望 [256, 1]

    print(merge_pair([1, 2, 1, 2], (1, 2), 256))
    # 期望 [256, 256]

    print(merge_pair([1, 2, 2, 1], (1, 2), 256))
    # 期望 [256, 2, 1]
