def biniry_search(lst, element):
    lst.sort()
    print(lst)
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        val = lst[mid]
        if val == element:
            return mid
        elif val < element:
            right = mid + 1
        else:
            left = mid - 1
    return -1

lst = [int(a) for a in input().split()]
element = int(input())
print(biniry_search(lst, element))
