from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Config.DataTypeConfig import DataType
from Util.SourceLine import SourceLine


class TestPythonLanguage_GenerateConstantValue(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateConstantValue_pattern_01(self):
        test = PythonLanguage()
        name = 'AAAA-BBBB-CCCC'
        DataTypeConfig = test.GetDataTypeConfig(DataType.INT32)
        value = 'DDDD'
        result = test.GenerateConstantValue(name, DataTypeConfig, value)
        self.assertEqual(result[0], 'AAAA_BBBB_CCCC: int = DDDD\r\n')
