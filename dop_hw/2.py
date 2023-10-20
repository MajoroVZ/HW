def next_max_int(n):
    b = n
    k1, k2 = '', ''
    i = len(n) - 1
    while int(n[i]) <= int(n[i-1]):
        i -= 1
    else:
        k1, k2 = n[i], n[i-1]
        #n[i], n[i-1] = k2, k1
        n = n.replace(n[i], k2, 1)
        n = n.replace(n[i-1], k1, 1)
    if n == b:
        return -1
    return n


n = input()
print(next_max_int(n))
