from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestPythonLanguage_GenerateProperty(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateProperty_pattern_01(self):
        test = PythonLanguage()
        field = FieldDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32))
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        result = test.GenerateProperty(field, config)
        self.assertEqual(result[0], '@property\r\n')
        self.assertEqual(result[1], 'def aaaa_bbbb_cccc(self) -> int:\r\n')
        self.assertEqual(result[2], '    return self.__aaaa_bbbb_cccc\r\n')

    def test_GenerateProperty_pattern_02(self):
        test = PythonLanguage()
        field = FieldDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32))
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ', enablePythonSpecialDataClass=True)
        result = test.GenerateProperty(field, config)
        self.assertEqual(result[0], 'aaaa_bbbb_cccc: int\r\n')
