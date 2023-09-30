x = float(input())
y = float(input())
if x > 0 and y > 0:
    print("1 координатная четверть")
elif x < 0 and y < 0:
    print("3 координатная четверть")
elif x < 0 and y > 0:
    print("2 координатная четверть")
elif x > 0 and y < 0:
    print("4 координатная четверть")
elif x == 0 and y == 0:
    print("Нулевая координата")
elif y == 0:
    print("Ось абцисс")
else:
    print("Ось оординат")
