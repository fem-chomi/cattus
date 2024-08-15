from enum import Enum
from typing import List
from Model.ParameterDefine import ParameterDefine


class ConstructorType(Enum):
    OTHER = 0
    FULL = 1
    OMIT = 2
    DEFAULT = 3
    COPY = 4
    COPY_DTO = 5
    COPY_ENTITY = 6
    RESERVED = 7


class ConstructorConfig():
    def __init__(self, type: ConstructorType, enableParameter: bool, enableDefaultValue: bool, enableCopy: bool, enableCopyDto: bool, enableCopyEntity: bool):
        self.__Type: ConstructorType = type

        self.__EnableParameter: bool = enableParameter
        
        self.__EnableDefaultValue: bool = enableDefaultValue
        
        self.__EnableCopy: bool = enableCopy
        
        self.__EnableCopyDto: bool = enableCopyDto
        
        self.__EnableCopyEntity: bool = enableCopyEntity

    @property
    def Type(self) -> ConstructorType:
        return self.__Type

    @property
    def EnableParameter(self) -> bool:
        return self.__EnableParameter

    @property
    def EnableDefaultValue(self) -> bool:
        return self.__EnableDefaultValue

    @property
    def EnableCopy(self) -> bool:
        return self.__EnableCopy

    @property
    def EnableCopyDto(self) -> bool:
        return self.__EnableCopyDto

    @property
    def EnableCopyEntity(self) -> bool:
        return self.__EnableCopyEntity


class FullConstructor(ConstructorConfig):
    def __init__(self):
        enableParameter = True
        enableDefaultValue = False
        enableCopy = False
        enableCopyDto = False
        enableCopyEntity = False
        super().__init__(ConstructorType.FULL, enableParameter, enableDefaultValue, enableCopy, enableCopyDto, enableCopyEntity)


class OmitConstructor(ConstructorConfig):
    def __init__(self):
        enableParameter = True
        enableDefaultValue = True
        enableCopy = False
        enableCopyDto = False
        enableCopyEntity = False
        super().__init__(ConstructorType.OMIT, enableParameter, enableDefaultValue, enableCopy, enableCopyDto, enableCopyEntity)


class DefaultConstructor(ConstructorConfig):
    def __init__(self):
        enableParameter = False
        enableDefaultValue = False
        enableCopy = False
        enableCopyDto = False
        enableCopyEntity = False
        super().__init__(ConstructorType.DEFAULT, enableParameter, enableDefaultValue, enableCopy, enableCopyDto, enableCopyEntity)


class CopyConstructor(ConstructorConfig):
    def __init__(self):
        enableParameter = False
        enableDefaultValue = False
        enableCopy = True
        enableCopyDto = False
        enableCopyEntity = False
        super().__init__(ConstructorType.COPY, enableParameter, enableDefaultValue, enableCopy, enableCopyDto, enableCopyEntity)


class CopyDtoConstructor(ConstructorConfig):
    def __init__(self):
        enableParameter = False
        enableDefaultValue = False
        enableCopy = False
        enableCopyDto = True
        enableCopyEntity = False
        super().__init__(ConstructorType.COPY_DTO, enableParameter, enableDefaultValue, enableCopy, enableCopyDto, enableCopyEntity)


class CopyEntityConstructor(ConstructorConfig):
    def __init__(self):
        enableParameter = False
        enableDefaultValue = False
        enableCopy = False
        enableCopyDto = False
        enableCopyEntity = True
        super().__init__(ConstructorType.COPY_ENTITY, enableParameter, enableDefaultValue, enableCopy, enableCopyDto, enableCopyEntity)
