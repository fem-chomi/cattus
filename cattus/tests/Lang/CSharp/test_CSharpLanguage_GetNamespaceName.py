from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage


class TestCSharpLanguage_GetNamespaceName(TestCase):
    def test_GetNamespaceName_pattern_01(self):
        test = CSharpLanguage()
        self.assertEqual(test.GetNamespaceName('AAAA-BBBB-CCCC'), 'AaaaBbbbCccc')
