from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.DataTypeConfig import DataType
from Util.SourceLine import SourceLine


class TestCSharpLanguage_GenerateConstantValue(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateConstantValue_pattern_01(self):
        test = CSharpLanguage()
        name = 'AAAA-BBBB-CCCC'
        DataTypeConfig = test.GetDataTypeConfig(DataType.INT32)
        value = 'DDDD'
        result = test.GenerateConstantValue(name, DataTypeConfig, value)
        self.assertEqual(result[0], 'public const int AAAA_BBBB_CCCC = DDDD\r\n')
