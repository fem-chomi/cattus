from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.DataTypeConfig import DataType, AllocationType, DataTypeConfig


class TestCSharpLanguage_GetDataTypeName(TestCase):
    def test_GetDataTypeName_pattern_01(self):
        test = CSharpLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.VALUE)
        self.assertEqual(test.GetDataTypeName(dataType), 'int')

    def test_GetDataTypeName_pattern_02(self):
        test = CSharpLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.ARRAY)
        self.assertEqual(test.GetDataTypeName(dataType), 'int[]')

    def test_GetDataTypeName_pattern_03(self):
        test = CSharpLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.LIST)
        self.assertEqual(test.GetDataTypeName(dataType), 'List<int>')

    def test_GetDataTypeName_pattern_04(self):
        test = CSharpLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.MAP, 'AAAA', DataType.INT64, 'long')
        self.assertEqual(test.GetDataTypeName(dataType), 'Dictionary<long, int>')

    def test_GetDataTypeName_pattern_05(self):
        test = CSharpLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.SET)
        self.assertEqual(test.GetDataTypeName(dataType), 'Set<int>')

    def test_GetDataTypeName_pattern_06(self):
        test = CSharpLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.STACK)
        self.assertEqual(test.GetDataTypeName(dataType), 'Stack<int>')

    def test_GetDataTypeName_pattern_07(self):
        test = CSharpLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.QUEUE)
        self.assertEqual(test.GetDataTypeName(dataType), 'Queue<int>')

    def test_GetDataTypeName_pattern_08(self):
        test = CSharpLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.OTHER)
        with self.assertRaises(NotImplementedError):
            test.GetDataTypeName(dataType)
