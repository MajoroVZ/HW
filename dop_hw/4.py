def diapozon_filter(a):
    b = []
    i = 0
    while i < len(a):
        k1 = a[i]                  #Первая переменная последовательности
        k2 = k1                    #Последняя переменная последовательности
        while i + 1 < len(a) and a[i + 1] == k2 + 1:
            k2 = a[i + 1]
            i += 1
        if k2 - k1 > 1: 
            b.append(str(k1) + '-' + str(k2))
        else:
            b.append(str(k1))
        i += 1
    return b


a = [int(a) for a in input().split()] #ввод 10 9 8 7 6 5 3 1
a.sort()
print(diapozon_filter(a)) #вывод ['1', '3', '5-10']