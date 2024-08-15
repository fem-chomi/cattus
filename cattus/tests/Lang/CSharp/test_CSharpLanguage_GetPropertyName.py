from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage


class TestCSharpLanguage_GetPropertyName(TestCase):
    def test_GetPropertyName_pattern_01(self):
        test = CSharpLanguage()
        self.assertEqual(test.GetPropertyName('AAAA-BBBB-CCCC'), 'AaaaBbbbCccc')
