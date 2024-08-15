from typing import List


class CommandParameter():
    def __init__(self, parameterList: List[str], optionMap: {str, str}):
        # パラメータリスト
        self.__ParameterList: List[str] = parameterList

        # オプションの連想配列
        self.__OptionMap: {str, str} = optionMap

    # パラメータ数を返す
    def GetParameterCount(self) -> int:
        return len(self.__ParameterList)
    
    # オプションが存在するか判定する
    def ContainsOption(self, option: str) -> bool:
        return option in self.__OptionMap
    
    # パラメータを取得する
    def GetParameter(self, index: int) -> str:
        if index < 0:
            return ''
        if index >= self.GetParameterCount():
            return ''
        return self.__ParameterList[index]

    # オプションを取得する
    def GetOption(self, option: str) -> str:
        if not self.ContainsOption(option):
            return ''
        return self.__OptionMap[option]
