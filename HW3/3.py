n = int(input())
def f(n):
    k = 1
    x = 0
    c = 0
    for i in range(1, n + 1):
        x = c + k
        print(x, end=" ")
        c = k
        k = x
f(n)
