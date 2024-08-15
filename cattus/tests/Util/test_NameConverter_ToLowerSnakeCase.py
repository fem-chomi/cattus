from unittest import TestCase
from Util.NameConverter import NameConverter


class TestNameConverter_ToLowerSnakeCase(TestCase):
    def test_ToLowerSnakeCase_pattern_01(self):
        test = NameConverter.ToLowerSnakeCase('AAAA-BBBB-CCCC')
        self.assertEqual(test, 'aaaa_bbbb_cccc')

    def test_ToLowerSnakeCase_pattern_02(self):
        test = NameConverter.ToLowerSnakeCase('AAAA_BBBB_CCCC')
        self.assertEqual(test, 'aaaa_bbbb_cccc')
