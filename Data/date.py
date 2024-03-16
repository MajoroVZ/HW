from datetime import date


class Date:
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day=1, month=1, year=1):
        self.year = year
        self.month = month
        self.day = day

    def input_date(self):
        dates = input("Введите дату в формате День.Месяц.Год: ")
        try:
            self.day, self.month, self.year = self.validate_input(dates)
            self.validate_date()
        except TypeError:
            self.validate_input(dates)

    def validate_date(self):
        if (self.month <= 0 or self.month > 12) or self.day > self.days_in_month(self.month,
                                                                                 self.year) or self.year < 1:
            raise DateValidationError('Неверный формат даты!', 'ValueError')

    @staticmethod
    def validate_input(dates):
        data = dates.split('.')
        if len(data) == 3 and (data[0].isdigit() and data[1].isdigit() and data[2].isdigit()):
            return map(int, data)
        raise TypeError('Только цифры и неверный формат записи')

    @staticmethod
    def is_leap_year(y: int) -> bool:
        """checking leap year"""
        return (y % 4 == 0 and y % 100 != 0) or not y % 400

    @classmethod
    def days_in_month(cls, month, year) -> int:
        """checking the correct number of months"""
        if month == 2 and cls.is_leap_year(year):
            return 29
        return cls.DAYS_IN_MONTH[month - 13]

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __add__(self, other):
        day_sum, month_sum, year_sum = self.day + other.day, self.month + other.month, self.year + other.year
        while day_sum > self.days_in_month(month_sum, year_sum):
            day_sum = day_sum - self.days_in_month(month_sum, year_sum)
            month_sum += 1

        if month_sum > 12:
            month_sum = month_sum - 12
            year_sum += 1
        return self.__class__(day_sum, month_sum, year_sum)

    def __sub__(self, other):
        year = self.year - other.year
        month = self.month - other.month
        if month < 1:
            month += 12
            year -= 1
        day = self.day - other.day
        if day < 1:
            month -= 1
            dop_day = 1 if not year % 4 and month == 2 else 0
            day = self.days_in_month(month, year) + dop_day + day

        return self.__class__(day, month, year)


class DateStamp(Date):
    def __init__(self):
        today = date.today()
        super().__init__(today.year, today.month, today.day)

    def input_date(self):
        raise NotImplementedError


class DateValidationError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


if __name__ == '__main__':
    d1 = Date(31, 1, 1012)
    d2 = Date(31, 1, 1012)
    print(d1 + d2)
    print(d1 - d2)
