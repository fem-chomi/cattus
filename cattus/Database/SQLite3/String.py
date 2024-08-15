from Config.DataTypeConfig import DataType, DataTypeConfig


class String(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.STRING, 'TEXT')


class FixedString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_STRING, 'TEXT')


class AnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.ANSI_STRING, 'TEXT')


class FixedAnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_ANSI_STRING, 'TEXT')


class SecureString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.SECURE_STRING, 'TEXT')

