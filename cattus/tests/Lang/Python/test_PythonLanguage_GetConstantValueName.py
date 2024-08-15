from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage


class TestPythonLanguage_GetConstantValueName(TestCase):
    def test_GetConstantValueName_pattern_01(self):
        test = PythonLanguage()
        self.assertEqual(test.GetConstantValueName('AAAA-BBBB-CCCC'), 'AAAA_BBBB_CCCC')
