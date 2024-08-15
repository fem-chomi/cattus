from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.DataTypeConfig import DataType
from Model.ParameterDefine import ParameterDefine
from Util.SourceLine import SourceLine


class TestCSharpLanguage_GenerateParameter(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateParameter_pattern_01(self):
        test = CSharpLanguage()
        parameter = ParameterDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32), 'EEEE')
        self.assertEqual(test.GenerateParameter(parameter), 'int aaaaBbbbCccc')

    def test_GenerateParameter_pattern_02(self):
        test = CSharpLanguage()
        parameter = ParameterDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32), 'EEEE')
        self.assertEqual(test.GenerateParameter(parameter, enableDefaultValue=True), 'int aaaaBbbbCccc=EEEE')
