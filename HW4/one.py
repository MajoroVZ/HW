def f(x):
    a = []
    while x:
        a.append(x)
        x = input("Сам список: ")
    return a

def sdvig(a, y):
    y %= len(a)
    return a[-y:] + a[:-y]

if __name__ == "__main__":
    y = int(input("На сколько сдвинуть список: "))
    x = input("Сам список: ")
    c = 0
    a = f(x)
    print(sdvig(a, y))

