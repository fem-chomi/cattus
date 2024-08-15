from Config.DataTypeConfig import DataType, DataTypeConfig


class String(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.STRING, 'str')


class FixedString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_STRING, 'str')


class AnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.ANSI_STRING, 'str')


class FixedAnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_ANSI_STRING, 'str')


class SecureString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.SECURE_STRING, 'str')

