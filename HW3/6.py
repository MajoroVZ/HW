n = int(input())
def f(n):
    k = 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            k += 1
        if k == 1:
            break
    if k == 0:
        return True
    else:
        return False
print(f(n))
 
