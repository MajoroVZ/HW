x = int(input())
y = int(input())
if x>0 and y>0:
    print("1 координатная четверть")
elif x<0 and y<0:
    print("3 координатная четверть")
elif x<0 and y>0:
    print("2 координатная четверть")
elif x>0 and y<0:
    print("4 координатная четверть")
elif x == 0 and y == 0:
    print("Нулевая координата")
elif x == 0 and y!=0:
    print("Ось абцисс")
elif y == 0 and x!=0:
    print("Ось координат")