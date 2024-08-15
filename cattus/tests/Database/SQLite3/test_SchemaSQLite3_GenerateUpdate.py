from unittest import TestCase
from Config.DataTypeConfig import DataType
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Database.SQLite3.SchemaSQLite3 import SchemaSQLite3


class TestSchemaSQLite3_GenerateUpdate(TestCase):
    def test_GenerateUpdate_pattern_01(self):
        test = SchemaSQLite3()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8), isKey=True))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16)))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32)))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        result = test.GenerateUpdate(entityModel)
        self.assertEqual(result, 'UPDATE AAAA_BBBB_CCCC SET IIII_JJJJ_KKKK = @IiiiJjjjKkkk, MMMM_NNNN_OOOO = @MmmmNnnnOooo WHERE EEEE_FFFF_GGGG = @EeeeFfffGggg')
