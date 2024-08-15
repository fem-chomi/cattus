from unittest import TestCase
from Util.SourceLine import SourceLine


class TestSourceLine_IndentDown(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_IndentDown_pattern_01(self):
        # インデントを1段下げる
        SourceLine.IndentDown()
        self.assertEqual(SourceLine.Indent(), '    ')
