import os
from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Lang.Python.Integer import Int8, Int16, Int32, Int64
from Generator.ConstructClass import ConstructClass
from Config.ClassTypeConfig import ClassType, ClassTypeConfig, DtoClassTypeConfig, DtoBuilderClassTypeConfig, EntityClassTypeConfig, EntityBuilderClassTypeConfig, ValueObjectClassTypeConfig, DaoClassTypeConfig, SearchConditionClassTypeConfig, SortConditionClassTypeConfig, FilterConditionClassTypeConfig, ListClassTypeConfig, MapClassTypeConfig, KeyClassTypeConfig
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Util.Diff import Diff
from Util.SourceLine import SourceLine


class TestConstructClass_ConstructClass(TestCase):
    maxDiff = None
   
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()
        if os.path.isfile('aaaa_bbbb_cccc_dto.generate.py'):
            os.remove('aaaa_bbbb_cccc_dto.generate.py')
        if os.path.isfile('aaaa_bbbb_cccc_dto_builder.generate.py'):
            os.remove('aaaa_bbbb_cccc_dto_builder.generate.py')
        if os.path.isfile('aaaa_bbbb_cccc_entity.generate.py'):
            os.remove('aaaa_bbbb_cccc_entity.generate.py')
        if os.path.isfile('aaaa_bbbb_cccc_entity_builder.generate.py'):
            os.remove('aaaa_bbbb_cccc_entity_builder.generate.py')

    def test_ConstructClass_pattern_01(self):
        lang = PythonLanguage()
        test = ConstructClass(lang)
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', Int8(), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', Int16(), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', Int32(), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = DtoClassTypeConfig()
        test.ConstructClass(entityModel, config)
        self.assertEqual(Diff.DiffFile('aaaa_bbbb_cccc_dto.generate.py', 'tests/Lang/Python/testdata/test_ConstructClass_aaaa_bbbb_cccc_dto.generate.py'), '')

    def test_ConstructClass_pattern_02(self):
        lang = PythonLanguage()
        test = ConstructClass(lang)
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', Int8(), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', Int16(), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', Int32(), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = DtoBuilderClassTypeConfig()
        test.ConstructClass(entityModel, config)
        self.assertEqual(Diff.DiffFile('aaaa_bbbb_cccc_dto_builder.generate.py', 'tests/Lang/Python/testdata/test_ConstructClass_aaaa_bbbb_cccc_dto_builder.generate.py'), '')

    def test_ConstructClass_pattern_03(self):
        lang = PythonLanguage()
        test = ConstructClass(lang)
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', Int8(), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', Int16(), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', Int32(), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = EntityClassTypeConfig()
        test.ConstructClass(entityModel, config)
        self.assertEqual(Diff.DiffFile('aaaa_bbbb_cccc_entity.generate.py', 'tests/Lang/Python/testdata/test_ConstructClass_aaaa_bbbb_cccc_entity.generate.py'), '')

    def test_ConstructClass_pattern_04(self):
        lang = PythonLanguage()
        test = ConstructClass(lang)
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', Int8(), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', Int16(), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', Int32(), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        config = EntityBuilderClassTypeConfig()
        test.ConstructClass(entityModel, config)
        self.assertEqual(Diff.DiffFile('aaaa_bbbb_cccc_entity_builder.generate.py', 'tests/Lang/Python/testdata/test_ConstructClass_aaaa_bbbb_cccc_entity_builder.generate.py'), '')
