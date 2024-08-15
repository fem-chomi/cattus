from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Config.DataTypeConfig import DataType
from Model.ParameterDefine import ParameterDefine
from Util.SourceLine import SourceLine


class TestPythonLanguage_GenerateParameter(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateParameter_pattern_01(self):
        test = PythonLanguage()
        parameter = ParameterDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32), 'EEEE')
        self.assertEqual(test.GenerateParameter(parameter), 'aaaa_bbbb_cccc: int')

    def test_GenerateParameter_pattern_02(self):
        test = PythonLanguage()
        parameter = ParameterDefine('AAAA-BBBB-CCCC', 'DDDD', test.GetDataTypeConfig(DataType.INT32), 'EEEE')
        self.assertEqual(test.GenerateParameter(parameter, enableDefaultValue=True), 'aaaa_bbbb_cccc: int=EEEE')
