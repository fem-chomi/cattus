from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from .ClassTypeConfig import ClassType, ClassTypeConfig
from .DataTypeConfig import DataType, AllocationType, DataTypeConfig


class MethodType(Enum):
    OTHER = 0

    # DTO, DTO Builder, Entity, EntityBuilder, ValueObject
    TO_STRING = 1
    EQUAL = 2
    COMPARE_TO = 3
    GET_HASH_CODE = 4
    EXPORT = 5
    IMPORT = 6
    BUILD_DTO = 7
    BUILD_ENTITY = 8
    
    # DAO
    CREATE_TABLE = 9
    INSERT = 10
    BULK_INSERT = 11
    MODIFY = 12
    UPDATE = 13
    UPSERT = 14
    DELTA_UPDATE =15
    DELETE = 16
    DELETE_ALL = 17
    SELECT = 18
    SEARCH = 19
    READ_RECORD = 20
    SELECT_ALL = 21
    CONTAINS_KEY = 22
    COUNT = 23

    RESERVED = 24


class MethodConfig():
    def __init__(self, type: MethodType, methodName: str, description: str, parameterList: List[ParameterDefine], returnType: DataTypeConfig, isOverride: bool=False):
        self.__Type: MethodType = type

        # メソッド名
        self.__MethodName: str = methodName
        
        # メソッドの概要
        self.__Description: str = description

        # パラメータリスト
        self.__ParameterList: List[ParameterDefine] = parameterList

        # 戻り値のデータ型
        self.__ReturnType: DataTypeConfig = returnType

        # オーバーライドの有無
        self.__IsOverride: bool = isOverride

    @property
    def Type(self) -> MethodType:
        return self.__Type

    @property
    def MethodName(self) -> str:
        return self.__MethodName

    @property
    def Description(self) -> str:
        return self.__Description

    @property
    def ParameterList(self) -> List[ParameterDefine]:
        return self.__ParameterList

    @property
    def ReturnType(self) -> DataTypeConfig:
        return self.__ReturnType

    @property
    def IsOverride(self) -> bool:
        return self.__IsOverride

    @abstractmethod
    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()
