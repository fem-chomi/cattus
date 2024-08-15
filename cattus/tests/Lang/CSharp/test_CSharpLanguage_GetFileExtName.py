from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage


class TestCSharpLanguage_GetFileExtName(TestCase):
    def test_GetFileExtName_pattern_01(self):
        test = CSharpLanguage()
        self.assertEqual(test.GetFileExtName(), 'cs')
