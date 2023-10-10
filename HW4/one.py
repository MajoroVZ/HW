y = int(input("На сколько сдвинуть список: "))
x = input("Сам список: ")
a = []
def sdvig(x):
    c = 0
    while x:
        a.append(x)
        x = input()
    b = []
    c = y % len(a)
    for i in range(len(a)-c):
        b.append(a[i+c])
    for i in range(c):
        b.append(a[i])
    return b
print(sdvig(x))
