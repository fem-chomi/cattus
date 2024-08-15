from typing import List
from Interface.IDatabase import DatabaseType
from Interface.IDatabaseSchema import IDatabaseSchema
from Config.DataTypeConfig import DataType
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Database.SQLite3.Integer import Int8, Int16, Int32, Int64, UInt8, UInt16, UInt32, UInt64
from Database.SQLite3.Float import Single, Double
from Database.SQLite3.Decimal import Decimal
from Database.SQLite3.String import String, FixedString, AnsiString, FixedAnsiString, SecureString
from Database.SQLite3.Boolean import Boolean
from Database.SQLite3.DateTime import DateTime, Date, Time, TimeSpan
from Database.SQLite3.UniqueID import UniqueID
from Database.SQLite3.Binary import Binary
from Database.SQLite3.Void import Void
from Util.NameConverter import NameConverter
import Util


class SchemaSQLite3(IDatabaseSchema):
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
        first = Util.First(', ')
        sql = f'CREATE TABLE IF NOT EXISTS {NameConverter.ToUpperSnakeCase(entityModel.EntityName)} ('
        for field in entityModel.FieldDefineList:
            sql += first.Delimiter()
            sql += f'{NameConverter.ToUpperSnakeCase(field.FieldName)}'
            if field.DataTypeConfig is not None:
                if field.DataTypeConfig.Type in self.__DataTypeConfigMap:
                    sql += f' {self.__DataTypeConfigMap[field.DataTypeConfig.Type].DataTypeName}'
                if field.DataTypeConfig.NotNull:
                    sql += f' NOT NULL'
        sql += ');'
        return sql

    def GenerateInsert(self, entityModel: EntityModel) -> str:
        first1 = Util.First(', ')
        first2 = Util.First(', ')
        sql = f'INSERT INTO {NameConverter.ToUpperSnakeCase(entityModel.EntityName)} ('
        for field in entityModel.FieldDefineList:
            sql += first1.Delimiter()
            sql += f'{NameConverter.ToUpperSnakeCase(field.FieldName)}'
        sql += f') VALUES ('
        for field in entityModel.FieldDefineList:
            sql += first2.Delimiter()
            sql += f'@{NameConverter.ToUpperCamelCase(field.FieldName)}'
        sql += ')'
        return sql

    def __GetWhere(self, entityModel: EntityModel) -> str:
        first = Util.First(', ')
        sql = ' WHERE '
        containKey = False
        for field in entityModel.FieldDefineList:
            if field.IsKey:
                sql += first.Delimiter()
                sql += f'{NameConverter.ToUpperSnakeCase(field.FieldName)} = @{NameConverter.ToUpperCamelCase(field.FieldName)}'
                containKey = True
        if not containKey:
            raise KeyError()
        return sql

    def GenerateUpdate(self, entityModel: EntityModel) -> str:
        first = Util.First(', ')
        sql = f'UPDATE {NameConverter.ToUpperSnakeCase(entityModel.EntityName)} SET '
        for field in entityModel.FieldDefineList:
            if not field.IsKey:
                sql += first.Delimiter()
                sql += f'{NameConverter.ToUpperSnakeCase(field.FieldName)} = @{NameConverter.ToUpperCamelCase(field.FieldName)}'
        sql += self.__GetWhere(entityModel)
        return sql

    def GenerateDelete(self, entityModel: EntityModel) -> str:
        return self.GenerateDeleteAll(entityModel) + self.__GetWhere(entityModel)

    def GenerateDeleteAll(self, entityModel: EntityModel) -> str:
        first = Util.First(', ')
        sql = f'DELETE FROM {NameConverter.ToUpperSnakeCase(entityModel.EntityName)}'
        return sql

    def GenerateSelect(self, entityModel: EntityModel) -> str:
        return self.GenerateSelectAll(entityModel) + self.__GetWhere(entityModel)

    def GenerateSearch(self, entityModel: EntityModel) -> str:
        return sql

    def GenerateSelectAll(self, entityModel: EntityModel) -> str:
        first = Util.First(', ')
        sql = f'SELECT '
        for field in entityModel.FieldDefineList:
            sql += first.Delimiter()
            sql += f'{NameConverter.ToUpperSnakeCase(field.FieldName)}'
        sql += f' FROM {NameConverter.ToUpperSnakeCase(entityModel.EntityName)}'
        return sql

    def GenerateContainsKey(self, entityModel: EntityModel) -> str:
        return sql

    def GenerateCount(self, entityModel: EntityModel) -> str:
        return sql
