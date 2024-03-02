from datetime import date


class Date:
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, year=1, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def input_date(self):
        date = input("Введите дату в формате День.Месяц.Год: ")
        self.day, self.month, self.year = map(int, date.split("."))
        return self.validate()

    def validate(self):
        if (self.month <= 0 or self.month > 12) or self.day > self.DAYS_IN_MONTH[self.month - 1]:
            raise ValueError('Неверный формат даты!')

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'


class DateStamp(Date):
    def __init__(self):
        today = date.today()
        super().__init__(today.year, today.month, today.day)

    def input_date(self):
        raise NotImplementedError

# d1 = DateStamp()
# print(d1)
