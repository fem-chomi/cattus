from typing import List
from Config.MethodConfig import MethodType, MethodConfig
from Config.DataTypeConfig import DataTypeConfig
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.Python.Integer import Int32
from Util.SourceLine import SourceLine
from Util.NameConverter import NameConverter


class CompareTo(MethodConfig):
    def __init__(self):
        methodName: str = 'COMPARE-TO'
        description: str = 'クラスインスタンス同士の大小を比較する。'
        parameterList: List[ParameterDefine] = []
        returnType: DataTypeConfig = Int32()
        super().__init__(MethodType.COMPARE_TO, methodName, description, parameterList, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes: List[str] = []
        codes.append(SourceLine.Indent() + f'pass' + SourceLine.NewLine())
        return codes
