import os
from unittest import TestCase
from Lang.CSharp.CSharpLanguage import CSharpLanguage
from Lang.CSharp.Integer import Int8, Int16, Int32, Int64
from Generator.ConstructClass import ConstructClass
from Config.ClassTypeConfig import ClassType, ClassTypeConfig, DtoClassType, DtoBuilderClassType, EntityClassType, EntityBuilderClassType, ValueObjectClassType, DaoClassType, SearchConditionClassType, SortConditionClassType, FilterConditionClassType, ListClassType, MapClassType, KeyClassType
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Util.SourceLine import SourceLine
from Util.Diff import Diff


class TestConstructClass_ConstructClass(TestCase):
    maxDiff = None
    
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()
        if os.path.isfile('AaaaBbbbCcccDto.generate.cs'):
            os.remove('AaaaBbbbCcccDto.generate.cs')
        if os.path.isfile('AaaaBbbbCcccDtoBuilder.generate.cs'):
            os.remove('AaaaBbbbCcccDtoBuilder.generate.cs')
        if os.path.isfile('AaaaBbbbCcccEntity.generate.cs'):
            os.remove('AaaaBbbbCcccEntity.generate.cs')
        if os.path.isfile('AaaaBbbbCcccEntityBuilder.generate.cs'):
            os.remove('AaaaBbbbCcccEntityBuilder.generate.cs')

    def test_ConstructClass_pattern_01(self):
        lang = CSharpLanguage()
        test = ConstructClass(lang)
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', Int8(), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', Int16(), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', Int32(), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = DtoClassType()
        test.ConstructClass(entityModel, config)
        self.assertEqual(Diff.DiffFile('AaaaBbbbCcccDto.generate.cs', 'tests/Lang/CSharp/testdata/test_ConstructClass_AaaaBbbbCcccDto.generate.cs'), '')

    def test_ConstructClass_pattern_02(self):
        lang = CSharpLanguage()
        test = ConstructClass(lang)
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', Int8(), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', Int16(), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', Int32(), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = DtoBuilderClassType()
        test.ConstructClass(entityModel, config)
        self.assertEqual(Diff.DiffFile('AaaaBbbbCcccDtoBuilder.generate.cs', 'tests/Lang/CSharp/testdata/test_ConstructClass_AaaaBbbbCcccDtoBuilder.generate.cs'), '')

    def test_ConstructClass_pattern_03(self):
        lang = CSharpLanguage()
        test = ConstructClass(lang)
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', Int8(), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', Int16(), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', Int32(), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = EntityClassType()
        test.ConstructClass(entityModel, config)
        self.assertEqual(Diff.DiffFile('AaaaBbbbCcccEntity.generate.cs', 'tests/Lang/CSharp/testdata/test_ConstructClass_AaaaBbbbCcccEntity.generate.cs'), '')

    def test_ConstructClass_pattern_04(self):
        lang = CSharpLanguage()
        test = ConstructClass(lang)
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', Int8(), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', Int16(), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', Int32(), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = EntityBuilderClassType()
        test.ConstructClass(entityModel, config)
        self.assertEqual(Diff.DiffFile('AaaaBbbbCcccEntityBuilder.generate.cs', 'tests/Lang/CSharp/testdata/test_ConstructClass_AaaaBbbbCcccEntityBuilder.generate.cs'), '')
