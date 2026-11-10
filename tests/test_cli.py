import contextlib
import io
import os
import tempfile
import unittest

from textstats.cli import main, read_text


class TestCliMissingFile(unittest.TestCase):
    def test_exit_code_and_message(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = main(["no-such-file.txt"])
        self.assertEqual(code, 2)
        self.assertIn("файл не найден", stderr.getvalue())


class TestReadText(unittest.TestCase):
    def test_propagates_missing_file(self):
        """read_text не управляет жизненным циклом процесса."""
        with self.assertRaises(FileNotFoundError):
            read_text("no-such-file.txt")


class TestCliHappyPath(unittest.TestCase):
    def test_reads_file_and_prints_stats(self):
        with tempfile.NamedTemporaryFile(
            "w", suffix=".txt", delete=False, encoding="utf-8"
        ) as fh:
            fh.write("два слова")
            name = fh.name
        try:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                self.assertEqual(main([name]), 0)
            self.assertIn("words: 2", out.getvalue())
        finally:
            os.unlink(name)


if __name__ == "__main__":
    unittest.main()
