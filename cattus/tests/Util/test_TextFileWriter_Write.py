import os
import tempfile
from unittest import TestCase
from Util.TextFileWriter import TextFileWriter


class TestTextFileWriter_Write(TestCase):
    def test_Write_pattern_01(self):
        with tempfile.TemporaryDirectory() as tmp_path:
            # 一時ファイルに出力する
            filename = os.path.join(tmp_path, 'test.txt')
            TextFileWriter.Write(filename, 'Hello World.ヤキソバ十個')

            # 一時ファイルを読み込みテストする
            with open(filename, mode='r', encoding='utf-8') as f:
                txt = f.read()
                self.assertEqual(txt, 'Hello World.ヤキソバ十個')
