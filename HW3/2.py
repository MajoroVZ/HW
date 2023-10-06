n = int(input())
def vremi_goda(n):
    if (n > 0 and n < 3) or n == 12:
        print("Зима")
    elif n > 2 and n < 6:
        print("Весна")
    elif n > 5 and n < 9:
        print("Лето")
    elif n > 8 and n < 12:
        print("Осень")