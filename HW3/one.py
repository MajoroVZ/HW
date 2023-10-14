def input_list(x):
    a = []
    while x:
        a.append(x)
        x = input()
    return a


x = input()
print(input_list(x))

