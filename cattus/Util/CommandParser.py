import re
import Util
from typing import List


class CommandParser():
    def __init__(self, minParameterCount: int, maxParameterCount: int, args: [str]):
        self.__MinParameterCount = minParameterCount
        self.__MaxParameterCount = maxParameterCount
        self.__Args = args

    def Parse(self) -> Util.CommandParameter:
        if self.__Args is None:
            print('error: コマンドライン引数にnullが指定されました。')
            return None

        if self.__MinParameterCount < 0:
            print('error: 「パラメータの最小数」は0以上にしてください。')
            return None

        if self.__MaxParameterCount < 0:
            print('error: 「パラメータの最大数」は0以上にしてください。')
            return None

        if self.__MinParameterCount > self.__MaxParameterCount:
            print('error: 「パラメータの最小数」と「パラメータの最大数」の指定に矛盾があります。')
            return None

        parameterList: List[str] = []
        optionMap: {str, str} = {}
        for arg in self.__Args:
            if len(arg.strip()) == 0:
                continue
            if arg[0] == '/':
                if re.match('^/[0-9a-zA-Z]$', arg):
                    # /x
                    optionMap[arg[1:]] = ''
                elif re.match('^/[0-9a-zA-Z]:.+', arg):
                    # /x:yyyy
                    tokens = re.split(':', arg[1:])
                    optionMap[tokens[0]] = tokens[1]
                else:
                    print(f'error: 無効なオプション {arg} が指定されました。')
                    return None
            elif arg[0:2] == '--':
                if re.match('^--[0-9a-zA-Z][0-9a-zA-Z-_]*[0-9a-zA-Z]$', arg):
                    # --xxxx
                    optionMap[arg[2:]] = ''
                elif re.match('^--[0-9a-zA-Z][0-9a-zA-Z-_]*[0-9a-zA-Z][+-]?$', arg):
                    # --xxxx+ or --xxxx-
                    optionMap[arg[2:]] = ''
                elif re.match('^--[0-9a-zA-Z][0-9a-zA-Z-_]*[0-9a-zA-Z][+-]?:.+', arg):
                    # --xxxx:yyyy or --xxxx+:yyyy or --xxxx-:yyyy
                    tokens = re.split(':', arg[2:])
                    optionMap[tokens[0]] = tokens[1]
                else:
                    print(f'error: 無効なオプション {arg} が指定されました。')
                    return None
            elif arg[0] == '-':
                if re.match('^-[0-9a-zA-Z]+$', arg):
                    # -zxvf（/z /x /v /fと等価）
                    for option in arg[1:]:
                        optionMap[option] = ''
                else:
                    print(f'error: 無効なオプション {arg} が指定されました。')
                    return None
            else:
                parameterList.append(arg)

        if len(parameterList) < self.__MinParameterCount:
            print('error: パラメータ数の最小数を満たしません。')
            return None

        if len(parameterList) > self.__MaxParameterCount:
            print('error: パラメータ数が最大数を超えました。')
            return None

        return Util.CommandParameter(parameterList, optionMap)
