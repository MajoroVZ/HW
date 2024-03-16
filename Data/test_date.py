import pytest
import builtins
from unittest import mock
from HW.Data.date import Date
from HW.Data.date import DateStamp
from HW.Data.date import DateValidationError
import freezegun


@pytest.mark.parametrize(
    ('in_year', 'in_month', 'in_day', 'year', 'month', 'day'),
    [
        (12, 2, 2005, 12, 2, 2005),
        (1, 2, 2005, 1, 2, 2005),
        (1, 7, 10249242, 1, 7, 10249242),
    ]
)
def test_init(in_year, in_month, in_day, year, month, day):
    d1 = Date(in_day, in_month, in_year)
    assert d1.day == day
    assert d1.month == month
    assert d1.year == year


@pytest.mark.parametrize(
    "input_values, expected_day, expected_month, expected_year",
    [
        ('1.1.1', 1, 1, 1),
        ("1.1.0001", 1, 1, 1),
        ("1.1.2023", 1, 1, 2023),
        ("28.2.2022", 28, 2, 2022),

    ]
)
def test_input_date(input_values, expected_day, expected_month, expected_year):
    d = Date()
    with mock.patch.object(builtins, 'input', lambda _: input_values):
        d.input_date()

    assert d.day == expected_day
    assert d.month == expected_month
    assert d.year == expected_year


# @pytest.mark.parametrize("input_values, result",
#                          [
#                              ('28.28.2025', 'Неверный формат даты!'),
#                              ("29.02.2023", 'Неверный формат даты!'),
#                          ])
# def test_format_check_exception(input_values, result):
#     d = Date()
#     with mock.patch.object(builtins, 'input', lambda _: input_values):
#         with pytest.raises(ValueError, match=result) as ex:
#             d.input_date()
@pytest.mark.parametrize(
    "day, month, year, error_message",
    [
        (32, 1, 1, 'даты'),
        (15, 13, 1, 'даты'),
        (1, 1, 0, 'даты'),
    ]
)
def test_validate_date(day, month, year, error_message):
    date = Date()
    date.day = day
    date.month = month
    date.year = year
    with pytest.raises(DateValidationError, match=error_message):
        date.validate_date()


@pytest.mark.parametrize(
    "dates, Error",
    [
        ('ы.a.s', 'Только цифры и неверный формат записи'),
        ('asdf,123,132', 'Только цифры и неверный формат записи'),
        ('123-123-123', 'Только цифры и неверный формат записи'),
        ('ы.123.123', 'Только цифры и неверный формат записи'),
        ('ы.123.444', 'Только цифры и неверный формат записи'),
        ('ы.a.s', 'Только цифры и неверный формат записи')

    ]
)
def test_validate_input(dates, Error):
    d = Date()
    with pytest.raises(TypeError, match=Error):
        assert d.validate_input(dates)


@pytest.mark.parametrize(
    "input_values, expected_day, expected_month, expected_year",
    [
        ('1.1.1', 1, 1, 1),
        ("1.1.1", 1, 1, 1),
        ("1.1.2023", 1, 1, 2023),
        ("28.2.2022", 28, 2, 2022),

    ]
)
def test_str_(input_values, expected_day, expected_month, expected_year):
    date = Date(expected_day, expected_month, expected_year)
    assert str(date) == input_values


# test class DateStamp

@pytest.mark.parametrize(
    "input_values, expected_day, expected_month, expected_year",
    [
        ('0001-1-1', 1, 1, 1),
        ("0001-1-1", 1, 1, 1),
        ("2023-1-2", 2023, 1, 2),
        ("2022-2-28", 2022, 2, 28),
        ("2024-2-29", 2024, 2, 29)

    ]
)
def test_init(input_values, expected_day, expected_month, expected_year):
    with freezegun.freeze_time(input_values):
        d1 = DateStamp()

    assert d1.day == expected_day
    assert d1.month == expected_month
    assert d1.year == expected_year


@pytest.mark.parametrize(
    'd1,m1,y1,d2,m2,y2, d3,m3,y3',
    [
        (10, 10, 10, 10, 10, 10, 20, 8, 21),
        (31, 1, 2024, 31, 3, 2024, 1, 6, 4048),
        (1, 12, 12, 1, 12, 12, 2, 12, 25),
    ]
)
def test_add(d1, m1, y1, d2, m2, y2, d3, m3, y3):
    d1 = Date(d1, m1, y1)
    d2 = Date(d2, m2, y2)
    f = d1 + d2
    assert f.day == d3
    assert f.month == m3
    assert f.year == y3


@pytest.mark.parametrize(
    'd1,m1,y1,d2,m2,y2, d3,m3,y3',
    [
        (15, 3, 2005, 10, 2, 2000, 5, 1, 5),
        (31, 1, 2000, 1, 1, 1000, 30, 12, 999),
        (1, 4, 2000, 1, 1, 1001, 28, 2, 999),
        (1, 4, 2000, 1, 1, 1000, 29, 2, 1000),
    ]
)
def test_sub(d1, m1, y1, d2, m2, y2, d3, m3, y3):
    d1 = Date(d1, m1, y1)
    d2 = Date(d2, m2, y2)
    f = d1 - d2
    assert f == Date(d3, m3, y3)


@pytest.mark.parametrize(
    ('d1,m1,y1,d2,m2,y2'),
    [
        (1, 1, 1, 1, 1, 1),
        (2, 2, 2, 2, 2, 2),
        (10, 3, 10, 10, 3, 10),
    ]
)
def test_eq(d1, m1, y1, d2, m2, y2):
    d1 = Date(d1, m1, y1)
    d2 = Date(d2, m2, y2)
    assert d1 == d2
    d3 = Date()
    d4 = Date()
    assert d3 == d4
