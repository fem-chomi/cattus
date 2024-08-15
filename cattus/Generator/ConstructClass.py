from typing import List
from Interface.IProgrammingLanguage import IProgrammingLanguage
from Config.ClassTypeConfig import ClassType, ClassTypeConfig
from Config.ConstructorConfig import ConstructorType
from Config.MethodConfig import MethodType
from Model.EntityModel import EntityModel
from Model.FieldDefine import FieldDefine
import Util


class ConstructClass():
    def __init__(self, lang: IProgrammingLanguage):
        self.__Lang = lang

    # デフォルト実装
    def ConstructClass(self, entityModel: EntityModel, config: ClassTypeConfig) -> None:
        codes: List[str] = []
        first = Util.First(Util.SourceLine.NewLine())

        self.InitSetup()

        if config.EnableNamespace:
            codes += first.Delimiter()
            codes += self.ConstructNamespaceBeginBlock(entityModel, config)
        
        if config.EnableClass:
            codes += first.Delimiter()
            codes += self.ConstructClassBeginBlock(entityModel, config)
        
        if config.EnableField:
            for field in entityModel.FieldDefineList:
                codes += first.Delimiter()
                codes += self.ConstructField(field, config)
        
        if config.EnableProperty:
            for field in entityModel.FieldDefineList:
                codes += first.Delimiter()
                codes += self.ConstructProperty(field, config)

        if config.EnableFullConstructor:
            codes += first.Delimiter()
            codes += self.ConstructFullConstructor(entityModel, config)
        
        if config.EnableOmitConstructor:
            codes += first.Delimiter()
            codes += self.ConstructOmitConstructor(entityModel, config)
        
        if config.EnableCopyConstructor:
            codes += first.Delimiter()
            codes += self.ConstructCopyConstructor(entityModel, config)
        
        if config.EnableCopyDtoConstructor:
            codes += first.Delimiter()
            codes += self.ConstructCopyDtoConstructor(entityModel, config)
        
        if config.EnableCopyEntityConstructor:
            codes += first.Delimiter()
            codes += self.ConstructCopyEntityConstructor(entityModel, config)
        
        if config.EnableToString:
            codes += first.Delimiter()
            codes += self.ConstructToString(entityModel, config)
        
        if config.EnableEqual:
            codes += first.Delimiter()
            codes += self.ConstructEqual(entityModel, config)
        
        if config.EnableCompareTo:
            codes += first.Delimiter()
            codes += self.ConstructCompareTo(entityModel, config)
        
        if config.EnableGetHashCode:
            codes += first.Delimiter()
            codes += self.ConstructGetHashCode(entityModel, config)
        
        if config.EnableExport:
            codes += first.Delimiter()
            codes += self.ConstructExport(entityModel, config)
        
        if config.EnableImport:
            codes += first.Delimiter()
            codes += self.ConstructImport(entityModel, config)
        
        if config.EnableBuildDto:
            codes += first.Delimiter()
            codes += self.ConstructBuildDto(entityModel, config)
        
        if config.EnableBuildEntity:
            codes += first.Delimiter()
            codes += self.ConstructBuildEntity(entityModel, config)
        
        if config.EnableClass:
            codes += first.Delimiter()
            codes += self.ConstructClassEndBlock(entityModel, config)

        if config.EnableNamespace:
            codes += first.Delimiter()
            codes += self.ConstructNamespaceEndBlock(entityModel, config)

        code = ''.join(codes)
        self.WriteFile(entityModel, config, code)

    def InitSetup(self) -> None:
        self.__Lang.ClearImportDefine()

    def ConstructFullConstructor(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateConstructor(self.__Lang.GetConstructorConfig(ConstructorType.FULL), entityModel, config)

    def ConstructOmitConstructor(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateConstructor(self.__Lang.GetConstructorConfig(ConstructorType.OMIT), entityModel, config)

    def ConstructCopyConstructor(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateConstructor(self.__Lang.GetConstructorConfig(ConstructorType.COPY), entityModel, config, config)

    def ConstructCopyDtoConstructor(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        dto = config.ConvertClassType(ClassType.DTO)
        return self.__Lang.GenerateConstructor(self.__Lang.GetConstructorConfig(ConstructorType.COPY_DTO), entityModel, config, dto)

    def ConstructCopyEntityConstructor(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        entity = config.ConvertClassType(ClassType.ENTITY)
        return self.__Lang.GenerateConstructor(self.__Lang.GetConstructorConfig(ConstructorType.COPY_ENTITY), entityModel, config, entity)

    def ConstructToString(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateMethod(self.__Lang.GetMethodConfig(MethodType.TO_STRING), entityModel, None, config)

    def ConstructEqual(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateMethod(self.__Lang.GetMethodConfig(MethodType.EQUAL), entityModel, None, config)

    def ConstructCompareTo(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateMethod(self.__Lang.GetMethodConfig(MethodType.COMPARE_TO), entityModel, None, config)
    
    def ConstructGetHashCode(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateMethod(self.__Lang.GetMethodConfig(MethodType.GET_HASH_CODE), entityModel, None, config)

    def ConstructExport(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateMethod(self.__Lang.GetMethodConfig(MethodType.EXPORT), entityModel, None, config)

    def ConstructImport(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateMethod(self.__Lang.GetMethodConfig(MethodType.IMPORT), entityModel, None, config)

    def ConstructBuildDto(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        dto = config.ConvertClassType(ClassType.DTO)
        return self.__Lang.GenerateMethod(self.__Lang.GetMethodConfig(MethodType.BUILD_DTO), entityModel, None, dto)

    def ConstructBuildEntity(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        entity = config.ConvertClassType(ClassType.ENTITY)
        return self.__Lang.GenerateMethod(self.__Lang.GetMethodConfig(MethodType.BUILD_ENTITY), entityModel, None, entity)

    # インポート文を生成
    def ConstructImportStatement(self) -> List[str]:
        #TODO 依存関係をリスト化しておく必要がある
        return self.__Lang.GenerateImport()

    # 名前空間開始ブロックを生成
    def ConstructNamespaceBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateNamespaceBeginBlock(entityModel, config)

    # 名前空間終了ブロックを生成
    def ConstructNamespaceEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateNamespaceEndBlock(entityModel, config)

    # クラス定義開始ブロックを生成
    def ConstructClassBeginBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateClassBeginBlock(entityModel, config)

    # クラス定義終了ブロックを生成
    def ConstructClassEndBlock(self, entityModel: EntityModel, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateClassEndBlock(entityModel, config)

    # フィールドを生成（プロパティ用の内部変数）
    def ConstructField(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateField(field, config)

    # プロパティを生成
    def ConstructProperty(self, field: FieldDefine, config: ClassTypeConfig) -> List[str]:
        return self.__Lang.GenerateProperty(field, config)

    # ファイルに出力する
    def WriteFile(self, entityModel: EntityModel, config: ClassTypeConfig, text: str) -> None:
        filename = self.__Lang.GetFileName(f'{entityModel.EntityName}-{config.ClassSuffixName}') + f'.generate.{self.__Lang.GetFileExtName()}'
        Util.TextFileWriter().Write(filename, text)
