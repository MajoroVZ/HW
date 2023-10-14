a = [a for a in input().split()]

def mn(a):
    m = len(max(a, key=len))
    a.sort(key=lambda x: x * m, reverse=True)
    r = int(''.join(a))
    return r


print(mn(a))
