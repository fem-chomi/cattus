from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage


class TestCSharpLanguage_GetFileName(TestCase):
    def test_GetFileName_pattern_01(self):
        test = CSharpLanguage()
        self.assertEqual(test.GetFileName('AAAA-BBBB-CCCC'), 'AaaaBbbbCccc')
