from unittest import TestCase
from Lang.Python.PythonLanguage import PythonLanguage
from Lang.Python.SQLite3.SQLite3 import SQLite3
from Config.DataTypeConfig import DataType
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine


class TestSQLite3_GenerateCreateTable(TestCase):
    def test_GenerateCreateTable_pattern_01(self):
        lang = PythonLanguage()
        test = SQLite3()
        fieldDefineList = []
        fieldDefineList.append(FieldDefine('EEEE-FFFF-GGGG', 'HHHH', lang.GetDataTypeConfig(DataType.INT8), '1'))
        fieldDefineList.append(FieldDefine('IIII-JJJJ-KKKK', 'LLLL', lang.GetDataTypeConfig(DataType.INT16), '2'))
        fieldDefineList.append(FieldDefine('MMMM-NNNN-OOOO', 'PPPP', lang.GetDataTypeConfig(DataType.INT32), '3'))
        entityModel = EntityModel('AAAA-BBBB-CCCC', 'DDDD', fieldDefineList)
        result = test.GenerateCreateTable(entityModel)
        self.assertEqual(len(result), 7)
        self.assertEqual(result[0], 'def CreateTable(filename: str) -> None:')
        self.assertEqual(result[1], '    conn = sqlite3.connect(filename)')
        self.assertEqual(result[2], '    cur = self.conn.cursor()')
        self.assertEqual(result[3], '    ddl = \'CREATE TABLE IF NOT EXISTS AAAA_BBBB_CCCC (EEEE_FFFF_GGGG integer, IIII_JJJJ_KKKK integer, MMMM_NNNN_OOOO integer) PRIMARY KEY(MMMM_NNNN_OOOO))\'')
        self.assertEqual(result[4], '    cur.execute(ddl)')
        self.assertEqual(result[5], '    cur.close()')
        self.assertEqual(result[6], '    conn.close()')
