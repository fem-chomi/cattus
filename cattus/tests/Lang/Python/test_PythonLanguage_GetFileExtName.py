from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage


class TestPythonLanguage_GetFileExtName(TestCase):
    def test_GetFileExtName_pattern_01(self):
        test = PythonLanguage()
        self.assertEqual(test.GetFileExtName(), 'py')
