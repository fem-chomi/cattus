from unittest import TestCase
from Util.First import First


class TestFirst_Delimiter(TestCase):
    def test_Delimiter_pattern_01(self):
        test = First(', ')
        self.assertEqual(test.Delimiter(), '')
        self.assertEqual(test.Delimiter(), ', ')
