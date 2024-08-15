from typing import List
from .FieldDefine import FieldDefine


class EntityModel():
    def __init__(self, entityName: str, description: str, fieldDefineList: List[FieldDefine]):
        # エンティティ名
        self.__EntityName: str = entityName

        # エンティティの概要
        self.__Description: str = description
        
        # フィールドリスト
        self.__FieldDefineList: List[FieldDefine] = fieldDefineList

    # エンティティ名
    @property
    def EntityName(self) -> str:
        return self.__EntityName

    # エンティティの概要
    @property
    def Description(self) -> str:
        return self.__Description

    # フィールドリスト
    @property
    def FieldDefineList(self) -> List[FieldDefine]:
        return self.__FieldDefineList
