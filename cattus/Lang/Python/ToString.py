from typing import List
from Config.MethodConfig import MethodType, MethodConfig
from Config.DataTypeConfig import DataTypeConfig
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.Python.String import String
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class ToString(MethodConfig):
    def __init__(self):
        methodName: str = 'TO-STRING'
        description: str = 'クラス内容を人が読みやすい形式で文字列出力する。'
        parameterList: List[ParameterDefine] = []
        returnType: DataTypeConfig = String()
        super().__init__(MethodType.TO_STRING, methodName, description, parameterList, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + 'text: str = \'\'' + SourceLine.NewLine())
        for field in entityModel.FieldDefineList:
            propertyName = NameConverter.ToLowerSnakeCase(field.FieldName) # TODO Python.GetPropertyName()
            codes.append(SourceLine.Indent() + f'text += f\'{NameConverter.ToLowerSnakeCase(field.FieldName)}: {{self.{propertyName}}}\'' + SourceLine.NewLine())
        return codes
