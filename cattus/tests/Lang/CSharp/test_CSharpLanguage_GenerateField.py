from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestCSharpLanguage_GenerateField(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateField_pattern_01(self):
        test = CSharpLanguage()
        field = FieldDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32))
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        result = test.GenerateField(field, config)
        self.assertEqual(result[0], 'private int aaaaBbbbCccc;\r\n')

    def test_GenerateField_pattern_02(self):
        test = CSharpLanguage()
        field = FieldDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32))
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ', enableImmutable = True)
        result = test.GenerateField(field, config)
        self.assertEqual(result[0], 'private readonly int aaaaBbbbCccc;\r\n')
