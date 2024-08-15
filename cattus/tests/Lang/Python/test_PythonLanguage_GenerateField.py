from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestPythonLanguage_GenerateField(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateField_pattern_01(self):
        test = PythonLanguage()
        field = FieldDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32))
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        result = test.GenerateField(field, config)
        self.assertEqual(result[0], '__aaaa_bbbb_cccc: int\r\n')

    def test_GenerateField_pattern_02(self):
        test = PythonLanguage()
        field = FieldDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32))
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ', enablePythonSpecialDataClass=True)
        result = test.GenerateField(field, config)
        self.assertEqual(len(result), 0)
