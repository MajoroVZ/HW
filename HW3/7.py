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


def longest(lst):
    return max(t, key=len)


def ct(lst):
    c = Counter(lst)
    return c.most_common(1)[0][0] 


lst = input("Введите список: ").split()

print("Самое длинное слово:", longest(lst))
print("Наиболее часто встречаемое слово:", ct(lst))
