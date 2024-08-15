from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from .ClassTypeConfig import ClassType, ClassTypeConfig
from .DataTypeConfig import DataTypeConfig


class FunctionType(Enum):
    OTHER = 0
    DUMMY = 1
    RESERVED = 2


class FunctionConfig():
    def __init__(self, type: FunctionType, functionName: str, description: str, parameterList: List[ParameterDefine], returnType: DataTypeConfig):
        self.__Type: FunctionType = type

        # 関数名
        self.__FunctionName: str = functionName
        
        # 関数の概要
        self.__Description: str = description

        # パラメータリスト
        self.__ParameterList: List[ParameterDefine] = parameterList

        # 戻り値のデータ型
        self.__ReturnType: DataTypeConfig = returnType

    @property
    def Type(self) -> FunctionType:
        return self.__Type

    @property
    def FunctionName(self) -> str:
        return self.__FunctionName

    @property
    def Description(self) -> str:
        return self.__Description

    @property
    def ParameterList(self) -> List[ParameterDefine]:
        return self.__ParameterList

    @property
    def ReturnType(self) -> DataTypeConfig:
        return self.__ReturnType
    
    @abstractmethod
    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()
