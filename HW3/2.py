def vremi_goda(n):
    if (n > 0 and n < 3) or n == 12:
        return "Зима"
    elif n > 2 and n < 6:
        return "Весна"
    elif n > 5 and n < 9:
        return "Лето"
    elif n > 8 and n < 12:
        return "Осень"
    return "Нет такого"


n = int(input())
print(vremi_goda(n))