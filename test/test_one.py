from HW4.one import sdvig
def test_sdvig():
    assert sdvig(['1', '2', '3', '4', '5'], 2) == ['4', '5', '1', '2', '3']
    assert sdvig(['1', '2', '3', '4', '5'], 3) == ['3', '4', '5', '1', '2']
    assert sdvig(['1', '2', '3', '4', '5'], 0) == ['1', '2', '3', '4', '5']
    