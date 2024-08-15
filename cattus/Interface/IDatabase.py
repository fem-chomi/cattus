from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List, Dict, Set
from Model.EntityModel import EntityModel


class DatabaseType(Enum):
    OTHER = 0
    SQLITE3 = 1
    SQL_SERVER = 2
    POSTGRESQL = 3
    MYSQL = 4
    ORACLE = 5
    RESERVED = 6
    

class IDatabase(metaclass=ABCMeta):
    def __init__(self, type: DatabaseType):

        # データベースタイプ
        self.__Type = type

    @abstractmethod
    def GenerateCreateTable(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateInsert(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateBulkInsert(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateModify(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateUpdate(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateUpsert(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateDeltaUpdate(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateDelete(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateDeleteAll(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateSelect(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateSearch(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateReadRecord(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateSelectAll(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateContainsKey(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateCount(self, entityModel: EntityModel) -> List[str]:
        raise NotImplementedError()
