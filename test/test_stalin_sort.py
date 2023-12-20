import pytest
from HW.HW8.stalin_sort import stalin_sort


@pytest.mark.parametrize("start_lst, end_lst", [
    ([4, 2, 5, 1, 6, 3], [4, 5, 6]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [5]),
    ([], []),
    ([1], [1]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([10, 5, 8, 12, 3, 15, 6], [10, 12, 15]),
    ([89, 1, 2, 33, 11, 5, 67, 10, 8], [89])
])
def test_stalin_sort(start_lst, end_lst):
    assert stalin_sort(start_lst) == end_lst
