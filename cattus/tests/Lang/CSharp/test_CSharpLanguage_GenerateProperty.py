from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestCSharpLanguage_GenerateProperty(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateProperty_pattern_01(self):
        test = CSharpLanguage()
        field = FieldDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32))
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        result = test.GenerateProperty(field, config)
        self.assertEqual(result[0], 'public int AaaaBbbbCccc() {\r\n')
        self.assertEqual(result[1], '    return this.aaaaBbbbCccc;\r\n')
        self.assertEqual(result[2], '}\r\n')
