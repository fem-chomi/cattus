from typing import List, Dict
from Interface.IProgrammingLanguage import LanguageType, IProgrammingLanguage
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Config.ConstructorConfig import ConstructorConfig
from Config.DataTypeConfig import DataType, DataTypeConfig
from Config.FunctionConfig import FunctionType, FunctionConfig
from Config.MethodConfig import MethodType, MethodConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.Python.Integer import Int8, Int16, Int32, Int64, UInt8, UInt16, UInt32, UInt64
from Lang.Python.Float import Single, Double
from Lang.Python.Decimal import Decimal
from Lang.Python.String import String, FixedString, AnsiString, FixedAnsiString, SecureString
from Lang.Python.Boolean import Boolean
from Lang.Python.DateTime import DateTime, Date, Time, TimeSpan
from Lang.Python.UniqueID import UniqueID
from Lang.Python.Binary import Binary
from Lang.Python.Classes import Class, Struct, Enum, ValueObject, UserClass
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class MockLanguage(IProgrammingLanguage):
    def __init__(self):
        # メソッドのテーブル引き用の連想配列
        self.__MethodConfigMap: Dict[MethodType, MethodConfig] = {}
        
        # 関数のテーブル引き用の連想配列
        self.__FunctionConfigMap: Dict[FunctionType, FunctionConfig] = {}

        # データ型のテーブル引き用の連想配列
        self.__DataTypeConfigMap: Dict[DataType, DataTypeConfig] = {}
        self.__DataTypeConfigMap[DataType.INT8] = Int8()
        self.__DataTypeConfigMap[DataType.INT16] = Int16()
        self.__DataTypeConfigMap[DataType.INT32] = Int32()
        self.__DataTypeConfigMap[DataType.INT64] = Int64()
        self.__DataTypeConfigMap[DataType.UINT8] = UInt8()
        self.__DataTypeConfigMap[DataType.UINT16] = UInt16()
        self.__DataTypeConfigMap[DataType.UINT32] = UInt32()
        self.__DataTypeConfigMap[DataType.UINT64] = UInt64()
        self.__DataTypeConfigMap[DataType.SINGLE] = Single()
        self.__DataTypeConfigMap[DataType.DOUBLE] = Double()
        self.__DataTypeConfigMap[DataType.DECIMAL] = Decimal()
        self.__DataTypeConfigMap[DataType.STRING] = String()
        self.__DataTypeConfigMap[DataType.FIXED_STRING] = FixedString()
        self.__DataTypeConfigMap[DataType.ANSI_STRING] = AnsiString()
        self.__DataTypeConfigMap[DataType.FIXED_ANSI_STRING] = FixedAnsiString()
        self.__DataTypeConfigMap[DataType.SECURE_STRING] = SecureString()
        self.__DataTypeConfigMap[DataType.BOOLEAN] = Boolean()
        self.__DataTypeConfigMap[DataType.DATETIME] = DateTime()
        self.__DataTypeConfigMap[DataType.DATE] = Date()
        self.__DataTypeConfigMap[DataType.TIME] = Time()
        self.__DataTypeConfigMap[DataType.TIMESPAN] = TimeSpan()
        self.__DataTypeConfigMap[DataType.UUID] = UniqueID()
        self.__DataTypeConfigMap[DataType.BINARY] = Binary()
        self.__DataTypeConfigMap[DataType.CLASS] = Class()
        self.__DataTypeConfigMap[DataType.STRUCT] = Struct()
        self.__DataTypeConfigMap[DataType.ENUM] = Enum()
        self.__DataTypeConfigMap[DataType.VALUE_OBJECT] = ValueObject()
        self.__DataTypeConfigMap[DataType.USER_CLASS] = UserClass()

        super().__init__(LanguageType.MOCK, \
            self.__MethodConfigMap, \
            self.__FunctionConfigMap, \
            self.__DataTypeConfigMap)

    def GetFileName(self, filename: str) -> str:
        return 'GetFileName()'

    def GetFileExtName(self) -> str:
        return 'GetFileExtName()'

    def GenerateImport(self) -> List[str]:
        return 'GenerateImport()'

    def GenerateNamespaceBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateNamespaceBeginBlock()')
        return codes

    def GenerateNamespaceEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateNamespaceEndBlock()')
        return codes

    def GetNamespaceName(self, name: str) -> str:
        return 'GetNamespaceName()'

    def GenerateClassBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateClassBeginBlock()')
        return codes

    def GenerateClassEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateClassEndBlock()')
        return codes

    def GetClassName(self, name: str, config: ClassTypeConfig) -> str:
        return 'GetClassName()'

    def GenerateConstructor(self, constructorConfig: ConstructorConfig, entityModel: EntityModel, config: ClassTypeConfig, thatClassTypeConfig: ClassTypeConfig=None) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateConstructor()')
        return codes

    def GetConstructorName(self, name: str, config: ClassTypeConfig) -> str:
        return 'GetConstructorName()'
    
    def GenerateField(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateField()')
        return codes

    def GetFieldName(self, name: str) -> str:
        return 'GetFieldName()'
    
    def GenerateProperty(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateProperty()')
        return codes

    def GetPropertyName(self, name: str) -> str:
        return 'GetPropertyName()'

    def GenerateParameter(self, parameterDefine: ParameterDefine) -> str:
        return 'GenerateParameter()'
        
    def GetParameterName(self, name: str) -> str:
        return 'GetParameterName()'
    
    def GenerateMethod(self, methodConfig: MethodConfig, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateMethod()')
        return codes

    def GetMethodName(self, name: str) -> str:
        return 'GetMethodName()'
    
    def GenerateFunction(self, functionConfig: FunctionConfig) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateFunction()')
        return codes

    def GetFunctionName(self, name: str) -> str:
        return 'GetFunctionName()'

    def GetDataTypeName(self, dataTypeConfig: DataTypeConfig) -> str:
        return 'GetDataTypeName()'

    def GenerateConstantValue(self, name: str, dataTypeConfig: DataTypeConfig, value: str) -> List[str]:
        codes: List[str] = []
        codes.append('GenerateConstantValue()')
        return codes

    def GetConstantValueName(self, name: str) -> str:
        return 'GetConstantValueName()'
