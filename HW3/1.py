x = input()
def f(x):
    a = []
    while x:
        a.append(x)
        x = input()
    return a


print(f(x))