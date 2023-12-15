def stalin_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    else:
        arr = [lst[0]]
        for i in range(1,len(lst)):
            if lst[i] > arr[-1]:
                arr.append(lst[i])
        return arr
