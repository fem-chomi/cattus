from unittest import TestCase
from Util.SourceLine import IndentType, SourceLine


class TestSourceLine_IndentN(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_IndentN_pattern_01(self):
        # インデントが4SPACEで3段
        self.assertEqual(SourceLine.IndentN(3), '            ')

        # インデント段数が変更されている
        self.assertEqual(SourceLine.Indent(), '            ')


    def test_IndentN_pattern_02(self):
        # インデントがTABで3段
        SourceLine.SetIndentType(IndentType.TAB)
        self.assertEqual(SourceLine.IndentN(3), '\t\t\t')

        # インデント段数が変更されている
        self.assertEqual(SourceLine.Indent(), '\t\t\t')
