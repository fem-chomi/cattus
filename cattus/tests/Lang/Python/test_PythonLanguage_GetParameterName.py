from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage


class TestPythonLanguage_GetParameterName(TestCase):
    def test_GetParameterName_pattern_01(self):
        test = PythonLanguage()
        self.assertEqual(test.GetParameterName('AAAA-BBBB-CCCC'), 'aaaa_bbbb_cccc')
