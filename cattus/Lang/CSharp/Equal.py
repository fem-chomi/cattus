from typing import List
from Config.MethodConfig import MethodType, MethodConfig
from Config.DataTypeConfig import DataTypeConfig
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.CSharp.Boolean import Boolean
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class Equal(MethodConfig):
    def __init__(self):
        methodName: str = 'EQUAL'
        description: str = 'クラスインスタンス同士が同一か比較する。'
        parameterList: List[ParameterDefine] = []
        returnType: DataTypeConfig = Boolean()
        super().__init__(MethodType.EQUAL, methodName, description, parameterList, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        return codes
