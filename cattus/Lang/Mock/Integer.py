from Config.DataTypeConfig import DataType, DataTypeConfig


class Int8(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT8, 'int8')


class Int16(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT16, 'int16')


class Int32(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT32, 'int32')


class Int64(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT64, 'int64')


class UInt8(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT8, 'uint8')


class UInt16(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT16, 'uint16')


class UInt32(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT32, 'uint32')


class UInt64(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT64, 'uint64')

