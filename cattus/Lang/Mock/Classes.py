from Config.DataTypeConfig import DataType, DataTypeConfig


class Class(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.CLASS, 'class')


class Struct(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.STRUCT, 'struct')


class Enum(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.ENUM, 'enum')


class ValueObject(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.VALUE_OBJECT, 'value_object')


class UserClass(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.USER_CLASS, 'user_class')

