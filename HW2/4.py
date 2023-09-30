x = input()
if x.count(')') == x.count('('):
    print("Все отлично")
elif x.count(')') > x.count('('):
    print("Не хватает (")
else:
    print("Не хватает )")
