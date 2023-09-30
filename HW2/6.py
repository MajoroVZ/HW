x = input()
y = int(input())
for i in x:
    if i.isdigit():
        y -= 1
        if not y:
            print(y, "-ая цифра в строке:", i)
            break
