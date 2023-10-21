def input_list():
    x = input("Сам список: ")
    a = []
    while x:
        a.append(x)
        x = input("Сам список: ")
    return a
