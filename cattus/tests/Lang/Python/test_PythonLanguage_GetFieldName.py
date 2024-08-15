from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage


class TestPythonLanguage_GetFieldName(TestCase):
    def test_GetFieldName_pattern_01(self):
        test = PythonLanguage()
        self.assertEqual(test.GetFieldName('AAAA-BBBB-CCCC'), '__aaaa_bbbb_cccc')
