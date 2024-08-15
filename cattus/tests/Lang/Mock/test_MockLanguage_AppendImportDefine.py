from unittest import TestCase
from typing import List
from Lang.Mock.MockLanguage import MockLanguage
from Model.ImportDefine import ImportDefine


class TestMockLanguage_AppendImportDefine(TestCase):
    def test_AppendImportDefine_pattern_01(self):
        import1 = ImportDefine('AAAA', 'BBBB', 'CCCC', 'DDDD', 'EEEE')
        import2 = ImportDefine('FFFF', 'GGGG', 'HHHH', 'IIII', 'JJJJ')
        import3 = ImportDefine('KKKK', 'LLLL', 'MMMM', 'NNNN', 'OOOO')
        test = MockLanguage()
        test.AppendImportDefine(import1)
        test.AppendImportDefine(import2)
        test.AppendImportDefine(import3)
        result = list(test.ImportDefineSet)

        aaaa_passed: bool = False
        bbbb_passed: bool = False
        cccc_passed: bool = False
        for i in range(0, 3):
            if result[i].PathName == 'AAAA':
                self.assertEqual(result[i].PathName, 'AAAA')
                self.assertEqual(result[i].FileName, 'BBBB')
                self.assertEqual(result[i].ModuleName, 'CCCC')
                self.assertEqual(result[i].NamespaceName, 'DDDD')
                self.assertEqual(result[i].ClassName, 'EEEE')
                aaaa_passed = True
            if result[i].PathName == 'FFFF':
                self.assertEqual(result[i].PathName, 'FFFF')
                self.assertEqual(result[i].FileName, 'GGGG')
                self.assertEqual(result[i].ModuleName, 'HHHH')
                self.assertEqual(result[i].NamespaceName, 'IIII')
                self.assertEqual(result[i].ClassName, 'JJJJ')
                bbbb_passed = True
            if result[i].PathName == 'KKKK':
                self.assertEqual(result[i].PathName, 'KKKK')
                self.assertEqual(result[i].FileName, 'LLLL')
                self.assertEqual(result[i].ModuleName, 'MMMM')
                self.assertEqual(result[i].NamespaceName, 'NNNN')
                self.assertEqual(result[i].ClassName, 'OOOO')
                cccc_passed = True
        self.assertTrue(aaaa_passed)
        self.assertTrue(bbbb_passed)
        self.assertTrue(cccc_passed)
