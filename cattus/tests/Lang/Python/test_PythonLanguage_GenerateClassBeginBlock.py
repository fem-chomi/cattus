from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestPythonLanguage_GenerateClassBeginBlock(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateClassBeginBlock_pattern_01(self):
        test = PythonLanguage()
        fieldDefineList = []
        field = FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT32))
        fieldDefineList.append(field)
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        result = test.GenerateClassBeginBlock(entityModel, config)
        self.assertEqual(result[0], 'class aaaa_bbbb_cccc_zzzz():\r\n')
        self.assertEqual(SourceLine.Indent(), '    ')
        self.assertEqual(len(test.ImportDefineSet), 0)

    def test_GenerateClassBeginBlock_pattern_02(self):
        test = PythonLanguage()
        fieldDefineList = []
        field = FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT32))
        fieldDefineList.append(field)
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ', enablePythonSpecialDataClass=True)
        result = test.GenerateClassBeginBlock(entityModel, config)
        self.assertEqual(result[0], '@dataclasses.dataclass\r\n')
        self.assertEqual(result[1], 'class aaaa_bbbb_cccc_zzzz():\r\n')
        self.assertEqual(SourceLine.Indent(), '    ')
        self.assertEqual(list(test.ImportDefineSet)[0].ModuleName, 'dataclasses')

    def test_GenerateClassBeginBlock_pattern_03(self):
        test = PythonLanguage()
        fieldDefineList = []
        field = FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT32))
        fieldDefineList.append(field)
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ', enableImmutable=True, enablePythonSpecialDataClass=True)
        result = test.GenerateClassBeginBlock(entityModel, config)
        self.assertEqual(result[0], '@dataclasses.dataclass(frozen=True)\r\n')
        self.assertEqual(result[1], 'class aaaa_bbbb_cccc_zzzz():\r\n')
        self.assertEqual(SourceLine.Indent(), '    ')
        self.assertEqual(list(test.ImportDefineSet)[0].ModuleName, 'dataclasses')
