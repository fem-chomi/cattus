from Config.DataTypeConfig import DataType, DataTypeConfig


class DateTime(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DATETIME, 'TEXT')


class Date(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.DATE, 'TEXT')


class Time(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.TIME, 'TEXT')


class TimeSpan(DataTypeConfig):
    def __init__(self):
        super().__init__(DataType.TIMESPAN, 'TEXT')

