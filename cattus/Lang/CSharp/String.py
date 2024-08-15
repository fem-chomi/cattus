from Config.DataTypeConfig import DataType, DataTypeConfig


class String(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.STRING, 'string')


class FixedString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_STRING, 'string')


class AnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.ANSI_STRING, 'string')


class FixedAnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_ANSI_STRING, 'string')


class SecureString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.SECURE_STRING, 'string')

