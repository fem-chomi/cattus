from unittest import TestCase
from typing import List
from Config.MethodConfig import MethodType, MethodConfig
from Config.DataTypeConfig import DataType
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Model.ParameterDefine import ParameterDefine
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
from Lang.Python.PythonLanguage import PythonLanguage
from Lang.Python.Integer import Int8, Int16, Int32, Int64
from Util.SourceLine import SourceLine


class DummyMethod(MethodConfig):
    def __init__(self):
        methodName: str = 'AAAA-BBBB-CCCC'
        description: str = 'DDDD'
        parameters: List[ParameterDefine] = []
        parameters.append(ParameterDefine('EEEE-FFFF-GGGG', 'HHHH', Int8()))
        parameters.append(ParameterDefine('IIII-JJJJ-KKKK', 'LLLL', Int16()))
        parameters.append(ParameterDefine('MMMM-NNNN-OOOO', 'PPPP', Int32()))
        returnType = Int64()
        super().__init__(MethodType.TO_STRING, methodName, description, parameters, returnType)

    def GenerateCode(self, entityModel: EntityModel, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        codes = []
        codes.append('    QQQQ\r\n')
        codes.append('    RRRR\r\n')
        codes.append('    SSSS\r\n')
        return codes


class TestPythonLanguage_GenerateMethod(TestCase):
    def setUp(self):
        SourceLine.Reset()

    def tearDown(self):
        SourceLine.Reset()

    def test_GenerateMethod_pattern_01(self):
        test = PythonLanguage()
        method = DummyMethod()
        fieldDefineList = []
        field = FieldDefine('TTTT', 'UUUU', test.GetDataTypeConfig(DataType.INT32))
        fieldDefineList.append(field)
        entityModel = EntityModel('VVVV', 'WWWW', fieldDefineList)
        config = ClassTypeConfig(ClassType.DTO, classSuffixName = 'ZZZZ')
        field = None
        result = test.GenerateMethod(method, entityModel, field, config)
        self.assertEqual(result[0], 'def aaaa_bbbb_cccc(self, eeee_ffff_gggg: int, iiii_jjjj_kkkk: int, mmmm_nnnn_oooo: int) -> long:\r\n')
        self.assertEqual(result[1], '    QQQQ\r\n')
        self.assertEqual(result[2], '    RRRR\r\n')
        self.assertEqual(result[3], '    SSSS\r\n')
