import random


def quick_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    else:
        rand = random.choice(lst)
        return quick_sort([i for i in lst if i < rand]) + [i for i in lst if i == rand] + quick_sort(
            [i for i in lst if i > rand])


def main():
    lst = [4, 5, 1, 3, 2]
    print(quick_sort(lst))


main()
