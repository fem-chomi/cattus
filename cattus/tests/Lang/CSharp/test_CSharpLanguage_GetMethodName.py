from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage


class TestCSharpLanguage_GetMethodName(TestCase):
    def test_GetMethodName_pattern_01(self):
        test = CSharpLanguage()
        self.assertEqual(test.GetMethodName('AAAA-BBBB-CCCC'), 'AaaaBbbbCccc')
