def f(x):
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
print(f(x), n(x))