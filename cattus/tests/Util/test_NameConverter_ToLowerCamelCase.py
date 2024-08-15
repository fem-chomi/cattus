from unittest import TestCase
from Util.NameConverter import NameConverter


class TestNameConverter_ToLowerCamelCase(TestCase):
    def test_ToLowerCamelCase_pattern_01(self):
        test = NameConverter.ToLowerCamelCase('AAAA-BBBB-CCCC')
        self.assertEqual(test, 'aaaaBbbbCccc')

    def test_ToLowerCamelCase_pattern_02(self):
        test = NameConverter.ToLowerCamelCase('AAAA_BBBB_CCCC')
        self.assertEqual(test, 'aaaaBbbbCccc')
