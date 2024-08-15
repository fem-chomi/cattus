from typing import List
from Config.MethodConfig import MethodType, MethodConfig
from Config.DataTypeConfig import DataTypeConfig
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.Python.Classes import UserClass
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class BuildDto(MethodConfig):
    def __init__(self):
        methodName: str = 'BUILD'
        description: str = 'ビルダークラスをビルドする。'
        parameterList: List[ParameterDefine] = []
        returnType: DataTypeConfig = UserClass()
        super().__init__(MethodType.BUILD_DTO, methodName, description, parameterList, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'pass' + SourceLine.NewLine())
        return codes


class BuildEntity(MethodConfig):
    def __init__(self):
        methodName: str = 'BUILD'
        description: str = 'ビルダークラスをビルドする。'
        parameterList: List[ParameterDefine] = []
        returnType: DataTypeConfig = UserClass()
        super().__init__(MethodType.BUILD_ENTITY, methodName, description, parameterList, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'pass' + SourceLine.NewLine())
        return codes
