class Date:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, year=1, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def input_date(self):
        date = input("Введите дату в формате День.Месяц.Год: ")
        self.day, self.month, self.year = map(int, date.split("."))
        if (self.month <= 0 or self.month > 12) or self.day > self.days_in_month[self.month - 1]:
            raise ValueError('Неверный формат даты!')

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'
