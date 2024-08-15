from Config.DataTypeConfig import DataType, DataTypeConfig


class Int8(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT8, 'tinyint')


class Int16(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT16, 'smallint')


class Int32(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT32, 'int')


class Int64(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.INT64, 'bigint')


class UInt8(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT8, 'tinyint')


class UInt16(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT16, 'smallint')


class UInt32(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT32, 'int')


class UInt64(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.UINT64, 'bigint')

