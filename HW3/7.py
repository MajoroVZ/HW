'''def f(x):
    m = 0
    k = ''
    for i in x:
        if x.count(i) > m:
            m = x.count(i)
            k = i
    return k


def n(x):
    mx = 0
    o = ''
    for i in x:
        if len(i) > mx:
            mx = len(i)
            o = i
    return o


x = [str(x) for x in input().split()]
print("Самое часто встречаемое", f(x))
<<<<<<< HEAD
print("Самое длинное", n(x))'''
from collections import Counter


def longest(t):
    return max(t, key=len)


def ct(t):
    c = Counter(t)
    return c.most_common(1)[0][0] 


lst = input("Введите список: ").split()

print("Самое длинное слово:", longest(lst))
print("Наиболее часто встречаемое слово:", ct(lst))
=======
print("Самое длинное", n(x))
>>>>>>> 57865164e05a0ea86a08fb355faf78e68ed38826
