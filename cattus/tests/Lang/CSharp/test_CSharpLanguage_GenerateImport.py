from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Model.ImportDefine import ImportDefine


class TestCSharpLanguage_GenerateImport(TestCase):
    def test_GenerateImport_pattern_01(self):
        import1 = ImportDefine(namespaceName='AAAA', className='BBBB')
        import2 = ImportDefine(namespaceName='CCCC', className='DDDD')
        import3 = ImportDefine(namespaceName='EEEE', className='FFFF')
        test = CSharpLanguage()
        test.AppendImportDefine(import1)
        test.AppendImportDefine(import2)
        test.AppendImportDefine(import3)
        result = test.GenerateImport()

        sample = list(test.ImportDefineSet)
        aaaa_passed: bool = False
        bbbb_passed: bool = False
        cccc_passed: bool = False
        for i in range(0, 3):
            if sample[i].NamespaceName == 'AAAA':
                self.assertEqual(result[i], 'using AAAA.BBBB;\r\n')
                aaaa_passed = True
            if sample[i].NamespaceName == 'CCCC':
                self.assertEqual(result[i], 'using CCCC.DDDD;\r\n')
                bbbb_passed = True
            if sample[i].NamespaceName == 'EEEE':
                self.assertEqual(result[i], 'using EEEE.FFFF;\r\n')
                cccc_passed = True
        self.assertTrue(aaaa_passed)
        self.assertTrue(bbbb_passed)
        self.assertTrue(cccc_passed)
