from typing import List
from Model.EntityModel import EntityModel
from .ConstructClass import ConstructClass

from Lang.Mock.MockLanguage import MockLanguage


class GenerateCode():
    def Generate(self):
        lang = MockLanguage() #TODO コマンドから変換
        cc = ConstructClass(lang)
        entityModelList: List[EntityModel] = [] #TODO XMLファイルからロード
        for entityModel in entityModelList:
            for classType in entityModel.ClassTypeList:
                config = lang.GetIClassTypeConfig(classType)
                cc.ConstructClass(entityModel, config)
            print('end of class type')
        print('end of entity')
