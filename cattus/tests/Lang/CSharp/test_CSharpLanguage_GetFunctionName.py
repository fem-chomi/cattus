from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage


class TestCSharpLanguage_GetFunctionName(TestCase):
    def test_GetFunctionName_pattern_01(self):
        test = CSharpLanguage()
        self.assertEqual(test.GetFunctionName('AAAA-BBBB-CCCC'), 'AaaaBbbbCccc')
