def f(x):
    a = []
    while x:
        a.append(x)
        x = input()
    return a


x = input()
print(f(x))

