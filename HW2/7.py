from random import randint
x = randint(0,10)
y = int(input())
while y != x:
    if x < y:
        print("Число больше загадонного")
        y = int(input())
    else:
        print("число меньше загадонного")
        y = int(input())
print("угадал")