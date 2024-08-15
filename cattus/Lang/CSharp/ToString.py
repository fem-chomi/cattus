from typing import List
from Config.MethodConfig import MethodType, MethodConfig
from Config.DataTypeConfig import DataTypeConfig
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.CSharp.String import String
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class ToString(MethodConfig):
    def __init__(self):
        methodName: str = 'TO-STRING'
        description: str = 'クラス内容を人が読みやすい形式で文字列出力する。'
        parameterList: List[ParameterDefine] = []
        returnType: DataTypeConfig = String()
        isOverride: bool = True
        super().__init__(MethodType.TO_STRING, methodName, description, parameterList, returnType, isOverride)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + 'return new StringBuilder()' + SourceLine.NewLine())
        SourceLine.IndentDown()
        for field in entityModel.FieldDefineList:
            propertyName = NameConverter.ToUpperCamelCase(field.FieldName) # TODO CSharp.GetPropertyName()
            codes.append(SourceLine.Indent() + f'.Append($"{NameConverter.ToUpperCamelCase(field.FieldName)}: {{this.{propertyName}}}")' + SourceLine.NewLine())
        codes.append(SourceLine.Indent() + '.ToString();' + SourceLine.NewLine())
        SourceLine.IndentUp()
        return codes
