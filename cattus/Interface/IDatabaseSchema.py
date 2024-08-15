from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List, Dict, Set
from .IDatabase import DatabaseType
from Config.DataTypeConfig import DataType, DataTypeConfig
from Model.EntityModel import EntityModel
    

class IDatabaseSchema(metaclass=ABCMeta):
    def __init__(self, type: DatabaseType, \
            dataTypeConfigMap: Dict[DataType, DataTypeConfig]):

        # データベースタイプ
        self.__Type = type

        # クラスタイプのコンフィグ設定のテーブル引き用の連想配列
        self.__ClassTypeConfigMap: Dict[ClassType, ClassTypeConfig] = dataTypeConfigMap

    def GetDataTypeConfig(self, key: DataType) -> DataTypeConfig:
        if self.__ClassTypeConfigMap is not None:
            if key in self.__ClassTypeConfigMap:
                return self.__ClassTypeConfigMap[key]
        return None

    @abstractmethod
    def GenerateCreateTable(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateInsert(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateUpdate(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateDelete(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateDeleteAll(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateSelect(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateSearch(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateSelectAll(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateContainsKey(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateCount(self, entityModel: EntityModel) -> str:
        raise NotImplementedError()
