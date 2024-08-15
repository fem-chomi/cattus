from enum import Enum


# データ型タイプ
class DataType(Enum):
    OTHER = 0
    INT8 = 1
    INT16 = 2
    INT32 = 3
    INT64 = 4
    UINT8 = 5
    UINT16 = 6
    UINT32 = 7
    UINT64 = 8
    SINGLE = 9
    DOUBLE = 10
    DECIMAL = 11
    STRING = 12
    FIXED_STRING = 13
    ANSI_STRING = 14
    FIXED_ANSI_STRING = 15
    SECURE_STRING = 16
    DATETIME = 17
    DATE = 18
    TIME = 19
    TIMESPAN = 20
    UUID = 21
    BOOLEAN = 22
    BINARY = 23
    CLASS = 24
    STRUCT = 25
    ENUM = 26
    VALUE_OBJECT = 27
    USER_CLASS = 28
    POINTER = 29         # 【特殊】生のポインタそのものを使用する場合に限る特殊な用途
    VOID = 30
    RESERVED = 31

# 生成タイプ
class AllocationType(Enum):
    OTHER = 0
    VALUE = 1
    ARRAY = 2
    LIST = 3
    MAP = 4
    SET = 5
    STACK = 6
    QUEUE = 7
    POINTER = 8          # 【通常】データ型を修飾する使用法
    RESERVED = 9


# データ型
class DataTypeConfig():
    def __init__(self, type: DataType, \
            dataTypeName: str, \
            allocationType: AllocationType = AllocationType.VALUE, \
            allocationTypeName: str = '', \
            keyType: DataType = DataType.OTHER, \
            keyTypeName: str = '', \
            notNull: bool = True):

        # データ型タイプ
        self.__Type: DataType = type

        # データ型名
        self.__DataTypeName: str = dataTypeName
        
        # 生成タイプ
        self.__AllocationType: AllocationType = allocationType
    
        # 生成タイプ名
        self.__AllocationTypeName: str = allocationTypeName
        
        # キータイプ
        self.__KeyType: DataType = keyType
        
        # キータイプ名
        self.__KeyTypeName: str = keyTypeName

        # ヌル禁止フラグ
        self.__NotNull: bool = notNull

    @property
    def DataTypeName(self) -> str:
        return self.__DataTypeName
    
    @property
    def AllocationTypeName(self) -> str:
        return self.__AllocationTypeName

    @property
    def KeyTypeName(self) -> str:
        return self.__KeyTypeName

    @property
    def Type(self) -> type:
        return self.__Type

    @property
    def AllocationType(self) -> AllocationType:
        return self.__AllocationType

    @property
    def KeyType(self) -> DataType:
        return self.__KeyType

    @property
    def NotNull(self) -> bool:
        return self.__NotNull
