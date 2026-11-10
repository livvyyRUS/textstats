"""Базовая статистика текста."""

from collections import Counter


def count_words(text: str) -> int:
    """Вернуть количество слов в тексте."""
    return len(text.split())


def count_chars(text: str) -> int:
    """Вернуть количество символов без завершающего перевода строки."""
    return len(text.rstrip("\n"))


def top_words(text: str, limit: int = 5) -> list[tuple[str, int]]:
    """Вернуть самые частые слова и число их вхождений."""
    words = [w.strip(".,!?;:()\"'").lower() for w in text.split()]
    counter = Counter(word for word in words if word)
    return counter.most_common(limit)
