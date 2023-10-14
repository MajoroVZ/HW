def fib(n):
<<<<<<< HEAD
    f = [0, 1, 1]
    for _ in range(n - 2):
        f.append(f[-2] + f[-1])
    return f[:n]

=======
    x = 0
    c1 = 0
    c2 = 1
    lst = []
    for i in range(n):
        x = c1 + c2
        lst.append(x)
        c1 = c2
        c2 = x
    return lst
    
>>>>>>> 57865164e05a0ea86a08fb355faf78e68ed38826

n = int(input())
print(fib(n))
