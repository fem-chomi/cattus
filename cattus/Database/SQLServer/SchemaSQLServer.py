from typing import List
from Interface.IDatabase import DatabaseType
from Interface.IDatabaseSchema import IDatabaseSchema
from Config.DataTypeConfig import DataType
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Database.SQLServer.Integer import Int8, Int16, Int32, Int64, UInt8, UInt16, UInt32, UInt64
from Database.SQLServer.Float import Single, Double
from Database.SQLServer.Decimal import Decimal
from Database.SQLServer.String import String, FixedString, AnsiString, FixedAnsiString, SecureString
from Database.SQLServer.Boolean import Boolean
from Database.SQLServer.DateTime import DateTime, Date, Time, TimeSpan
from Database.SQLServer.UniqueID import UniqueID
from Database.SQLServer.Binary import Binary
from Database.SQLServer.Void import Void


class SchemaSQLServer(IDatabaseSchema):
    def __init__(self):
        # データ型のテーブル引き用の連想配列
        self.__DataTypeConfigMap: Dict[DataType, DataTypeConfig] = {}
        self.__DataTypeConfigMap[DataType.INT8] = Int8()
        self.__DataTypeConfigMap[DataType.INT16] = Int16()
        self.__DataTypeConfigMap[DataType.INT32] = Int32()
        self.__DataTypeConfigMap[DataType.INT64] = Int64()
        self.__DataTypeConfigMap[DataType.UINT8] = UInt8()
        self.__DataTypeConfigMap[DataType.UINT16] = UInt16()
        self.__DataTypeConfigMap[DataType.UINT32] = UInt32()
        self.__DataTypeConfigMap[DataType.UINT64] = UInt64()
        self.__DataTypeConfigMap[DataType.SINGLE] = Single()
        self.__DataTypeConfigMap[DataType.DOUBLE] = Double()
        self.__DataTypeConfigMap[DataType.DECIMAL] = Decimal()
        self.__DataTypeConfigMap[DataType.STRING] = String()
        self.__DataTypeConfigMap[DataType.FIXED_STRING] = FixedString()
        self.__DataTypeConfigMap[DataType.ANSI_STRING] = AnsiString()
        self.__DataTypeConfigMap[DataType.FIXED_ANSI_STRING] = FixedAnsiString()
        self.__DataTypeConfigMap[DataType.SECURE_STRING] = SecureString()
        self.__DataTypeConfigMap[DataType.BOOLEAN] = Boolean()
        self.__DataTypeConfigMap[DataType.DATETIME] = DateTime()
        self.__DataTypeConfigMap[DataType.DATE] = Date()
        self.__DataTypeConfigMap[DataType.TIME] = Time()
        self.__DataTypeConfigMap[DataType.TIMESPAN] = TimeSpan()
        self.__DataTypeConfigMap[DataType.UUID] = UniqueID()
        self.__DataTypeConfigMap[DataType.BINARY] = Binary()

        super().__init__(DatabaseType.SQLITE3, \
            self.__DataTypeConfigMap)

    def GenerateCreateTable(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql

    def GenerateInsert(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql

    def GenerateUpdate(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql

    def GenerateDelete(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql

    def GenerateDeleteAll(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql

    def GenerateSelect(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql

    def GenerateSearch(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql

    def GenerateSelectAll(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql

    def GenerateContainsKey(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql

    def GenerateCount(self, entityModel: EntityModel) -> str:
        sql = ''
        return sql
