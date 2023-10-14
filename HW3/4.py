<<<<<<< HEAD
from one import f
from collections import Counter


x = input()
a = f(x)
a = Counter(a)
print("Элемент | Частота")
for i in a:
    print("{:7}".format(i), "|", a[i])
=======
def f(x):
    a = []
    while x:
        a.append(x)
        x = input()
    lst = []
    print("Элемент | частота")
    for i in a:
        if i not in lst:
            print("{:7}".format(i),"|", a.count(i))
            lst.append(i)


x = input()
f(x)
>>>>>>> 57865164e05a0ea86a08fb355faf78e68ed38826
