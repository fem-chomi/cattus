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


class GetHashCode(MethodConfig):
    def __init__(self):
        methodName: str = 'GET-HASH-CODE'
        description: str = 'クラスインスタンスのハッシュコードを取得する。'
        parameterList: List[ParameterDefine] = []
        returnType: DataTypeConfig = String()
        super().__init__(MethodType.GET_HASH_CODE, methodName, description, parameterList, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        return codes
