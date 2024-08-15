from Config.DataTypeConfig import DataTypeConfig


class ParameterDefine():
    def __init__(self, parameterName: str, \
            description: str, \
            DataTypeConfig: DataTypeConfig, \
            defaultValue: str = ''):
        
        # パラメータ名
        self.__ParameterName: str = parameterName
        
        # パラメータの概要
        self.__Description: str = description
        
        # パラメータのデータ型
        self.__DataTypeConfig: DataTypeConfig = DataTypeConfig

        # 既定値
        self.__DefaultValue: str = defaultValue
    
    @property
    def ParameterName(self) -> str:
        return self.__ParameterName
    
    @property
    def Description(self) -> str:
        return self.__Description
    
    @property
    def DataTypeConfig(self) -> DataTypeConfig:
        return self.__DataTypeConfig

    @property
    def DefaultValue(self) -> str:
        return self.__DefaultValue
