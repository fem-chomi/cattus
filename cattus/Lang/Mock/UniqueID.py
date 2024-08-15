from Config.DataTypeConfig import DataType, DataTypeConfig


class UniqueID(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UUID, 'uuid')

