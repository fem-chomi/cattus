from Config.DataTypeConfig import DataType, DataTypeConfig


class String(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.STRING, 'string')


class FixedString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_STRING, 'fixed_string')


class AnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.ANSI_STRING, 'ansi_string')


class FixedAnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_ANSI_STRING, 'fixed_ansi_string')


class SecureString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.SECURE_STRING, 'secure_string')

