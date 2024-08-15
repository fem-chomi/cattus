from Config.DataTypeConfig import DataType, DataTypeConfig


class Decimal(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DECIMAL, '')

