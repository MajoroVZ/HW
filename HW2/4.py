x = input()
k = 0 
b = 0
for i in range(len(x)):
    if x[i] == '(':
        k += 1
    if x[i] == ')':
        b += 1
if k == b:
    print("Все скобки есть")
elif k < b:
    print("Не хватает открывающейся скобки")
else:
    print("Не хватает закрывающийся скобки")