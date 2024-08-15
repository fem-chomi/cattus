from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestCSharpLanguage_GenerateNamespaceEndBlock(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateNamespaceEndBlock_pattern_01(self):
        test = CSharpLanguage()
        fieldDefineList = []
        field = FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT32))
        fieldDefineList.append(field)
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        SourceLine.IndentDown()
        result = test.GenerateNamespaceEndBlock(entityModel, config)
        self.assertEqual(result[0], '}\r\n')
        self.assertEqual(SourceLine.Indent(), '')
