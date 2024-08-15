from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage


class TestCSharpLanguage_GetParameterName(TestCase):
    def test_GetParameterName_pattern_01(self):
        test = CSharpLanguage()
        self.assertEqual(test.GetParameterName('AAAA-BBBB-CCCC'), 'aaaaBbbbCccc')
