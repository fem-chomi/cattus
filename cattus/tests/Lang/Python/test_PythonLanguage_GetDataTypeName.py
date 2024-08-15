from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Config.DataTypeConfig import DataType, AllocationType, DataTypeConfig


class TestPythonLanguage_GetDataTypeName(TestCase):
    def test_GetDataTypeName_pattern_01(self):
        test = PythonLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.VALUE)
        self.assertEqual(test.GetDataTypeName(dataType), 'int')

    def test_GetDataTypeName_pattern_02(self):
        test = PythonLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.ARRAY)
        self.assertEqual(test.GetDataTypeName(dataType), 'Array[int]')

    def test_GetDataTypeName_pattern_03(self):
        test = PythonLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.LIST)
        self.assertEqual(test.GetDataTypeName(dataType), 'List[int]')

    def test_GetDataTypeName_pattern_04(self):
        test = PythonLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.MAP, 'AAAA', DataType.INT64, 'long')
        self.assertEqual(test.GetDataTypeName(dataType), 'Dict[long, int]')

    def test_GetDataTypeName_pattern_05(self):
        test = PythonLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.SET)
        self.assertEqual(test.GetDataTypeName(dataType), 'Set[int]')

    def test_GetDataTypeName_pattern_06(self):
        test = PythonLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.STACK)
        self.assertEqual(test.GetDataTypeName(dataType), 'deque')

    def test_GetDataTypeName_pattern_07(self):
        test = PythonLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.QUEUE)
        self.assertEqual(test.GetDataTypeName(dataType), 'deque')

    def test_GetDataTypeName_pattern_08(self):
        test = PythonLanguage()
        dataType = DataTypeConfig(DataType.INT32, 'int', AllocationType.OTHER)
        with self.assertRaises(NotImplementedError):
            test.GetDataTypeName(dataType)
