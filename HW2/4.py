x = input()
a = x.count(')') 
b = x.count('(')
if a == b:
    print("Все отлично")
elif a < b:
    print("Не хватает (")
else:
    print("Не хватает )")
