from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage


class TestCSharpLanguage_GetFieldName(TestCase):
    def test_GetFieldName_pattern_01(self):
        test = CSharpLanguage()
        self.assertEqual(test.GetFieldName('AAAA-BBBB-CCCC'), 'aaaaBbbbCccc')
