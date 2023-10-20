def next_max_int(n):
    i = len(n) - 1
    while n[i] <= n[i-1]:
        i -= 1
        if i == 0:
            return -1
    k1, k2 = n[i], n[i-1]
    n = n.replace(n[i], k2, 1)
    n = n.replace(n[i-1], k1, 1)
    return n


n = input()
print(next_max_int(n))
