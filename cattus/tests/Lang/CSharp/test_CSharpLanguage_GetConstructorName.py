from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.ClassTypeConfig import ClassType, ClassTypeConfig


class TestCSharpLanguage_GetConstructorName(TestCase):
    def test_GetConstructorName_pattern_01(self):
        test = CSharpLanguage()
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        self.assertEqual(test.GetConstructorName('AAAA-BBBB-CCCC', config), 'AaaaBbbbCcccZzzz')
