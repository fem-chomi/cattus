from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage


class TestPythonLanguage_GetNamespaceName(TestCase):
    def test_GetNamespaceName_pattern_01(self):
        test = PythonLanguage()
        self.assertEqual(test.GetNamespaceName('AAAA-BBBB-CCCC'), 'aaaa_bbbb_cccc')
