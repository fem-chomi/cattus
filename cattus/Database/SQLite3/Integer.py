from Config.DataTypeConfig import DataType, DataTypeConfig


class Int8(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT8, 'INTEGER')


class Int16(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT16, 'INTEGER')


class Int32(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT32, 'INTEGER')


class Int64(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT64, 'INTEGER')


class UInt8(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT8, 'INTEGER')


class UInt16(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT16, 'INTEGER')


class UInt32(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT32, 'INTEGER')


class UInt64(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT64, 'INTEGER')

