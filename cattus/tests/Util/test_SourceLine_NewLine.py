from unittest import TestCase
from Util.SourceLine import SourceLine


class TestSourceLine_NewLine(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_NewLine_pattern_01(self):
        # 既定の改行コードは\r\n
        self.assertEqual(SourceLine.NewLine(), '\r\n')
