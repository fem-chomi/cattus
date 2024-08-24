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
from Lang.CSharp.Integer import Int8, Int16, Int32, Int64, UInt8, UInt16, UInt32, UInt64
from Lang.CSharp.Float import Single, Double
from Lang.CSharp.Decimal import Decimal
from Lang.CSharp.String import String, FixedString, AnsiString, FixedAnsiString, SecureString
from Lang.CSharp.Boolean import Boolean
from Lang.CSharp.DateTime import DateTime, Date, Time, TimeSpan
from Lang.CSharp.UniqueID import UniqueID
from Lang.CSharp.Binary import Binary
from Lang.CSharp.Void import Void
from Lang.CSharp.Classes import Class, Struct, Enum, ValueObject, UserClass
from Lang.CSharp.ToString import ToString
from Lang.CSharp.Equal import Equal
from Lang.CSharp.CompareTo import CompareTo
from Lang.CSharp.GetHashCode import GetHashCode
from Lang.CSharp.Export import Export
from Lang.CSharp.Import import Import
from Lang.CSharp.Build import BuildDto, BuildEntity
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class CSharpLanguage(IProgrammingLanguage):
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

        super().__init__(LanguageType.CSHARP, \
            self.__MethodConfigMap, \
            self.__FunctionConfigMap, \
            self.__DataTypeConfigMap)

    def GetFileName(self, filename: str) -> str:
        return NameConverter.ToUpperCamelCase(filename)

    def GetFileExtName(self) -> str:
        return 'cs'

    def GenerateImport(self) -> List[str]:
        codes: List[str] = []
        for item in list(self.ImportDefineSet):
            if len(item.NamespaceName) > 0 and len(item.ClassName) > 0:
                codes.append(SourceLine.Indent() + f'using {item.NamespaceName}.{item.ClassName};' + SourceLine.NewLine())
        return codes

    def GenerateNamespaceBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'namespace {self.GetNamespaceName(entityModel.EntityName)} ' + '{' + SourceLine.NewLine())
        SourceLine.IndentDown()
        return codes

    def GenerateNamespaceEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        SourceLine.IndentUp()
        codes.append(SourceLine.Indent() + '}' + SourceLine.NewLine())
        return codes

    def GetNamespaceName(self, name: str) -> str:
        return NameConverter.ToUpperCamelCase(name)

    def GenerateClassBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'public class {self.GetClassName(entityModel.EntityName, config)} ' + '{' + SourceLine.NewLine())
        SourceLine.IndentDown()
        return codes

    def GenerateClassEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        SourceLine.IndentUp()
        codes.append(SourceLine.Indent() + '}' + SourceLine.NewLine())
        return codes

    def GetClassName(self, name: str, config: ClassTypeConfig) -> str:
        return NameConverter.ToUpperCamelCase(f'{name}-{config.ClassSuffixName}')

    def GenerateConstructor(self, constructorConfig: ConstructorConfig, entityModel: EntityModel, config: ClassTypeConfig, thatClassTypeConfig: ClassTypeConfig=None) -> List[str]:
        codes: List[str] = []
        if constructorConfig.EnableCopy or constructorConfig.EnableCopyDto or constructorConfig.EnableCopyEntity:
            codes.append(SourceLine.Indent() + f'public {self.GetConstructorName(entityModel.EntityName, config)}({self.GetClassName(entityModel.EntityName, thatClassTypeConfig)} that) ' + '{' + SourceLine.NewLine())
            SourceLine.IndentDown()
            for field in entityModel.FieldDefineList:
                codes.append(SourceLine.Indent() + f'this.{self.GetFieldName(field.FieldName)} = that.{self.GetPropertyName(field.FieldName)};' + SourceLine.NewLine())
            SourceLine.IndentUp()
            codes.append(SourceLine.Indent() + '}' + SourceLine.NewLine())
        else:
            parameters: str = ''
            if constructorConfig.EnableParameter:
                first: bool = True
                for field in entityModel.FieldDefineList:
                    if first:
                        first = False
                    else:
                        parameters += ', '
                    parameter = ParameterDefine(field.FieldName, field.Description, field.DataTypeConfig, field.DefaultValue)
                    parameters += self.GenerateParameter(parameter, enableDefaultValue=constructorConfig.EnableDefaultValue)
            codes.append(SourceLine.Indent() + f'public {self.GetConstructorName(entityModel.EntityName, config)}({parameters}) ' + '{' + SourceLine.NewLine())
            SourceLine.IndentDown()
            for field in entityModel.FieldDefineList:
                parameter = ParameterDefine(field.FieldName, field.Description, field.DataTypeConfig, field.DefaultValue)
                if constructorConfig.EnableParameter:
                    codes.append(SourceLine.Indent() + f'this.{self.GetFieldName(parameter.ParameterName)} = {self.GetParameterName(parameter.ParameterName)};' + SourceLine.NewLine())
                else:
                    # パラメータがないため、既定値を入れる
                    if len(parameter.DefaultValue) > 0:
                        codes.append(SourceLine.Indent() + f'this.{self.GetFieldName(parameter.ParameterName)} = {parameter.DefaultValue};' + SourceLine.NewLine())
                    else:
                        # 既定値が無い場合は未定義となるため、例外を投げる
                        raise NotImplementedError()
            SourceLine.IndentUp()
            codes.append(SourceLine.Indent() + '}' + SourceLine.NewLine())
        return codes

    def GetConstructorName(self, name: str, config: ClassTypeConfig) -> str:
        return NameConverter.ToUpperCamelCase(f'{name}-{config.ClassSuffixName}')
    
    def GenerateField(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        line: List[str] = []
        line.append(SourceLine.Indent() + f'private ')
        if config.EnableImmutable:
            line.append('readonly ')
        line.append(f'{self.GetDataTypeName(field.DataTypeConfig)} {self.GetFieldName(field.FieldName)};' + SourceLine.NewLine())
        codes: List[str] = []
        codes.append(''.join(line))
        return codes

    def GetFieldName(self, name: str) -> str:
        return NameConverter.ToLowerCamelCase(name)
    
    def GenerateProperty(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'public {self.GetDataTypeName(field.DataTypeConfig)} {self.GetPropertyName(field.FieldName)}() ' + '{' + SourceLine.NewLine())
        SourceLine.IndentDown()
        codes.append(SourceLine.Indent() + f'return this.{self.GetFieldName(field.FieldName)};' + SourceLine.NewLine())
        SourceLine.IndentUp()
        codes.append(SourceLine.Indent() + '}' + SourceLine.NewLine())
        return codes

    def GetPropertyName(self, name: str) -> str:
        return NameConverter.ToUpperCamelCase(name)

    def GenerateParameter(self, parameterDefine: ParameterDefine, enableDefaultValue=False) -> str:
        if enableDefaultValue and len(parameterDefine.DefaultValue) > 0:
            return f'{self.GetDataTypeName(parameterDefine.DataTypeConfig)} {self.GetParameterName(parameterDefine.ParameterName)}={parameterDefine.DefaultValue}'
        else:
            return f'{self.GetDataTypeName(parameterDefine.DataTypeConfig)} {self.GetParameterName(parameterDefine.ParameterName)}'
        
    def GetParameterName(self, name: str) -> str:
        return NameConverter.ToLowerCamelCase(name)

    def GenerateMethod(self, methodConfig: MethodConfig, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        parameters: str = ''
        first: bool = True
        for parameter in methodConfig.ParameterList:
            if first:
                first = False
            else:
                parameters += ', '
            parameters += self.GenerateParameter(parameter)
        override: str = ''
        if methodConfig.IsOverride:
            override = 'override '
        codes.append(SourceLine.Indent() + f'public {override}{self.GetDataTypeName(methodConfig.ReturnType, entityModel, config)} {self.GetMethodName(methodConfig.MethodName)}({parameters})' + ' {' + SourceLine.NewLine())
        SourceLine.IndentDown()
        codes += methodConfig.GenerateCode(entityModel, field, config)
        SourceLine.IndentUp()
        codes.append(SourceLine.Indent() + '}' + SourceLine.NewLine())
        return codes

    def GetMethodName(self, name: str) -> str:
        return NameConverter.ToUpperCamelCase(name)
    
    def GenerateFunction(self, functionConfig: FunctionConfig, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        parameters: str = ''
        first: bool = True
        for parameter in functionConfig.ParameterList:
            if first:
                first = False
            else:
                parameters += ', '
            parameters += self.GenerateParameter(parameter)
        codes.append(SourceLine.Indent() + f'private {self.GetDataTypeName(functionConfig.ReturnType)} {self.GetFunctionName(functionConfig.FunctionName)}({parameters})' + ' {' + SourceLine.NewLine())
        SourceLine.IndentDown()
        codes += functionConfig.GenerateCode(entityModel, field, config)
        SourceLine.IndentUp()
        codes.append(SourceLine.Indent() + '}' + SourceLine.NewLine())
        return codes

    def GetFunctionName(self, name: str) -> str:
        return NameConverter.ToUpperCamelCase(name)

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
            return f'{dataTypeName}[]'
        elif dataTypeConfig.AllocationType == AllocationType.LIST:
            return f'List<{dataTypeName}>'
        elif dataTypeConfig.AllocationType == AllocationType.MAP:
            return f'Dictionary<{dataTypeConfig.KeyTypeName}, {dataTypeName}>'
        elif dataTypeConfig.AllocationType == AllocationType.SET:
            return f'Set<{dataTypeName}>'
        elif dataTypeConfig.AllocationType == AllocationType.STACK:
            return f'Stack<{dataTypeName}>'
        elif dataTypeConfig.AllocationType == AllocationType.QUEUE:
            return f'Queue<{dataTypeName}>'
        else:
            raise NotImplementedError()

    def GenerateConstantValue(self, name: str, dataTypeConfig: DataTypeConfig, value: str) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'public const {self.GetDataTypeName(dataTypeConfig)} {self.GetConstantValueName(name)} = {value}' + SourceLine.NewLine())
        return codes

    def GetConstantValueName(self, name: str) -> str:
        return NameConverter.ToUpperSnakeCase(name)
