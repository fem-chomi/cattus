from typing import List, Dict
from Interface.IProgrammingLanguage import LanguageType, IProgrammingLanguage
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Config.ConstructorConfig import ConstructorConfig
from Config.DataTypeConfig import DataType, AllocationType, DataTypeConfig
from Config.FunctionConfig import FunctionType, FunctionConfig
from Config.MethodConfig import MethodType, MethodConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Model.ImportDefine import ImportDefine
from Lang.Python.Integer import Int8, Int16, Int32, Int64, UInt8, UInt16, UInt32, UInt64
from Lang.Python.Float import Single, Double
from Lang.Python.Decimal import Decimal
from Lang.Python.String import String, FixedString, AnsiString, FixedAnsiString, SecureString
from Lang.Python.Boolean import Boolean
from Lang.Python.DateTime import DateTime, Date, Time, TimeSpan
from Lang.Python.UniqueID import UniqueID
from Lang.Python.Binary import Binary
from Lang.Python.Classes import Class, Struct, Enum, ValueObject, UserClass
from Lang.Python.Void import Void
from Lang.Python.ToString import ToString
from Lang.Python.Equal import Equal
from Lang.Python.CompareTo import CompareTo
from Lang.Python.GetHashCode import GetHashCode
from Lang.Python.Export import Export
from Lang.Python.Import import Import
from Lang.Python.Build import BuildDto, BuildEntity
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class PythonLanguage(IProgrammingLanguage):
    def __init__(self):
        # メソッドのテーブル引き用の連想配列
        self.__MethodConfigMap: Dict[MethodType, MethodConfig] = {}
        self.__MethodConfigMap[MethodType.TO_STRING] = ToString()
        self.__MethodConfigMap[MethodType.EQUAL] = Equal()
        self.__MethodConfigMap[MethodType.COMPARE_TO] = CompareTo()
        self.__MethodConfigMap[MethodType.GET_HASH_CODE] = GetHashCode()
        self.__MethodConfigMap[MethodType.EXPORT] = Export()
        self.__MethodConfigMap[MethodType.IMPORT] = Import()
        self.__MethodConfigMap[MethodType.BUILD_DTO] = BuildDto()
        self.__MethodConfigMap[MethodType.BUILD_ENTITY] = BuildEntity()

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
        self.__DataTypeConfigMap[DataType.VOID] = Void()

        super().__init__(LanguageType.PYTHON, \
            self.__MethodConfigMap, \
            self.__FunctionConfigMap, \
            self.__DataTypeConfigMap)

    def GetFileName(self, filename: str) -> str:
        return NameConverter.ToLowerSnakeCase(filename)

    def GetFileExtName(self) -> str:
        return 'py'

    def GenerateImport(self) -> List[str]:
        codes: List[str] = []
        for item in list(self.ImportDefineSet):
            if len(item.ModuleName) > 0:
                if len(item.PathName) > 0:
                    codes.append(SourceLine.Indent() + f'from {item.PathName} import {item.ModuleName}' + SourceLine.NewLine())
                else:
                    codes.append(SourceLine.Indent() + f'import {item.ModuleName}' + SourceLine.NewLine())
        return codes

    def GenerateNamespaceBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        return codes

    def GenerateNamespaceEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        return codes

    def GetNamespaceName(self, name: str) -> str:
        return NameConverter.ToLowerSnakeCase(name)

    def GenerateClassBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        if config.Type == ClassType.DTO and config.EnablePythonSpecialDataClass:
            self.AppendImportDefine(ImportDefine(moduleName='dataclasses'))
            if config.EnableImmutable:
                codes.append(SourceLine.Indent() + f'@dataclasses.dataclass(frozen=True)' + SourceLine.NewLine())
            else:
                codes.append(SourceLine.Indent() + f'@dataclasses.dataclass' + SourceLine.NewLine())
        codes.append(SourceLine.Indent() + f'class {self.GetClassName(entityModel.EntityName, config)}():' + SourceLine.NewLine())
        SourceLine.IndentDown()
        return codes

    def GenerateClassEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        SourceLine.IndentUp()
        return codes

    def GetClassName(self, name: str, config: ClassTypeConfig) -> str:
        return NameConverter.ToLowerSnakeCase(f'{name}-{config.ClassSuffixName}')

    def GenerateConstructor(self, constructorConfig: ConstructorConfig, entityModel: EntityModel, config: ClassTypeConfig, thatClassTypeConfig: ClassTypeConfig=None) -> List[str]:
        codes: List[str] = []
        if config.Type == ClassType.DTO and config.EnablePythonSpecialDataClass:
            return codes
        if constructorConfig.EnableCopy or constructorConfig.EnableCopyDto or constructorConfig.EnableCopyEntity:
            codes.append(SourceLine.Indent() + f'def {self.GetConstructorName(entityModel.EntityName, config)}(self, that: {self.GetClassName(entityModel.EntityName, thatClassTypeConfig)}) -> None:' + SourceLine.NewLine())
            SourceLine.IndentDown()
            for field in entityModel.FieldDefineList:
                codes.append(SourceLine.Indent() + f'self.{self.GetFieldName(field.FieldName)} = that.{self.GetPropertyName(field.FieldName)}' + SourceLine.NewLine())
            SourceLine.IndentUp()
        else:
            parameters: str = ''
            if constructorConfig.EnableParameter:
                for field in entityModel.FieldDefineList:
                    parameter = ParameterDefine(field.FieldName, field.Description, field.DataTypeConfig, field.DefaultValue)
                    parameters += f', {self.GenerateParameter(parameter, enableDefaultValue=constructorConfig.EnableDefaultValue)}'
            codes.append(SourceLine.Indent() + f'def {self.GetConstructorName(entityModel.EntityName, config)}(self{parameters}) -> None:' + SourceLine.NewLine())
            SourceLine.IndentDown()
            for field in entityModel.FieldDefineList:
                parameter = ParameterDefine(field.FieldName, field.Description, field.DataTypeConfig, field.DefaultValue)
                if constructorConfig.EnableParameter:
                    codes.append(SourceLine.Indent() + f'self.{self.GetFieldName(parameter.ParameterName)} = {self.GetParameterName(parameter.ParameterName)}' + SourceLine.NewLine())
                else:
                    # パラメータがないため、既定値を入れる
                    if len(parameter.DefaultValue) > 0:
                        codes.append(SourceLine.Indent() + f'self.{self.GetFieldName(parameter.ParameterName)} = {parameter.DefaultValue}' + SourceLine.NewLine())
                    else:
                        # 既定値が無い場合は未定義となるため、例外を投げる
                        raise NotImplementedError()
            SourceLine.IndentUp()
        return codes

    def GetConstructorName(self, name: str, config: ClassTypeConfig) -> str:
        return '__init__'
    
    def GenerateField(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        if config.EnablePythonSpecialDataClass:
            return codes
        codes.append(SourceLine.Indent() + f'{self.GetFieldName(field.FieldName)}: {self.GetDataTypeName(field.DataTypeConfig)}' + SourceLine.NewLine())
        return codes

    def GetFieldName(self, name: str) -> str:
        return f'__{NameConverter.ToLowerSnakeCase(name)}'
    
    def GenerateProperty(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        if config.EnablePythonSpecialDataClass:
            codes.append(SourceLine.Indent() + f'{self.GetPropertyName(field.FieldName)}: {self.GetDataTypeName(field.DataTypeConfig)}' + SourceLine.NewLine())
        else:
            codes.append(SourceLine.Indent() + '@property' + SourceLine.NewLine())
            codes.append(SourceLine.Indent() + f'def {self.GetPropertyName(field.FieldName)}(self) -> {self.GetDataTypeName(field.DataTypeConfig)}:' + SourceLine.NewLine())
            SourceLine.IndentDown()
            codes.append(SourceLine.Indent() + f'return self.{self.GetFieldName(field.FieldName)}' + SourceLine.NewLine())
            SourceLine.IndentUp()
        return codes

    def GetPropertyName(self, name: str) -> str:
        return NameConverter.ToLowerSnakeCase(name)

    def GenerateParameter(self, parameterDefine: ParameterDefine, enableDefaultValue=False) -> str:
        if enableDefaultValue and len(parameterDefine.DefaultValue) > 0:
            return f'{self.GetParameterName(parameterDefine.ParameterName)}: {self.GetDataTypeName(parameterDefine.DataTypeConfig)}={parameterDefine.DefaultValue}'
        else:
            return f'{self.GetParameterName(parameterDefine.ParameterName)}: {self.GetDataTypeName(parameterDefine.DataTypeConfig)}'
        
    def GetParameterName(self, name: str) -> str:
        return NameConverter.ToLowerSnakeCase(name)
    
    def GenerateMethod(self, methodConfig: MethodConfig, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        SourceLine.PushIndent()
        parameters: str = ''
        for parameter in methodConfig.ParameterList:
            parameters += f', {self.GenerateParameter(parameter)}'
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'def {self.GetMethodName(methodConfig.MethodName)}(self{parameters}) -> {self.GetDataTypeName(methodConfig.ReturnType, entityModel, config)}:' + SourceLine.NewLine())
        SourceLine.IndentDown()
        codes += methodConfig.GenerateCode(entityModel, field, config)
        SourceLine.IndentUp()
        SourceLine.PopIndent()
        return codes

    def GetMethodName(self, name: str) -> str:
        return NameConverter.ToLowerSnakeCase(name)
    
    def GenerateFunction(self, functionConfig: FunctionConfig, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        SourceLine.PushIndent()
        parameters: str = ''
        for parameter in functionConfig.ParameterList:
            parameters += f', {self.GenerateParameter(parameter)}'
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'def {self.GetFunctionName(functionConfig.FunctionName)}(self{parameters}) -> {self.GetDataTypeName(functionConfig.ReturnType)}:' + SourceLine.NewLine())
        SourceLine.IndentDown()
        codes += functionConfig.GenerateCode(entityModel, field, config)
        SourceLine.IndentUp()
        SourceLine.PopIndent()
        return codes

    def GetFunctionName(self, name: str) -> str:
        return f'__{NameConverter.ToLowerSnakeCase(name)}'

    def GetDataTypeName(self, dataTypeConfig: DataTypeConfig, entityModel: EntityModel=None, config: ClassTypeConfig=None) -> str:
        if len(dataTypeConfig.DataTypeName) > 0:
            dataTypeName = dataTypeConfig.DataTypeName
        elif entityModel is not None and config is not None:
            dataTypeName = self.GetClassName(entityModel.EntityName, config)
        else:
            raise NotImplementedError()
        if dataTypeConfig.AllocationType == AllocationType.VALUE:
            return dataTypeName
        elif dataTypeConfig.AllocationType == AllocationType.ARRAY:
            return f'Array[{dataTypeName}]'
        elif dataTypeConfig.AllocationType == AllocationType.LIST:
            return f'List[{dataTypeName}]'
        elif dataTypeConfig.AllocationType == AllocationType.MAP:
            return f'Dict[{dataTypeConfig.KeyTypeName}, {dataTypeName}]'
        elif dataTypeConfig.AllocationType == AllocationType.SET:
            return f'Set[{dataTypeName}]'
        elif dataTypeConfig.AllocationType == AllocationType.STACK:
            return 'deque'
        elif dataTypeConfig.AllocationType == AllocationType.QUEUE:
            return 'deque'
        else:
            raise NotImplementedError()

    def GenerateConstantValue(self, name: str, dataTypeConfig: DataTypeConfig, value: str) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'{self.GetConstantValueName(name)}: {self.GetDataTypeName(dataTypeConfig)} = {value}' + SourceLine.NewLine())
        return codes

    def GetConstantValueName(self, name: str) -> str:
        return NameConverter.ToUpperSnakeCase(name)
