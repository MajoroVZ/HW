<<<<<<< HEAD
def f(n):
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
=======
def prost(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
>>>>>>> 57865164e05a0ea86a08fb355faf78e68ed38826
            return False
    return True


<<<<<<< HEAD
n = input()
print(f(n))
=======
n = int(input())
print(prost(n))
 
>>>>>>> 57865164e05a0ea86a08fb355faf78e68ed38826
