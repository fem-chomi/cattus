from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage


class TestCSharpLanguage_GetConstantValueName(TestCase):
    def test_GetConstantValueName_pattern_01(self):
        test = CSharpLanguage()
        self.assertEqual(test.GetConstantValueName('AAAA-BBBB-CCCC'), 'AAAA_BBBB_CCCC')
