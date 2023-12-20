import random


def quick_sort(lst: list) -> list:
    if not lst:
        return lst
    rand = random.choice(lst)
    return quick_sort([i for i in lst if i < rand]) + [i for i in lst if i == rand] + quick_sort([i for i in lst if i > rand])
