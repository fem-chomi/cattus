from Config.DataTypeConfig import DataType, DataTypeConfig


class Binary(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.BINARY, 'str')

