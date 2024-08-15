from unittest import TestCase
from Util.SourceLine import IndentType, SourceLine


class TestSourceLine_SetIndentType(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_SetNoComment_pattern_01(self):
        # 既定の改行コードは\r\n
        SourceLine.SetIndentType(IndentType.TAB)
        SourceLine.IndentN(3)
        self.assertEqual(SourceLine.Indent(), '\t\t\t')
