def next_max_int(n):
    b = n
    i = len(n) - 1
    while int(n[i]) <= int(n[i-1]):
        i -= 1
    k1, k2 = n[i], n[i-1]
    n = n[:i] + k2 + n[i+1:]
    n = n[:i-1] + k1 + n[i:]
    if n == b:
        return -1
    return n


n = input()
print(next_max_int(n))
