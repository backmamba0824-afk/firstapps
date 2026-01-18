from __future__ import annotations

import re
from collections import Counter
from typing import Iterable


_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
_WORD_RE = re.compile(r"[A-Za-zÀ-ÿ]+")


def _sentences(text: str) -> list[str]:
    cleaned = " ".join(text.split())
    if not cleaned:
        return []
    return [sentence.strip() for sentence in _SENTENCE_SPLIT.split(cleaned) if sentence.strip()]


def _keywords(tokens: Iterable[str]) -> Counter:
    stop_words = {
        "the",
        "and",
        "for",
        "with",
        "that",
        "this",
        "from",
        "your",
        "you",
        "are",
        "was",
        "were",
        "has",
        "have",
        "how",
        "why",
        "what",
        "into",
        "about",
        "but",
        "its",
        "not",
        "their",
        "they",
        "will",
        "can",
        "our",
        "out",
        "use",
        "using",
    }
    filtered = [token for token in tokens if token not in stop_words]
    return Counter(filtered)


def summarize(text: str, max_sentences: int = 3) -> list[str]:
    sentences = _sentences(text)
    if not sentences:
        return []

    tokens = _WORD_RE.findall(text.lower())
    scores = _keywords(tokens)
    if not scores:
        return sentences[:max_sentences]

    ranked = []
    for index, sentence in enumerate(sentences):
        sentence_tokens = _WORD_RE.findall(sentence.lower())
        score = sum(scores.get(token, 0) for token in sentence_tokens)
        ranked.append((score, index, sentence))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    top = sorted(ranked[:max_sentences], key=lambda item: item[1])
    return [sentence for _, _, sentence in top]
