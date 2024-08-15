from collections import deque
from enum import Enum
from typing import List


class IndentType(Enum):
	OTHER = 0
	TAB = 1
	SPACE = 2


class SourceLine():
    # 改行コード
    #__newLine: str

    # コメント出力の制御フラグ
    #__noComment: bool

    # インデント位置（段数）
    #__indent: int

    # インデントのスタック
    #__indentStack: deque

    # インデントの種類
    #__indentType: IndentType

    # インデントの種類が半角空白の時の半角空白の充填数
    #__indentFillColumn: int

    @classmethod
    def __new__(cls):
        cls.Reset()

    # 改行コード変更
    @classmethod
    def SetNewLine(cls, newLine: str) -> None:
        cls.__newLine = newLine

    # コメント出力の制御フラグ変更
    @classmethod
    def SetNoComment(cls, noComment: bool) -> None:
        cls.__noComment = noComment

    # インデントの種類変更
    @classmethod
    def SetIndentType(cls, indentType: IndentType) -> None:
        cls.__indentType = indentType

    # インデントの種類が半角空白の時の半角空白の充填数変更
    @classmethod
    def SetIndentFillColumn(cls, indentFillColumn: int) -> None:
        cls.__indentFillColumn = indentFillColumn

    # コメント出力
    @classmethod
    def Comment(cls, comment: str) -> str:
        if cls.__noComment:
            return ''
        return comment

    # インデント出力
    @classmethod
    def Indent(cls) -> str:
        builder: List[str] = []
        for i in range(0, cls.__indent):
            if cls.__indentType == IndentType.TAB:
                builder.append('\t')
            elif cls.__indentType == IndentType.SPACE:
                for j in range(0, cls.__indentFillColumn):
                    builder.append(' ')
        return ''.join(builder)

    # インデントの位置を変更してから出力
    @classmethod
    def IndentN(cls, n: int) -> str:
        cls.__indent = n
        return cls.Indent()

    # 初期値に戻す
    @classmethod
    def Reset(cls) -> None:
        # 改行コード
        cls.__newLine: str = '\r\n'
        
        # コメント出力の制御フラグ
        cls.__noComment: bool = False
        
        # インデント位置（段数）
        cls.__indent: int = 0
        
        # インデントのスタック
        cls.__indentStack: deque = deque()
        
        # インデントの種類
        cls.__indentType: IndentType = IndentType.SPACE
        
        # インデントの種類が半角空白の時の半角空白の充填数
        cls.__indentFillColumn: int = 4

    # インデント位置を初期化する
    @classmethod
    def ResetIndent(cls) -> None:
        cls.__indent = 0
        cls.__indentStack.clear()

    # インデントの段数を変更する
    @classmethod
    def SetIndentCount(cls, n: int) -> None:
        cls.__indent = n

    # インデントを1段下げる
    @classmethod
    def IndentDown(cls) -> None:
        cls.__indent += 1

    # インデントを1段上げる
    @classmethod
    def IndentUp(cls) -> None:
        cls.__indent -= 1

    # 現在のインデントの段数をスタックに保存する
    @classmethod
    def PushIndent(cls) -> None:
        cls.__indentStack.append(cls.__indent)

    # スタックからインデントの段数を復元する
    @classmethod
    def PopIndent(cls) -> None:
        if len(cls.__indentStack) <= 0:
            return
        cls.__indent = cls.__indentStack.pop()

    # 現在のインデントの段数をスタックに保存してから新しいインデントの段数に変更する
    @classmethod
    def PushIndentN(cls, n: int) -> None:
        cls.__indentStack.append(cls.__indent)
        cls.__indent = n

    @classmethod
    def NewLine(cls) -> str:
        return cls.__newLine
