"""Sanity checks for the BPE tokenizer lab.

These tests describe behavior without providing the implementation.
"""

from bpe_tokenizer import (
    BPEModel,
    bytes_to_tokens,
    count_pairs,
    decode,
    encode,
    merge_pair,
    tokens_to_bytes,
    train_bpe,
)


def test_byte_baseline_round_trips_ascii_and_chinese() -> None:
    text = "Hello, 你好!"

    tokens = bytes_to_tokens(text)
    reconstructed = tokens_to_bytes(tokens).decode("utf-8")

    assert reconstructed == text


def test_count_pairs_on_tiny_sequence() -> None:
    tokens = [1, 2, 1, 2, 1]

    counts = count_pairs(tokens)

    assert counts[(1, 2)] == 2
    assert counts[(2, 1)] == 2


def test_merge_pair_replaces_non_overlapping_occurrences() -> None:
    tokens = [1, 1, 1]

    merged = merge_pair(tokens, (1, 1), 256)

    assert merged == [256, 1]


def test_train_bpe_records_requested_number_of_merges() -> None:
    model = train_bpe("aaabdaaabac", num_merges=3)

    assert isinstance(model, BPEModel)
    assert len(model.merges) == 3
    assert len(model.vocab) == 259


def test_encode_decode_round_trips_unseen_text() -> None:
    model = train_bpe("the cat in the hat", num_merges=4)
    text = "the quick brown fox 你好"

    ids = encode(text, model)
    reconstructed = decode(ids, model)

    assert reconstructed == text
