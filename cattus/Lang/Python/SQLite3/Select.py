from typing import List
from Config.MethodConfig import MethodType, MethodConfig
from Config.DataTypeConfig import DataTypeConfig
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.Python.String import String
from Lang.Python.Void import Void
from Util.SourceLine import SourceLine


class Select(MethodConfig):
    def __init__(self):
        methodName: str = 'SELECT'
        description: str = 'レコードを選択する。'
        parameterList: List[ParameterDefine] = []
        parameterList.append(ParameterDefine('FILENAME', 'エクスポートファイル名', String()))
        returnType: DataTypeConfig = Void()
        super().__init__(MethodType.EXPORT, methodName, description, parameterList, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'pass' + SourceLine.NewLine())
        return codes
