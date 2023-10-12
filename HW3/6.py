n = int(input())
def f(n):
    t = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            t = False
    return t
print(f(n))
 
