from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestCSharpLanguage_GenerateClassBeginBlock(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateClassBeginBlock_pattern_01(self):
        test = CSharpLanguage()
        fieldDefineList = []
        field = FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT32))
        fieldDefineList.append(field)
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        result = test.GenerateClassBeginBlock(entityModel, config)
        self.assertEqual(result[0], 'public class AaaaBbbbCcccZzzz {\r\n')
        self.assertEqual(SourceLine.Indent(), '    ')
