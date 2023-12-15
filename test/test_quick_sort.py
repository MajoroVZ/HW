import pytest
from HW.HW8.quick_sort import quick_sort


@pytest.mark.parametrize("start_lst, end_lst", [
    ([], []),
    ([1], [1]),
    ([33, 3], [3, 33]),
    ([1, 2, 3], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]),
    ([3, 3, 2, 2, 1, 1], [1, 1, 2, 2, 3, 3]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([5, 4, 1, 2, 3], [1, 2, 3, 4, 5]),
    ([1, 2, 5, 4, 3], [1, 2, 3, 4, 5]),
    ([4, 5, 3, 1, 2], [1, 2, 3, 4, 5]),
    ([44, 11, 33], [11, 33, 44]),
])
def test_quick_sort(start_lst, end_lst):
    assert quick_sort(start_lst) == end_lst

