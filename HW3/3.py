n = int(input())
def f(n):
    k = 1
    x = 0
    c = 0
    for i in range(n):
        x = c + k
        print(x, end=" ")
        c = k
        k = x
print(f(n))