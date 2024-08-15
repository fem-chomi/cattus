from unittest import TestCase
from typing import List
from Lang.Python.PythonLanguage import PythonLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.Python.ToString import ToString
from Util.SourceLine import SourceLine


class TestToString_GenerateCode(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateCode_pattern_01(self):
        test = PythonLanguage()
        method = ToString()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT8)))
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT16)))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT32)))
        entityModel = EntityModel('VVVV', 'WWWW', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        field = None
        result = test.GenerateMethod(method, entityModel, field, config)
        self.assertEqual(result[0], 'def to_string(self) -> str:\r\n')
        self.assertEqual(result[1], '    text: str = \'\'\r\n')
        self.assertEqual(result[2], '    text += f\'aaaa_bbbb_cccc: {self.aaaa_bbbb_cccc}\'\r\n')
        self.assertEqual(result[3], '    text += f\'eeee_ffff_gggg: {self.eeee_ffff_gggg}\'\r\n')
        self.assertEqual(result[4], '    text += f\'iiii_jjjj_kkkk: {self.iiii_jjjj_kkkk}\'\r\n')
