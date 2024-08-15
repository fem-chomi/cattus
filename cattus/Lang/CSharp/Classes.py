from Config.DataTypeConfig import DataType, DataTypeConfig


class Class(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.CLASS, '')


class Struct(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.STRUCT, '')


class Enum(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.ENUM, '')


class ValueObject(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.VALUE_OBJECT, '')


class UserClass(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.USER_CLASS, '')

