def next_max_int(n):
    n = list(n)
    i = len(n) - 1
    if len(n) == 1:
        return -1
    while n[i] <= n[i-1]:
        i -= 1
    if i == 0:
        return -1
    n[i], n[i-1] = n[i-1], n[i]
    return ''.join(n)


n = input()
print(next_max_int(n))
