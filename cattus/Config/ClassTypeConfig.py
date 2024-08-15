from enum import Enum
from typing import Self, Dict


class ClassType(Enum):
    OTHER = 0
    DTO = 1
    DTO_BUILDER = 2
    ENTITY = 3
    ENTITY_BUILDER = 4
    VALUE_OBJECT = 5
    DAO = 6
    SEARCH_CONDITION = 7
    SORT_CONDITION = 8
    FILTER_CONDITION = 9
    LIST = 10
    MAP = 11
    SET = 12
    KEY = 13
    RESERVED = 14


class ClassTypeConfig():
    __classSuffixNameMap: Dict[ClassType, str] = {\
        ClassType.DTO: 'DTO', \
        ClassType.DTO_BUILDER: 'DTO-BUILDER', \
        ClassType.ENTITY: 'ENTITY', \
        ClassType.ENTITY_BUILDER: 'ENTITY-BUILDER', \
        ClassType.VALUE_OBJECT: 'VALUE-OBJECT', \
        ClassType.DAO: 'DAO', \
        ClassType.SEARCH_CONDITION: 'SEARCH-CONDITION', \
        ClassType.SORT_CONDITION: 'SORT-CONDITION', \
        ClassType.FILTER_CONDITION: 'FILTER_CONDITION', \
        ClassType.LIST: 'LIST', \
        ClassType.MAP: 'MAP', \
        ClassType.SET: 'SET', \
        ClassType.KEY: 'KEY', \
    }

    def __init__(self, \
            type: ClassType, \
            classSuffixName: str='', \
            enableNamespace: bool=False, \
            enableClass: bool=False, \
            enableField: bool=False, \
            enableProperty: bool=False, \
            enableFullConstructor: bool=False, \
            enableOmitConstructor: bool=False, \
            enableCopyConstructor: bool=False, \
            enableCopyDtoConstructor: bool=False, \
            enableCopyEntityConstructor: bool=False, \

            # DTO, DTO Builder, Entity, Entity Builder, ValueObject
            enableToString: bool=False, \
            enableEqual: bool=False, \
            enableCompareTo: bool=False, \
            enableGetHashCode: bool=False, \
            enableExport: bool=False, \
            enableImport: bool=False, \
            enableBuildDto: bool=False, \
            enableBuildEntity: bool=False, \
            enableImmutable: bool=False, \
            enablePythonSpecialDataClass: bool=False, \

            # DAO
            createTable: bool=False, \
            insert: bool=False, \
            bulkInsert: bool=False, \
            modify: bool=False, \
            update: bool=False, \
            upsert: bool=False, \
            deltaUpdate: bool=False, \
            delete: bool=False, \
            deleteAll: bool=False, \
            select: bool=False, \
            search: bool=False, \
            readRecord: bool=False, \
            selectAll: bool=False, \
            containsKey: bool=False, \
            count: bool=False):
        self.__Type: ClassType = type
        if classSuffixName != '':
            self.__ClassSuffixName: str = classSuffixName
        else:
            self.__ClassSuffixName: str = self.__classSuffixNameMap[type]
        self.__EnableNamespace: bool = enableNamespace
        self.__EnableClass: bool = enableClass
        self.__EnableField: bool = enableField
        self.__EnableProperty: bool = enableProperty
        self.__EnableFullConstructor: bool = enableFullConstructor
        self.__EnableOmitConstructor: bool = enableOmitConstructor
        self.__EnableCopyConstructor: bool = enableCopyConstructor
        self.__EnableCopyDtoConstructor: bool = enableCopyDtoConstructor
        self.__EnableCopyEntityConstructor: bool = enableCopyEntityConstructor
        
        # DTO, DTO Builder, Entity, Entity Builder, ValueObject
        self.__EnableToString: bool = enableToString
        self.__EnableEqual: bool = enableEqual
        self.__EnableCompareTo: bool = enableCompareTo
        self.__EnableGetHashCode: bool = enableGetHashCode
        self.__EnableExport: bool = enableExport
        self.__EnableImport: bool = enableImport
        self.__EnableBuildDto: bool = enableBuildDto
        self.__EnableBuildEntity: bool = enableBuildEntity
        self.__EnableImmutable: bool = enableImmutable
        self.__EnablePythonSpecialDataClass: bool = enablePythonSpecialDataClass

        # DAO
        self.__CreateTable: bool = createTable
        self.__Insert: bool = insert
        self.__BulkInsert: bool = bulkInsert
        self.__Modify: bool = modify
        self.__Update: bool = update
        self.__Upsert: bool = upsert
        self.__DeltaUpdate: bool = deltaUpdate
        self.__Delete: bool = delete
        self.__DeleteAll: bool = deleteAll
        self.__Select: bool = select
        self.__Search: bool = search
        self.__ReadRecord: bool = readRecord
        self.__SelectAll: bool = selectAll
        self.__ContainsKey: bool = containsKey
        self.__Count: bool = count

    @property
    def Type(self) -> ClassType:
        return self.__Type

    # Namespaceを有効化する
    @property
    def EnableNamespace(self) -> bool:
        return self.__EnableNamespace

    # Classを有効化する
    @property
    def EnableClass(self) -> bool:
        return self.__EnableClass

    # Fieldを有効化する
    @property
    def EnableField(self) -> bool:
        return self.__EnableField

    # Propertyを有効化する
    @property
    def EnableProperty(self) -> bool:
        return self.__EnableProperty

    # FullConstructorを有効化する
    @property
    def EnableFullConstructor(self) -> bool:
        return self.__EnableFullConstructor

    # OmitConstructorを有効化する
    @property
    def EnableOmitConstructor(self) -> bool:
        return self.__EnableOmitConstructor

    # CopyConstructorを有効化する
    @property
    def EnableCopyConstructor(self) -> bool:
        return self.__EnableCopyConstructor

    # CopyDtoConstructorを有効化する
    @property
    def EnableCopyDtoConstructor(self) -> bool:
        return self.__EnableCopyDtoConstructor

    # CopyEntityConstructorを有効化する
    @property
    def EnableCopyEntityConstructor(self) -> bool:
        return self.__EnableCopyEntityConstructor

    # ToStringを有効化する
    @property
    def EnableToString(self) -> bool:
        return self.__EnableToString

    # Equalを有効化する
    @property
    def EnableEqual(self) -> bool:
        return self.__EnableEqual

    # CompareToを有効化する
    @property
    def EnableCompareTo(self) -> bool:
        return self.__EnableCompareTo

    # GetHashCodeを有効化する
    @property
    def EnableGetHashCode(self) -> bool:
        return self.__EnableGetHashCode

    # Exportを有効化する
    @property
    def EnableExport(self) -> bool:
        return self.__EnableExport

    # Importを有効化する
    @property
    def EnableImport(self) -> bool:
        return self.__EnableImport

    # BuildDtoを有効化する
    @property
    def EnableBuildDto(self) -> bool:
        return self.__EnableBuildDto

    # BuildEntityを有効化する
    @property
    def EnableBuildEntity(self) -> bool:
        return self.__EnableBuildEntity

    # イミュータブルを有効化する
    @property
    def EnableImmutable(self) -> bool:
        return self.__EnableImmutable

    @property
    def ClassSuffixName(self) -> str:
        return self.__ClassSuffixName

    @property
    def EnablePythonSpecialDataClass(self) -> bool:
        return self.__EnablePythonSpecialDataClass

    @property
    def CreateTable(self) -> bool:
        return self.__CreateTable

    @property
    def Insert(self) -> bool:
        return self.__Insert

    @property
    def BulkInsert(self) -> bool:
        return self.__BulkInsert

    @property
    def Modify(self) -> bool:
        return self.__Modify

    @property
    def Update(self) -> bool:
        return self.__Update

    @property
    def Upsert(self) -> bool:
        return self.__Upsert

    @property
    def DeltaUpdate(self) -> bool:
        return self.__DeltaUpdate

    @property
    def Delete(self) -> bool:
        return self.__Delete

    @property
    def DeleteAll(self) -> bool:
        return self.__DeleteAll

    @property
    def Select(self) -> bool:
        return self.__Select

    @property
    def Search(self) -> bool:
        return self.__Search

    @property
    def ReadRecord(self) -> bool:
        return self.__ReadRecord

    @property
    def SelectAll(self) -> bool:
        return self.__SelectAll

    @property
    def ContainsKey(self) -> bool:
        return self.__ContainsKey

    @property
    def Count(self) -> bool:
        return self.__Count

    def ConvertClassType(self, type: ClassType, classSuffixName: str='') -> Self:
        _classSuffixName = ''
        if classSuffixName != '':
            _classSuffixName: str = classSuffixName
        else:
            _classSuffixName: str = self.__classSuffixNameMap[type]
        temp = ClassTypeConfig(
            type, \
            _classSuffixName, \
            self.__EnableNamespace, \
            self.__EnableClass, \
            self.__EnableField, \
            self.__EnableProperty, \
            self.__EnableFullConstructor, \
            self.__EnableOmitConstructor, \
            self.__EnableCopyConstructor, \
            self.__EnableCopyDtoConstructor, \
            self.__EnableCopyEntityConstructor, \
            self.__EnableToString, \
            self.__EnableEqual, \
            self.__EnableCompareTo, \
            self.__EnableGetHashCode, \
            self.__EnableExport, \
            self.__EnableImport, \
            self.__EnableBuildDto, \
            self.__EnableBuildEntity, \
            self.__EnableImmutable, \
            self.__EnablePythonSpecialDataClass)

        return temp


class DtoClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = True
        enableProperty: bool = True
        enableFullConstructor: bool = True
        enableOmitConstructor: bool = True
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = True
        enableEqual: bool = True
        enableCompareTo: bool = True
        enableGetHashCode: bool = True
        enableExport: bool = True
        enableImport: bool = True
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = True
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.DTO, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class DtoBuilderClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = True
        enableProperty: bool = True
        enableFullConstructor: bool = True
        enableOmitConstructor: bool = True
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = True
        enableCopyEntityConstructor: bool = False
        enableToString: bool = False
        enableEqual: bool = False
        enableCompareTo: bool = False
        enableGetHashCode: bool = False
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = True
        enableBuildEntity: bool = False
        enableImmutable: bool = False
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.DTO_BUILDER, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class EntityClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = True
        enableProperty: bool = True
        enableFullConstructor: bool = True
        enableOmitConstructor: bool = True
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = True
        enableEqual: bool = True
        enableCompareTo: bool = True
        enableGetHashCode: bool = True
        enableExport: bool = True
        enableImport: bool = True
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = True
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.ENTITY, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class EntityBuilderClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = True
        enableProperty: bool = True
        enableFullConstructor: bool = True
        enableOmitConstructor: bool = True
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = True
        enableToString: bool = False
        enableEqual: bool = False
        enableCompareTo: bool = False
        enableGetHashCode: bool = False
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = False
        enableBuildEntity: bool = True
        enableImmutable: bool = False
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.ENTITY_BUILDER, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class ValueObjectClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = True
        enableProperty: bool = True
        enableFullConstructor: bool = True
        enableOmitConstructor: bool = True
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = True
        enableEqual: bool = True
        enableCompareTo: bool = True
        enableGetHashCode: bool = True
        enableExport: bool = True
        enableImport: bool = True
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = True
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.VALUE_OBJECT, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class DaoClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = False
        enableProperty: bool = False
        enableFullConstructor: bool = False
        enableOmitConstructor: bool = False
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = False
        enableEqual: bool = False
        enableCompareTo: bool = False
        enableGetHashCode: bool = False
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = True
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.DAO, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class SearchConditionClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = True
        enableProperty: bool = True
        enableFullConstructor: bool = True
        enableOmitConstructor: bool = True
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = True
        enableEqual: bool = True
        enableCompareTo: bool = True
        enableGetHashCode: bool = True
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = True
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.SEARCH_CONDITION, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class SortConditionClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = True
        enableProperty: bool = True
        enableFullConstructor: bool = True
        enableOmitConstructor: bool = True
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = True
        enableEqual: bool = True
        enableCompareTo: bool = True
        enableGetHashCode: bool = True
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = True
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.SORT_CONDITION, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class FilterConditionClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = True
        enableProperty: bool = True
        enableFullConstructor: bool = True
        enableOmitConstructor: bool = True
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = True
        enableEqual: bool = True
        enableCompareTo: bool = True
        enableGetHashCode: bool = True
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = True
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.FILTER_CONDITION, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class ListClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = False
        enableProperty: bool = False
        enableFullConstructor: bool = False
        enableOmitConstructor: bool = False
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = False
        enableEqual: bool = False
        enableCompareTo: bool = False
        enableGetHashCode: bool = False
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = False
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.LIST, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class MapClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = False
        enableProperty: bool = False
        enableFullConstructor: bool = False
        enableOmitConstructor: bool = False
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = False
        enableEqual: bool = False
        enableCompareTo: bool = False
        enableGetHashCode: bool = False
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = False
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.MAP, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class SetClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = False
        enableProperty: bool = False
        enableFullConstructor: bool = False
        enableOmitConstructor: bool = False
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = False
        enableEqual: bool = False
        enableCompareTo: bool = False
        enableGetHashCode: bool = False
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = False
        enablePythonSpecialDataClass: bool = False
        super().__init__(ClassType.SET, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)


class KeyClassType(ClassTypeConfig):
    def __init__(self):
        classSuffixName: str = ''
        enableNamespace: bool = True
        enableClass: bool = True
        enableField: bool = True
        enableProperty: bool = True
        enableFullConstructor: bool = True
        enableOmitConstructor: bool = True
        enableCopyConstructor: bool = False
        enableCopyDtoConstructor: bool = False
        enableCopyEntityConstructor: bool = False
        enableToString: bool = True
        enableEqual: bool = True
        enableCompareTo: bool = True
        enableGetHashCode: bool = True
        enableExport: bool = False
        enableImport: bool = False
        enableBuildDto: bool = False
        enableBuildEntity: bool = False
        enableImmutable: bool = True
        enablePythonSpecialDataClass: bool =False
        super().__init__(ClassType.KEY, \
            classSuffixName, \
            enableNamespace, \
            enableClass, \
            enableField, \
            enableProperty, \
            enableFullConstructor, \
            enableOmitConstructor, \
            enableCopyConstructor, \
            enableCopyDtoConstructor, \
            enableCopyEntityConstructor, \
            enableToString, \
            enableEqual, \
            enableCompareTo, \
            enableGetHashCode, \
            enableExport, \
            enableImport, \
            enableBuildDto, \
            enableBuildEntity, \
            enableImmutable, \
            enablePythonSpecialDataClass)
