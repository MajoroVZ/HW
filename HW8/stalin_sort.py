def stalin_sort(lst: list) -> list: return lst if not lst else [lst[x] for x in range(len(lst)) if
                                                                x == 0 or lst[x] >= max(lst[:x])]


print(stalin_sort([1, 2, 3, 4, 5]))
print(stalin_sort([89, 1, 2, 33, 11, 5, 67, 10, 8]))
print(stalin_sort([]))
print(stalin_sort([1]))
print(stalin_sort([1, 1, 1, 1]))
print(stalin_sort([10, 5, 8, 12, 3, 15, 6]))
