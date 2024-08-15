from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.ClassTypeConfig import ClassType, ClassTypeConfig


class TestCSharpLanguage_GetClassName(TestCase):
    def test_GetClassName_pattern_01(self):
        test = CSharpLanguage()
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        self.assertEqual(test.GetClassName('AAAA-BBBB-CCCC', config), 'AaaaBbbbCcccZzzz')
