from HW4.two import fac
import pytest


@pytest.mark.parametrize(
    ('x', 'result'),
    [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1)
    ]
)
def test(x, result):
    assert fac(x) == result