import unittest

from textstats.core import count_chars, count_words


class TestCountWords(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(count_words(""), 0)

    def test_several_words(self):
        self.assertEqual(count_words("git status --short"), 3)


class TestCountChars(unittest.TestCase):
    def test_ignores_trailing_newline(self):
        self.assertEqual(count_chars("abc\n"), 3)

    def test_counts_spaces(self):
        self.assertEqual(count_chars("a b"), 3)


if __name__ == "__main__":
    unittest.main()
