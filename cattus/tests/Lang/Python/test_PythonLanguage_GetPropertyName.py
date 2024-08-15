from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage


class TestPythonLanguage_GetPropertyName(TestCase):
    def test_GetPropertyName_pattern_01(self):
        test = PythonLanguage()
        self.assertEqual(test.GetPropertyName('AAAA-BBBB-CCCC'), 'aaaa_bbbb_cccc')
