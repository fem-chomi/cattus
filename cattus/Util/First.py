from collections import deque
from enum import Enum
from typing import List


class IndentType(Enum):
	OTHER = 0
	TAB = 1
	SPACE = 2


class First():
    def __init__(self, delimiter: str):
        self.__first = True
        self.__delimiter = delimiter
    
    def Delimiter(self) -> str:
        if self.__first:
             self.__first = False
             return ''
        else:
             return self.__delimiter
