from Config.DataTypeConfig import DataType, DataTypeConfig


class DateTime(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DATETIME, 'DateTimeOffset')


class Date(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DATE, 'DateTime')


class Time(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.TIME, 'DateTime')


class TimeSpan(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.TIMESPAN, 'TimeSpan')

