from unittest import TestCase
from typing import List
from Lang.Mock.MockLanguage import MockLanguage
from Model.ImportDefine import ImportDefine


class TestMockLanguage_ClearImportDefine(TestCase):
    def test_AppendImportDefine_pattern_01(self):
        import1 = ImportDefine('AAAA', 'BBBB', 'CCCC', 'DDDD', 'EEEE')
        import2 = ImportDefine('FFFF', 'GGGG', 'HHHH', 'IIII', 'JJJJ')
        import3 = ImportDefine('KKKK', 'LLLL', 'MMMM', 'NNNN', 'OOOO')
        test = MockLanguage()
        test.AppendImportDefine(import1)
        test.AppendImportDefine(import2)
        test.AppendImportDefine(import3)

        test.ClearImportDefine()
        self.assertEqual(len(test.ImportDefineSet), 0)
