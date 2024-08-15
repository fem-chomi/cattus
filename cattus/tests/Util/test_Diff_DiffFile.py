import os
import tempfile
from unittest import TestCase
from Util.Diff import Diff
from Util.TextFileWriter import TextFileWriter


class TestDiff_DiffFile(TestCase):
    maxDiff = None

    def test_DiffFile_pattern_01(self):
        with tempfile.TemporaryDirectory() as tmp_path:
            # 一時ファイルに出力する
            filename1 = os.path.join(tmp_path, 'test1.txt')
            TextFileWriter.Write(filename1, 'Hello World.ヤキソバ十個')

            filename2 = os.path.join(tmp_path, 'test2.txt')
            TextFileWriter.Write(filename2, 'Hello World.ヤキソバ十個')

            self.assertEqual(Diff.DiffFile(filename1, filename2), '')

    def test_DiffFile_pattern_01(self):
        with tempfile.TemporaryDirectory() as tmp_path:
            # 一時ファイルに出力する
            filename1 = os.path.join(tmp_path, 'test1.txt')
            TextFileWriter.Write(filename1, '1行目\n2行目\n3行目')

            filename2 = os.path.join(tmp_path, 'test2.txt')
            TextFileWriter.Write(filename2, '先頭行追加\n1行目\n2行目(変更)')

            msg = '*** \n\n--- \n\n***************\n\n*** 1,3 ****\n\n  1行目\n\n! 2行目\n\n! 3行目\n--- 1,3 ----\n\n+ 先頭行追加\n\n  1行目\n\n! 2行目(変更)'
            self.assertEqual(Diff.DiffFile(filename1, filename2), msg)
