class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))  # 这里使用Date硬编码的形式，如果类名变了这个也要变，使用下面类方法可避免

    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year) > 0 and (int(month) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) <= 31):
            return True

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"


if __name__ == '__main__':
    new_day = Date(2018, 12, 11)
    new_day.tomorrow()
    print(new_day)

    # 可将下面操作写到类的静态函数里
    date_str = "2018-12-31"
    # year, month, day = tuple(date_str.split("-"))
    # new_day = Date(int(year), int(month), int(day))
    # print(new_day)

    # 使用静态方法初始化
    # new_day = Date.parse_from_string(date_str)
    # print(new_day)

    # 使用classmethod类方法初始化
    new_day = Date.from_string(date_str)
    print(new_day)

    # 检验合法性
    print(Date.valid_str(date_str))
