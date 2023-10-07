n = int(input())
def f(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            break
            return False
    retutn True
print(f(n))
 
