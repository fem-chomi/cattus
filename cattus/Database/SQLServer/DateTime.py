from Config.DataTypeConfig import DataType, DataTypeConfig


class DateTime(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DATETIME, 'datetimeoffset')


class Date(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DATE, 'date')


class Time(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.TIME, 'time')


class TimeSpan(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.TIMESPAN, '')

