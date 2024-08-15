from Config.DataTypeConfig import DataTypeConfig


class FieldDefine():
    def __init__(self, fieldName: str, \
            description: str, \
            DataTypeConfig: DataTypeConfig, \
            defaultValue: str = '', \
            isKey: bool = False):
        
        # フィールド名
        self.__FieldName: str = fieldName
        
        # フィールドの概要
        self.__Description: str = description
        
        # フィールドのデータ型
        self.__DataTypeConfig: DataTypeConfig = DataTypeConfig

        # 既定値
        self.__DefaultValue: str = defaultValue

        # キー制約フラグ
        self.__IsKey: bool = isKey

    @property
    def FieldName(self) -> str:
        return self.__FieldName

    @property
    def Description(self) -> str:
        return self.__Description

    @property
    def DataTypeConfig(self) -> DataTypeConfig:
        return self.__DataTypeConfig

    @property
    def DefaultValue(self) -> str:
        return self.__DefaultValue

    @property
    def IsKey(self) -> bool:
        return self.__IsKey
