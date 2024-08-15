from unittest import TestCase
from Util.SourceLine import SourceLine


class TestSourceLine_SetNoComment(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_SetNoComment_pattern_01(self):
        # 既定の改行コードは\r\n
        SourceLine.SetNoComment(True)
        self.assertEqual(SourceLine.Comment('comment'), '')
