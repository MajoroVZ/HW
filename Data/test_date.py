import pytest
import builtins
from unittest import mock
from HW.Data.date import Date


@pytest.mark.parametrize(
    ('in_year', 'in_month', 'in_day', 'year', 'month', 'day'),
    [
        (12, 2, 2005, 12, 2, 2005),
        (1, 2, 2005, 1, 2, 2005),
        (1, 7, 10249242, 1, 7, 10249242),
    ]
)
def test_init(in_year, in_month, in_day, year, month, day):
    d1 = Date(in_year, in_month, in_day)
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


@pytest.mark.parametrize("input_values, result",
                         [
                             ('28.28.2025', 'Неверный формат даты!'),
                             ("29.02.2024", 'Неверный формат даты!')

                         ])
def test_format_check_exception(input_values, result):
    d = Date()
    with mock.patch.object(builtins, 'input', lambda _: input_values):
        with pytest.raises(ValueError, match=result) as ex:
            d.input_date()

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
    date = Date(expected_year, expected_month, expected_day)
    assert str(date) == input_values
