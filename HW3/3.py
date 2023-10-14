def fib(n):
    k = 1
    x = 0
    c = 0
    lst = []
    for i in range(0, n):
        x = c + k
        lst.append(x)
        c = k
        k = x
    return lst


n = int(input())
print(fib(n))
