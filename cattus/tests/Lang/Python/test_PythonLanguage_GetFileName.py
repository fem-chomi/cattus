from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage


class TestPythonLanguage_GetFileName(TestCase):
    def test_GetFileName_pattern_01(self):
        test = PythonLanguage()
        self.assertEqual(test.GetFileName('AAAA-BBBB-CCCC'), 'aaaa_bbbb_cccc')
