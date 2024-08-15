from unittest import TestCase
from Util.SourceLine import SourceLine


class TestSourceLine_PushIndentN(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_PushIndent_pattern_01(self):
        # インデントを保存する
        SourceLine.SetIndentCount(3)
        SourceLine.PushIndentN(6)
        self.assertEqual(SourceLine.Indent(), '                        ')

        # インデントを戻す
        SourceLine.PopIndent()
        self.assertEqual(SourceLine.Indent(), '            ')
