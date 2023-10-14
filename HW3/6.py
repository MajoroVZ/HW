def f(n):
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True


n = input()
print(f(n))
