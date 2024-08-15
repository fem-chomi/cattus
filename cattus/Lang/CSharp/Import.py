from typing import List
from Config.MethodConfig import MethodType, MethodConfig
from Config.DataTypeConfig import DataTypeConfig
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.CSharp.Classes import UserClass
from Lang.CSharp.String import String
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class Import(MethodConfig):
    def __init__(self):
        methodName: str = 'IMPORT-FILE'
        description: str = 'クラスインスタンスをインポートする。'
        parameterList: List[ParameterDefine] = []
        parameterList.append(ParameterDefine('FILENAME', 'インポートファイル名', String()))
        returnType: DataTypeConfig = UserClass()
        super().__init__(MethodType.IMPORT, methodName, description, parameterList, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        return codes
