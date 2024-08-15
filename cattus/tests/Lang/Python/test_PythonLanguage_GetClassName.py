from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Config.ClassTypeConfig import ClassType, ClassTypeConfig


class TestPythonLanguage_GetClassName(TestCase):
    def test_GetClassName_pattern_01(self):
        test = PythonLanguage()
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        self.assertEqual(test.GetClassName('AAAA-BBBB-CCCC', config), 'aaaa_bbbb_cccc_zzzz')
