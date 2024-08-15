from unittest import TestCase
from Util.SourceLine import SourceLine


class TestSourceLine_IndentUp(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_IndentUp_pattern_01(self):
        # インデントを1段上げる
        SourceLine.SetIndentCount(3)
        SourceLine.IndentUp()
        self.assertEqual(SourceLine.Indent(), '        ')
