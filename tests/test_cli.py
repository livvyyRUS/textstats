import contextlib
import io
import os
import tempfile
import unittest

from textstats.cli import main


class TestCliMissingFile(unittest.TestCase):
    def test_exit_code_and_message(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as ctx:
                main(["no-such-file.txt"])
        self.assertEqual(ctx.exception.code, 2)
        self.assertIn("файл не найден", stderr.getvalue())


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
