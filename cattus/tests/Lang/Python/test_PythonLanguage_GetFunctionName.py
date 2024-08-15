from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage


class TestPythonLanguage_GetFunctionName(TestCase):
    def test_GetFunctionName_pattern_01(self):
        test = PythonLanguage()
        self.assertEqual(test.GetFunctionName('AAAA-BBBB-CCCC'), '__aaaa_bbbb_cccc')
