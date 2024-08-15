from unittest import TestCase
from typing import List
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.CSharp.ToString import ToString
from Util.SourceLine import SourceLine


class TestToString_GenerateCode(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateCode_pattern_01(self):
        test = CSharpLanguage()
        method = ToString()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT8)))
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT16)))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT32)))
        entityModel = EntityModel('VVVV', 'WWWW', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        field = None
        result = test.GenerateMethod(method, entityModel, field, config)
        self.assertEqual(result[0], 'public override string ToString() {\r\n')
        self.assertEqual(result[1], '    return new StringBuilder()\r\n')
        self.assertEqual(result[2], '        .Append($"AaaaBbbbCccc: {this.AaaaBbbbCccc}")\r\n')
        self.assertEqual(result[3], '        .Append($"EeeeFfffGggg: {this.EeeeFfffGggg}")\r\n')
        self.assertEqual(result[4], '        .Append($"IiiiJjjjKkkk: {this.IiiiJjjjKkkk}")\r\n')
        self.assertEqual(result[5], '        .ToString();\r\n')
        self.assertEqual(result[6], '}\r\n')
