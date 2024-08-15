from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Model.ImportDefine import ImportDefine


class TestPythonLanguage_GenerateImport(TestCase):
    def test_GenerateImport_pattern_01(self):
        import1 = ImportDefine(moduleName='CCCC')
        import2 = ImportDefine(moduleName='FFFF')
        import3 = ImportDefine(moduleName='IIII')
        test = PythonLanguage()
        test.AppendImportDefine(import1)
        test.AppendImportDefine(import2)
        test.AppendImportDefine(import3)
        result = test.GenerateImport()

        sample = list(test.ImportDefineSet)
        aaaa_passed: bool = False
        bbbb_passed: bool = False
        cccc_passed: bool = False
        for i in range(0, 3):
            if sample[i].ModuleName == 'CCCC':
                self.assertEqual(result[i], 'import CCCC\r\n')
                aaaa_passed = True
            if sample[i].ModuleName == 'FFFF':
                self.assertEqual(result[i], 'import FFFF\r\n')
                bbbb_passed = True
            if sample[i].ModuleName == 'IIII':
                self.assertEqual(result[i], 'import IIII\r\n')
                cccc_passed = True
        self.assertTrue(aaaa_passed)
        self.assertTrue(bbbb_passed)
        self.assertTrue(cccc_passed)

    def test_GenerateImport_pattern_02(self):
        import1 = ImportDefine(pathName='AAAA', moduleName='CCCC')
        import2 = ImportDefine(pathName='DDDD', moduleName='FFFF')
        import3 = ImportDefine(pathName='GGGG', moduleName='IIII')
        test = PythonLanguage()
        test.AppendImportDefine(import1)
        test.AppendImportDefine(import2)
        test.AppendImportDefine(import3)
        result = test.GenerateImport()

        sample = list(test.ImportDefineSet)
        aaaa_passed: bool = False
        bbbb_passed: bool = False
        cccc_passed: bool = False
        for i in range(0, 3):
            if sample[i].PathName == 'AAAA':
                self.assertEqual(result[i], 'from AAAA import CCCC\r\n')
                aaaa_passed = True
            if sample[i].PathName == 'DDDD':
                self.assertEqual(result[i], 'from DDDD import FFFF\r\n')
                bbbb_passed = True
            if sample[i].PathName == 'GGGG':
                self.assertEqual(result[i], 'from GGGG import IIII\r\n')
                cccc_passed = True
        self.assertTrue(aaaa_passed)
        self.assertTrue(bbbb_passed)
        self.assertTrue(cccc_passed)
