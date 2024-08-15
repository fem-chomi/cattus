from unittest import TestCase
from Util.SourceLine import SourceLine


class TestSourceLine_SetNewLine(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_SetNewLine_pattern_01(self):
        # 既定の改行コードは\r\n
        SourceLine.SetNewLine('\n')
        self.assertEqual(SourceLine.NewLine(), '\n')
