from Config.DataTypeConfig import DataType, DataTypeConfig


class Void(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.VOID, 'None')

