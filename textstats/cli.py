"""Командная строка для подсчёта статистики текста."""

import argparse
import json
import sys

from .core import count_chars, count_words, top_words


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="textstats", description="Подсчёт статистики текста"
    )
    parser.add_argument(
        "--json", action="store_true", help="вывести результат в JSON"
    )
    parser.add_argument(
        "--top", type=int, default=3, help="сколько частых слов показать"
    )
    parser.add_argument(
        "--encoding", default="utf-8", help="кодировка входного файла"
    )
    parser.add_argument(
        "path", nargs="?", help="путь к файлу (по умолчанию читается stdin)"
    )
    return parser


def read_text(path: str | None, encoding: str = "utf-8") -> str:
    if path is None:
        return sys.stdin.read()
    try:
        with open(path, encoding=encoding) as fh:
            return fh.read()
    except FileNotFoundError:
        print(f"textstats: файл не найден: {path}", file=sys.stderr)
        raise SystemExit(2) from None


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    text = read_text(args.path, args.encoding)
    if args.json:
        payload = {
            "words": count_words(text),
            "chars": count_chars(text),
            "top": top_words(text, args.top),
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    print(f"words: {count_words(text)}")
    print(f"chars: {count_chars(text)}")
    for word, count in top_words(text, args.top):
        print(f"top: {word} = {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
