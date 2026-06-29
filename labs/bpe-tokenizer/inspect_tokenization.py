"""Manual inspection script for the BPE tokenizer lab.

Fill in the tokenizer implementation first, then run this script to inspect
learned merges and tokenization behavior on different text types.
"""

from __future__ import annotations

from bpe_tokenizer import decode, encode, train_bpe


EXAMPLES = [
    "hello hello",
    "你好，世界。你好。",
    "def train_bpe(text): return text",
    "--- a/file.py\n+++ b/file.py\n@@\n-print(old)\n+print(new)\n",
    "ValueError: invalid literal for int() with base 10: 'abc'",
]


def main() -> None:
    training_text = "\n".join(EXAMPLES)
    model = train_bpe(training_text, num_merges=20)

    print("merges:")
    for i, pair in enumerate(model.merges):
        print(i, pair, "=>", model.vocab[256 + i])

    print("\nexamples:")
    for text in EXAMPLES:
        ids = encode(text, model)
        reconstructed = decode(ids, model)
        print("-" * 40)
        print(text)
        print(ids)
        print("round trip:", reconstructed == text)


if __name__ == "__main__":
    main()
