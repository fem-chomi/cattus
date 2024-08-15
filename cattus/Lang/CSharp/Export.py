from typing import List
from Config.MethodConfig import MethodType, MethodConfig
from Config.DataTypeConfig import DataTypeConfig
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.CSharp.Void import Void
from Lang.CSharp.String import String
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class Export(MethodConfig):
    def __init__(self):
        methodName: str = 'EXPORT-FILE'
        description: str = 'クラスインスタンスをエクスポートする。'
        parameterList: List[ParameterDefine] = []
        parameterList.append(ParameterDefine('FILENAME', 'エクスポートファイル名', String()))
        returnType: DataTypeConfig = Void()
        super().__init__(MethodType.EXPORT, methodName, description, parameterList, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        return codes
