from Config.DataTypeConfig import DataType, DataTypeConfig


class String(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.STRING, 'nvarchar')


class FixedString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_STRING, 'nchar')


class AnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.ANSI_STRING, 'varchar')


class FixedAnsiString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.FIXED_ANSI_STRING, 'char')


class SecureString(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.SECURE_STRING, 'nvarchar')

