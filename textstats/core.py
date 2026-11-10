"""Базовая статистика текста."""


def count_words(text: str) -> int:
    """Вернуть количество слов в тексте."""
    return len(text.split())


def count_chars(text: str) -> int:
    """Вернуть количество символов без завершающего перевода строки."""
    return len(text.rstrip("\n"))
