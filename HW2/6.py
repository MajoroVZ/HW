x = input()
y = int(input())
a = 0
b = 0
for i in x:
    if i.isdigit():
        a += 1
        if a == y:
            b = i
            break
print(y, "-ая цифра в строке:", b)