from unittest import TestCase
from Util.SourceLine import IndentType, SourceLine


class TestSourceLine_Indent(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_Indent_pattern_01(self):
        # 初期化後のインデント位置は0
        self.assertEqual(SourceLine.Indent(), '')

    def test_Indent_pattern_02(self):
        # インデントが4SPACEで3段
        SourceLine.IndentDown()
        SourceLine.IndentDown()
        SourceLine.IndentDown()
        self.assertEqual(SourceLine.Indent(), '            ')


    def test_Indent_pattern_03(self):
        # インデントがTABで3段
        SourceLine.SetIndentType(IndentType.TAB)
        SourceLine.IndentDown()
        SourceLine.IndentDown()
        SourceLine.IndentDown()
        self.assertEqual(SourceLine.Indent(), '\t\t\t')
