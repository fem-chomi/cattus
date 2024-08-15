from Config.DataTypeConfig import DataType, DataTypeConfig


class Single(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.SINGLE, 'real')


class Double(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DOUBLE, 'float')

