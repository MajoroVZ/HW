class Date:

    def __init__(self, year=1, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def input_date(self, DAYS_IN_MONTH=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]):
        date = input("Введите дату в формате День.Месяц.Год: ")
        self.day, self.month, self.year = map(int, date.split("."))
        if (self.month <= 0 or self.month > 12) or self.day > DAYS_IN_MONTH[self.month - 1]:
            raise ValueError('Неверный формат даты!')

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'
