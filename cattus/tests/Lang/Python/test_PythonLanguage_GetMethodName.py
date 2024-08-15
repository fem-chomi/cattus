from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage


class TestPythonLanguage_GetMethodName(TestCase):
    def test_GetMethodName_pattern_01(self):
        test = PythonLanguage()
        self.assertEqual(test.GetMethodName('AAAA-BBBB-CCCC'), 'aaaa_bbbb_cccc')
