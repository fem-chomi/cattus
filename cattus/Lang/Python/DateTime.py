from Config.DataTypeConfig import DataType, DataTypeConfig


class DateTime(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DATETIME, 'str')


class Date(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DATE, 'str')


class Time(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.TIME, 'str')


class TimeSpan(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.TIMESPAN, 'str')

