from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestPythonLanguage_GenerateNamespaceBeginBlock(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateNamespaceBeginBlock_pattern_01(self):
        test = PythonLanguage()
        fieldDefineList = []
        field = FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT32))
        fieldDefineList.append(field)
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        result = test.GenerateNamespaceBeginBlock(entityModel, config)
        self.assertEqual(len(result), 0)
