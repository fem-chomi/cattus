from Config.DataTypeConfig import DataType, DataTypeConfig


class Int8(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT8, 'int')


class Int16(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT16, 'int')


class Int32(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT32, 'int')


class Int64(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT64, 'long')


class UInt8(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT8, 'int')


class UInt16(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT16, 'int')


class UInt32(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT32, 'int')


class UInt64(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT64, 'long')

