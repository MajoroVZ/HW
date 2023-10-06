x = input()
a = []
def f(x):
    while x:
        a.append(x)
        x = input()
    lst = []
    print("Элемент | частота")
    for i in a:
        if i not in lst:
            print("{:7}".format(i),"|", a.count(i))
            lst.append(i)
print(f(x))