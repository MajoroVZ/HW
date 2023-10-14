from one import f
from collections import Counter


x = input()
a = f(x)
a = Counter(a)
print("Элемент | Частота")
for i in a:
    print("{:7}".format(i), "|", a[i])