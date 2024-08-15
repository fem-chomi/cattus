from unittest import TestCase
from Util.NameConverter import NameConverter


class TestNameConverter_ToUpperCamelCase(TestCase):
    def test_ToUpperCamelCase_pattern_01(self):
        test = NameConverter.ToUpperCamelCase('AAAA-BBBB-CCCC')
        self.assertEqual(test, 'AaaaBbbbCccc')

    def test_ToUpperCamelCase_pattern_02(self):
        test = NameConverter.ToUpperCamelCase('AAAA_BBBB_CCCC')
        self.assertEqual(test, 'AaaaBbbbCccc')
