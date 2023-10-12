def max_n(n):
    n.sort(key=lambda x: x*3, reverse=True)
    mn = ''.join(n)
    return int(mn)
n = [n for n in input().split()]
mn = max_n(n)
print(mn)
