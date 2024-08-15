from Config.DataTypeConfig import DataType, DataTypeConfig


class Boolean(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.BOOLEAN, 'bit')

