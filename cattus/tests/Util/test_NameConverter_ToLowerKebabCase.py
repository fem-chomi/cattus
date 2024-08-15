from unittest import TestCase
from Util.NameConverter import NameConverter


class TestNameConverter_ToLowerKebabCase(TestCase):
    def test_ToLowerKebabCase_pattern_01(self):
        test = NameConverter.ToLowerKebabCase('AAAA-BBBB-CCCC')
        self.assertEqual(test, 'aaaa-bbbb-cccc')

    def test_ToLowerKebabCase_pattern_02(self):
        test = NameConverter.ToLowerKebabCase('AAAA_BBBB_CCCC')
        self.assertEqual(test, 'aaaa-bbbb-cccc')
