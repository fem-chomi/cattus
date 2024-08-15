from unittest import TestCase
from typing import List
from Lang.Python.PythonLanguage import PythonLanguage
from Config.ConstructorConfig import ConstructorType, ConstructorConfig
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestPythonLanguage_GenerateConstructor(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateConstructor_pattern_01(self):
        test = PythonLanguage()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')

        result = test.GenerateConstructor(test.GetConstructorConfig(ConstructorType.FULL), entityModel, config)
        self.assertEqual(result[0], 'def __init__(self, eeee_ffff_gggg: int, iiii_jjjj_kkkk: int, mmmm_nnnn_oooo: int) -> None:\r\n')
        self.assertEqual(result[1], '    self.__eeee_ffff_gggg = eeee_ffff_gggg\r\n')
        self.assertEqual(result[2], '    self.__iiii_jjjj_kkkk = iiii_jjjj_kkkk\r\n')
        self.assertEqual(result[3], '    self.__mmmm_nnnn_oooo = mmmm_nnnn_oooo\r\n')

    def test_GenerateConstructor_pattern_02(self):
        test = PythonLanguage()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')

        result = test.GenerateConstructor(test.GetConstructorConfig(ConstructorType.OMIT), entityModel, config)
        self.assertEqual(result[0], 'def __init__(self, eeee_ffff_gggg: int=1, iiii_jjjj_kkkk: int=2, mmmm_nnnn_oooo: int=3) -> None:\r\n')
        self.assertEqual(result[1], '    self.__eeee_ffff_gggg = eeee_ffff_gggg\r\n')
        self.assertEqual(result[2], '    self.__iiii_jjjj_kkkk = iiii_jjjj_kkkk\r\n')
        self.assertEqual(result[3], '    self.__mmmm_nnnn_oooo = mmmm_nnnn_oooo\r\n')

    def test_GenerateConstructor_pattern_03(self):
        test = PythonLanguage()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')

        result = test.GenerateConstructor(test.GetConstructorConfig(ConstructorType.DEFAULT), entityModel, config)
        self.assertEqual(result[0], 'def __init__(self) -> None:\r\n')
        self.assertEqual(result[1], '    self.__eeee_ffff_gggg = 1\r\n')
        self.assertEqual(result[2], '    self.__iiii_jjjj_kkkk = 2\r\n')
        self.assertEqual(result[3], '    self.__mmmm_nnnn_oooo = 3\r\n')

    def test_GenerateConstructor_pattern_04(self):
        test = PythonLanguage()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        that = ClassTypeConfig(ClassType.DTO, classSuffixName = 'YYYY')

        result = test.GenerateConstructor(test.GetConstructorConfig(ConstructorType.COPY), entityModel, config, that)
        self.assertEqual(result[0], 'def __init__(self, that: aaaa_bbbb_cccc_yyyy) -> None:\r\n')
        self.assertEqual(result[1], '    self.__eeee_ffff_gggg = that.eeee_ffff_gggg\r\n')
        self.assertEqual(result[2], '    self.__iiii_jjjj_kkkk = that.iiii_jjjj_kkkk\r\n')
        self.assertEqual(result[3], '    self.__mmmm_nnnn_oooo = that.mmmm_nnnn_oooo\r\n')

    def test_GenerateConstructor_pattern_05(self):
        test = PythonLanguage()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ', enablePythonSpecialDataClass=True)

        result = test.GenerateConstructor(test.GetConstructorConfig(ConstructorType.FULL), entityModel, config)
        self.assertEqual(len(result), 0)
