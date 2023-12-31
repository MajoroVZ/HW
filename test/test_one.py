from HW.HW4.one import s_list
import pytest


@pytest.mark.parametrize(
    ('a', 'n', 'result'),
    [
        (['1', '2', '3', '4', '5'], 2, ['4', '5', '1', '2', '3']),
        (['1', '2', '3', '4', '5'], 3, ['3', '4', '5', '1', '2']),
        (['1', '2', '3', '4', '5'], 0, ['1', '2', '3', '4', '5']),
        (['1', '2', '3', '4', '5'], 7, ['4', '5', '1', '2', '3']),
    ]
)
def test(a, n, result):
    assert s_list(a, n) == result
