from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List, Dict, Set
from Config.ClassTypeConfig import ClassType, ClassTypeConfig, DtoClassTypeConfig, DtoBuilderClassTypeConfig, EntityClassTypeConfig, EntityBuilderClassTypeConfig, ValueObjectClassTypeConfig, DaoClassTypeConfig, SearchConditionClassTypeConfig, SortConditionClassTypeConfig, FilterConditionClassTypeConfig, ListClassTypeConfig, MapClassTypeConfig, KeyClassTypeConfig
from Config.ConstructorConfig import ConstructorType, ConstructorConfig, FullConstructor, OmitConstructor, DefaultConstructor, CopyConstructor, CopyDtoConstructor, CopyEntityConstructor
from Config.DataTypeConfig import DataType, DataTypeConfig
from Config.FunctionConfig import FunctionType, FunctionConfig
from Config.MethodConfig import MethodType, MethodConfig
from Model.ParameterDefine import ParameterDefine
from Model.ImportDefine import ImportDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine


class LanguageType(Enum):
    OTHER = 0
    CSHARP = 1
    PYTHON = 2
    JAVA = 3
    MOCK = 4
    RESERVED = 5
    

class IProgrammingLanguage(metaclass=ABCMeta):
    def __init__(self, type: LanguageType, \
            methodConfigMap: Dict[MethodType, MethodConfig], \
            functionConfigMap: Dict[FunctionType, FunctionConfig], \
            dataTypeConfigMap: Dict[DataType, DataTypeConfig]):

        # プログラミング言語タイプ
        self.__Type = type

        # クラスタイプのコンフィグ設定のテーブル引き用の連想配列
        self.__ClassTypeConfigMap: Dict[ClassType, ClassTypeConfig] = {}
        self.__ClassTypeConfigMap[ClassType.DTO] = DtoClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.DTO_BUILDER] = DtoBuilderClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.ENTITY] = EntityClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.ENTITY_BUILDER] = EntityBuilderClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.VALUE_OBJECT] = ValueObjectClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.DAO] = DaoClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.SEARCH_CONDITION] = SearchConditionClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.SORT_CONDITION] = SortConditionClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.FILTER_CONDITION] = FilterConditionClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.LIST] = ListClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.MAP] = MapClassTypeConfig()
        self.__ClassTypeConfigMap[ClassType.KEY] = KeyClassTypeConfig()

        # コンストラクタのテーブル引き用の連想配列
        self.__ConstructorConfigMap: Dict[ConstructorType, ConstructorConfig] = {}
        self.__ConstructorConfigMap[ConstructorType.FULL] = FullConstructor()
        self.__ConstructorConfigMap[ConstructorType.OMIT] = OmitConstructor()
        self.__ConstructorConfigMap[ConstructorType.DEFAULT] = DefaultConstructor()
        self.__ConstructorConfigMap[ConstructorType.COPY] = CopyConstructor()
        self.__ConstructorConfigMap[ConstructorType.COPY_DTO] = CopyDtoConstructor()
        self.__ConstructorConfigMap[ConstructorType.COPY_ENTITY] = CopyEntityConstructor()
        
        # メソッドのテーブル引き用の連想配列
        self.__MethodConfigMap: Dict[MethodType, MethodConfig] = methodConfigMap
        
        # 関数のテーブル引き用の連想配列
        self.__FunctionConfigMap: Dict[FunctionType, FunctionConfig] = functionConfigMap
        
        # データ型のテーブル引き用の連想配列
        self.__DataTypeConfigMap: Dict[DataType, DataTypeConfig] = dataTypeConfigMap

        self.__ImportDefineSet: Set[ImportDefine] = set()

    @property
    def Type(self) -> LanguageType:
        return self.__Type

    @property
    def ImportDefineSet(self) -> Set[ImportDefine]:
        return self.__ImportDefineSet

    def GetClassTypeConfig(self, key: ClassType) -> ClassTypeConfig:
        return self.__ClassTypeConfigMap[key]

    def GetConstructorConfig(self, key: ConstructorType) -> ConstructorConfig:
        return self.__ConstructorConfigMap[key]

    def GetMethodConfig(self, key: MethodType) -> MethodConfig:
        return self.__MethodConfigMap[key]

    def GetFunctionConfig(self, key: FunctionType) -> FunctionConfig:
        return self.__FunctionConfigMap[key]

    def GetDataTypeConfig(self, key: DataType) -> DataTypeConfig:
        return self.__DataTypeConfigMap[key]

    def AppendImportDefine(self, importDefine: ImportDefine) -> None:
        self.__ImportDefineSet.add(importDefine)

    def ClearImportDefine(self) -> None:
        self.__ImportDefineSet = set()

    @abstractmethod
    def GetFileName(self, filename: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GetFileExtName(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateImport(self) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateNamespaceBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateNamespaceEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GetNamespaceName(self, name: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateClassBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GenerateClassEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GetClassName(self, name: str, config: ClassTypeConfig) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateConstructor(self, constructorConfig: ConstructorConfig, entityModel: EntityModel, config: ClassTypeConfig, thatClassTypeConfig: ClassTypeConfig=None) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GetConstructorName(self, name: str, config: ClassTypeConfig) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def GenerateField(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GetFieldName(self, name: str) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def GenerateProperty(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GetPropertyName(self, name: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateParameter(self, parameterDefine: ParameterDefine, enableDefaultValue=False) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GetParameterName(self, name: str) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def GenerateMethod(self, methodConfig: MethodConfig, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GetMethodName(self, name: str) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def GenerateFunction(self, functionConfig: FunctionConfig, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        raise NotImplementedError()

    @abstractmethod
    def GetFunctionName(self, name: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GetDataTypeName(self, dataTypeConfig: DataTypeConfig, entityModel: EntityModel=None, config: ClassTypeConfig=None) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GenerateConstantValue(self, name: str, dataTypeConfig: DataTypeConfig, value: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def GetConstantValueName(self, name: str) -> str:
        raise NotImplementedError()
