x = input()
a = []
def f(x):
    while x:
        a.append(x)
        x = input()
    return a
print(f(x))