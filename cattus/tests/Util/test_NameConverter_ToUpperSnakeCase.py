from unittest import TestCase
from Util.NameConverter import NameConverter


class TestNameConverter_ToUpperSnakeCase(TestCase):
    def test_ToUpperSnakeCase_pattern_01(self):
        test = NameConverter.ToUpperSnakeCase('AAAA-BBBB-CCCC')
        self.assertEqual(test, 'AAAA_BBBB_CCCC')

    def test_ToUpperSnakeCase_pattern_02(self):
        test = NameConverter.ToUpperSnakeCase('AAAA_BBBB_CCCC')
        self.assertEqual(test, 'AAAA_BBBB_CCCC')
