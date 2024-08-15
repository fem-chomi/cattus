from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Config.ClassTypeConfig import ClassType, ClassTypeConfig


class TestPythonLanguage_GetConstructorName(TestCase):
    def test_GetConstructorName_pattern_01(self):
        test = PythonLanguage()
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        self.assertEqual(test.GetConstructorName('AAAA-BBBB-CCCC', config), '__init__')
