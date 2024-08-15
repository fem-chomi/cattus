from unittest import TestCase
from typing import List
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Config.ConstructorConfig import ConstructorType, ConstructorConfig
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine


class TestCSharpLanguage_GenerateConstructor(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateConstructor_pattern_01(self):
        test = CSharpLanguage()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')

        result = test.GenerateConstructor(test.GetConstructorConfig(ConstructorType.FULL), entityModel, config)
        self.assertEqual(result[0], 'public AaaaBbbbCcccZzzz(sbyte eeeeFfffGggg, short iiiiJjjjKkkk, int mmmmNnnnOooo) {\r\n')
        self.assertEqual(result[1], '    this.eeeeFfffGggg = eeeeFfffGggg;\r\n')
        self.assertEqual(result[2], '    this.iiiiJjjjKkkk = iiiiJjjjKkkk;\r\n')
        self.assertEqual(result[3], '    this.mmmmNnnnOooo = mmmmNnnnOooo;\r\n')
        self.assertEqual(result[4], '}\r\n')

    def test_GenerateConstructor_pattern_02(self):
        test = CSharpLanguage()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')

        result = test.GenerateConstructor(test.GetConstructorConfig(ConstructorType.OMIT), entityModel, config)
        self.assertEqual(result[0], 'public AaaaBbbbCcccZzzz(sbyte eeeeFfffGggg=1, short iiiiJjjjKkkk=2, int mmmmNnnnOooo=3) {\r\n')
        self.assertEqual(result[1], '    this.eeeeFfffGggg = eeeeFfffGggg;\r\n')
        self.assertEqual(result[2], '    this.iiiiJjjjKkkk = iiiiJjjjKkkk;\r\n')
        self.assertEqual(result[3], '    this.mmmmNnnnOooo = mmmmNnnnOooo;\r\n')
        self.assertEqual(result[4], '}\r\n')

    def test_GenerateConstructor_pattern_03(self):
        test = CSharpLanguage()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')

        result = test.GenerateConstructor(test.GetConstructorConfig(ConstructorType.DEFAULT), entityModel, config)
        self.assertEqual(result[0], 'public AaaaBbbbCcccZzzz() {\r\n')
        self.assertEqual(result[1], '    this.eeeeFfffGggg = 1;\r\n')
        self.assertEqual(result[2], '    this.iiiiJjjjKkkk = 2;\r\n')
        self.assertEqual(result[3], '    this.mmmmNnnnOooo = 3;\r\n')
        self.assertEqual(result[4], '}\r\n')

    def test_GenerateConstructor_pattern_04(self):
        test = CSharpLanguage()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        that = ClassTypeConfig(ClassType.DTO, classSuffixName = 'YYYY')

        result = test.GenerateConstructor(test.GetConstructorConfig(ConstructorType.COPY), entityModel, config, that)
        self.assertEqual(result[0], 'public AaaaBbbbCcccZzzz(AaaaBbbbCcccYyyy that) {\r\n')
        self.assertEqual(result[1], '    this.eeeeFfffGggg = that.EeeeFfffGggg;\r\n')
        self.assertEqual(result[2], '    this.iiiiJjjjKkkk = that.IiiiJjjjKkkk;\r\n')
        self.assertEqual(result[3], '    this.mmmmNnnnOooo = that.MmmmNnnnOooo;\r\n')
        self.assertEqual(result[4], '}\r\n')
