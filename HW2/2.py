from itertools import *
x = [str(a) for a in input().split()]
print(max(list(permutations(x, r=len(x)))))
