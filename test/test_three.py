from HW.HW4.three import uniq
import pytest


@pytest.mark.parametrize('input, result', [
    ([1, 2, 3], True),
    ([1, True], True),
    ([1, 2, 2, 3], False),
    ([1, 'hello', 'world'], True),
    ([1, 'hello', 'hello'], False),
    (['a', 'b', 'c'], True),
    (['a', 'b', 'b', 'c'], False),
])
def test_uniq(input, result):
    assert uniq(input) == result
