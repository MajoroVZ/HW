x = input()
y = y0 = int(input())

for i in x:
    if i.isdigit():
        y -= 1
        if not y:
            print(y0, "-ая цифра в строке:", i)
            break
