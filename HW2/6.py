x = input()
<<<<<<< HEAD
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
=======
y = y0 = int(input())

for i in x:
    if i.isdigit():
        y -= 1
        if not y:
            print(y0, "-ая цифра в строке:", i)
            break
>>>>>>> a926ab590f98f3976675967b41bd14816abe7c1d
