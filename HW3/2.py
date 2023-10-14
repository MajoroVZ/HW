def vremi_goda(n):
    if (n > 0 and n < 3) or n == 12:
        return "Зима"
    if n > 2 and n < 6:
        return "Весна"
    if n > 5 and n < 9:
        return "Лето"
    if n > 8 and n < 12:
        return "Осень"
<<<<<<< HEAD
    return "Нет такого"


n = int(input())
print(vremi_goda(n))
=======
    return "Нет такого месяца"


n = int(input())
print(vremi_goda(n))
>>>>>>> 57865164e05a0ea86a08fb355faf78e68ed38826
