"""Командная строка для подсчёта статистики текста."""

import argparse
import sys

from .core import count_chars, count_words


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="textstats", description="Подсчёт статистики текста"
    )
    parser.add_argument(
        "path", nargs="?", help="путь к файлу (по умолчанию читается stdin)"
    )
    return parser


def read_text(path: str | None) -> str:
    if path is None:
        return sys.stdin.read()
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    text = read_text(args.path)
    print(f"words: {count_words(text)}")
    print(f"chars: {count_chars(text)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
