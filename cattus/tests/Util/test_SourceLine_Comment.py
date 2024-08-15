from unittest import TestCase
from Util.SourceLine import SourceLine


class TestSourceLine_Comment(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_Comment_pattern_01(self):
        # コメント出力する場合
        self.assertEqual(SourceLine.Comment('foo'), 'foo')

    def test_Comment_pattern_02(self):
        # コメント出力しない場合
        SourceLine.SetNoComment(True)
        self.assertEqual(SourceLine.Comment('foo'), '')
