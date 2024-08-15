from unittest import TestCase
from Util.NameConverter import NameConverter


class TestNameConverter_ToUpperKebabCase(TestCase):
    def test_ToUpperKebabCase_pattern_01(self):
        test = NameConverter.ToUpperKebabCase('AAAA-BBBB-CCCC')
        self.assertEqual(test, 'AAAA-BBBB-CCCC')

    def test_ToUpperKebabCase_pattern_02(self):
        test = NameConverter.ToUpperKebabCase('AAAA_BBBB_CCCC')
        self.assertEqual(test, 'AAAA-BBBB-CCCC')
