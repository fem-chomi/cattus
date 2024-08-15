from unittest import TestCase
from Util.SourceLine import SourceLine


class TestSourceLine_SetIndentFillColumn(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_SetIndentFillColumn_pattern_01(self):
        # 既定の改行コードは\r\n
        SourceLine.SetIndentFillColumn(8)
        SourceLine.IndentN(3)
        self.assertEqual(SourceLine.Indent(), '                        ')
