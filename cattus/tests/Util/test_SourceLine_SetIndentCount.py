from unittest import TestCase
from Util.SourceLine import SourceLine


class TestSourceLine_SetIndentCount(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_ResetIndent_pattern_01(self):
        SourceLine.PushIndentN(3)
        self.assertEqual(SourceLine.Indent(), '            ')

        # リセット後はインデント段数が初期化されている
        SourceLine.ResetIndent()
        self.assertEqual(SourceLine.Indent(), '')
