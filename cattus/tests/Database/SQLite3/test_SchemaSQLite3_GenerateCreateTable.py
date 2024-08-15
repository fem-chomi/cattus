from unittest import TestCase
from Config.DataTypeConfig import DataType
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Database.SQLite3.SchemaSQLite3 import SchemaSQLite3


class TestSchemaSQLite3_GenerateCreateTable(TestCase):
    def test_GenerateCreateTable_pattern_01(self):
        test = SchemaSQLite3()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', test.GetDataTypeConfig(DataType.INT8)))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', test.GetDataTypeConfig(DataType.INT16)))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', test.GetDataTypeConfig(DataType.INT32)))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        result = test.GenerateCreateTable(entityModel)
        self.assertEqual(result, 'CREATE TABLE IF NOT EXISTS AAAA_BBBB_CCCC (EEEE_FFFF_GGGG INTEGER NOT NULL, IIII_JJJJ_KKKK INTEGER NOT NULL, MMMM_NNNN_OOOO INTEGER NOT NULL);')
